from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'product'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "product_name"
    __hidden__ = True

    # ProductPortfolios fields
    product_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    product_name = db.Column(db.String(255), nullable=False)
    product_description = db.Column(db.String)
    upcoming_change = db.Column(db.Boolean)
    deprecated = db.Column(db.Boolean)
    product_status = db.Column(db.String(255))
    last_updated = db.Column(db.Date)
    created = db.Column(db.Date)
    product_status_detail = db.Column(db.String(255))

    # Relationships
    product_types_map = db.relationship('ProductTypeMap', backref='product', lazy='dynamic')
    product_portfolios = db.relationship('ProductPortfolioMap', backref='product', lazy='dynamic')

class ProductType(db.Model):
    __tablename__ = 'product_types'
    __table_args__ = {'schema': 'brand_opl'}

    # ProductType fields
    type_id = db.Column(db.String, primary_key=True)
    product_type = db.Column(db.String(255), nullable=False)

class ProductTypeMap(db.Model):
    __tablename__ = 'product_types_map'
    __table_args__ = {'schema': 'brand_opl'}

    # ProductTypeMap fields    
    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    type_id = db.Column(db.String, db.ForeignKey('brand_opl.product_types.type_id'), primary_key=True)

class ProductPortfolios(db.Model):
    __tablename__ = 'product_portfolios'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "category_id"
    __term__ = "category_name"

    # ProductPortfolios fields
    category_id = db.Column(db.String, primary_key=True)
    category_name = db.Column(db.String(255), nullable=False)

class ProductPortfolioMap(db.Model):
    __tablename__ = 'product_portfolio_map'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "category_id"

    # ProductPortfolioMap fields
    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    category_id = db.Column(db.String, db.ForeignKey('brand_opl.product_portfolios.category_id'), primary_key=True)

class ProductNotes(db.Model):
    __tablename__ = 'product_notes'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "product_note"

    # ProductNotes fields
    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    product_note = db.Column(db.String(65535), nullable=False)

    # Define the relationship to the Product model
    product = db.relationship('Product', backref=db.backref('product_notes', lazy='dynamic'))
