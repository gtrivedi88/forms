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

        # If product_status is Deprecated, set product_status_detail to 'NULL'
        if form.product_status.data == 'Deprecated':
                form.product_status_detail.data = 'NULL'


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

    save_to_database = any(component_id != 'Select' and component_type != 'Select' for component_id, component_type in zip(component_ids, component_types))

    if save_to_database:
        for component_id, component_type in zip(component_ids, component_types):
            product_components_data.append({
                'component_id': component_id,
                'component_type': component_type
            })

        # Loop to save components
        for component_data in product_components_data:
            component_id = component_data['component_id']
            component_type = component_data['component_type']

            # Assuming you have a ProductComponents model with appropriate fields
            product_component = ProductComponents(
                product_id=new_product.product_id,
                component_id=component_id,
                component_type=component_type
            )
            db.session.add(product_component)


            
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
