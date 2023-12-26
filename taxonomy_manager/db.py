/home/gtrivedi/git/gitlab/opl-ui/app.py:41: SAWarning: Column 'brand_opl.product.product_id' is marked as a member of the primary key for table 'brand_opl.product', but has no Python-side or server-side default generator indicated, nor does it indicate 'autoincrement=True' or 'nullable=True', and no explicit value is passed.  Primary key columns typically may not store NULL.
  db.session.commit()
INFO:sqlalchemy.engine.Engine:INSERT INTO brand_opl.product (product_name, product_description, upcoming_change, deprecated, product_status, last_updated, created, product_status_detail) VALUES (%(product_name)s, %(product_description)s, %(upcoming_change)s, %(deprecated)s, %(product_status)s, %(last_updated)s, %(created)s, %(product_status_detail)s)
INFO:sqlalchemy.engine.Engine:[generated in 0.00019s] {'product_name': 'dfdfwe', 'product_description': '', 'upcoming_change': False, 'deprecated': False, 'product_status': '', 'last_updated': datetime.date(2023, 12, 28), 'created': datetime.date(2023, 12, 28), 'product_status_detail': ''}
INFO:sqlalchemy.engine.Engine:ROLLBACK
INFO:werkzeug:127.0.0.1 - - [27/Dec/2023 00:08:52] "POST /opl/add-product HTTP/1.1" 500 -
Traceback (most recent call last):
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask/app.py", line 1478, in __call__
    return self.wsgi_app(environ, start_response)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask/app.py", line 1458, in wsgi_app
    response = self.handle_exception(e)
               ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask/app.py", line 1455, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask/app.py", line 869, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask/app.py", line 867, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask/app.py", line 852, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/git/gitlab/opl-ui/app.py", line 41, in add_product
    db.session.commit()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/scoping.py", line 598, in commit
    return self._proxied.commit()
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/session.py", line 1969, in commit
    trans.commit(_to_root=True)
  File "<string>", line 2, in commit
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/state_changes.py", line 139, in _go
    ret_value = fn(self, *arg, **kw)
                ^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/session.py", line 1256, in commit
    self._prepare_impl()
  File "<string>", line 2, in _prepare_impl
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/state_changes.py", line 139, in _go
    ret_value = fn(self, *arg, **kw)
                ^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/session.py", line 1231, in _prepare_impl
    self.session.flush()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/session.py", line 4312, in flush
    self._flush(objects)
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/session.py", line 4447, in _flush
    with util.safe_reraise():
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/util/langhelpers.py", line 146, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/session.py", line 4414, in _flush
    flush_context.finalize_flush_changes()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/unitofwork.py", line 487, in finalize_flush_changes
    self.session._register_persistent(other)
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/session.py", line 3313, in _register_persistent
    raise exc.FlushError(
sqlalchemy.orm.exc.FlushError: Instance <Product at 0x7ffbb6d85a60> has a NULL identity key.  If this is an auto-generated value, check that the database table allows generation of new primary key values, and that the mapped Column object is configured to expect these generated values.  Ensure also that this flush() is not occurring at an inappropriate time, such as within a load() event.
