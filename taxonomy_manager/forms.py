    # Add a new field for selecting a component
    component = SelectField('Parent', choices=[('', 'Select')], validators=[Optional()])
    component_type = SelectField('Component Type', choices=[('', 'Select'), ('component', 'Component'), ('operator', 'Operator'), ('variant', 'Variant')], validators=[Optional()])




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
