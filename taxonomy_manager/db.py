INFO:sqlalchemy.engine.Engine:BEGIN (implicit)
INFO:sqlalchemy.engine.Engine:INSERT INTO brand_opl.product (id, product_name, product_description, upcoming_change, deprecated, product_status, last_updated, created, product_status_detail) VALUES (%(id)s, %(product_name)s, %(product_description)s, %(upcoming_change)s, %(deprecated)s, %(product_status)s, %(last_updated)s, %(created)s, %(product_status_detail)s)
INFO:sqlalchemy.engine.Engine:[generated in 0.00026s] {'id': 'cc5a9164-48e1-4325-b5dc-54ca784f5a62', 'product_name': 'dfdf', 'product_description': '', 'upcoming_change': False, 'deprecated': False, 'product_status': '', 'last_updated': datetime.date(2023, 12, 28), 'created': datetime.date(2023, 12, 28), 'product_status_detail': ''}
INFO:sqlalchemy.engine.Engine:ROLLBACK
INFO:werkzeug:127.0.0.1 - - [27/Dec/2023 00:01:44] "POST /opl/add-product HTTP/1.1" 500 -
Traceback (most recent call last):
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
    cursor.execute(statement, parameters)
psycopg2.errors.UndefinedColumn: column "id" of relation "product" does not exist
LINE 1: INSERT INTO brand_opl.product (id, product_name, product_des...
                                       ^


The above exception was the direct cause of the following exception:

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
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/session.py", line 4408, in _flush
    flush_context.execute()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/unitofwork.py", line 466, in execute
    rec.execute(self)
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/unitofwork.py", line 642, in execute
    util.preloaded.orm_persistence.save_obj(
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/persistence.py", line 93, in save_obj
    _emit_insert_statements(
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/persistence.py", line 1226, in _emit_insert_statements
    result = connection.execute(
             ^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1416, in execute
    return meth(
           ^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/sql/elements.py", line 516, in _execute_on_connection
    return connection._execute_clauseelement(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1639, in _execute_clauseelement
    ret = self._execute_context(
          ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1848, in _execute_context
    return self._exec_single_context(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1988, in _exec_single_context
    self._handle_dbapi_exception(
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 2343, in _handle_dbapi_exception
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/engine/base.py", line 1969, in _exec_single_context
    self.dialect.do_execute(
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/engine/default.py", line 922, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedColumn) column "id" of relation "product" does not exist
LINE 1: INSERT INTO brand_opl.product (id, product_name, product_des...
                                       ^

[SQL: INSERT INTO brand_opl.product (id, product_name, product_description, upcoming_change, deprecated, product_status, last_updated, created, product_status_detail) VALUES (%(id)s, %(product_name)s, %(product_description)s, %(upcoming_change)s, %(deprecated)s, %(product_status)s, %(last_updated)s, %(created)s, %(product_status_detail)s)]
[parameters: {'id': 'cc5a9164-48e1-4325-b5dc-54ca784f5a62', 'product_name': 'dfdf', 'product_description': '', 'upcoming_change': False, 'deprecated': False, 'product_status': '', 'last_updated': datetime.date(2023, 12, 28), 'created': datetime.date(2023, 12, 28), 'product_status_detail': ''}]
(Background on this error at: https://sqlalche.me/e/20/f405)
