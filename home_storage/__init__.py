"""Initialize Flask app."""

####################################################################################################
# IMPORTS ################################################################################ IMPORTS #
####################################################################################################

# Standard library
import logging

# Installed
import flask
import pytz
from flask_sqlalchemy import SQLAlchemy

####################################################################################################
# GLOBAL VARIABLES ############################################################## GLOBAL VARIABLES #
####################################################################################################

# Current time zone
C_TZ = pytz.timezone("Europe/Stockholm")

# Database - not yet init
db = SQLAlchemy()

####################################################################################################
# FUNCTIONS ############################################################################ FUNCTIONS #
####################################################################################################


def create_app(testing=False, database_uri=None):
    """Construct the core application."""
    # Initiate app object
    app = flask.Flask(__name__, instance_relative_config=False)

    # Default development config
    app.config.from_object("home_storage.config.Config")

    # User config file, if e.g. using in production
    app.config.from_envvar("HS_APP_CONFIG", silent=True)

    # Test related configs
    if database_uri is not None:
        app.config["SQLALCHEMY_DATABASE_URI"] = database_uri

    # Set app.logger as the general logger
    app.logger = logging.getLogger("general")
    app.logger.info("Logging initiated.")

    # Initialize database
    db.init_app(app)

    with app.app_context():  # Everything in here has access to sessions
        db.create_all()  # TODO: remove this when we have migrations
        from home_storage import models

        # Register blueprints
        from home_storage.api import api_blueprint

        app.register_blueprint(api_blueprint, url_prefix="/api/v1")

        return app
