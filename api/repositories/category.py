from api.models import Category, category_schema, Word


class CategoryRepository:

	@staticmethod
	def get_all():
		""" Query all categories """
		return Category.query.all()

	def get_one(name):
		""" Query all categories """
		return Category.query.filter_by(name=name).first()
	

	@staticmethod
	def create(name, description, words):
		""" Create a new category """
		words_obj=[]
		if words:
			for word in words:
				words_obj.append(Word(word=word))
		category = Category(name=name, description=description, words=words_obj)
		return category.save()
