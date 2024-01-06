from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

class Product(db.Model):
    """
    Represents a product in the system.

    Attributes:
    - product_id: Unique identifier for the product.
    - product_name: Name of the product.
    - product_description: Description of the product.
    - upcoming_change: Indicates if there is an upcoming change for the product.
    - deprecated: Indicates if the product is deprecated.
    - product_status: Status of the product.
    - last_updated: Date when the product was last updated.
    - created: Date when the product was created.
    - product_status_detail: Additional details about the product status.
    """

    __tablename__ = 'product'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "product_name"
    __hidden__ = True

    product_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    product_name = db.Column(db.String(255), nullable=False)
    product_description = db.Column(db.String)
    upcoming_change = db.Column(db.Boolean)
    deprecated = db.Column(db.Boolean)
    product_status = db.Column(db.String(255))
    last_updated = db.Column(db.Date)
    created = db.Column(db.Date)
    product_status_detail = db.Column(db.String(255))

class ProductType(db.Model):
    """
    Represents different types of products.

    Attributes:
    - type_id: Unique identifier for the product type.
    - product_type: Type of the product.
    """

    __tablename__ = 'product_types'
    __table_args__ = {'schema': 'brand_opl'}

    type_id = db.Column(db.String, primary_key=True)
    product_type = db.Column(db.String(255), nullable=False)

    # Relationships
    product_types_map = db.relationship('ProductTypeMap', backref='product_type', lazy='dynamic')

class ProductTypeMap(db.Model):
    """
    Represents a many-to-many relationship between Product and ProductType.

    Attributes:
    - product_id: Foreign key to Product.
    - type_id: Foreign key to ProductType.
    """

    __tablename__ = 'product_types_map'
    __table_args__ = {'schema': 'brand_opl'}

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    type_id = db.Column(db.String, db.ForeignKey('brand_opl.product_types.type_id'), primary_key=True)

class ProductPortfolios(db.Model):
    """
    Represents different portfolios for products.

    Attributes:
    - category_id: Unique identifier for the product portfolio.
    - category_name: Name of the product portfolio.
    """

    __tablename__ = 'product_portfolios'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "category_id"
    __term__ = "category_name"

    category_id = db.Column(db.String, primary_key=True)
    category_name = db.Column(db.String(255), nullable=False)

    # Relationships
    product_portfolio_map = db.relationship('ProductPortfolioMap', backref='product_portfolio', lazy='dynamic')

class ProductPortfolioMap(db.Model):
    """
    Represents a many-to-many relationship between Product and ProductPortfolios.

    Attributes:
    - product_id: Foreign key to Product.
    - category_id: Foreign key to ProductPortfolios.
    """

    __tablename__ = 'product_portfolio_map'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "category_id"

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    category_id = db.Column(db.String, db.ForeignKey('brand_opl.product_portfolios.category_id'), primary_key=True)

class ProductNotes(db.Model):
    """
    Represents notes associated with a product.

    Attributes:
    - product_id: Foreign key to Product.
    - product_note: Note associated with the product.
    """

    __tablename__ = 'product_notes'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "product_note"

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    product_note = db.Column(db.String(65535), nullable=False)

    # Define the relationship to the Product model
    product = db.relationship('Product', backref=db.backref('product_notes', lazy='dynamic'))


class ProductReferences(db.Model):
    """
    Represents references associated with a product.

    Attributes:
    - product_id: Foreign key to Product.
    - product_link: Link associated with the product reference.
    - link_description: Description associated with the product reference.

    Relationships:
    - product: Relationship to Product for easy access to the associated product references.
    """

    __tablename__ = 'product_references'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "product_link"

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    product_link = db.Column(db.String(65535), nullable=False)
    link_description = db.Column(db.String(65535), nullable=False)

    # Define the relationship to the Product model
    product = db.relationship('Product', backref=db.backref('product_references', lazy='dynamic'))


