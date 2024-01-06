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
