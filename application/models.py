from application import db

class Books(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(50), nullable=False)
    author_name = db.Column(db.String(50), nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(20), nullable=False)

class Reviews(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('Books.book_id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(200), nullable=False)
