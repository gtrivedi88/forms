        # Print or log form data for debugging
        print("Alias names:", request.form.getlist('alias_name'))
        print("Alias types:", request.form.getlist('alias_type'))

        product_alias_data = []
        for i in range(len(request.form.getlist('alias_name'))):
            alias_name = request.form.getlist('alias_name')[i]
            alias_type = request.form.getlist('alias_type')[i]
            alias_approved = request.form.getlist('alias_approved')[i]
            previous_name = request.form.getlist('previous_name')[i]
            tech_docs = request.form.getlist('tech_docs')[i]
            tech_docs_cli = request.form.getlist('tech_docs_cli')[i]
            alias_notes = request.form.getlist('alias_notes')[i]

            if alias_name and alias_type:
                product_alias_data.append({
                    'alias_name': alias_name,
                    'alias_type': alias_type,
                    'alias_approved': alias_approved,
                    'previous_name': previous_name,
                    'tech_docs': tech_docs,
                    'tech_docs_cli': tech_docs_cli,
                    'alias_notes': alias_notes
                })

        # Print or log product_alias_data for debugging
        print("Product alias data:", product_alias_data)

        # Loop to save aliases
        for alias_data in product_alias_data:
            # Check if 'alias_approved' key exists in alias_data
            if 'alias_approved' in alias_data:
                alias_approved = alias_data['alias_approved'].lower() == 'y'
                previous_name = alias_data['previous_name'].lower() == 'y'
                tech_docs = alias_data['tech_docs'].lower() == 'y'
                tech_docs_cli = alias_data['tech_docs_cli'].lower() == 'y'
            else:
                # If the key is not present, provide a default value (False in this case)
                alias_approved = False
                previous_name = False
                tech_docs = False
                tech_docs_cli = False

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

        # Commit changes to the database session
        db.session.commit()
