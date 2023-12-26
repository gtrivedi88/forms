from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from forms import MyForm
from models import db, Product
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    success_message = None
    show_form = True  # Flag to determine whether to display the form

    if form.validate_on_submit():
        if not form.product_id.data or not form.product_name.data or not form.last_updated.data or not form.created.data:
            flash('Please enter data in all the required fields.', 'error')
        else:
            new_product = Product(
                product_id=form.product_id.data,
                product_name=form.product_name.data,
                product_description=form.product_description.data,
                upcoming_change=form.upcoming_change.data,
                deprecated=form.deprecated.data,
                product_status=form.product_status.data,
                last_updated=form.last_updated.data,
                created=form.created.data,
                product_status_detail=form.product_status_detail.data
            )
            db.session.add(new_product)
            db.session.commit()
            success_message = (f'Successfully added the following product: {form.product_name.data}')
            show_form = False  # Set to False to hide the form after successful submission

    return render_template('index.html', form=form, success_message=success_message, show_form=show_form)

@app.route('/opl/edit-product', methods=['GET', 'POST'])
def edit_product():
    form = MyForm()

    if form.validate_on_submit():
        # Logic for editing the product
        return render_template('opl/edit.html', form=form, success_message=f'Successfully edited: {form.product_id.data}, {form.product_name.data}')

    return render_template('opl/edit.html', form=form)

@app.route('/opl/view-product', methods=['GET'])
def view_product():
    return render_template('opl/view.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)






from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from forms import MyForm
from models import db, Product
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/opl/add-product', methods=['GET', 'POST'])
def add_product():
    form = MyForm()
    success_message = None
    show_form = True  # Flag to determine whether to display the form

    if form.validate_on_submit():
        if not form.product_id.data or not form.product_name.data or not form.last_updated.data or not form.created.data:
            flash('Please enter data in all the required fields.', 'error')
        else:
            new_product = Product(
                product_id=form.product_id.data,
                product_name=form.product_name.data,
                product_description=form.product_description.data,
                upcoming_change=form.upcoming_change.data,
                deprecated=form.deprecated.data,
                product_status=form.product_status.data,
                last_updated=form.last_updated.data,
                created=form.created.data,
                product_status_detail=form.product_status_detail.data
            )
            db.session.add(new_product)
            db.session.commit()
            success_message = (f'Successfully added the following product: {form.product_name.data}')
            show_form = False  # Set to False to hide the form after successful submission

    return render_template('opl/add.html', form=form, success_message=success_message, show_form=show_form)

@app.route('/opl/edit-product', methods=['GET', 'POST'])
def edit_product():
    form = MyForm()

    if form.validate_on_submit():
        # Logic for editing the product
        return render_template('opl/edit.html', form=form, success_message=f'Successfully edited: {form.product_id.data}, {form.product_name.data}')

    return render_template('opl/edit.html', form=form)

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

<form method="post" action="/">
    {{ form.hidden_tag() }}

    <label for="{{ form.product_id.id }}">{{ form.product_id.label }}</label>
    {{ form.product_id(size=20) }}

    <br><br>

    <label for="{{ form.product_name.id }}">{{ form.product_name.label }}</label>
    {{ form.product_name(size=20) }}

    <br><br>

    <label for="{{ form.product_description.id }}">{{ form.product_description.label }}</label>
    {{ form.product_description(rows=4, cols=50) }}

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
    {{ form.product_status(size=20) }}

    <br><br>

    <label for="{{ form.last_updated.id }}">{{ form.last_updated.label }}</label>
    {{ form.last_updated() }}

    <br><br>

    <label for="{{ form.created.id }}">{{ form.created.label }}</label>
    {{ form.created() }}

    <br><br>

    <label for="{{ form.product_status_detail.id }}">{{ form.product_status_detail.label }}</label>
    {{ form.product_status_detail(rows=4, cols=50) }}

    <br><br>

    {{ form.submit(style="background-color: #1a73e8; color: #ffffff;") }}
</form>
{% endif %}

{% if success_message %}
<p class="success">{{ success_message }}</p>
<br><br>
<a href="{{ url_for('index') }}" class="button-link">Add more products</a>
{% endif %}
{% endblock %}



{% extends 'base.html' %}

{% block heading %}
<h1 class="pf-v5-c-title pf-m-4xl">Welcome to OPL</h1>
{% endblock %}


{% block content %}
<p>View a product information.</p>
{% endblock %}




class Product(db.Model):
    __tablename__ = 'product'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "product_name"
    __hidden__ = True
    id = db.Column(db.String(255), primary_key=True, default=str(uuid.uuid4()))
    product_name = db.Column(db.String(255), nullable=False)
    product_description = db.Column(db.String)
    upcoming_change = db.Column(db.Boolean)
    deprecated = db.Column(db.Boolean)
    product_status = db.Column(db.String(255))
    last_updated = db.Column(db.Date)
    created = db.Column(db.Date)
    product_status_detail = db.Column(db.String(255))
