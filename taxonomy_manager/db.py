from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

class Product(db.Model):
    """
    Represents a product in the system.

    Attributes:
    - product_id: Unique identifier for the product.
    - product_name: Name of the product.
    - product_description: Description of the product.
    - upcoming_change: Indicates if there is an upcoming change for the product.
    - deprecated: Indicates if the product is deprecated.
    - product_status: Status of the product.
    - last_updated: Date when the product was last updated.
    - created: Date when the product was created.
    - product_status_detail: Additional details about the product status.
    """

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

class ProductPortfolios(db.Model):
    """
    Represents different portfolios for products.

    Attributes:
    - category_id: Unique identifier for the product portfolio.
    - category_name: Name of the product portfolio.
    """

    __tablename__ = 'product_portfolios'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "category_id"
    __term__ = "category_name"

    category_id = db.Column(db.String, primary_key=True)
    category_name = db.Column(db.String(255), nullable=False)

    # Relationships
    product_portfolio_map = db.relationship('ProductPortfolioMap', backref='product_portfolio', lazy='dynamic')

class ProductPortfolioMap(db.Model):
    """
    Represents a many-to-many relationship between Product and ProductPortfolios.

    Attributes:
    - product_id: Foreign key to Product.
    - category_id: Foreign key to ProductPortfolios.
    """

    __tablename__ = 'product_portfolio_map'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "category_id"

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    category_id = db.Column(db.String, db.ForeignKey('brand_opl.product_portfolios.category_id'), primary_key=True)

class ProductNotes(db.Model):
    """
    Represents notes associated with a product.

    Attributes:
    - product_id: Foreign key to Product.
    - product_note: Note associated with the product.
    """

    __tablename__ = 'product_notes'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "product_note"

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    product_note = db.Column(db.String(65535), nullable=False)

    # The relationship to the Product model
    product = db.relationship('Product', backref=db.backref('product_notes', lazy='dynamic'))


class ProductReferences(db.Model):
    """
    Represents references associated with a product.

    Attributes:
    - product_id: Foreign key to Product.
    - product_link: Link associated with the product reference.
    - link_description: Description associated with the product reference.

    Relationships:
    - product: Relationship to Product for easy access to the associated product references.
    """

    __tablename__ = 'product_references'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "product_link"

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    product_link = db.Column(db.String(65535), nullable=False)
    link_description = db.Column(db.String(65535), nullable=False)

    # The relationship to the Product model
    product = db.relationship('Product', backref=db.backref('product_references', lazy='dynamic'))


class ProductAlias(db.Model):
    """
    Represents aliases associated with a product.

    Attributes:
    - alias_id: Unique identifier for the alias.
    - product_id: Foreign key to Product.
    - alias_name: Name associated with the alias.
    - alias_type: Type of the alias (Short, Acronym, Cli, Former).
    - alias_approved: Indicates if the alias is approved.
    - previous_name: Indicates if the alias is a previous name.
    - tech_docs: Indicates if the alias is approved for tech docs.
    - tech_docs_cli: Indicates if the alias is approved for tech docs code/CLI.
    - alias_notes: Notes associated with the alias.

    Relationships:
    - product: Relationship to Product for easy access to the associated product.
    """

    __tablename__ = 'product_alias'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "alias_id"
    __term__ = "alias_name"

    alias_id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), nullable=False)
    alias_name = db.Column(db.String(255), nullable=False)
    alias_type = db.Column(db.String(255), nullable=False)
    alias_approved = db.Column(db.Boolean, nullable=True)
    previous_name = db.Column(db.Boolean, nullable=True)
    tech_docs = db.Column(db.Boolean, nullable=True)
    tech_docs_cli = db.Column(db.Boolean, nullable=True)
    alias_notes = db.Column(db.String(65535))

    # The relationship to the Product model
    product = db.relationship('Product', backref=db.backref('aliases', lazy='dynamic'))


class ProductMktLife(db.Model):
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

    # The relationship to the Product model
    product = db.relationship('Product', backref=db.backref('mkt_life', lazy='dynamic'))


class Partner(db.Model):
    """
    Represents partners.

    Attributes:
    - partner_id: Unique identifier for the partner.
    - partner_name: Name of the partner.
    - persona_id: Persona ID for the partner.
    """

    __tablename__ = 'partners'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "partner_id"
    __term__ = "partner_name"

    partner_id = db.Column(db.String, primary_key=True)
    partner_name = db.Column(db.String(255), nullable=False)

    # Relationships
    product_partners = db.relationship('ProductPartners', backref='partner', lazy='dynamic')

class ProductPartners(db.Model):
    """
    Represents a many-to-many relationship between Product and Partners.

    Attributes:
    - product_id: Foreign key to Product.
    - partner_id: Foreign key to Partners.
    """

    __tablename__ = 'product_partners'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "partner_id"

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    partner_id = db.Column(db.String, db.ForeignKey('brand_opl.partners.partner_id'), primary_key=True)


class ProductComponents(db.Model):
    """
    Represents a many-to-many relationship between Product and Components.

    Attributes:
    - product_id: Foreign key to Product.
    - component_id: Foreign key to Components.
    """

    __tablename__ = 'product_components'
    __table_args__ = {'schema': 'brand_opl'}
    __uuid__ = "product_id"
    __term__ = "component_id"

    product_id = db.Column(db.String, db.ForeignKey('brand_opl.product.product_id'), primary_key=True)
    component_id = db.Column(db.String(255), nullable=False, primary_key=True)
    component_type = db.Column(db.String(255), nullable=False)

    # The relationship to the existing Product model
    product = db.relationship('Product', backref='components', foreign_keys=[product_id])
