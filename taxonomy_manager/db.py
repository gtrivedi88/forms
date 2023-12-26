from db import db
import uuid
from datetime import datetime

# Below are the models for each taxonomy
# They use the standard SQLAlchemy modeling, but with a few added bits a pieces:
#   __tablename__       SQLAlchemy attribute to map the model to a specific table
#   __table_args__      SQLAlchemy attribute to set options for the model.
#                       Mostly used to define the PGSQL schema.
#   __uuid__            Defines the field to use as the UUID. Since the UUID
#                       field name is different for each model, this is a way to
#                       Standardize the field names
#   __term__            Defines the field to use as the term name. This is
#                       similar in function as the UUID.

# OPL DATA MODELS

# class OplPartner(db.Model):
#     __tablename__ = 'partners'
#     __table_args__ = {'schema': 'brand_opl'}
#     __uuid__ = "partner_id"
#     __term__ = "partner_name"
#     __hidden__ = True
#     partner_id = db.Column(db.String, primary_key=True)
#     partner_name = db.Column(db.String)
#     persona_id = db.Column(db.String)
#     ccs_data_metadata_partner_attributes = db.relationship('PartnerAttribute', back_populates='brand_opl_partner')

class Product(db.Model):
    __tablename__ = 'product'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "product_name"
    __hidden__ = True
    product_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
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


class ProductPortfolios(db.Model):
    __tablename__ = 'product_portfolios'
    __table_args__ = {'schema': 'brand_opl'}

    category_id = db.Column(db.String, primary_key=True)
    category_name = db.Column(db.String(255), nullable=False)

    # Add a relationship to the ProductPortfolioMap model
    product_portfolio_map = db.relationship('ProductPortfolioMap', backref='portfolio', lazy='dynamic')



class ProductPortfolioMap(db.Model):
    __tablename__ = 'product_portfolio_map'
    __table_args__ = {'schema': 'brand_opl'}

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    category_id = db.Column(db.String, db.ForeignKey('brand_opl.product_portfolios.category_id'), primary_key=True)
