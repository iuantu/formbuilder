import logging

""" jwt create access monkey patch"""
import datetime
import flask_jwt_extended
_create_access_token = flask_jwt_extended.create_access_token
def monkey_patch_create_access_token(identity, fresh=False, expires_delta=None, user_claims=None):
    return _create_access_token(identity, fresh, datetime.timedelta(days=365), user_claims)
flask_jwt_extended.create_access_token = monkey_patch_create_access_token

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger("flask_appbuilder")
logger.setLevel(logging.ERROR)
logging.getLogger("app").setLevel(logging.DEBUG)
# logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLA(app)
CORS(app)

migrate = Migrate(app, db)
appbuilder = AppBuilder(app, db.session)


"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""

from . import views, models