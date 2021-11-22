"""Database table models."""

####################################################################################################
# IMPORTS ################################################################################ IMPORTS #
####################################################################################################

# Own modules
from home_storage import db


####################################################################################################
# MODELS ################################################################################## MODELS #
####################################################################################################


class Shelf(db.Model):
    """Data model for locations."""

    # Primary key
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Columns
    name = db.Column(db.String(255), unique=True, nullable=False)
    room = db.Column(db.String(255), unique=False, nullable=False)