class ProductAlias(db.Model):
    """
    Represents aliases associated with a product.

    Attributes:
    - alias_id: Unique identifier for the alias.
    - product_id: Foreign key to Product.
    - alias_name: Name associated with the alias.
    - alias_type: Type of the alias (Short, Acronym, Cli, Former).
    - alias_approved: Indicates if the alias is approved.
    - previous_name: Indicates if the alias is a previous name.
    - tech_docs: Indicates if the alias is approved for tech docs.
    - tech_docs_cli: Indicates if the alias is approved for tech docs code/CLI.
    - alias_notes: Notes associated with the alias.

    Relationships:
    - product: Relationship to Product for easy access to the associated product.
    """

    __tablename__ = 'product_alias'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "alias_id"
    __term__ = "alias_name"

    alias_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), nullable=False)
    alias_name = db.Column(db.String(255), nullable=False)
    alias_type = db.Column(db.String(255), nullable=False)
    alias_approved = db.Column(db.Boolean, nullable=True)
    previous_name = db.Column(db.Boolean, nullable=True)
    tech_docs = db.Column(db.Boolean, nullable=True)
    tech_docs_cli = db.Column(db.Boolean, nullable=True)
    alias_notes = db.Column(db.String(65535))

    # Define the relationship to the Product model
    product = db.relationship('Product', backref=db.backref('aliases', lazy='dynamic'))


class ProductMktLife(db.Model):
    """
    Represents marketing life information for a product.

    Attributes:
    - product_id: Foreign key to Product.
    - product_release: Release date of the product.
    - product_release_detail: Details about the product release.
    - product_release_link: Reference link for the product release.
    - product_eol: End of Life date of the product.
    - product_eol_detail: Details about the End of Life of the product.
    - product_eol_link: Reference link for the End of Life of the product.

    Relationships:
    - product: Relationship to Product for easy access to the associated product.
    """

    __tablename__ = 'product_mkt_life'
    __table_args__ = {'schema': 'brand_opl'}

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    product_release = db.Column(db.Date, nullable=True)
    product_release_detail = db.Column(db.String(255))
    product_release_link = db.Column(db.String(255))
    product_eol = db.Column(db.Date, nullable=True)
    product_eol_detail = db.Column(db.String(255))
    product_eol_link = db.Column(db.String(255))

    # Define the relationship to the Product model
    product = db.relationship('Product', backref=db.backref('mkt_life', lazy='dynamic'))


class Partner(db.Model):
    """
    Represents partners.

    Attributes:
    - partner_id: Unique identifier for the partner.
    - partner_name: Name of the partner.
    - persona_id: Persona ID for the partner.
    """

    __tablename__ = 'partners'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "partner_id"
    __term__ = "partner_name"

    partner_id = db.Column(db.String, primary_key=True)
    partner_name = db.Column(db.String(255), nullable=False)

    # Relationships
    product_partners = db.relationship('ProductPartners', backref='partner', lazy='dynamic')

class ProductPartners(db.Model):
    """
    Represents a many-to-many relationship between Product and Partners.

    Attributes:
    - product_id: Foreign key to Product.
    - partner_id: Foreign key to Partners.
    """

    __tablename__ = 'product_partners'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "partner_id"

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    partner_id = db.Column(db.String, db.ForeignKey('brand_opl.partners.partner_id'), primary_key=True)


class ProductComponents(db.Model):
    """
    Represents a many-to-many relationship between Product and Components.

    Attributes:
    - product_id: Foreign key to Product.
    - component_id: Foreign key to Components.
    """

    __tablename__ = 'product_components'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "component_id"

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    component_id = db.Column(db.String(255), nullable=False, primary_key=True)
    component_type = db.Column(db.String(255), nullable=False)

    # Define the relationship to the existing Product model
    product = db.relationship('Product', backref='components', foreign_keys=[product_id])




















from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Optional, InputRequired
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField, SelectMultipleField, DateField 

# Import DateField is duplicated, removed the second import
# from wtforms import DateField

# Below are the form classes for each taxonomy. Each is based on the wtforms
# specification. However, there are some additional variables to help with a
# few things:
#
#   form_choices        Used with forms that contain SelectField and
#                       SelectMultipleField. In some cases, the choices option
#                       for these two field types are usually taken from another
#                       table, which means they need to be set within the
#                       context of the Flask app. So this variable sets a
#                       mapping to data from another table, which the
#                       utils.get_choices_for_selectfields method renders and
#                       adds to the choices option of the relevant field. The
#                       mapping is as follows:
#                           'model'     The name of the model to pull data from.
#                           'value'     The column to use for the select field value
#                           'label'     The column to use for the select field label
#   mapped_data         This variable acts as a trigger to let the Flask app
#                       know that secondary table mapping is used. This is used
#                       to both get data and set data to the secondary table.

