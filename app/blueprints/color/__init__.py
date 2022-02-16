from flask import Blueprint

bp = Blueprint('color', __name__, url_prefix='/color')

from .import routes