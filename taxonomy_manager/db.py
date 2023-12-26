sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedColumn) column "id" of relation "product" does not exist
LINE 1: INSERT INTO brand_opl.product (id, product_name, product_des...
                                       ^

[SQL: INSERT INTO brand_opl.product (id, product_name, product_description, upcoming_change, deprecated, product_status, last_updated, created, product_status_detail) VALUES (%(id)s, %(product_name)s, %(product_description)s, %(upcoming_change)s, %(deprecated)s, %(product_status)s, %(last_updated)s, %(created)s, %(product_status_detail)s)]
[parameters: {'id': '29325b93-22e7-44a6-b8f5-986f9167495d', 'product_name': 'DJ', 'product_description': '', 'upcoming_change': False, 'deprecated': False, 'product_status': '', 'last_updated': datetime.date(2023, 12, 20), 'created': datetime.date(2023, 12, 28), 'product_status_detail': ''}]
(Background on this error at: https://sqlalche.me/e/20/f405)


from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from forms import MyForm
from models import db, Product
from datetime import datetime
import uuid

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
        if not form.product_name.data or not form.last_updated.data or not form.created.data:
            flash('Please enter data in all the required fields.', 'error')
        else:
            new_product = Product(
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
