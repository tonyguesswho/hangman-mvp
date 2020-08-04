"""
Define the REST verbs relative to the categories
"""

from flask_restful import Resource
from api.repositories import CategoryRepository
from flask_restful.reqparse import Argument
from api.util import parse_params
from api.models import categories_schema, category_schema

class CategoryResource(Resource):
	""" Verbs relative to the categories """

	@staticmethod
	def get():
		""" Return all categories """
		categories = CategoryRepository.get_all()
		return {
			"status":"success",
			"categories":categories_schema.dump(categories)
		}

	@staticmethod
	@parse_params(Argument("name", location='json', required=True, help="Name is required"))
	@parse_params(Argument("description", location='json', required=False))
	@parse_params(Argument("words", location='json', type=str, action='append'))
	def post(name, description, words):
		""" Create an category based on the sent information """
		existing_category = CategoryRepository.get_one(name=name.lower())
		if existing_category:
			return {
				'status':"error",
				'messagee': 'Category already exists',
			}, 409
		category = CategoryRepository.create(name=name.lower(), description=description, words=words)

		return {
			"status":"success",
			"data": category_schema.dump(category)
		}
