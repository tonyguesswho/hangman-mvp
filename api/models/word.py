"""
Define the Word model
"""
from . import db, ma
from .abc import BaseModel



class Word(db.Model, BaseModel):
	"""Answer model"""
	id = db.Column(db.Integer, primary_key=True)
	word= db.Column(db.String(100), unique=True)
	category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
	

	def __init__(self, word):
		""" Create a new Word """
		self.word = word
    

class WordSchema(ma.Schema):
	class Meta:
		fields=("id", "word")

word_schema = WordSchema()
words_schema = WordSchema(many=True)