sqlalchemy.exc.ProgrammingError: (psycopg2.ProgrammingError) can't adapt type 'Product'
[SQL: INSERT INTO brand_opl.product_notes (product_id, product_note) VALUES (%(product_id__0)s, %(product_note__0)s), (%(product_id__1)s, %(product_note__1)s), (%(product_id__2)s, %(product_note__2)s)]
[parameters: {'product_note__0': 'O', 'product_id__0': <Product af409531-408d-4fc3-86ee-f41849e04eb3>, 'product_note__1': 'l', 'product_id__1': <Product af409531-408d-4fc3-86ee-f41849e04eb3>, 'product_note__2': 'd', 'product_id__2': <Product af409531-408d-4fc3-86ee-f41849e04eb3>}]
(Background on this error at: https://sqlalche.me/e/20/f405)
