from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField

class BookForm(FlaskForm):
    book_name = StringField("Name of book")
    author_name = StringField("Name of author")
    pages = IntegerField("How many pages?")
    genre = StringField("What is the genre?")
    submit = SubmitField("Submit")

class ReviewForm(FlaskForm):
    book_id = IntegerField("What is the id of the book you are reviewing?")
    rating = SelectField("What rating would you give this book out of 5?", choices=[
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5")
    ])
    review = StringField("Please write a short review of this book")
    book_ref = BookForm.book_name
    submit = SubmitField("Submit")