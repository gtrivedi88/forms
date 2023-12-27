    <label for="{{ form.product_notes.id }}">{{ form.product_notes.label }}</label>
    {{ form.product_notes(rows=4, cols=70) }}

sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedColumn) column product_notes.id does not exist
LINE 1: ..., p1, sen_counter) ORDER BY sen_counter RETURNING brand_opl....
                                                             ^

[SQL: INSERT INTO brand_opl.product_notes (product_id, product_note) SELECT p0::VARCHAR, p1::VARCHAR FROM (VALUES (%(product_id__0)s, %(product_note__0)s, 0), (%(product_id__1)s, %(product_note__1)s, 1), (%(product_id__2)s, %(product_note__2)s, 2), (%(product_id__3)s, %(product_note__3)s, 3)) AS imp_sen(p0, p1, sen_counter) ORDER BY sen_counter RETURNING brand_opl.product_notes.id, brand_opl.product_notes.id AS id__1]
[parameters: {'product_id__0': '94722e16-c442-4af2-9c67-ad2b0bdd8003', 'product_note__0': 'P', 'product_id__1': '94722e16-c442-4af2-9c67-ad2b0bdd8003', 'product_note__1': 'u', 'product_id__2': '94722e16-c442-4af2-9c67-ad2b0bdd8003', 'product_note__2': 'k', 'product_id__3': '94722e16-c442-4af2-9c67-ad2b0bdd8003', 'product_note__3': 'i'}]
(Background on this error at: https://sqlalche.me/e/20/f405)
