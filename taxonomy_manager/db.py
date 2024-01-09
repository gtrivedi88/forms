# The route definition to view a product.
@app.route('/', methods=['GET', 'POST'])
def view_products():
    form = SearchForm()

    # Define the query for products
    products_query = Product.query

    # If the form is submitted and valid, filter products based on form data
    if form.validate_on_submit():
        # Filter products based on form data
        if form.product_name.data:
            products_query = products_query.filter(Product.product_name.ilike(f"%{form.product_name.data}%"))

        if form.product_status.data and form.product_status.data != 'Select':
            products_query = products_query.filter(Product.product_status == form.product_status.data)

    # Get the list of products based on the filtered query
    products = products_query.all()

    # Check if a specific product is clicked to display detailed information
    selected_product_id = request.args.get('product_id')
    selected_product = None

    if selected_product_id:
        selected_product = Product.query.get(selected_product_id)

    return render_template('index.html', form=form, products=products, selected_product=selected_product)

# The route definition to view detailed information for a specific product.

@app.route('/opl/product/<string:product_id>', methods=['GET'])
def view_product_details(product_id):
    # Retrieve the product based on the provided product_id
    product = Product.query.get_or_404(product_id)
    product = Product.query.get(product_id)

    if product:
        # Fetch the associated product types
        product_types = ProductType.query.join(ProductTypeMap).filter_by(product_id=product_id).all()
    else:
        # Handle the case where the product is not found
        return render_template('product_details.html', product=None)

    # Get product portfolio choices
    product_portfolio_choices = [(portfolio.category_id, portfolio.category_name) for portfolio in ProductPortfolios.query.all()]

    # Get partner choices
    partner_choices = [(partner.partner_id, partner.partner_name) for partner in Partner.query.all()]

    # Get component choices
    component_choices = [('', 'Select')] + [(component.product_id, component.product_name) for component in Product.query.all()]

    # Get product notes
    product_notes = ProductNotes.query.filter_by(product_id=product_id).first()

    # Get product references
    if product:
        # Fetch the associated product references
        product_references = product.product_references.all()
    else:
        # Handle the case where the product is not found
        return render_template('opl/product_details.html', product=None)

    # Get product aliases
    if product:
        # Fetch the associated product aliases
        product_aliases = product.aliases.all()
    else:
        # Handle the case where the product is not found
        return render_template('opl/product_details.html', product=None)

    # Get product mkt life details
    if product:
        # Fetch the associated product release information
        product_mkt_life = ProductMktLife.query.filter_by(product_id=product_id).first()
    else:
        # Handle the case where the product is not found
        return render_template('opl/product_details.html', product=None)

    # Get product partners
    if product:      
        # Fetch the associated product partners
        product_partners = ProductPartners.query.filter_by(product_id=product_id).all()
    else:
        # Handle the case where the product is not found
        return render_template('opl/product_details.html', product=None)

    # Get product components
    if product:       
        # Fetch the associated product components
        product_components = ProductComponents.query.filter_by(product_id=product_id).all()

        # Additional queries to retrieve product names based on component product_id
        component_product_names = {comp.component_id: Product.query.get(comp.component_id).product_name for comp in product_components}
    else:
        # Handle the case where the product is not found
        return render_template('opl/product_details.html', product=None)

    return render_template('opl/product_details.html', 
                           product=product,
                           product_types=product_types,
                           product_portfolio_choices=product_portfolio_choices,
                           partner_choices=partner_choices,
                           component_choices=component_choices,
                           product_notes=product_notes,
                           product_references=product_references,
                           product_aliases=product_aliases,
                           product_mkt_life=product_mkt_life,
                           product_partners=product_partners,
                           product_components=product_components,
                           component_product_names=component_product_names)
