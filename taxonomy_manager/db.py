# Get product type choices
    product_type_choices = [(ptype.type_id, ptype.product_type) for ptype in ProductType.query.all()]
# Add product type mapping
        selected_product_types = form.product_type.data
        for product_type_id in selected_product_types:
            product_type_map = ProductTypeMap(product_id=new_product.product_id, type_id=product_type_id)
            db.session.add(product_type_map)


<div class="form-field">
                <label for="{{ form.product_type.id }}">{{ form.product_type.label }}</label>
                <select id="{{ form.product_type.id }}" name="{{ form.product_type.name }}" multiple>
                    {% for value, label in form.product_type.choices %}
                    <option value="{{ value }}">{{ label }}</option>
                    {% endfor %}
                </select>
            </div>


            

class ProductType(db.Model):
    """
    Represents different types of products.

    Attributes:
    - type_id: Unique identifier for the product type.
    - product_type: Type of the product.
    """

    __tablename__ = 'product_types'
    __table_args__ = {'schema': 'brand_opl'}

    type_id = db.Column(db.String, primary_key=True)
    product_type = db.Column(db.String(255), nullable=False)

    # Relationships
    product_types_map = db.relationship('ProductTypeMap', backref='product_type', lazy='dynamic')
