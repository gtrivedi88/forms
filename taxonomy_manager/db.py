        # Print or log form data for debugging
        print("Alias names:", request.form.getlist('alias_name'))
        print("Alias types:", request.form.getlist('alias_type'))

        product_alias_data = []
        for i in range(len(request.form.getlist('alias_name'))):
            alias_name = request.form.getlist('alias_name')[i]
            alias_type = request.form.getlist('alias_type')[i]
            alias_approved = request.form.getlist('alias_approved')[i]

            if alias_name and alias_type:
                product_alias_data.append({
                    'alias_name': alias_name,
                    'alias_type': alias_type,
                    'alias_approved': alias_approved
                })

        # Print or log product_alias_data for debugging
        print("Product alias data:", product_alias_data)

        # Loop to save aliases
        for alias_data in product_alias_data:
            product_alias = ProductAlias(
                product_id=new_product.product_id,
                alias_name=alias_data['alias_name'],
                alias_type=alias_data['alias_type'],
                alias_approved=alias_data['alias_approved']
            )
            db.session.add(product_alias)




sqlalchemy.exc.StatementError: (builtins.TypeError) Not a boolean value: 'y'
[SQL: INSERT INTO brand_opl.product_alias (alias_id, product_id, alias_name, alias_type, alias_approved, previous_name, tech_docs, tech_docs_cli, alias_notes) VALUES (%(alias_id)s, %(product_id)s, %(alias_name)s, %(alias_type)s, %(alias_approved)s, %(previous_name)s, %(tech_docs)s, %(tech_docs_cli)s, %(alias_notes)s)]
[parameters: [{'product_id': '8bce8b1a-ecf5-47b1-a25a-14761d88e15f', 'alias_name': 'werty', 'alias_type': 'Acronym', 'alias_approved': 'y', 'previous_name': None, 'alias_notes': None, 'tech_docs': None, 'tech_docs_cli': None}, {'product_id': '8bce8b1a-ecf5-47b1-a25a-14761d88e15f', 'alias_name': 'asas', 'alias_type': 'Short', 'alias_approved': '', 'previous_name': None, 'alias_notes': None, 'tech_docs': None, 'tech_docs_cli': None}]]
