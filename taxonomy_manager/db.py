sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedColumn) column product_notes.id does not exist
LINE 1: ..., p1, sen_counter) ORDER BY sen_counter RETURNING brand_opl....
                                                             ^

[SQL: INSERT INTO brand_opl.product_notes (product_id, product_note) SELECT p0::VARCHAR, p1::VARCHAR FROM (VALUES (%(product_id__0)s, %(product_note__0)s, 0), (%(product_id__1)s, %(product_note__1)s, 1), (%(product_id__2)s, %(product_note__2)s, 2)) AS imp_sen(p0, p1, sen_counter) ORDER BY sen_counter RETURNING brand_opl.product_notes.id, brand_opl.product_notes.id AS id__1]
[parameters: {'product_note__0': 'O', 'product_id__0': '06a49073-0cde-461a-bc96-d0d38cc456df', 'product_note__1': 'l', 'product_id__1': '06a49073-0cde-461a-bc96-d0d38cc456df', 'product_note__2': 'a', 'product_id__2': '06a49073-0cde-461a-bc96-d0d38cc456df'}]
(Background on this error at: https://sqlalche.me/e/20/f405)
