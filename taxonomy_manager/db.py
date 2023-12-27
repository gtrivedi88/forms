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
    {{ form.product_name() }}

    <br><br>

    <label for="{{ form.product_description.id }}">{{ form.product_description.label }}</label>
    {{ form.product_description(rows=4, cols=50) }}

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

    <label for="{{ form.product_references.id }}">{{ form.product_references.label }}</label>
    {% for field in form.product_references %}
    {{ field }}
    {% endfor %}

    <br><br>

    <label for="{{ form.product_descriptions.id }}">{{ form.product_descriptions.label }}</label>
    {% for field in form.product_descriptions %}
    {{ field }}
    {% endfor %}

    <br><br>

    <div class="checkbox-row">
        {{ form.deprecated() }}
        <label for="{{ form.deprecated.id }}">{{ form.deprecated.label }}</label>
    </div>
    
    <br><br>

    <div class="checkbox-row">
        {{ form.upcoming_change() }}
        <label for="{{ form.upcoming_change.id }}">{{ form.upcoming_change.label }}</label>
    </div>

    <br><br>

    <label for="{{ form.product_status.id }}">{{ form.product_status.label }}</label>
    <select id="{{ form.product_status.id }}" name="{{ form.product_status.name }}">
        {% for value, label in form.product_status.choices %}
        <option value="{{ value }}">{{ label }}</option>
        {% endfor %}
    </select>
    
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
<a href="{{ url_for('add_product') }}" class="button-link">Add more products</a>
{% endif %}
{% endblock %}
