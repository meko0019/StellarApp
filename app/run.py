import os

from config import *
from . import create_app


if os.environ['FLASK_ENV'] == 'development':
	app = create_app(DevelopmentConfig)

else:
	app = create_app(ProductionConfig)