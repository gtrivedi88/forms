{% extends 'base.html' %}

{% block heading %}
<h1 class="pf-v5-c-title pf-m-4xl">{{ product.product_name }} Details</h1>
{% endblock %}


{% block content %}
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

        <br>
        
        <fieldset class="product-reference-group">
            <legend>Product Reference Information</legend>
            <div id="product-references">
                {% for i in range(product_reference_count) %}
                <div class="product-reference-pair">
                    <div class="form-field">
                        <label for="{{ form.product_link.id }}">Product Reference</label>
                        {{ form.product_link(disabled=true) }}
                    </div>
        
                    <div class="form-field">
                        <label for="{{ form.link_description.id }}">Reference Description</label>
                        {{ form.link_description(disabled=true) }}
                    </div>
                </div>
                {% endfor %}
            </div>
        </fieldset>
        
        <br>
        
        <fieldset class="product-status-group">
            <legend>Product Status Details</legend>
            <div class="form-group">
                <div class="checkbox-field">
                    {{ form.deprecated(disabled=true) }}
                    <label for="{{ form.deprecated.id }}">{{ form.deprecated.label }}</label>
                </div>
        
                <div class="checkbox-field">
                    {{ form.upcoming_change(disabled=true) }}
                    <label for="{{ form.upcoming_change.id }}">{{ form.upcoming_change.label }}</label>
                </div>
            </div>
        
            <br>
        
            <div class="form-group">
                <div class="form-field">
                    <label for="{{ form.product_status.id }}">Status</label>
                    {{ form.product_status(id="status-dropdown", class="status-dropdown", disabled=true) }}
                </div>
        
                <div class="form-field">
                    <label for="{{ form.product_status_detail.id }}">Status details</label>
                    {{ form.product_status_detail(id="status-details-dropdown", class="status-details-dropdown", disabled=true)
                    }}
                </div>
            </div>
        </fieldset>
        
        <br>
        
        <fieldset class="product-alias-group">
            <legend>Product Alias Information</legend>
            <div class="form-group">
                <div class="form-field">
                    <label for="{{ form.alias_name.id }}">{{ form.alias_name.label }}</label>
                    {{ form.alias_name(cols=40, disabled=true) }}
                </div>
        
                <div class="form-field">
                    <label for="{{ form.alias_type.id }}">{{ form.alias_type.label }}</label>
                    {{ form.alias_type(id="alias-type-dropdown", class="alias-type-dropdown", disabled=true) }}
                </div>
            </div>
        
            <br>
        
            <div class="form-group">
                <div class="checkbox-field">
                    {{ form.alias_approved(disabled=true) }}
                    <label for="{{ form.alias_approved.id }}" data-toggle="tooltip"
                        title="Leaving it blank for unapproved aliases.">{{ form.alias_approved.label }}</label>
                </div>
        
                <div class="checkbox-field">
                    {{ form.previous_name(disabled=true) }}
                    <label for="{{ form.previous_name.id }}">{{ form.previous_name.label }}</label>
                </div>
        
                <div class="checkbox-field">
                    {{ form.tech_docs(disabled=true) }}
                    <label for="{{ form.tech_docs.id }}">{{ form.tech_docs.label }}</label>
                </div>
        
                <div class="checkbox-field">
                    {{ form.tech_docs_cli(disabled=true) }}
                    <label for="{{ form.tech_docs_cli.id }}">{{ form.tech_docs_cli.label }}</label>
                </div>
            </div>
        
            <br>
        
            <label for="{{ form.alias_notes.id }}">{{ form.alias_notes.label }}</label>
            {{ form.alias_notes(cols=40, disabled=true) }}
        
        </fieldset>
        
        <br>
        
        <fieldset class="product-release-info">
            <legend>Product Release Information</legend>
        
            <label for="{{ form.product_release.id }}">{{ form.product_release.label }}</label>
            {{ form.product_release(disabled=true) }}
        
            <br>
        
            <label for="{{ form.product_release_detail.id }}">{{ form.product_release_detail.label }}</label>
            {{ form.product_release_detail(cols=40, disabled=true) }}
        
            <br>
        
            <label for="{{ form.product_release_link.id }}">{{ form.product_release_link.label }}</label>
            {{ form.product_release_link(cols=40, disabled=true) }}
        </fieldset>
        
        <fieldset class="product-eol-info">
            <legend>Product End of Life Information</legend>
        
            <label for="{{ form.product_eol.id }}">{{ form.product_eol.label }}</label>
            {{ form.product_eol(disabled=true) }}
        
            <br>
        
            <label for="{{ form.product_eol_detail.id }}">{{ form.product_eol_detail.label }}</label>
            {{ form.product_eol_detail(cols=40, disabled=true) }}
        
            <br>
        
            <label for="{{ form.product_eol_link.id }}">{{ form.product_eol_link.label }}</label>
            {{ form.product_eol_link(cols=40, disabled=true) }}
        </fieldset>
        
        <br><br>
        
        <fieldset class="product-partner-group">
            <legend>Product Partners Information</legend>
            <div class="form-field">
                <label for="{{ form.partner.id }}">{{ form.partner.label }}</label>
                <select id="{{ form.partner.id }}" name="{{ form.partner.name }}" multiple disabled>
                    {% for value, label in form.partner.choices %}
                    <option value="{{ value }}" {% if value in selected_partner_ids %} selected {% endif %}>{{ label }}</option>
                    {% endfor %}
                </select>
            </div>
        </fieldset>
        
        <br><br>
        
        <fieldset class="product-component-group">
            <legend>Product Parent Information</legend>
            <div class="form-field">
                <label for="{{ form.component.id }}">{{ form.component.label }}</label>
                <select id="{{ form.component.id }}" name="{{ form.component.name }}" disabled>
                    {% for value, label in form.component.choices %}
                    <option value="{{ value }}" {% if value==selected_component_id %} selected {% endif %}>{{ label }}</option>
                    {% endfor %}
                </select>
            </div>
        
            <div class="form-field">
                <label for="{{ form.component_type.id }}">{{ form.component_type.label }}</label>
                <select id="{{ form.component_type.id }}" name="{{ form.component_type.name }}" disabled>
                    {% for value, label in form.component_type.choices %}
                    <option value="{{ value }}" {% if value==selected_component_type %} selected {% endif %}>{{ label }}
                    </option>
                    {% endfor %}
                </select>
            </div>
            <br>
        </fieldset>
        
        <br>
    </form>

{% else %}
<p>No product details available.</p>
{% endif %}

{% endblock %}
