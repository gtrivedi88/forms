from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, abort
)
import flask_principal
from werkzeug.exceptions import abort
import taxonomy_manager.permissions as permissions
import taxonomy_manager.models as models
import taxonomy_manager.forms as forms
from taxonomy_manager.db import db
from taxonomy_manager.utils import (
    convert_to_classname, convert_to_title, get_choices_for_selectfields, get_mapped_data, set_mapped_data, set_pagination, create_list_table
)
import uuid
from pprint import pprint

# Initialize the flask blueprint for our taxonomy pages
bp = Blueprint('taxonomy', __name__)

# List a page of a taxonomy. If no page number is supplied in the URL, set it to the first page
@bp.route('/taxonomy/<taxonomy_name>')
@bp.route('/taxonomy/<taxonomy_name>/<int:page>')
@permissions.view_permission.require()
def list_taxonomy(taxonomy_name, page = 1):

    # Get the model based on the taxonomy_name from the URL. If the model doesn't exist or is hidden, redirect to an error 404.
    try:
        TaxonomyClass = getattr(models, convert_to_classname(taxonomy_name))
    except:
        abort(404)

    if hasattr(TaxonomyClass, '__hidden__') and TaxonomyClass.__hidden__ is True:
        abort(404)

    # Set the field for the UUID and Term field to display in the list
    uuid_field = TaxonomyClass.__uuid__

    # Set the field for Term field to display in the table
    term_field = TaxonomyClass.__term__

    #print(dir(TaxonomyClass.brand_opl_partner.partner_name))

    # Get the column names
    columns = TaxonomyClass.metadata.tables[TaxonomyClass.__table_args__["schema"] + "." + TaxonomyClass.__tablename__].c.keys()

    # Query the database and convert the results into a list
    taxonomy_result = db.session.execute(db.select(TaxonomyClass))
    taxonomy = [r for r, in taxonomy_result]
    taxonomy_table = create_list_table(taxonomy, term_field, uuid_field)

    # Values to calculate the pagination
    pagination=set_pagination(taxonomy_table, page)

    # Choose the subset of taxonomy based on the current pagination data
    taxonomy_subset = taxonomy_table[pagination['start_value']:pagination['end_value']]

    # Render the list of taxonomy for a page
    return render_template('taxonomy/list.html',
        taxonomy_name = taxonomy_name,
        taxonomy = taxonomy_subset,
        pagination = pagination,
        title = convert_to_title(taxonomy_name),
        permissions = permissions
        )

# Create a new term for a taxonomy
@bp.route('/taxonomy/<taxonomy_name>/create', methods=('GET', 'POST'))
@permissions.create_permission.require()
def add_term(taxonomy_name):

    # Get the model based on the taxonomy_name from the URL. If the model doesn't exist or is hidden, redirect to an error 404.
    try:
        TaxonomyClass = getattr(models, convert_to_classname(taxonomy_name))
        TaxonomyForm = getattr(forms, "Form" + convert_to_classname(taxonomy_name))
    except:
        abort(404)

    if hasattr(TaxonomyClass, '__hidden__') and TaxonomyClass.__hidden__ is True:
        abort(404)

    # Set the field for the UUID
    uuid_field = TaxonomyClass.__uuid__

    # Create our form from the taxonomy class
    form = TaxonomyForm(request.form)

    # Get select field choices if there's a relationship to another database column
    get_choices_for_selectfields(form)

    # If the user has submitted the form (POST), add the new term data to the  database
    if request.method == 'POST' and form.validate():
        # Create a new taxonomy object from our model
        taxonomy = TaxonomyClass()

        # Get the column names
        columns = TaxonomyClass.metadata.tables[TaxonomyClass.__table_args__["schema"] + "." + TaxonomyClass.__tablename__].c.keys()

        # Set the values for each column in the taxonomy object. Since UUID doesn't exist, we create a new one.
        for column in columns:
            if column == uuid_field and column not in request.form:
                setattr(taxonomy, column, str(uuid.uuid4()))
            else:
                setattr(taxonomy, column, request.form[column])

        # Save the main taxonomy object
        db.session.add(taxonomy)

        # If there is a secondary table that maps data to another table, save the content to the seconadry table.
        set_mapped_data(form, taxonomy, request)

        # Save the term data in the database
        db.session.commit()

        # After saving the data, go back to the taxonomy list page
        return redirect(url_for('taxonomy.list_taxonomy', taxonomy_name = taxonomy_name))

    # If the user isn't submitting the a form to this URL, just display the form (GET)
    return render_template('taxonomy/create.html',
        taxonomy_name=taxonomy_name,
        title = convert_to_title(taxonomy_name),
        form = form
        )

