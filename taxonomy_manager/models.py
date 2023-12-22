from taxonomy_manager.db import db
from flask import current_app as app

# Secondary table that maps Job Types and Personas
metadata_job_types_map = db.Table('metadata_job_types_map',
                          db.Column('job_id', db.String, db.ForeignKey('ccs_data.metadata_job_types.job_id')),
                          db.Column('persona_id', db.String, db.ForeignKey('ccs_data.metadata_personas.persona_id')),
                          schema='ccs_data',
                          )

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

# CCS DATA MODELS

class Categories(db.Model):
    __tablename__ = 'metadata_categories'
    __table_args__ = {'schema': 'ccs_data'}
    __uuid__ = "category_id"
    __term__ = "category_name"
    category_id = db.Column(db.String, primary_key=True)
    category_name = db.Column(db.String)
    category_abstract = db.Column(db.String)
    doc_attribute = db.Column(db.String)

class ContentType(db.Model):
    __tablename__ = 'metadata_content_types'
    __table_args__ = {'schema': 'ccs_data'}
    __uuid__ = "type_id"
    __term__ = "content_type"
    type_id = db.Column(db.String, primary_key=True)
    content_type = db.Column(db.String)
    content_defintion = db.Column(db.String)
    content_purpose = db.Column(db.String)
    doc_attribute = db.Column(db.String)

class Industry(db.Model):
    __tablename__ = 'metadata_industry'
    __table_args__ = {'schema': 'ccs_data'}
    __uuid__ = "industry_id"
    __term__ = "industry"
    industry_id = db.Column(db.String, primary_key=True)
    industry = db.Column(db.String)
    doc_attribute = db.Column(db.String)

class JobType(db.Model):
    __tablename__ = 'metadata_job_types'
    __table_args__ = {'schema': 'ccs_data'}
    __uuid__ = "job_id"
    __term__ = "job_name"
    job_id = db.Column(db.String, primary_key=True)
    job_name = db.Column(db.String)
    doc_attribute = db.Column(db.String)
    metadata_personas = db.relationship('Persona', lazy='subquery', secondary=metadata_job_types_map, back_populates='metadata_job_types')

class JourneyStage(db.Model):
    __tablename__ = 'metadata_journey_stage'
    __table_args__ = {'schema': 'ccs_data'}
    __uuid__ = "journey_id"
    __term__ = "journey_name"
    journey_id = db.Column(db.String, primary_key=True)
    journey_name = db.Column(db.String)
    journey_abstract = db.Column(db.String)
    doc_attribute = db.Column(db.String)

class ModType(db.Model):
    __tablename__ = 'metadata_mod_types'
    __table_args__ = {'schema': 'ccs_data'}
    __uuid__ = "type_id"
    __term__ = "mod_type"
    type_id = db.Column(db.String, primary_key=True)
    mod_type = db.Column(db.String)
    doc_attribute = db.Column(db.String)

class PartnerAttribute(db.Model):
    __tablename__ = 'metadata_partner_attributes'
    __table_args__ = {'schema': 'ccs_data'}
    __uuid__ = "partner_id"
    __term__ = {'relationship': 'brand_opl_partner', 'column': 'partner_name'}
    partner_id = db.Column(db.String, db.ForeignKey('brand_opl.partners.partner_id'), primary_key=True)
    doc_attribute = db.Column(db.String)
    brand_opl_partner = db.relationship('OplPartner', lazy='subquery', back_populates='ccs_data_metadata_partner_attributes')

class Persona(db.Model):
    __tablename__ = 'metadata_personas'
    __table_args__ = {'schema': 'ccs_data'}
    __uuid__ = "persona_id"
    __term__ = "persona_name"
    persona_id = db.Column(db.String, primary_key=True)
    persona_name = db.Column(db.String)
    persona_abstract = db.Column(db.String)
    doc_attribute = db.Column(db.String)
    metadata_job_types = db.relationship('JobType', lazy='subquery', secondary=metadata_job_types_map, back_populates='metadata_personas')

class Platform(db.Model):
    __tablename__ = 'metadata_platform'
    __table_args__ = {'schema': 'ccs_data'}
    __uuid__ = "platform_id"
    __term__ = "platform"
    platform_id = db.Column(db.String, primary_key=True)
    platform = db.Column(db.String)
    doc_attribute = db.Column(db.String)

