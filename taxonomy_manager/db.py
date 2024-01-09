{% extends 'base.html' %}

{% block heading %}
<h1 class="pf-v5-c-title pf-m-4xl">Product Details</h1>
{% endblock %}

{% block content %}
<p>Product information:</p>

<br>

{% if product %}

<form id="my-form">

    <fieldset class="product-information-group">
        <legend>Product Information</legend>

        <div class="form-group">
            <div class="form-field">
                <label for="product_name">Product Name *</label>
                <textarea id="product_name" name="product_name" cols="40" readonly>{{ product.product_name }}</textarea>
            </div>

            <div class="form-field">
                <label for="product_type">Product Type *</label>
                <select id="product_type" name="product_type" multiple readonly>
                    {% for product_type in product.product_types %}
                    <option value="{{ product_type.type_id }}" selected>{{ product_type.product_type }}</option>
                    {% endfor %}
                </select>
            </div>
        </div>

        <div class="form-group">
            <div class="form-field">
                <label for="product_description">Product Description</label>
                <textarea id="product_description" name="product_description" cols="40"
                    readonly>{{ product.product_description }}</textarea>
            </div>

            <div class="form-field">
                <label for="product_portfolio">Product Portfolio</label>
                <select id="product_portfolio" name="product_portfolio" multiple readonly>
                    {% for portfolio in product.product_portfolios %}
                    <option value="{{ portfolio.category_id }}" selected>{{ portfolio.category_name }}</option>
                    {% endfor %}
                </select>
            </div>
        </div>

        <div class="form-group">
            <div class="form-field">
                <label for="product_notes">Product Notes</label>
                <textarea id="product_notes" name="product_notes" cols="40"
                    readonly>{{ product.product_notes }}</textarea>
            </div>
        </div>

    </fieldset>

    <!-- Add other fieldsets as needed -->

    <fieldset class="product-reference-group">
        <legend>Product Reference Information</legend>
        <div id="product-references">
            {% for reference in product.product_references %}
            <div class="product-reference-pair">
                <div class="form-field">
                    <label for="product_link">Product Reference</label>
                    <textarea id="product_link" name="product_link" cols="40"
                        readonly>{{ reference.product_link }}</textarea>
                </div>

                <div class="form-field">
                    <label for="link_description">Reference Description</label>
                    <textarea id="link_description" name="link_description" cols="40"
                        readonly>{{ reference.link_description }}</textarea>
                </div>
            </div>
            {% endfor %}
        </div>
    </fieldset>

    <!-- Repeat similar code for other fieldsets -->

    <fieldset class="product-status-group">
        <legend>Product Status Details</legend>
        <div class="form-group">
            <div class="checkbox-field">
                <input type="checkbox" id="deprecated" name="deprecated" {% if product.deprecated %}checked{% endif %}
                    disabled>
                <label for="deprecated">Deprecated</label>
            </div>

            <div class="checkbox-field">
                <input type="checkbox" id="upcoming_change" name="upcoming_change" {% if product.upcoming_change
                    %}checked{% endif %} disabled>
                <label for="upcoming_change">Upcoming Change</label>
            </div>
        </div>

        <br>

        <div class="form-group">
            <div class="form-field">
                <label for="product_status">Status</label>
                <select id="product_status" name="product_status" disabled>
                    <option value="{{ product.product_status }}" selected>{{ product.product_status }}</option>
                </select>
            </div>

            <div class="form-field">
                <label for="product_status_detail">Status details</label>
                <select id="product_status_detail" name="product_status_detail" disabled>
                    <option value="{{ product.product_status_detail }}" selected>{{ product.product_status_detail }}
                    </option>
                </select>
            </div>
        </div>
    </fieldset>

    <!-- Repeat similar code for other fieldsets -->

    <fieldset class="product-alias-group">
        <legend>Product Alias Information</legend>
        {% for alias in product.product_aliases %}
        <div class="form-group">
            <div class="form-field">
                <label for="alias_name">Alias Name</label>
                <textarea id="alias_name" name="alias_name" cols="40" readonly>{{ alias.alias_name }}</textarea>
            </div>

            <div class="form-field">
                <label for="alias_type">Alias Type</label>
                <select id="alias_type" name="alias_type" disabled>
                    <option value="{{ alias.alias_type }}" selected>{{ alias.alias_type }}</option>
                </select>
            </div>
        </div>

        <br>

        <div class="form-group">
            <div class="checkbox-field">
                <input type="checkbox" id="alias_approved" name="alias_approved" {% if alias.alias_approved %}checked{%
                    endif %} disabled>
                <label for="alias_approved" data-toggle="tooltip" title="Leaving it blank for unapproved aliases.">Alias
                    Approved</label>
            </div>

            <div class="checkbox-field">
                <input type="checkbox" id="previous_name" name="previous_name" {% if alias.previous_name %}checked{%
                    endif %} disabled>
                <label for="previous_name">Previous Name</label>
            </div>

            <div class="checkbox-field">
                <input type="checkbox" id="tech_docs" name="tech_docs" {% if alias.tech_docs %}checked{% endif %}
                    disabled>
                <label for="tech_docs">Approved For Tech Docs</label>
            </div>

            <div class="checkbox-field">
                <input type="checkbox" id="tech_docs_cli" name="tech_docs_cli" {% if alias.tech_docs_cli %}checked{%
                    endif %} disabled>
                <label for="tech_docs_cli">Approved For Tech Docs Code/CLI</label>
            </div>
        </div>

        <br>

        <label for="alias_notes">Alias Notes</label>
        <textarea id="alias_notes" name="alias_notes" cols="40" readonly>{{ alias.alias_notes }}</textarea>
        {% endfor %}
    </fieldset>

    <fieldset class="product-release-info">
        <legend>Product Release Information</legend>
    
        <label for="product_release">Release Date</label>
        <input type="text" id="product_release" name="product_release" value="{{ product.product_release }}" readonly>
    
        <br>
    
        <label for="product_release_detail">Release Detail</label>
        <textarea id="product_release_detail" name="product_release_detail"
            readonly>{{ product.product_release_detail }}</textarea>
    
        <br>
    
        <label for="product_release_link">Release Reference</label>
        <textarea id="product_release_link" name="product_release_link"
            readonly>{{ product.product_release_link }}</textarea>
    </fieldset>
    
    <fieldset class="product-eol-info">
        <legend>Product End of Life Information</legend>
    
        <label for="product_eol">Product End Of Life (EOL) Date</label>
        <input type="text" id="product_eol" name="product_eol" value="{{ product.product_eol }}" readonly>
    
        <br>
    
        <label for="product_eol_detail">Product End Of Life (EOL) Details</label>
        <textarea id="product_eol_detail" name="product_eol_detail" readonly>{{ product.product_eol_detail }}</textarea>
    
        <br>
    
        <label for="product_eol_link">Product End Of Life (EOL) Reference</label>
        <textarea id="product_eol_link" name="product_eol_link" readonly>{{ product.product_eol_link }}</textarea>
    </fieldset>
    
    <!-- Repeat similar code for other fieldsets -->

    <!-- Repeat similar code for other fieldsets -->

    <fieldset class="product-partner-group">
        <legend>Product Partners Information</legend>
        <div class="form-field">
            <label for="partner">In Partnership with</label>
            <select id="partner" name="partner" multiple disabled>
                {% for partner in product.product_partners %}
                <option value="{{ partner.partner_id }}" selected>{{ partner.partner.partner_name }}</option>
                {% endfor %}
            </select>
        </div>
    </fieldset>

    <!-- Repeat similar code for other fieldsets -->

    <fieldset class="product-component-group">
        <legend>Product Parent Information</legend>
    
        <label for="component_name">Component Name</label>
        <input type="text" id="component_name" name="component_name" value="{{ product.component_name }}" readonly>
    
        <br>
    
        <label for="component_type">Component Type</label>
        <input type="text" id="component_type" name="component_type" value="{{ product.component_type }}" readonly>
    
    </fieldset>

    <!-- Repeat similar code for other fieldsets -->




</form>

{% else %}
<p>No product details available.</p>
{% endif %}

{% endblock %}
