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




 The route definition to add a product.
@app.route('/opl/add-product', methods=['GET', 'POST'])
def add_product():
    form = MyForm()
    success_message = None
    show_form = True

    # Initialize the variables here
    formatted_created_date = None
    formatted_last_updated_date = None

    # Populate product type choices
    form.product_type.choices = [(ptype.type_id, ptype.product_type) for ptype in ProductType.query.all()]

    # Populate product portfolio choices
    form.product_portfolio.choices = [(portfolio.category_id, portfolio.category_name) for portfolio in ProductPortfolios.query.all()]

    # Populate partner choices
    form.partner.choices = [(partner.partner_id, partner.partner_name) for partner in Partner.query.all()]

    # Populate component choices
    form.component.choices = [('', 'Select')] + [(component.product_id, component.product_name) for component in Product.query.all()]

    if form.validate_on_submit():
        # Logic for adding a new product
        created_date = datetime.now()

        # Create a new product instance
        new_product = Product(
            product_name=form.product_name.data,
            product_description=form.product_description.data,
            upcoming_change=form.upcoming_change.data,
            deprecated=form.deprecated.data,
            product_status=form.product_status.data if form.product_status.data != 'Select' else '',
            product_status_detail='NULL' if form.product_status.data == 'Deprecated' else form.product_status_detail.data,
            last_updated=created_date,
            created=created_date
        )

        # If product_status is Deprecated, set product_status_detail to 'NULL'
        if form.product_status.data == 'Deprecated':
                form.product_status_detail.data = 'NULL'


        # Add and commit the new product to the database
        db.session.add(new_product)
        db.session.commit()

        # Add product type mapping
        selected_product_types = form.product_type.data
        for product_type_id in selected_product_types:
            product_type_map = ProductTypeMap(product_id=new_product.product_id, type_id=product_type_id)
            db.session.add(product_type_map)

        # Add product portfolio mapping
        selected_portfolios = form.product_portfolio.data
        for portfolio_id in selected_portfolios:
            product_portfolio_map = ProductPortfolioMap(product_id=new_product.product_id, category_id=portfolio_id)
            db.session.add(product_portfolio_map)

        # Add Product Notes
        product_notes_data = form.product_notes.data
        if product_notes_data:
            product_notes = ProductNotes(product_id=new_product.product_id, product_note=product_notes_data)
            db.session.add(product_notes)

        # Add Product References
        product_references_data = []
        for i in range(len(request.form.getlist('product_link'))):
            product_link = request.form.getlist('product_link')[i]
            link_description = request.form.getlist('link_description')[i]

            if product_link and link_description:
                product_references_data.append({
                    'product_link': product_link,
                    'link_description': link_description
                })

        for reference_data in product_references_data:
            product_references = ProductReferences(
                product_id=new_product.product_id,
                product_link=reference_data['product_link'],
                link_description=reference_data['link_description']
            )
            db.session.add(product_references)

        # Add Product Alias
        product_alias_data = []
        alias_names = request.form.getlist('alias_name')
        alias_types = request.form.getlist('alias_type')
        alias_approved_list = request.form.getlist('alias_approved')
        previous_name_list = request.form.getlist('previous_name')
        tech_docs_list = request.form.getlist('tech_docs')
        tech_docs_cli_list = request.form.getlist('tech_docs_cli')
        alias_notes_list = request.form.getlist('alias_notes')

        for i in range(len(alias_names)):
            alias_name = alias_names[i]
            alias_type = alias_types[i]
            alias_approved = alias_approved_list[i].lower() == 'y' if i < len(alias_approved_list) else False
            previous_name = previous_name_list[i].lower() == 'y' if i < len(previous_name_list) else False
            tech_docs = tech_docs_list[i].lower() == 'y' if i < len(tech_docs_list) else False
            tech_docs_cli = tech_docs_cli_list[i].lower() == 'y' if i < len(tech_docs_cli_list) else False
            alias_notes = alias_notes_list[i] if i < len(alias_notes_list) else ''

            if alias_name:
                product_alias_data.append({
                    'alias_name': alias_name,
                    'alias_type': alias_type,
                    'alias_approved': alias_approved,
                    'previous_name': previous_name,
                    'tech_docs': tech_docs,
                    'tech_docs_cli': tech_docs_cli,
                    'alias_notes': alias_notes
                })

        # Loop to save aliases
        for alias_data in product_alias_data:
            # Directly use boolean values, no need for lower()
            alias_approved = alias_data['alias_approved']
            previous_name = alias_data['previous_name']
            tech_docs = alias_data['tech_docs']
            tech_docs_cli = alias_data['tech_docs_cli']

            # Create ProductAlias object and add to the session
            product_alias = ProductAlias(
                product_id=new_product.product_id,
                alias_name=alias_data['alias_name'],
                alias_type=alias_data['alias_type'],
                alias_approved=alias_approved,
                previous_name=previous_name,
                tech_docs=tech_docs,
                tech_docs_cli=tech_docs_cli,
                alias_notes=alias_data['alias_notes']
            )
            db.session.add(product_alias)

        
        # Get the selected partner_id from the form
        selected_partner_ids = form.partner.data

        # Add product partners mapping
        for selected_partner_id in selected_partner_ids:
            product_partners = ProductPartners(
                product_id=new_product.product_id,
                partner_id=selected_partner_id
            )
            db.session.add(product_partners)


        # Add Product Components
        product_components_data = []
        component_ids = request.form.getlist('component')
        component_types = request.form.getlist('component_type')

        for i in range(len(component_ids)):
            component_id = component_ids[i]
            component_type = component_types[i]

            # Check if component_id is not 'Select'
            if component_id != 'Select':
                product_components_data.append({
                    'component_id': component_id,
                    'component_type': component_type
                })

        # Loop to save components
        for component_data in product_components_data:
            # Directly use boolean values, no need for lower()
            component_id = component_data['component_id']
            component_type = component_data['component_type']

            # Check if component_id is not 'Select' before saving to the database
            if component_id:
                # Create ProductComponent object and add to the session
                product_component = ProductComponents(
                    product_id=new_product.product_id,
                    component_id=component_id,
                    component_type=component_type
                )
                db.session.add(product_component)

        # Commit the changes to the database
        db.session.commit()
         
        # Commit changes outside the loop
        db.session.commit()

        # Format dates for display
        formatted_created_date = created_date.strftime('%Y-%m-%d')
        formatted_last_updated_date = created_date.strftime('%Y-%m-%d')

        # Set success message and hide the form
        success_message = f'Successfully added the product: {form.product_name.data}'
        show_form = False

    return render_template('opl/add.html', form=form, success_message=success_message,
                           show_form=show_form, formatted_created_date=formatted_created_date,
                           formatted_last_updated_date=formatted_last_updated_date)
