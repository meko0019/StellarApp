from flask import Blueprint

api_blueprint = Blueprint('api_blueprint', __name__, template_folder='templates')

@api_blueprint.route('/hello')
def hello():
    return 'Hello, World!'