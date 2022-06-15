from flask import Blueprint

index_blu = Blueprint("index_blu", __name__, template_folder="templates")

from .views import *