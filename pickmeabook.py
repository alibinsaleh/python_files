class Book:
	def __init__(self, book_id, book_title, book_author, book_genre, num_pages=0):
		self.book_id = book_id
		self.book_title = book_title
		self.book_author = book_author
		self.book_genre = book_genre
		self.num_pages = num_pages


class Read:
	def __init__(self, book_id)