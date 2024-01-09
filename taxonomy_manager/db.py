    # Get product mkt life details
    product_mkt_life = ProductMktLife.query.filter_by(product_id=product_id).first()


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
