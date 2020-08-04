from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

from .category import Category, category_schema, categories_schema
from .word import Word, words_schema, word_schema