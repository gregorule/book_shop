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

@app.route('/reviews')
def readReviews():
    review = Reviews.query.all()
    return render_template('reviews.html', reviews=review)

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

@app.route('/addReview', methods=['GET','POST'])
def addReview():
    form = ReviewForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            reviewData = Reviews(
                book_id = form.book_id.data,
                rating = form.rating.data,
                review = form.review.data
            )
            db.session.add(reviewData)
            db.session.commit()
            return redirect(url_for('readReviews'))
    return render_template('addreview.html', form=form)

@app.route('/update/<int:id>', methods= ['GET', 'POST'])
def updateBooks(id):
    form = BookForm()
    book = Books.query.get(id)
    if form.validate_on_submit():
        book.book_name = form.book_name.data
        book.author_name = form.author_name.data
        book.pages = form.pages.data
        book.genre = form.genre.data
        db.session.commit()
        return redirect(url_for('readBooks'))
    elif request.method == 'GET':
        form.book_name.data = book.book_name
        form.author_name.data = book.author_name
        form.pages.data = book.pages
        form.genre.data = book.genre
    return render_template('updateBooks.html', form=form)

@app.route('/updateReview/<int:id>', methods= ['GET', 'POST'])
def updateReviews(id):
    form = ReviewForm()
    review = Reviews.query.get(id)
    if form.validate_on_submit():
        review.book_id = form.book_id.data
        review.rating = form.rating.data
        review.review = form.review.data
        db.session.commit()
        return redirect(url_for('readReviews'))
    elif request.method == 'GET':
        form.book_id.data = review.book_id
        form.rating.data = review.rating
        form.review.data = review.review
    return render_template('updateReviews.html', form=form)

@app.route('/delete/<int:id>')
def deleteBooks(id):
    book = Books.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('readBooks'))

@app.route('/deleteReview/<int:id>')
def deleteReviews(id):
    review = Reviews.query.get(id)
    db.session.delete(review)
    db.session.commit()
    return redirect(url_for('readReviews'))