class MyForm(FlaskForm):
    product_name = TextAreaField('Product Name *', validators=[DataRequired()])
    product_description = TextAreaField('Product Description')
    upcoming_change = BooleanField('Upcoming Change')
    deprecated = BooleanField('Deprecated')
    
    # SelectField for Product Status
    product_status = SelectField('Status', choices=[('', 'Select'), ('Deprecated', 'Deprecated'), ('Upcoming', 'Upcoming'), ('Available', 'Available')])

    # SelectField for Product Status Details
    product_status_detail = SelectField('Status', choices=[('', 'Select'), ('General availability', 'General availability'), ('Live', 'Live'), ('Developer Preview', 'Developer Preview'), ('Technology Preview', 'Technology Preview'), ('Limited availability', 'Limited availability'), ('Service Preview', 'Service Preview'), ('Null', 'NULL')])

    # SelectField for Product Type
    product_type = SelectMultipleField('Product Type *', validators=[InputRequired()])

    # SelectField for Product Portfolio
    product_portfolio = SelectMultipleField('Portfolio')

    # Field for Product Notes
    product_notes = TextAreaField('Product Notes')

    # Field for Product References
    product_link = TextAreaField('Product Reference')
    link_description = TextAreaField('Reference Description')

    # Fields for Product Alias
    alias_name = TextAreaField('Alias Name')
    alias_type = SelectField('Alias Type', choices=[('Short', 'Short'), ('Acronym', 'Acronym'), ('Cli', 'Cli'), ('Former', 'Former')], validators=[InputRequired(Optional)])
    alias_approved = BooleanField('Alias Approved')
    previous_name = BooleanField('Previous Name')
    tech_docs = BooleanField('Approved For Tech Docs')
    tech_docs_cli = BooleanField('Approved For Tech Docs Code/CLI')
    alias_notes = TextAreaField('Alias Notes')

    # Fields for Product Mkt Life
    product_release = DateField('Release Date', format='%Y-%m-%d', validators=[Optional()])
    product_release_detail = TextAreaField('Release Detail')
    product_release_link = TextAreaField('Release Reference')
    product_eol = DateField('Product End Of Life (EOL) Date', format='%Y-%m-%d', validators=[Optional()])
    product_eol_detail = TextAreaField('Product End Of Life (EOL) Details')
    product_eol_link = TextAreaField('Product End Of Life (EOL) Reference')


    # Add a new field for selecting a partner
    partner = SelectMultipleField('In Partnership with', choices=[], coerce=str)

    # Add a new field for selecting a component
    component = SelectField('Parent', choices=[('', 'Select')], validators=[Optional()])
    component_type = SelectField('Component Type', choices=[('component', 'Component'), ('operator', 'Operator'), ('variant', 'Variant')], validators=[Optional()])

    submit = SubmitField('Add Product')

























from flask import Flask, render_template, flash, request
from flask_sqlalchemy import SQLAlchemy
from forms import MyForm
from models import db, Product, ProductType, ProductTypeMap, ProductPortfolios, ProductPortfolioMap, ProductNotes, ProductReferences, ProductAlias, ProductMktLife, ProductPartners, Partner, ProductComponents
from datetime import datetime

# For troubleshooting
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = Flask(__name__)
<data>

# Initialize the database
db.init_app(app)

