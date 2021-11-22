"""Config for Home Storage setup."""

####################################################################################################
# IMPORTS ################################################################################ IMPORTS #
####################################################################################################

# Standard library
import os

####################################################################################################
# CLASSES ################################################################################ CLASSES #
####################################################################################################


class Config(object):
    """Base config"""

    SITE_NAME = "Home Storage"
    SECRET_KEY = "REPLACE_THE_STRING_IN_PRODUCTION"

    # DB related config
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://TEST_USER:TEST_PASSWORD@db/HomeStorage"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Data related config
    MAX_CONTENT_LENGTH = 16777216
    MAX_DOWNLOAD_LIMIT = 1000000000

    # Expected paths - these are the bind paths *inside* the container
    USE_LOCAL_DB = True
    LOGS_DIR = "/home_storage/logs"

    # Devel settings
    TEMPLATES_AUTO_RELOAD = True
