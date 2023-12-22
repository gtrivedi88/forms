import flask_principal

# These are permissions for accessing certain part sof the app

# All users can view taxonomy
view_permission = flask_principal.Permission(
    flask_principal.TypeNeed('all')
    )

# Users is the ccs-metadata group can create taxonomy terms
create_permission = flask_principal.Permission(
    flask_principal.Need('group','/ccs-metadata')
    )

# Users is the ccs-metadata group can edit taxonomy terms
edit_taxonomy_permission = flask_principal.Permission(
    flask_principal.Need('group','/ccs-metadata')
    )

# ccs-metadata admins can edit the docs attribute field for a taxonomy term
edit_attributes_permission = flask_principal.Permission(
    flask_principal.Need('group','/ccs-metadata-admin')
    )

# ccs-metadata group admins can delete a taxonomy term
delete_permission = flask_principal.Permission(
    flask_principal.Need('group','/ccs-metadata-admin')
    )
