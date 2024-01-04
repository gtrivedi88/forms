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
