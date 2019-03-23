import os

from config import *
from . import create_app

def run():
	if os.environ['FLASK_ENV'] == 'development':
		return create_app(DevelopmentConfig)

	return create_app(ProductionConfig)