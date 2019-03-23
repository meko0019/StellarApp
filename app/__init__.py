import os

from flask import Flask
from flask_migrate import Migrate


def create_app(config_object=None):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config_object)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .db import db
    from .views import api_blueprint
    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(api_blueprint)

    return app