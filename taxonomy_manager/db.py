from db import db
import uuid
from datetime import datetime




class Product(db.Model):
    __tablename__ = 'product'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "product_name"
    __hidden__ = True
    product_id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    product_name = db.Column(db.String(255), nullable=False)
    product_description = db.Column(db.String)
    upcoming_change = db.Column(db.Boolean)
    deprecated = db.Column(db.Boolean)
    product_status = db.Column(db.String(255))
    last_updated = db.Column(db.Date)
    created = db.Column(db.Date)
    product_status_detail = db.Column(db.String(255))
    # ccs_data_metadata_product_attributes = db.relationship('ProductAttribute', lazy='subquery', back_populates='brand_opl_product')
    # brand_opl_product_alias = db.relationship('OplProductAlias', lazy='subquery', back_populates='brand_opl_product')


    # Add a relationship to the ProductType model
    product_type_maps = db.relationship('ProductTypeMap', backref='product', lazy='dynamic')

class ProductType(db.Model):
    __tablename__ = 'product_types'
    __table_args__ = {'schema': 'brand_opl'}

    type_id = db.Column(db.String, primary_key=True)
    product_type = db.Column(db.String, nullable=False)

class ProductTypeMap(db.Model):
    __tablename__ = 'product_types_map'
    __table_args__ = {'schema': 'brand_opl'}

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    type_id = db.Column(db.String, db.ForeignKey('brand_opl.product_types.type_id'), primary_key=True)



from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, TextAreaField, DateField, BooleanField, SelectField
from wtforms import DateField



class MyForm(FlaskForm):
    product_name = StringField('Product Name *', validators=[DataRequired()])
    product_description = TextAreaField('Product Description')
    upcoming_change = BooleanField('Upcoming Change')
    deprecated = BooleanField('Deprecated')
    product_status = SelectField('Product Status', choices=[('deprecated', 'Deprecated'), ('upcoming', 'Upcoming'), ('available', 'Available')])
    product_status_detail = TextAreaField('Product Status Detail')
    product_portfolio = SelectField('Portfolio', coerce=str)
    product_type = SelectField('Product Type', validators=[DataRequired()])
    submit = SubmitField('Add Product')
    


from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from forms import MyForm
from models import db, Product, ProductTypeMap, ProductType
from datetime import datetime

# For troubleshooting
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = Flask(__name__)
<data>


db.init_app(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/opl/add-product', methods=['GET', 'POST'])
def add_product():
    form = MyForm()
    success_message = None
    show_form = True

    # Always populate product type choices, even on GET requests
    form.product_type.choices = [(ptype.type_id, ptype.product_type) for ptype in ProductType.query.all()]

    # Initialize the variables here
    formatted_created_date = None
    formatted_last_updated_date = None

    if form.validate_on_submit():
        created_date = datetime.now()

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
        db.session.add(new_product)
        db.session.commit()

        selected_product_type_id = form.product_type.data

        product_type_map = ProductTypeMap(product_id=new_product.product_id, type_id=selected_product_type_id)
        db.session.add(product_type_map)
        db.session.commit()

        formatted_created_date = created_date.strftime('%Y-%m-%d')
        formatted_last_updated_date = created_date.strftime('%Y-%m-%d')

        success_message = f'Successfully added the product: {form.product_name.data}'
        show_form = False

    return render_template('opl/add.html', form=form, success_message=success_message,
                           show_form=show_form, formatted_created_date=formatted_created_date,
                           formatted_last_updated_date=formatted_last_updated_date)

if __name__ == '__main__':
    with app.app_context():
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
    {{ form.product_name(size=20, style="width: 768px;") }}

    <br><br>

    <label for="{{ form.product_description.id }}">{{ form.product_description.label }}</label>
    {{ form.product_description(rows=4, cols=70) }}

    <br><br>

    <div class="checkbox-row">
        {{ form.upcoming_change() }}
        <label for="{{ form.upcoming_change.id }}">{{ form.upcoming_change.label }}</label>
    </div>

    <br><br>

    <div class="checkbox-row">
        {{ form.deprecated() }}
        <label for="{{ form.deprecated.id }}">{{ form.deprecated.label }}</label>
    </div>

    <br><br>

    <label for="{{ form.product_status.id }}">{{ form.product_status.label }}</label>
    {{ form.product_status() }}

    <br><br>

    <label for="{{ form.product_status_detail.id }}">{{ form.product_status_detail.label }}</label>
    {{ form.product_status_detail(rows=4, cols=70) }}

    <br> <br>

    <label for="{{ form.product_type.id }}">{{ form.product_type.choices.label }}</label>
    {{ form.product_type() }}

    <br><br>

    {{ form.submit(style="background-color: #1a73e8; color: #ffffff;") }}
</form>
{% endif %}

{% if success_message %}
<p class="success">{{ success_message }}</p>
<br><br>
<a href="{{ url_for('add_product') }}" class="button-link">Add more products</a>
{% endif %}
{% endblock %}
