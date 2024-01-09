lass ProductMktLife(db.Model):
    """
    Represents marketing life information for a product.

    Attributes:
    - product_id: Foreign key to Product.
    - product_release: Release date of the product.
    - product_release_detail: Details about the product release.
    - product_release_link: Reference link for the product release.
    - product_eol: End of Life date of the product.
    - product_eol_detail: Details about the End of Life of the product.
    - product_eol_link: Reference link for the End of Life of the product.

    Relationships:
    - product: Relationship to Product for easy access to the associated product.
    """

    __tablename__ = 'product_mkt_life'
    __table_args__ = {'schema': 'brand_opl'}

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    product_release = db.Column(db.Date, nullable=True)
    product_release_detail = db.Column(db.String(255))
    product_release_link = db.Column(db.String(255))
    product_eol = db.Column(db.Date, nullable=True)
    product_eol_detail = db.Column(db.String(255))
    product_eol_link = db.Column(db.String(255))




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