# Define the index route
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Define the route to add a product
@app.route('/opl/add-product', methods=['GET', 'POST'])
def add_product():
    form = MyForm()
    success_message = None
    show_form = True

    # Initialize the variables here
    formatted_created_date = None
    formatted_last_updated_date = None

    # Populate product type choices
    form.product_type.choices = [(ptype.type_id, ptype.product_type) for ptype in ProductType.query.all()]

    # Populate product portfolio choices
    form.product_portfolio.choices = [(portfolio.category_id, portfolio.category_name) for portfolio in ProductPortfolios.query.all()]

    # Populate partner choices
    form.partner.choices = [(partner.partner_id, partner.partner_name) for partner in Partner.query.all()]

    # Populate component choices
    form.component.choices = [('', 'Select')] + [(component.product_id, component.product_name) for component in Product.query.all()]

    if form.validate_on_submit():
        # Logic for adding a new product
        created_date = datetime.now()

        # Create a new product instance
        new_product = Product(
            product_name=form.product_name.data,
            product_description=form.product_description.data,
            upcoming_change=form.upcoming_change.data,
            deprecated=form.deprecated.data,
            product_status=form.product_status.data if form.product_status.data != 'Select' else '',
            product_status_detail='NULL' if form.product_status.data == 'Deprecated' else form.product_status_detail.data,
            last_updated=created_date,
            created=created_date
        )

        # Add and commit the new product to the database
        db.session.add(new_product)
        db.session.commit()

        # Add product type mapping
        selected_product_types = form.product_type.data
        for product_type_id in selected_product_types:
            product_type_map = ProductTypeMap(product_id=new_product.product_id, type_id=product_type_id)
            db.session.add(product_type_map)

        # Add product portfolio mapping
        selected_portfolios = form.product_portfolio.data
        for portfolio_id in selected_portfolios:
            product_portfolio_map = ProductPortfolioMap(product_id=new_product.product_id, category_id=portfolio_id)
            db.session.add(product_portfolio_map)

        # Add Product Notes
        product_notes_data = form.product_notes.data
        if product_notes_data:
            product_notes = ProductNotes(product_id=new_product.product_id, product_note=product_notes_data)
            db.session.add(product_notes)

        # Add Product References
        product_references_data = []
        for i in range(len(request.form.getlist('product_link'))):
            product_link = request.form.getlist('product_link')[i]
            link_description = request.form.getlist('link_description')[i]

            if product_link and link_description:
                product_references_data.append({
                    'product_link': product_link,
                    'link_description': link_description
                })

        for reference_data in product_references_data:
            product_references = ProductReferences(
                product_id=new_product.product_id,
                product_link=reference_data['product_link'],
                link_description=reference_data['link_description']
            )
            db.session.add(product_references)

        # Add Product Alias
        product_alias_data = []
        alias_names = request.form.getlist('alias_name')
        alias_types = request.form.getlist('alias_type')
        alias_approved_list = request.form.getlist('alias_approved')
        previous_name_list = request.form.getlist('previous_name')
        tech_docs_list = request.form.getlist('tech_docs')
        tech_docs_cli_list = request.form.getlist('tech_docs_cli')
        alias_notes_list = request.form.getlist('alias_notes')

        for i in range(len(alias_names)):
            alias_name = alias_names[i]
            alias_type = alias_types[i]
            alias_approved = alias_approved_list[i].lower() == 'y' if i < len(alias_approved_list) else False
            previous_name = previous_name_list[i].lower() == 'y' if i < len(previous_name_list) else False
            tech_docs = tech_docs_list[i].lower() == 'y' if i < len(tech_docs_list) else False
            tech_docs_cli = tech_docs_cli_list[i].lower() == 'y' if i < len(tech_docs_cli_list) else False
            alias_notes = alias_notes_list[i] if i < len(alias_notes_list) else ''

            if alias_name:
                product_alias_data.append({
                    'alias_name': alias_name,
                    'alias_type': alias_type,
                    'alias_approved': alias_approved,
                    'previous_name': previous_name,
                    'tech_docs': tech_docs,
                    'tech_docs_cli': tech_docs_cli,
                    'alias_notes': alias_notes
                })

        # Loop to save aliases
        for alias_data in product_alias_data:
            # Directly use boolean values, no need for lower()
            alias_approved = alias_data['alias_approved']
            previous_name = alias_data['previous_name']
            tech_docs = alias_data['tech_docs']
            tech_docs_cli = alias_data['tech_docs_cli']

            # Create ProductAlias object and add to the session
            product_alias = ProductAlias(
                product_id=new_product.product_id,
                alias_name=alias_data['alias_name'],
                alias_type=alias_data['alias_type'],
                alias_approved=alias_approved,
                previous_name=previous_name,
                tech_docs=tech_docs,
                tech_docs_cli=tech_docs_cli,
                alias_notes=alias_data['alias_notes']
            )
            db.session.add(product_alias)

        # Add Product Components
        product_components_data = []
        component_ids = request.form.getlist('component')
        component_types = request.form.getlist('component_type')

        for i in range(len(component_ids)):
            component_id = component_ids[i]
            component_type = component_types[i]

            # Check if component_id is not 'Select'
            if component_id != 'Select':
                product_components_data.append({
                    'component_id': component_id,
                    'component_type': component_type
                })

        # Loop to save components
        for component_data in product_components_data:
            # Directly use boolean values, no need for lower()
            component_id = component_data['component_id']
            component_type = component_data['component_type']

            # Check if component_id is not 'Select' before saving to the database
            if component_id:
                # Create ProductComponent object and add to the session
                product_component = ProductComponents(
                    product_id=new_product.product_id,
                    component_id=component_id,
                    component_type=component_type
                )
                db.session.add(product_component)

        # Commit the changes to the database
        db.session.commit()
            
        # Commit changes outside the loop
        db.session.commit()

        # Format dates for display
        formatted_created_date = created_date.strftime('%Y-%m-%d')
        formatted_last_updated_date = created_date.strftime('%Y-%m-%d')

        # Set success message and hide the form
        success_message = f'Successfully added the product: {form.product_name.data}'
        show_form = False

    return render_template('opl/add.html', form=form, success_message=success_message,
                           show_form=show_form, formatted_created_date=formatted_created_date,
                           formatted_last_updated_date=formatted_last_updated_date)

