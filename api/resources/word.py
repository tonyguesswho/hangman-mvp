"""
Define the REST verbs relative to words
"""
from flask import request
from flask_restful import Resource
from api.repositories import WordRepository
from api.models import words_schema

class WordResource(Resource):
	""" Verbs relative to the words """

	@staticmethod
	def get():
		""" Return all words by category """
		category_id = request.args.get('category_id')
		words = WordRepository.get_by_category(category_id)
		return {
			"status":"success",
			"words":words_schema.dump(words)
		}