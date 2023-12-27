Traceback (most recent call last):
  File "/home/gtrivedi/git/gitlab/opl-ui/app.py", line 4, in <module>
    from models import db, Product, ProductType, ProductTypeMap, ProductPortfolios, ProductPortfolioMap, ProductNotes, ProductReference
  File "/home/gtrivedi/git/gitlab/opl-ui/models.py", line 77, in <module>
    class ProductReference(db.Model):
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask_sqlalchemy/model.py", line 92, in __init__
    super().__init__(name, bases, d, **kwargs)
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask_sqlalchemy/model.py", line 144, in __init__
    super().__init__(name, bases, d, **kwargs)
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/decl_api.py", line 195, in __init__
    _as_declarative(reg, cls, dict_)
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/decl_base.py", line 247, in _as_declarative
    return _MapperConfig.setup_mapping(registry, cls, dict_, None, {})
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/decl_base.py", line 328, in setup_mapping
    return _ClassScanMapperConfig(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/decl_base.py", line 582, in __init__
    self._early_mapping(mapper_kw)
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/decl_base.py", line 369, in _early_mapping
    self.map(mapper_kw)
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/decl_base.py", line 1957, in map
    mapper_cls(self.cls, self.local_table, **self.mapper_args),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 2, in __init__
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/util/deprecations.py", line 281, in warned
    return fn(*args, **kwargs)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/mapper.py", line 853, in __init__
    self._configure_pks()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/sqlalchemy/orm/mapper.py", line 1637, in _configure_pks
    raise sa_exc.ArgumentError(
sqlalchemy.exc.ArgumentError: Mapper Mapper[ProductReference(product_references)] could not assemble any primary key columns for mapped table 'product_references'
