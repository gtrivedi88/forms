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



    # SelectField for Product Portfolio
    product_portfolio = SelectMultipleField('Portfolio')


    # Populate product portfolio choices
    form.product_portfolio.choices = [(portfolio.category_id, portfolio.category_name) for portfolio in ProductPortfolios.query.all()]

<code in between>

        # Add product portfolio mapping
        selected_portfolios = form.product_portfolio.data
        for portfolio_id in selected_portfolios:
            product_portfolio_map = ProductPortfolioMap(product_id=new_product.product_id, category_id=portfolio_id)
            db.session.add(product_portfolio_map)


<div class="form-field">
                <label for="{{ form.product_portfolio.id }}">{{ form.product_portfolio.label }}</label>
                <select id="{{ form.product_portfolio.id }}" name="{{ form.product_portfolio.name }}" multiple>
                    {% for value, label in form.product_portfolio.choices %}
                    <option value="{{ value }}">{{ label }}</option>
                    {% endfor %}
                </select>
            </div>
