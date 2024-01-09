{% extends 'base.html' %}

{% block heading %}
<h1 class="pf-v5-c-title pf-m-4xl">Welcome to OPL</h1>
{% endblock %}


{% block content %}
<p>Search for a product information.</p>


<!-- Section 1: Search -->
<div id="search-form">
    <h2>Search Products</h2>
    <form method="post" action="{{ url_for('view_products') }}">
        {{ form.csrf_token }}
        {{ form.hidden_tag() }}

        <label for="product_name">Product Name:</label>
        {{ form.product_name(class="form-control") }}

        <label for="product_status">Product Status:</label>
        {{ form.product_status(class="form-control") }}

        {{ form.submit(class="btn btn-primary") }}
        {{ form.reset(class="btn btn-secondary") }}
    </form>
</div>

<!-- Section 2: Search Results -->
{% if form.is_submitted() and form.validate() %}
<div id="search-results">
    <h2>Search Results</h2>
    {% if products %}
    <ul>
        {% for product in products %}
        <li>
            <a href="{{ url_for('view_product_details', product_id=product.product_id) }}">
                {{ product.product_name }}
            </a>
        </li>
        {% endfor %}
    </ul>
    {% else %}
    <p>No results found.</p>
    {% endif %}
</div>
{% endif %}

{% endblock %}
