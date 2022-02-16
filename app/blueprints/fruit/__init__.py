from flask import Blueprint

bp = Blueprint('fruit', __name__, url_prefix='/fruit')

from .import routes