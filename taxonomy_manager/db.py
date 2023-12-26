from db import db
import uuid
from datetime import datetime


class Product(db.Model):
    __tablename__ = 'product'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "product_name"
    __hidden__ = True
    product_id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    product_name = db.Column(db.String(255), nullable=False)
    product_description = db.Column(db.String)
    upcoming_change = db.Column(db.Boolean)
    deprecated = db.Column(db.Boolean)
    product_status = db.Column(db.String(255))
    last_updated = db.Column(db.Date)
    created = db.Column(db.Date)
    product_status_detail = db.Column(db.String(255))
    # ccs_data_metadata_product_attributes = db.relationship('ProductAttribute', lazy='subquery', back_populates='brand_opl_product')
    # brand_opl_product_alias = db.relationship('OplProductAlias', lazy='subquery', back_populates='brand_opl_product')

    # Add a relationship to the ProductType model
    product_type_maps = db.relationship('ProductTypeMap', backref='product', lazy='subquery')

class ProductType(db.Model):
    __tablename__ = 'product_types'
    __table_args__ = {'schema': 'brand_opl'}

    type_id = db.Column(db.String, primary_key=True)
    product_type = db.Column(db.String(255), nullable=False)

class ProductTypeMap(db.Model):
    __tablename__ = 'product_types_map'
    __table_args__ = {'schema': 'brand_opl'}

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    type_id = db.Column(db.String, db.ForeignKey('brand_opl.product_types.type_id'), primary_key=True)
