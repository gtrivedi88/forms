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

    alias_id = db.Column(db.String, default=lambda: str(uuid.uuid4()))
    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True, nullable=False)
    alias_name = db.Column(db.String(255), nullable=False)

    # Define the relationship to the Product model
    product = db.relationship('Product', backref=db.backref('aliases', lazy='dynamic'))



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

    <fieldset class="product-alias-group">
        <legend>Product Alias Information</legend>
        <label for="{{ form.alias_name.id }}">{{ form.alias_name.label }}</label>
        {{ form.alias_name(cols=40) }}
        
        <br><br>
        
        <label for="{{ form.alias_type.id }}">{{ form.alias_type.label }}</label>
        {{ form.alias_type(id="alias-type-dropdown", class="alias-type-dropdown") }}
        
        <br><br>

        <button type="button" class="add-alias-group" style="margin-top: 10px;">Add more aliases</button>
        <button type="button" class="remove-alias-group"
            style="background-color: #ff0000; color: white; margin-top: 10px; padding: 5px 10px; border: none; border-radius: 4px; cursor: pointer; display: none;">Delete</button>
    </fieldset>

    <br><br>
    
    {{ form.submit(style="background-color: #1a73e8; color: #ffffff;") }}
</form>

<script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
<script src="{{ url_for('static', filename='scripts/status.js') }}"></script>
<script src="{{ url_for('static', filename='scripts/preferences.js') }}"></script>
<script src="{{ url_for('static', filename='scripts/alias.js') }}"></script>

{% endif %}

{% if success_message %}
<p class="success">{{ success_message }}</p>
<br><br>
<a href="{{ url_for('add_product') }}" class="button-link">Add more products</a>
{% endif %}
{% endblock %}


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
        
        product_alias_data = []
        for i in range(len(request.form.getlist('alias_name'))):
            alias_name = request.form.getlist('alias_name')[i]
            alias_type = request.form.getlist('alias_type')[i]

            if alias_name and alias_type:
                product_alias_data.append({
                    'alias_name': alias_name,
                    'alias_type': alias_type
                })
        for alias_data in product_alias_data:
            product_alias = ProductAlias(
                product_id=new_product.product_id,
                alias_name=alias_data['alias_name'],
                alias_type=alias_data['alias_type']
            )
            db.session.add(product_alias)

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
