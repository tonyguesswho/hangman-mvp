from api.models import Word


class WordRepository:

	@staticmethod
	def get_by_category(category_id):
		""" Query all categories """
		if category_id:
			return Word.query.filter_by(category_id=category_id)
		return Word.query.all()

