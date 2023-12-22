from werkzeug.exceptions import abort
import taxonomy_manager.models as models
import math

# Additional functions to make life a bit easier in the Flask app

# Function to convert a snake_case name to a ClassName
def convert_to_classname(snake_case):
     return snake_case.replace("_", " ").title().replace(" ", "")

# Function to convert a snake_case name to a title
def convert_to_title(snake_case):
     return snake_case.replace("_", " ").title()

# Populate a selectfield or multiselectfield with choices from another table
def get_choices_for_selectfields(form):
    if hasattr(form, 'form_choices'):
        form_choices = form.form_choices
        for rel, rel_dict in form_choices.items():
            selectfield = getattr(form, rel)
            choices = []
            SelectClass = getattr(models, rel_dict['model'])
            for row in SelectClass.query.all():
                value = getattr(row, rel_dict['value'])
                label = getattr(row, rel_dict['label'])
                choices.append((value, label))
            choices.sort(key = lambda x: x[1])
            setattr(selectfield, 'choices', choices)


# Get mapped selections saved in a secondary table
def get_mapped_data(form, taxonomy, request):
    if hasattr(form, 'mapped_data'):
        for field, model_name in form.mapped_data.items():
            mapped_data_selections = getattr(form, field)
            mapped_data_column = getattr(taxonomy, field)
            model = getattr(models, model_name)
            rows = model.query.all()
            choice_id = form.form_choices[field]['value']
            for selection in mapped_data_column:
                mapped_data_selections.data.append(getattr(selection, choice_id))

# Save mapped selections in a secondary table
def set_mapped_data(form, taxonomy, request):
    if hasattr(form, 'mapped_data'):
        for field, model_name in form.mapped_data.items():
            selections = dict(request.form.lists())[field]
            mapped_data_column = getattr(taxonomy, field)
            model = getattr(models, model_name)
            mapped_data_column.clear()
            for selection in selections:
                entry = model.query.get(selection)
                if entry:
                    mapped_data_column.append(entry)

# Great pagination values for the list view
def set_pagination(taxonomy, page):
    pagination={}
    pagination['current_page'] = page
    pagination['page_size'] = 50
    pagination['total_items'] = len(taxonomy)
    pagination['total_pages'] = math.ceil(pagination['total_items'] / pagination['page_size'])
    if (pagination['current_page'] > pagination['total_pages']) and (pagination['total_pages'] != 0):
        abort(404)
    pagination['start_value'] = (pagination['current_page'] - 1) * pagination['page_size']
    pagination['end_value'] = pagination['current_page'] * pagination['page_size'] - 1
    return pagination

def create_list_table(taxonomy, term_field, uuid_field):
    table_result = []
    for row in taxonomy:
        if type(term_field).__name__ == "str":
            term = getattr(row, term_field)
        elif type(term_field).__name__ == "dict":
            relationship_data = getattr(row, term_field['relationship'])
            if relationship_data is not None:
                term = getattr(relationship_data, term_field['column'])
            else:
                term = "MISSING"
        uuid = getattr(row, uuid_field)
        doc_attribute = getattr(row, 'doc_attribute')
        table_result.append({'uuid': uuid, 'term': term, 'doc_attribute': doc_attribute})
    return table_result
