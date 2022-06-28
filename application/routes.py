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

@app.route('/add', methods=['GET','POST'])
def addBooks():
    form = BookForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            bookData = Books(
                book_name = form.book_name.data,
                author_name = form.author_name.data,
                pages = form.pages.data,
                genre = form.genre.data
            )
            db.session.add(bookData)
            db.session.commit()
            return redirect(url_for('readBooks'))
    return render_template('addbook.html', form=form)



@app.route('/delete/<int:id>')
def deleteBooks(id):
    book = Books.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('readBooks'))