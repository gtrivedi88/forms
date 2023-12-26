from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, TextAreaField, DateField, BooleanField, SelectField
from wtforms import DateField

# Below are the form classes for each taxonomy. Each is based on the wtforms
# specification. However, there are some additional variables to help with a
# few things:
#
#   form_choices        Used with forms that contain SelectField and
#                       SelectMultipleField. In some cases, the choices option
#                       for these two field types are usually taken from another
#                       table. which means they need to be set within the
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
    product_name = StringField('Product Name *', validators=[DataRequired()])
    product_description = TextAreaField('Product Description')
    upcoming_change = BooleanField('Upcoming Change')
    deprecated = BooleanField('Deprecated')
    product_status = StringField('Product Status')
    product_status_detail = TextAreaField('Product Status Detail')
    product_type = SelectField('Product Type', validators=[DataRequired()])
    product_portfolio = SelectField('Portfolio')
    submit = SubmitField('Add Product')



