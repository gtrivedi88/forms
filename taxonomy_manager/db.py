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

    <!-- Product Alias Information Group -->
    <fieldset class="product-alias-group">
        <legend>Product Alias Information</legend>
    
        <!-- Fields for Product Alias -->
        <div class="form-group">
            <label for="{{ form.alias_name.id }}">{{ form.alias_name.label }}</label>
            {{ form.alias_name() }}
        </div>
    
        <br>
    
        <label for="{{ form.alias_type.id }}">{{ form.alias_type.label }}</label>
        {{ form.alias_type() }}
    
        <br><br>
    
        <!-- Fields for Product Alias -->
        <div class="form-group">
            <div class="checkbox-field">
                {{ form.alias_approved() }}
                <label for="{{ form.alias_approved.id }}" data-toggle="tooltip"
                    title="Leaving it blank for unapproved aliases.">{{ form.alias_approved.label }}</label>
            </div>
    
            <div class="checkbox-field">
                {{ form.previous_name() }}
                <label for="{{ form.previous_name.id }}">{{ form.previous_name.label }}</label>
            </div>
    
            <div class="checkbox-field">
                {{ form.tech_docs() }}
                <label for="{{ form.tech_docs.id }}">{{ form.tech_docs.label }}</label>
            </div>
    
            <div class="checkbox-field">
                {{ form.tech_docs_cli() }}
                <label for="{{ form.tech_docs_cli.id }}">{{ form.tech_docs_cli.label }}</label>
            </div>
        </div>
    
        <br>
    
        <label for="{{ form.alias_notes.id }}">{{ form.alias_notes.label }}</label>
        {{ form.alias_notes(cols=40) }}
    
        <br><br>
    
        <!-- "Add" button for the current group -->
        <button type="button" class="group-btn add-group-btn" onclick="addGroup()">Add Another Alias Group</button>
        <button type="button" class="remove-reference" style="display: none;">Delete</button>
    </fieldset>

    <br><br>

    {{ form.submit(style="background-color: #1a73e8; color: #ffffff;") }}
</form>

<script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
<script src="{{ url_for('static', filename='scripts/status.js') }}"></script>
<script src="{{ url_for('static', filename='scripts/preferences.js') }}"></script>
<script>
    function addGroup() {
        // Clone the product alias group and append it to the form
        var groupClone = document.querySelector('.product-alias-group').cloneNode(true);
        document.querySelector('form').appendChild(groupClone);

        // Clear values in the cloned group
        var inputs = groupClone.querySelectorAll('input, select');
        inputs.forEach(function (input) {
            input.value = '';
        });

        // Hide the "Add" button in the cloned group
        var addBtn = groupClone.querySelector('.add-group-btn');
        addBtn.style.display = 'none';

        // Display the "Delete" button for the cloned group
        var deleteBtn = groupClone.querySelector('.remove-reference');
        deleteBtn.style.display = 'inline-block';

        // Hide the "Delete" button for the existing groups
        var existingGroups = document.querySelectorAll('.product-alias-group');
        existingGroups.forEach(function (existingGroup) {
            var existingDeleteBtn = existingGroup.querySelector('.remove-reference');
            existingDeleteBtn.style.display = 'none';
        });
    }

    function deleteGroup(button) {
        // Remove the parent of the clicked "Delete" button (i.e., the entire group)
        button.parentNode.remove();

        // Display the "Add" button if there is at least one product alias group
        var groupCount = document.querySelectorAll('.product-alias-group').length;
        if (groupCount === 1) {
            document.querySelector('.add-group-btn').style.display = 'inline-block';
        }
    }
</script>

{% endif %}

{% if success_message %}
<p class="success">{{ success_message }}</p>
<br><br>
<a href="{{ url_for('add_product') }}" class="button-link">Add more products</a>
{% endif %}
{% endblock %}
