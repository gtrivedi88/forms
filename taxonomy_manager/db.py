sqlalchemy.exc.NoForeignKeysError: Could not determine join condition between parent/child tables on relationship ProductPortfolioMap.product_notes - there are no foreign keys linking these tables.  Ensure that referencing columns are associated with a ForeignKey or ForeignKeyConstraint, or specify a 'primaryjoin' expression.



from db import db
import uuid
from datetime import datetime

# Below are the models for each taxonomy
# They use the standard SQLAlchemy modeling, but with a few added bits and pieces:
#   __tablename__       SQLAlchemy attribute to map the model to a specific table
#   __table_args__      SQLAlchemy attribute to set options for the model.
#                       Mostly used to define the PGSQL schema.
#   __uuid__            Defines the field to use as the UUID. Since the UUID
#                       field name is different for each model, this is a way to
#                       standardize the field names
#   __term__            Defines the field to use as the term name. This is
#                       similar in function as the UUID.

# OPL DATA MODELS

# Define the OplPartner model (commented out for brevity)

class Product(db.Model):
    __tablename__ = 'product'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "product_name"
    __hidden__ = True

    # Product fields
    product_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    product_name = db.Column(db.String(255), nullable=False)
    product_description = db.Column(db.String)
    upcoming_change = db.Column(db.Boolean)
    deprecated = db.Column(db.Boolean)
    product_status = db.Column(db.String(255))
    last_updated = db.Column(db.Date)
    created = db.Column(db.Date)
    product_status = db.Column(db.String(255))
    product_status_detail = db.Column(db.String(255))

    # Relationships
    product_type_maps = db.relationship('ProductTypeMap', backref='product', lazy='dynamic')

class ProductType(db.Model):
    __tablename__ = 'product_types'
    __table_args__ = {'schema': 'brand_opl'}

    # ProductType fields
    type_id = db.Column(db.String, primary_key=True)
    product_type = db.Column(db.String(255), nullable=False)

class ProductTypeMap(db.Model):
    __tablename__ = 'product_types_map'
    __table_args__ = {'schema': 'brand_opl'}

    # ProductTypeMap fields
    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    type_id = db.Column(db.String, db.ForeignKey('brand_opl.product_types.type_id'), primary_key=True)

class ProductPortfolios(db.Model):
    __tablename__ = 'product_portfolios'
    __table_args__ = {'schema': 'brand_opl'}

    # ProductPortfolios fields
    category_id = db.Column(db.String, primary_key=True)
    category_name = db.Column(db.String(255), nullable=False)

    # Relationships
    product_portfolio_map = db.relationship('ProductPortfolioMap', backref='portfolio', lazy='dynamic')

class ProductPortfolioMap(db.Model):
    __tablename__ = 'product_portfolio_map'
    __table_args__ = {'schema': 'brand_opl'}

    # ProductPortfolioMap fields
    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    category_id = db.Column(db.String, db.ForeignKey('brand_opl.product_portfolios.category_id'), primary_key=True)



   # Add a relationship to the ProductNotes model
    product_notes = db.relationship('ProductNotes', backref='product', lazy='dynamic')

class ProductNotes(db.Model):
    __tablename__ = 'product_notes'
    __table_args__ = {'schema': 'brand_opl'}

    # ProductNotes fields
    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    product_note = db.Column(db.String(255), nullable=False)

    def __init__(self, product_note):
        self.product_note = product_note




from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from forms import MyForm
from models import db, Product, ProductType, ProductTypeMap, ProductPortfolios, ProductPortfolioMap, ProductNotes
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
        selected_notes = form.product_notes.data
        for note in selected_notes:
            product_note = ProductNotes(product_note=note)
            new_product.product_notes.append(product_note)
        
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
