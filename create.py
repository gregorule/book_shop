from application import db
from application.models import Books, Reviews

db.drop_all()
db.create_all()

sample_book = Books(
    book_name = "1984",
    author_name = "George Orwell"
    pages = 328
    genre = "Science Fiction"
)
db.session.add(sample_book)
db.session.commit()

sample_review = Reviews(
    book_id = 1
    rating = "5"
    review = "I loved this book!"
)
db.session.add(sample_review)
db.session.commit()