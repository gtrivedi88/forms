        # Add Product Components
        product_components_data = []
        component_ids = request.form.getlist('component')
        component_types = request.form.getlist('component_type')

        for i in range(len(component_ids)):
            component_id = component_ids[i]
            component_type = component_types[i]

            if component_id:
                product_components_data.append({
                    'component_id': component_id,
                    'component_type': component_type
                })

        # Loop to save components
        for component_data in product_components_data:
            product_component = ProductComponents(
                product_id=new_product.product_id,
                component_id=component_data['component_id'],
                component_type=component_data['component_type']
            )
            db.session.add(product_component)