class ProductAttribute(db.Model):
    __tablename__ = 'metadata_product_attributes'
    __table_args__ = {'schema': 'ccs_data'}
    __uuid__ = "product_id"
    __term__ = {'relationship': 'brand_opl_product', 'column': 'product_name'}
    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    doc_attribute = db.Column(db.String)
    brand_opl_product = db.relationship('OplProduct', lazy='subquery', back_populates='ccs_data_metadata_product_attributes')

class ProductAliasAttribute(db.Model):
    __tablename__ = 'metadata_product_alias_attributes'
    __table_args__ = {'schema': 'ccs_data'}
    __uuid__ = "alias_id"
    __term__ = {'relationship': 'brand_opl_product_alias', 'column': 'alias_name'}
    alias_id = db.Column(db.String, db.ForeignKey('brand_opl.product_alias.alias_id'), primary_key=True)
    doc_attribute = db.Column(db.String)
    brand_opl_product_alias = db.relationship('OplProductAlias', lazy='subquery', back_populates='ccs_data_metadata_product_alias_attributes')

class Proficiency(db.Model):
    __tablename__ = 'metadata_proficiency'
    __table_args__ = {'schema': 'ccs_data'}
    __uuid__ = "proficiency_id"
    __term__ = "proficiency"
    proficiency_id = db.Column(db.String, primary_key=True)
    proficiency = db.Column(db.String)
    doc_attribute = db.Column(db.String)

class Solution(db.Model):
    __tablename__ = 'metadata_solutions'
    __table_args__ = {'schema': 'ccs_data'}
    __uuid__ = "solution_id"
    __term__ = "solution"
    solution_id = db.Column(db.String, primary_key=True)
    solution = db.Column(db.String)
    doc_attribute = db.Column(db.String)

class Topic(db.Model):
    __tablename__ = 'metadata_topics'
    __table_args__ = {'schema': 'ccs_data'}
    __uuid__ = "topic_id"
    __term__ = "topic"
    topic_id = db.Column(db.String, primary_key=True)
    topic = db.Column(db.String)
    doc_attribute = db.Column(db.String)

# OPL MODELS

class OplPartner(db.Model):
    __tablename__ = 'partners'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "partner_id"
    __term__ = "partner_name"
    __hidden__ = True
    partner_id = db.Column(db.String, primary_key=True)
    partner_name = db.Column(db.String)
    persona_id = db.Column(db.String)
    ccs_data_metadata_partner_attributes = db.relationship('PartnerAttribute', back_populates='brand_opl_partner')

class OplProduct(db.Model):
    __tablename__ = 'product'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "product_name"
    __hidden__ = True
    product_id = db.Column(db.String, primary_key=True)
    product_name = db.Column(db.String)
    product_description = db.Column(db.String)
    upcoming_change = db.Column(db.String)
    deprecated = db.Column(db.String)
    product_status = db.Column(db.String)
    last_updated = db.Column(db.DateTime)
    created = db.Column(db.DateTime)
    product_status_detail = db.Column(db.String)
    ccs_data_metadata_product_attributes = db.relationship('ProductAttribute', lazy='subquery', back_populates='brand_opl_product')
    brand_opl_product_alias = db.relationship('OplProductAlias', lazy='subquery', back_populates='brand_opl_product')

class OplProductAlias(db.Model):
    __tablename__ = 'product_alias'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "alias_id"
    __term__ = "alias_name"
    __hidden__ = True
    alias_id = db.Column(db.String, primary_key=True)
    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'))
    alias_name = db.Column(db.String)
    alias_type = db.Column(db.String)
    alias_approved = db.Column(db.String)
    previous_name = db.Column(db.String)
    tech_docs = db.Column(db.String)
    alias_notes = db.Column(db.String)
    tech_docs_cli = db.Column(db.String)
    ccs_data_metadata_product_alias_attributes = db.relationship('ProductAliasAttribute', lazy='subquery', back_populates='brand_opl_product_alias')
    brand_opl_product = db.relationship('OplProduct', lazy='subquery', back_populates='brand_opl_product_alias')
