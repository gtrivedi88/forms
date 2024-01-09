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

class ProductTypeMap(db.Model):
    """
    Represents a many-to-many relationship between Product and ProductType.

    Attributes:
    - product_id: Foreign key to Product.
    - type_id: Foreign key to ProductType.
    """

    __tablename__ = 'product_types_map'
    __table_args__ = {'schema': 'brand_opl'}

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    type_id = db.Column(db.String, db.ForeignKey('brand_opl.product_types.type_id'), primary_key=True)
