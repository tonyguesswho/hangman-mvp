"""
Define the Category model
"""
from . import db, ma
from .abc import BaseModel

class Category(db.Model, BaseModel):
	"""	The Category Model"""

	__tablename__ = "category"
	id = db.Column(db.Integer, primary_key=True)
	name= db.Column(db.String(100), unique=True)
	description= db.Column(db.String(), unique=False)
	words = db.relationship('Word', backref=db.backref('category', lazy=True))

	def __init__(self, name, description, words):
		"""Create a new category"""
		self.name = name
		self.description = description
		self.words = words



class CategorySchema(ma.Schema):
	class Meta:
		fields=("id", "name", 'description')

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)