# Define the route to edit a product
@app.route('/opl/edit-product', methods=['GET', 'POST'])
def edit_product():
    form = MyForm()

    if form.validate_on_submit():
        # Logic for editing the product
        return render_template('opl/edit.html', form=form, success_message=f'Successfully edited: {form.product_id.data}, {form.product_name.data}')

    return render_template('opl/edit.html', form=form)

# Run the application if executed directly
if __name__ == '__main__':
    with app.app_context():
        # Create all database tables
        db.create_all()
    app.run(debug=True)



















{% extends 'base.html' %}

{% block heading %}
<h1 class="pf-v5-c-title pf-m-4xl">Welcome to OPL</h1>
{% endblock %}

{% block content %}
<p>Add a product information.</p>

<br>

{% if show_form %}

<p style="color:red;">Fields marked with * are mandatory.</p>

<form method="post" action="{{ url_for('add_product') }}" id="my-form">
    {{ form.hidden_tag() }}

    <fieldset class="product-information-group">
    <legend>Product Information</legend>

        <div class="form-group">
            <div class="form-field">
                <label for="{{ form.product_name.id }}">{{ form.product_name.label }}</label>
                {{ form.product_name(cols=40) }}
            </div>


            <div class="form-field">
                <label for="{{ form.product_type.id }}">{{ form.product_type.label }}</label>
                <select id="{{ form.product_type.id }}" name="{{ form.product_type.name }}" multiple>
                    {% for value, label in form.product_type.choices %}
                    <option value="{{ value }}">{{ label }}</option>
                    {% endfor %}
                </select>
            </div>
        </div>


        <div class="form-group">
            
            <div class="form-field">
                <label for="{{ form.product_description.id }}">{{ form.product_description.label }}</label>
                {{ form.product_description(cols=40) }}
            </div>

            <div class="form-field">
                <label for="{{ form.product_portfolio.id }}">{{ form.product_portfolio.label }}</label>
                <select id="{{ form.product_portfolio.id }}" name="{{ form.product_portfolio.name }}" multiple>
                    {% for value, label in form.product_portfolio.choices %}
                    <option value="{{ value }}">{{ label }}</option>
                    {% endfor %}
                </select>
            </div>
        </div>

        <div class="form-group">
            <div class="form-field">
                <label for="{{ form.product_notes.id }}">{{ form.product_notes.label }}</label>
                {{ form.product_notes(cols=40) }}
            </div>
        </div>

    </fieldset>

    <br>
    
    <fieldset class="product-reference-group">
    <legend>Product Reference Information</legend>
    <div id="product-references">
        <div class="product-reference-pair">
            <div class="form-field">
                <label for="{{ form.product_link.id }}">Product Reference</label>
                {{ form.product_link(cols=40) }}
            </div>
    
            <div class="form-field">
                <label for="{{ form.link_description.id }}">Reference Description</label>
                {{ form.link_description(cols=40) }}
            </div>
    
            <div class="form-field buttons-row">
                <button type="button" class="add-reference">Add more</button>
                <button type="button" class="remove-reference" style="display: none;">Delete</button>
            </div>
        </div>
    </div>
    </fieldset>

    <br>

    <fieldset class="product-status-group">
    <legend>Product Status Details</legend>
    <div class="form-group">
        <div class="checkbox-field">
            {{ form.deprecated() }}
            <label for="{{ form.deprecated.id }}">{{ form.deprecated.label }}</label>
        </div>
    
        <div class="checkbox-field">
            {{ form.upcoming_change() }}
            <label for="{{ form.upcoming_change.id }}">{{ form.upcoming_change.label }}</label>
        </div>
    </div>

    <br>

    <div class="form-group">
        <div class="form-field">
            <label for="{{ form.product_status.id }}">Status</label>
            {{ form.product_status(id="status-dropdown", class="status-dropdown") }}
        </div>

        <div class="form-field">
            <label for="{{ form.product_status_detail.id }}">Status details</label>
            {{ form.product_status_detail(id="status-details-dropdown", class="status-details-dropdown") }}
        </div>
    </div>
    </fieldset>

    <br>

    <fieldset class="product-alias-group">
        <legend>Product Alias Information</legend>
        <div class="form-group">
            <div class="form-field">
                <label for="{{ form.alias_name.id }}">{{ form.alias_name.label }}</label>
                {{ form.alias_name(cols=40) }}
            </div>
                
            <div class="form-field">
                <label for="{{ form.alias_type.id }}">{{ form.alias_type.label }}</label>
                {{ form.alias_type(id="alias-type-dropdown", class="alias-type-dropdown") }}
            </div>       
        </div>

        <br>

        <div class="form-group">
            <div class="checkbox-field">
                {{ form.alias_approved() }}
                <label for="{{ form.alias_approved.id }}" data-toggle="tooltip"
                    title="Leaving it blank for unapproved aliases.">{{ form.alias_approved.label }}</label>
            </div>
        
            <div class="checkbox-field">
                {{ form.previous_name() }}
                <label for="{{ form.previous_name.id }}">{{ form.previous_name.label }}</label>
            </div>
        
            <div class="checkbox-field">
                {{ form.tech_docs() }}
                <label for="{{ form.tech_docs.id }}">{{ form.tech_docs.label }}</label>
            </div>
        
            <div class="checkbox-field">
                {{ form.tech_docs_cli() }}
                <label for="{{ form.tech_docs_cli.id }}">{{ form.tech_docs_cli.label }}</label>
            </div>
        </div>
        
        <br>

        <label for="{{ form.alias_notes.id }}">{{ form.alias_notes.label }}</label>
        {{ form.alias_notes(cols=40) }}

        <br>
        <button type="button" class="add-alias-group" style="margin-top: 10px;">Add more aliases</button>
        <button type="button" class="remove-alias-group" style="display: none;">Delete</button>
    </fieldset>

    <br>

    <fieldset class="product-release-info">
        <legend>Product Release Information</legend>
    
        <label for="{{ form.product_release.id }}">{{ form.product_release.label }}</label>
        {{ form.product_release() }}
    
        <br>
    
        <label for="{{ form.product_release_detail.id }}">{{ form.product_release_detail.label }}</label>
        {{ form.product_release_detail(cols=40) }}
    
        <br>
    
        <label for="{{ form.product_release_link.id }}">{{ form.product_release_link.label }}</label>
        {{ form.product_release_link(cols=40) }}
    </fieldset>
    
    <fieldset class="product-eol-info">
        <legend>Product End of Life Information</legend>
    
        <label for="{{ form.product_eol.id }}">{{ form.product_eol.label }}</label>
        {{ form.product_eol() }}
    
        <br>
    
        <label for="{{ form.product_eol_detail.id }}">{{ form.product_eol_detail.label }}</label>
        {{ form.product_eol_detail(cols=40) }}
    
        <br>
    
        <label for="{{ form.product_eol_link.id }}">{{ form.product_eol_link.label }}</label>
        {{ form.product_eol_link(cols=40) }}
    </fieldset>

    <br><br>

    <fieldset class="product-partner-group">
    <legend>Product Partners Information</legend>
        <div class="form-field">
            <label for="{{ form.partner.id }}">{{ form.partner.label }}</label>
            <select id="{{ form.partner.id }}" name="{{ form.partner.name }}" multiple>
                {% for value, label in form.partner.choices %}
                <option value="{{ value }}">{{ label }}</option>
                {% endfor %}
            </select>
        </div>
    </fieldset>

    <br><br>

    <fieldset class="product-component-group">
    <legend>Product Parent Information</legend>
        <div class="form-field">
            <label for="{{ form.component.id }}">{{ form.component.label }}</label>
            <select id="{{ form.component.id }}" name="{{ form.component.name }}">
                {% for value, label in form.component.choices %}
                <option value="{{ value }}">{{ label }}</option>
                {% endfor %}
            </select>
        </div>

        <div class="form-field">
            <label for="{{ form.component_type.id }}">{{ form.component_type.label }}</label>
            <select id="{{ form.component_type.id }}" name="{{ form.component_type.name }}">
                {% for value, label in form.component_type.choices %}
                <option value="{{ value }}">{{ label }}</option>
                {% endfor %}
            </select>
        </div>
        <br>
        <button type="button" class="add-component-group" style="margin-top: 10px;">Add more components</button>
        <button type="button" class="remove-component-group" style="display: none;">Delete</button>
    </fieldset>


    <br><br>

  
    {{ form.submit(style="background-color: #0a63ca; color: #ffffff; font-size: 20px; padding: 10px; border: none;
    border-radius: 5px; cursor: pointer;") }}
</form>

<script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
<script src="{{ url_for('static', filename='scripts/status.js') }}"></script>
<script src="{{ url_for('static', filename='scripts/preferences.js') }}"></script>
<script src="{{ url_for('static', filename='scripts/alias.js') }}"></script>
<script src="{{ url_for('static', filename='scripts/parent.js') }}"></script>

{% endif %}

{% if success_message %}
<p class="success">{{ success_message }}</p>
<br>
<a href="{{ url_for('add_product') }}" class="button-link">Add more products</a>
{% endif %}
{% endblock %}



























$(document).ready(function () {
    // Add more Product Alias Information groups
    $(document).on("click", ".add-alias-group", function () {
        var newAliasGroup = $(".product-alias-group:first").clone();
        newAliasGroup.find('input, select').val('');
        newAliasGroup.find('.remove-alias-group').show();
        newAliasGroup.find('.add-alias-group').remove(); // Remove the Add button in the cloned group
        $(".product-alias-group:last").after(newAliasGroup);
    });

    // Remove the current Product Alias Information group
    $(document).on("click", ".remove-alias-group", function () {
        if ($(".product-alias-group").length > 1) {
            $(this).closest(".product-alias-group").remove();
        }
    });
});










$(document).ready(function () {
    // Add more Product Component Information groups
    $(document).on("click", ".add-component-group", function () {
        var newComponentGroup = $(".product-component-group:first").clone();
        newComponentGroup.find('select').val('');
        newComponentGroup.find('.remove-component-group').show();
        newComponentGroup.find('.add-component-group').remove(); // Remove the Add button in the cloned group
        $(".product-component-group:last").after(newComponentGroup);
    });

    // Remove the current Product Component Information group
    $(document).on("click", ".remove-component-group", function () {
        if ($(".product-component-group").length > 1) {
            $(this).closest(".product-component-group").remove();
        }
    });
});














$(document).ready(function () {
        // Add more Product Reference and Reference Description pairs
        $(".add-reference").click(function () {
            var referencePair = $(".product-reference-pair:first").clone();
            referencePair.find("input, textarea").val('');
            referencePair.find(".add-reference").hide();
            referencePair.find(".remove-reference").show();
            $("#product-references").append(referencePair);
        });

        // Remove the current Product Reference and Reference Description pair
        $(document).on("click", ".remove-reference", function () {
            $(this).closest(".product-reference-pair").remove();
        });
    });














function updateStatusDetailsChoices() {
    var selectedStatus = $('#status-dropdown').val();
    var statusDetailsDropdown = $('#status-details-dropdown');

    // Reset choices to initial state
    statusDetailsDropdown.empty();

    if (selectedStatus === 'Deprecated') {
        // If Deprecated is selected, show a default option and 'NULL' in Status Details
        statusDetailsDropdown.append($('<option>', { value: '', text: 'Select' }));
        statusDetailsDropdown.append($('<option>', { value: 'Null', text: 'NULL' }));
    } else {
        // If any other status is selected, show all choices including 'NULL'
        $.each(initialStatusDetailsChoices, function (value, label) {
            statusDetailsDropdown.append($('<option>', { value: value, text: label }));
        });
        // Include 'NULL' as an option for other statuses
        statusDetailsDropdown.append($('<option>', { value: 'Null', text: 'NULL' }));
    }
}