# Edit an existing taxonomy term
@bp.route('/taxonomy/<taxonomy_name>/<uuid:id>/edit', methods=('GET', 'POST'))
@permissions.edit_taxonomy_permission.require()
def edit_term(taxonomy_name, id):

    # Get the model based on the taxonomy_name from the URL
    try:
        TaxonomyClass = getattr(models, convert_to_classname(taxonomy_name))
        TaxonomyForm = getattr(forms, "Form" + convert_to_classname(taxonomy_name))
    except:
        abort(404)

    if hasattr(TaxonomyClass, '__hidden__') and TaxonomyClass.__hidden__ is True:
        abort(404)

    # Set the field for the UUID
    uuid_field = TaxonomyClass.__uuid__

    # Get the column names
    columns = TaxonomyClass.metadata.tables[TaxonomyClass.__table_args__["schema"] + "." + TaxonomyClass.__tablename__].c.keys()

    # Query the database and save as an object
    taxonomy = db.session.execute(db.select(TaxonomyClass).where(TaxonomyClass.metadata.tables[TaxonomyClass.__table_args__["schema"] + "." + TaxonomyClass.__tablename__].c[uuid_field] == str(id))).scalar_one()

    # Create our form from the taxonomy class
    form = TaxonomyForm(obj=taxonomy)

    # Get select field choices if there's a relationship to another database column
    get_choices_for_selectfields(form)
    get_mapped_data(form, taxonomy, request)


    # If the user has submitted the form (POST), update the term data in the database
    if request.method == 'POST':

        # Create a new taxonomy object and set the values for each column.
        for column in columns:
            if column == uuid_field:
                setattr(taxonomy, column, str(id))
            else:
                setattr(taxonomy, column, request.form[column])

        # If there is a secondary table that maps data to another table, save the content to the seconadry table.
        set_mapped_data(form, taxonomy, request)

        # Update the term data in the database
        db.session.commit()

        # After saving the data, go back to the taxonomy list page
        return redirect(url_for('taxonomy.list_taxonomy', taxonomy_name = taxonomy_name))

    # If the user is just viewing the data through this route (GET), then grab the database and prepopulate the form so that the user can edit it.
    return render_template('taxonomy/update.html',
        taxonomy_name = taxonomy_name,
        title = convert_to_title(taxonomy_name),
        taxonomy = taxonomy,
        form = form,
        permissions = permissions
        )

# Delete an existing taxonomy term
@bp.route('/taxonomy/<taxonomy_name>/<uuid:id>/delete')
@permissions.delete_permission.require()
def delete_term(taxonomy_name, id):

    # Get the model based on the taxonomy_name from the URL
    try:
        TaxonomyClass = getattr(models, convert_to_classname(taxonomy_name))
    except:
        abort(404)

    if hasattr(TaxonomyClass, '__hidden__') and TaxonomyClass.__hidden__ is True:
        abort(404)

    # Set the field for the UUID
    uuid_field = TaxonomyClass.__uuid__

    # Query the database and save as an object
    taxonomy = db.session.execute(db.select(TaxonomyClass).where(TaxonomyClass.metadata.tables[TaxonomyClass.__table_args__["schema"] + "." + TaxonomyClass.__tablename__].c[uuid_field] == str(id))).scalar_one()

    # Delete the term from the database
    db.session.delete(taxonomy)
    db.session.commit()

    # Go back to the taxonomy list page
    return redirect(url_for('taxonomy.list_taxonomy', taxonomy_name = taxonomy_name))
