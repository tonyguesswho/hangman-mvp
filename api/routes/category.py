"""
Defines the blueprint for the categories
"""
from flask import Blueprint
from flask_restful import Api

from api.resources import CategoryResource

CATEGORY_BLUEPRINT = Blueprint("category", __name__)
Api(CATEGORY_BLUEPRINT).add_resource(
    CategoryResource, "/category"
)
