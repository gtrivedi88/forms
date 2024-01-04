label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

input,
textarea,
select {
    padding: 5px;
    margin-bottom: 10px;
}

button {
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}

.checkbox-row {
    display: flex;
    align-items: center;
}

.checkbox-row input {
    margin-right: 10px;
}

.button-link {
    display: inline-block;
    padding: 10px 20px;
    background-color: #1a73e8;
    color: white;
    text-decoration: none;
    border-radius: 12px;
}

.success {
    color: green;
    font-weight: bold;
}

.product-reference-pair {
    display: flex;
}

.form-group {
    display: flex;
}

.form-field {
    flex: 1;
    /* Adjust the width as needed */
}

.checkbox-field {
    display: flex;
    flex: auto;
}

.checkbox-field input {
    margin-right: 10px;
    /* Adjust the space between the checkbox and label */
}

.buttons-row {
    align-items: center;
    margin-top: 35px;
}

.buttons-row button {
    margin-left: 10px;
}

.remove-reference {
    background-color: #ff0000;
    color: white;
}

.remove-reference:hover {
    background-color: #cc0000;
}




from flask import Flask, render_template, flash, request
from flask_sqlalchemy import SQLAlchemy
from forms import MyForm
from models import db, Product, ProductType, ProductTypeMap, ProductPortfolios, ProductPortfolioMap, ProductNotes, ProductReferences, ProductAlias
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


    if form.validate_on_submit():
        # Logic for adding a new product
        created_date = datetime.now()

        # Create a new product instance
        new_product = Product(
            product_name=form.product_name.data,
            product_description=form.product_description.data,
            upcoming_change=form.upcoming_change.data,
            deprecated=form.deprecated.data,
            product_status=form.product_status.data,
            last_updated=created_date,
            created=created_date,
            product_status_detail=form.product_status_detail.data
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

        # Create a new alias instance
            new_alias = ProductAlias(
                product_id=new_product.product_id,
                alias_name=form.alias_name.data,
                alias_type=form.alias_type.data,
                alias_approved=form.alias_approved.data,
                previous_name=form.previous_name.data,
                tech_docs=form.tech_docs.data,
                tech_docs_cli=form.tech_docs_cli.data,
                alias_notes=form.alias_notes.data
            )
            db.session.add(new_alias)
        
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

<br><br>

{% if show_form %}

<p style="color:red;">Fields marked with * are mandatory.</p>

<form method="post" action="{{ url_for('add_product') }}">
    {{ form.hidden_tag() }}

    <label for="{{ form.product_name.id }}">{{ form.product_name.label }}</label>
    {{ form.product_name(row=4, cols=40) }}

    <br><br>

    <label for="{{ form.product_description.id }}">{{ form.product_description.label }}</label>
    {{ form.product_description(cols=40) }}

    <br><br>

    <label for="{{ form.product_portfolio.id }}">{{ form.product_portfolio.label }}</label>
    <select id="{{ form.product_portfolio.id }}" name="{{ form.product_portfolio.name }}" multiple>
        {% for value, label in form.product_portfolio.choices %}
        <option value="{{ value }}">{{ label }}</option>
        {% endfor %}
    </select>

    <br><br>

    <label for="{{ form.product_notes.id }}">{{ form.product_notes.label }}</label>
    {{ form.product_notes() }}

    <br><br>

    <label for="{{ form.product_type.id }}">{{ form.product_type.label }}</label>
    <select id="{{ form.product_type.id }}" name="{{ form.product_type.name }}" multiple>
        {% for value, label in form.product_type.choices %}
        <option value="{{ value }}">{{ label }}</option>
        {% endfor %}
    </select>

    <br><br>

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


    <br><br>

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

    <br><br>

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

    <br><br>

    <label for="{{ form.alias_name.id }}">{{ form.alias_name.label }}</label>
    {{ form.alias_name(cols=40) }}
    
    <br><br>
    
    <label for="{{ form.alias_type.id }}">{{ form.alias_type.label }}</label>
    {{ form.alias_type(id="alias-type-dropdown", class="alias-type-dropdown") }}
    
    <br><br>

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
    
    <br><br>

    <label for="{{ form.alias_notes.id }}">{{ form.alias_notes.label }}</label>
    {{ form.alias_notes(cols=40) }}

    <br><br>

    {{ form.submit(style="background-color: #1a73e8; color: #ffffff;") }}
</form>

<script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
<script src="{{ url_for('static', filename='scripts/status.js') }}"></script>
<script src="{{ url_for('static', filename='scripts/preferences.js') }}"></script>

{% endif %}

{% if success_message %}
<p class="success">{{ success_message }}</p>
<br><br>
<a href="{{ url_for('add_product') }}" class="button-link">Add more products</a>
{% endif %}
{% endblock %}




from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField, SelectMultipleField

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
    product_status = SelectField('Status', choices=[('Deprecated', 'Deprecated'), ('Upcoming', 'Upcoming'), ('Available', 'Available')])

    # SelectField for Product Status Details
    product_status_detail = SelectField('Status', choices=[('General Availability', 'General Availability'), ('Live', 'Live'), ('Developer Preview', 'Developer Preview'), ('Technology Preview', 'Technology Preview'), ('Limited Availability', 'Limited Availability'), ('Service Preview', 'Service Preview'), ('Null', 'NULL')])

    # SelectField for Product Type
    product_type = SelectMultipleField('Product Type', validators=[DataRequired()])

    # SelectField for Product Portfolio
    product_portfolio = SelectMultipleField('Portfolio')

    # Field for Product Notes
    product_notes = TextAreaField('Product Notes')

    # Field for Product References
    product_link = TextAreaField('Product Reference')
    link_description = TextAreaField('Reference Description')

    # Fields for Product Alias
    alias_name = StringField('Alias Name *', validators=[DataRequired()])
    alias_type = SelectField('Alias Type *', choices=[('Short', 'Short'), ('Acronym', 'Acronym'), ('Cli', 'Cli'), ('Former', 'Former')], validators=[DataRequired()])
    alias_approved = BooleanField('Alias Approved')
    previous_name = BooleanField('Previous Name')
    tech_docs = BooleanField('Approved For Tech Docs')
    tech_docs_cli = BooleanField('Approved For Tech Docs Code/CLI')
    alias_notes = TextAreaField('Alias Notes')

    submit = SubmitField('Add Product')





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



