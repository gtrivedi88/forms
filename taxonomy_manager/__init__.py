import os
import inspect
import flask_saml
import flask_principal
from flask import Flask, url_for, session, current_app, g
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from taxonomy_manager.db import db

def create_app(test_config=None):

    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # Initialize the module to provide user permissions
    principals = flask_principal.Principal(app)

    # Config settings taken from environment variables
    pg_user = os.environ["PGUSER"]
    pg_pass = os.environ["PGPASS"]
    pg_host = os.environ["PGHOST"]
    pg_port = os.environ["PGPORT"]
    pg_db = os.environ["PGDB"]
    db_conn = "postgresql+psycopg2://%s:%s@%s:%s/%s" % (pg_user, pg_pass, pg_host, pg_port, pg_db)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI = db_conn,
        SAML_METADATA_URL = os.environ["SAML_METADATA_URL"],
        SAML_DEFAULT_REDIRECT = '/',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize the app
    db.init_app(app)

    # Create a SAML connection for our app
    flask_saml.FlaskSAML(app)

    # Actions to perform when a user logs in
    @flask_saml.saml_authenticated.connect_via(app)
    def on_saml_authenticated(sender, subject, attributes, auth):
        # We have a logged in user, inform Flask-Principal
        flask_principal.identity_changed.send(
            current_app._get_current_object(), identity=get_identity())

    # Actions to perform when a user logs out
    @flask_saml.saml_log_out.connect_via(app)
    def on_saml_logout(sender):
        # Let Flask-Principal know the user is gone
        flask_principal.identity_changed.send(
            current_app._get_current_object(), identity=get_identity())

    # Set the user identity for the application
    @principals.identity_loader
    def get_identity():
        if 'saml' in session:
            return flask_principal.Identity(session['saml']['subject'])
        else:
            return flask_principal.AnonymousIdentity()

    # Actions to perform after setting the user identity
    @flask_principal.identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        # Define the permission need for all users
        identity.provides.add(
            flask_principal.TypeNeed("all")
        )
        if not isinstance(identity, flask_principal.AnonymousIdentity):
            # Define the permission need for the user's roles
            for role in session['saml']['attributes']['Role']:
                identity.provides.add(
                    flask_principal.RoleNeed(role)
                )
            # Define the permission need for the user's groups
            for group in session['saml']['attributes']['group']:
                identity.provides.add(
                    flask_principal.Need('group', group)
                )
            # Define the permission need for an authenticated user
            identity.provides.add(
                flask_principal.TypeNeed("authenticated")
            )
        else:
            # Define the permission need for an anonymous user
            identity.provides.add(
                flask_principal.TypeNeed("anonymous")
            )

    # Set the variable for the username, which we use in our masthead for an
    # authenticated user.
    @app.context_processor
    def get_current_user():
        needs={}
        for need in g.identity.provides:
            if need.method not in needs:
                needs[need.method]=[]
            needs[need.method].append(need.value)
        return dict(user=g.identity.id, needs=needs)

    # If a user does not have access to a particular resource, send them
    # to our 403 page.
    @app.errorhandler(flask_principal.PermissionDenied)
    def handle_permission_denied(error):
        return render_template('403.html'), 403

    # render the root
    @app.route('/')
    def index():
        return render_template('index.html', title='Welcome')

    # handle 404 errors
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    # taxonomy routes
    from . import taxonomy
    app.register_blueprint(taxonomy.bp)



    return app
