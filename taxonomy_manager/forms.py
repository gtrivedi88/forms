from wtforms import Form, BooleanField, StringField, TextAreaField, SelectField, SelectMultipleField, validators, widgets
from wtforms_sqlalchemy.fields import QuerySelectMultipleField

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

class FormCategories(Form):
    category_name = StringField('Category Name', validators = [validators.InputRequired()])
    category_abstract = TextAreaField('Category Abstract')
    doc_attribute = StringField('Doc Attribute', validators = [validators.InputRequired()])

class FormContentType(Form):
    content_type = StringField('Content Type', validators = [validators.InputRequired()])
    content_defintion = TextAreaField('Content Definition')
    content_purpose = TextAreaField('Content Purpose')
    doc_attribute = StringField('Doc Attribute', validators = [validators.InputRequired()])

class FormIndustry(Form):
    industry = StringField('Industry', validators = [validators.InputRequired()])
    doc_attribute = StringField('Doc Attribute', validators = [validators.InputRequired()])

class FormJobType(Form):
    form_choices={'metadata_personas': {'model': 'Persona', 'value': 'persona_id', 'label': 'persona_name'}}
    mapped_data={'metadata_personas': 'Persona'}
    job_name = StringField('Job Name', validators = [validators.InputRequired()])
    doc_attribute = StringField('Doc Attribute', validators = [validators.InputRequired()])
    metadata_personas = SelectMultipleField('Personas')

class FormJourneyStage(Form):
    journey_name = StringField('Journey Name', validators = [validators.InputRequired()])
    journey_abstract = StringField('Journey Abstract')
    doc_attribute = StringField('Doc Attribute', validators = [validators.InputRequired()])

class FormModType(Form):
    mod_type = StringField('Module Type', validators = [validators.InputRequired()])
    doc_attribute = StringField('Doc Attribute', validators = [validators.InputRequired()])

class FormPartnerAttribute(Form):
    form_choices={'partner_id': {'model': 'OplPartner', 'value': 'partner_id', 'label': 'partner_name'}}
    partner_id = SelectField('Partner')
    doc_attribute = StringField('Doc Attribute', validators = [validators.InputRequired()])

class FormPersona(Form):
    persona_name = StringField('Persona Name', validators = [validators.InputRequired()])
    persona_abstract = StringField('Persona Abstract')
    doc_attribute = StringField('Doc Attribute', validators = [validators.InputRequired()])

class FormPlatform(Form):
    platform = StringField('Platform', validators = [validators.InputRequired()])
    doc_attribute = StringField('Doc Attribute', validators = [validators.InputRequired()])

class FormProductAttribute(Form):
    form_choices={'product_id': {'model': 'OplProduct', 'value': 'product_id', 'label': 'product_name'}}
    product_id = SelectField('Product')
    doc_attribute = StringField('Doc Attribute', validators = [validators.InputRequired()])
    alias_id = StringField('Alias ID', validators = [validators.InputRequired()])

class FormProficiency(Form):
    proficiency = StringField('Proficiency', validators = [validators.InputRequired()])
    doc_attribute = StringField('Doc Attribute', validators = [validators.InputRequired()])

class FormSolution(Form):
    solution = StringField('Solution', validators = [validators.InputRequired()])
    doc_attribute = StringField('Doc Attribute', validators = [validators.InputRequired()])

class FormTopic(Form):
    topic = StringField('Topic', validators = [validators.InputRequired()])
    doc_attribute = StringField('Doc Attribute', validators = [validators.InputRequired()])
