{% extends 'base.html' %}

{% block heading %}
<h1 class="pf-v5-c-title pf-m-4xl">Welcome to OPL</h1>
{% endblock %}

{% block content %}
<p>Add a product information.</p>

<br>

{% if show_form %}

<p style="color:red;">Fields marked with * are mandatory.</p>

<form method="post" action="{{ url_for('add_product') }}" id="my-form">
    {{ form.hidden_tag() }}

    <fieldset class="product-information-group">
    <legend>Product Information</legend>

        <div class="form-group">
            <div class="form-field">
                <label for="{{ form.product_name.id }}">{{ form.product_name.label }}</label>
                {{ form.product_name(cols=40) }}
            </div>


            <div class="form-field">
                <label for="{{ form.product_type.id }}">{{ form.product_type.label }}</label>
                <select id="{{ form.product_type.id }}" name="{{ form.product_type.name }}" multiple>
                    {% for value, label in form.product_type.choices %}
                    <option value="{{ value }}">{{ label }}</option>
                    {% endfor %}
                </select>
            </div>
        </div>


        <div class="form-group">
            
            <div class="form-field">
                <label for="{{ form.product_description.id }}">{{ form.product_description.label }}</label>
                {{ form.product_description(cols=40) }}
            </div>

            <div class="form-field">
                <label for="{{ form.product_portfolio.id }}">{{ form.product_portfolio.label }}</label>
                <select id="{{ form.product_portfolio.id }}" name="{{ form.product_portfolio.name }}" multiple>
                    {% for value, label in form.product_portfolio.choices %}
                    <option value="{{ value }}">{{ label }}</option>
                    {% endfor %}
                </select>
            </div>
        </div>

        <div class="form-group">
            <div class="form-field">
                <label for="{{ form.product_notes.id }}">{{ form.product_notes.label }}</label>
                {{ form.product_notes(cols=40) }}
            </div>
        </div>

    </fieldset>

    <br>
    
    <fieldset class="product-reference-group">
    <legend>Product Reference Information</legend>
    <div id="product-references">
        <div class="product-reference-pair">
            <div class="form-field">
                <label for="{{ form.product_link.id }}">Product Reference</label>
                {{ form.product_link(cols=40) }}
            </div>
    
            <div class="form-field">
                <label for="{{ form.link_description.id }}">Reference Description</label>
                {{ form.link_description(cols=40) }}
            </div>
    
            <div class="form-field buttons-row">
                <button type="button" class="add-reference">Add more</button>
                <button type="button" class="remove-reference" style="display: none;">Delete</button>
            </div>
        </div>
    </div>
    </fieldset>

    <br>

    <fieldset class="product-status-group">
    <legend>Product Status Details</legend>
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

    <br>

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
    </fieldset>

    <br>

    <fieldset class="product-alias-group">
        <legend>Product Alias Information</legend>
        <div class="form-group">
            <div class="form-field">
                <label for="{{ form.alias_name.id }}">{{ form.alias_name.label }}</label>
                {{ form.alias_name(cols=40) }}
            </div>
                
            <div class="form-field">
                <label for="{{ form.alias_type.id }}">{{ form.alias_type.label }}</label>
                {{ form.alias_type(id="alias-type-dropdown", class="alias-type-dropdown") }}
            </div>       
        </div>

        <br>

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

        <br>
        <button type="button" class="add-alias-group" style="margin-top: 10px;">Add more aliases</button>
        <button type="button" class="remove-alias-group" style="display: none;">Delete</button>
    </fieldset>

    <br>

    <fieldset class="product-release-info">
        <legend>Product Release Information</legend>
    
        <label for="{{ form.product_release.id }}">{{ form.product_release.label }}</label>
        {{ form.product_release() }}
    
        <br>
    
        <label for="{{ form.product_release_detail.id }}">{{ form.product_release_detail.label }}</label>
        {{ form.product_release_detail(cols=40) }}
    
        <br>
    
        <label for="{{ form.product_release_link.id }}">{{ form.product_release_link.label }}</label>
        {{ form.product_release_link(cols=40) }}
    </fieldset>
    
    <fieldset class="product-eol-info">
        <legend>Product End of Life Information</legend>
    
        <label for="{{ form.product_eol.id }}">{{ form.product_eol.label }}</label>
        {{ form.product_eol() }}
    
        <br>
    
        <label for="{{ form.product_eol_detail.id }}">{{ form.product_eol_detail.label }}</label>
        {{ form.product_eol_detail(cols=40) }}
    
        <br>
    
        <label for="{{ form.product_eol_link.id }}">{{ form.product_eol_link.label }}</label>
        {{ form.product_eol_link(cols=40) }}
    </fieldset>

    <br><br>

    <fieldset class="product-partner-group">
    <legend>Product Partners Information</legend>
        <div class="form-field">
            <label for="{{ form.partner.id }}">{{ form.partner.label }}</label>
            <select id="{{ form.partner.id }}" name="{{ form.partner.name }}" multiple>
                {% for value, label in form.partner.choices %}
                <option value="{{ value }}">{{ label }}</option>
                {% endfor %}
            </select>
        </div>
    </fieldset>

    <br><br>

    <fieldset class="product-component-group">
    <legend>Product Parent Information</legend>
        <div class="form-field">
            <label for="{{ form.component.id }}">{{ form.component.label }}</label>
            <select id="{{ form.component.id }}" name="{{ form.component.name }}">
                {% for value, label in form.component.choices %}
                <option value="{{ value }}">{{ label }}</option>
                {% endfor %}
            </select>
        </div>

        <div class="form-field">
            <label for="{{ form.component_type.id }}">{{ form.component_type.label }}</label>
            <select id="{{ form.component_type.id }}" name="{{ form.component_type.name }}">
                {% for value, label in form.component_type.choices %}
                <option value="{{ value }}">{{ label }}</option>
                {% endfor %}
            </select>
        </div>
        <br>
        <button type="button" class="add-component-group" style="margin-top: 10px;">Add more components</button>
        <button type="button" class="remove-component-group" style="display: none;">Delete</button>
    </fieldset>

    <br><br>

  
    {{ form.submit(style="background-color: #0a63ca; color: #ffffff; font-size: 20px; padding: 10px; border: none;
    border-radius: 5px; cursor: pointer;") }}
</form>

<script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
<script src="{{ url_for('static', filename='scripts/status.js') }}"></script>
<script src="{{ url_for('static', filename='scripts/preferences.js') }}"></script>
<script src="{{ url_for('static', filename='scripts/alias.js') }}"></script>
<script src="{{ url_for('static', filename='scripts/component.js') }}"></script>
<script src="{{ url_for('static', filename='scripts/product_type.js') }}"></script>

{% endif %}

{% endblock %}
