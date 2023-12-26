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
  File "/home/gtrivedi/git/gitlab/opl-ui/app.py", line 26, in add_product
    product_portfolios = ProductPortfolio.query.all()
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask_sqlalchemy/model.py", line 22, in __get__
    return cls.query_class(
           ^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/query.py", line 276, in __init__
    self._set_entities(entities)
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/query.py", line 289, in _set_entities
    coercions.expect(
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/sql/coercions.py", line 406, in expect
    insp._post_inspect
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/util/langhelpers.py", line 1260, in __get__
    obj.__dict__[self.__name__] = result = self.fget(obj)
                                           ^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/mapper.py", line 2707, in _post_inspect
    self._check_configure()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/mapper.py", line 2386, in _check_configure
    _configure_registries({self.registry}, cascade=True)
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/mapper.py", line 4199, in _configure_registries
    _do_configure_registries(registries, cascade)
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/mapper.py", line 4240, in _do_configure_registries
    mapper._post_configure_properties()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/mapper.py", line 2403, in _post_configure_properties
    prop.init()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/interfaces.py", line 579, in init
    self.do_init()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/relationships.py", line 1637, in do_init
    self._setup_join_conditions()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/relationships.py", line 1882, in _setup_join_conditions
    self._join_condition = jc = JoinCondition(
                                ^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/relationships.py", line 2306, in __init__
    self._determine_joins()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/relationships.py", line 2419, in _determine_joins
    self.primaryjoin = join_condition(
                       ^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/sql/util.py", line 123, in join_condition
    return Join._join_condition(
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/sql/selectable.py", line 1341, in _join_condition
    constraints = cls._joincond_scan_left_right(
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/sql/selectable.py", line 1450, in _joincond_scan_left_right
    col = fk.get_referent(b)
          ^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/sql/schema.py", line 3022, in get_referent
    return table.columns.corresponding_column(self.column)  # type: ignore
                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/util/langhelpers.py", line 1146, in __get__
    obj.__dict__[self.__name__] = result = self.fget(obj)
                                           ^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/sql/schema.py", line 3159, in column
    return self._resolve_column()
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/sql/schema.py", line 3198, in _resolve_column
    return self._link_to_col_by_colstring(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/sql/schema.py", line 3120, in _link_to_col_by_colstring
    raise exc.NoReferencedColumnError(
sqlalchemy.exc.NoReferencedColumnError: Could not initialize target column for ForeignKey 'brand_opl.product.id' on table 'product_portfolio_map': table 'product' has no column named 'id'
