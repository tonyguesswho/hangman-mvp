"""
Defines the blueprint for words
"""
from flask import Blueprint
from flask_restful import Api

from api.resources import WordResource

WORD_BLUEPRINT = Blueprint("word", __name__)
Api(WORD_BLUEPRINT).add_resource(
    WordResource, "/word"
)
