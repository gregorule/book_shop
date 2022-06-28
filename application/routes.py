from application import app, db
from application.models import Books, Reviews
from application.forms import BookForm, ReviewForm
from flask import redirect, url_for, render_template, request

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/books')
def readBooks():
    book = Books.query.all()
    return render_template('books.html', books=book)