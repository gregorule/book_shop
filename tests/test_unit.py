from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Books, Reviews
from application.forms import BookForm,ReviewForm
from flask import redirect, url_for, render_template, request


class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY="testSecretKey",
            DEBUG=True,
            WTF_CSRF_ENABLED=False
            )
        return app

    def setUp(self):
        db.create_all()
        testBooks = Books(
            book_name='Test',
            author_name='Test',
            pages=123,
            genre='Test'
            )
        db.session.add(testBooks)
        db.session.commit()

        testReview = Reviews(
            book_id=1,
            rating="1",
            review="Test"
        )
        db.session.add(testReview)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_books_get(self):
        response = self.client.get(url_for('readBooks'))
        self.assertEqual(response.status_code, 200)
    def test_reviews_get(self):
        response = self.client.get(url_for('readReviews'))
        self.assertEqual(response.status_code, 200)
    def test_readReviews_get(self):
        response = self.client.get(url_for('readReviewsTwo',id=1))
        self.assertEqual(response.status_code, 200)

    def test_addBooks_get(self):
        response = self.client.get(url_for('addBooks'))
        self.assertEqual(response.status_code, 200)
    def test_addReviews_get(self):
        response = self.client.get(url_for('addReview'))
        self.assertEqual(response.status_code, 200)
    def test_addReviewTwo_get(self):
        response = self.client.get(url_for('addReviewTwo', id=1))
        self.assertEqual(response.status_code, 200)

    def test_updateBooks_get(self):
        response = self.client.get(url_for('updateBooks', id=1))
        self.assertEqual(response.status_code, 200)
    def test_updateReviews_get(self):
        response = self.client.get(url_for('updateReviews', id=1))
        self.assertEqual(response.status_code, 200)
        
    def test_deleteBooks_get(self):
        response = self.client.get(url_for('deleteBooks', id=1))
        self.assertEqual(response.status_code, 200)
    def test_deleteReviews_get(self):
        response = self.client.get(url_for('deleteReviews', id=1))
        self.assertEqual(response.status_code, 302)

class TestAdd(TestBase):
    def test_book_add(self):
        response = self.client.post(
            url_for('addBooks'),
            data = dict(book_name="James and the Giant Peach",author_name="Roald Dahl",pages=160,genre="Fantasy")
        )
        assert Books.query.filter_by(book_name="James and the Giant Peach").first().book_id == 2
        assert len(Books.query.all()) == 2
        

    def test_review_add(self):
        response = self.client.post(
            url_for('addReview'),
            data = dict(book_id=2,rating="3",review="What a large fruit!")
        )
        assert Reviews.query.filter_by(book_id=2).first().review_id == 2
        assert len(Reviews.query.all()) == 2


    def test_reviewTwo_add(self):
        response = self.client.post(
            url_for('addReviewTwo',id=2),
            data = dict(book_id=2,rating="3",review="What a large fruit!")
        )
        assert Reviews.query.filter_by(book_id=2).first().review_id == 2
        assert len(Reviews.query.all()) == 2
    

class TestUpdate(TestBase):
    def test_book_update(self):
        response = self.client.post(
            url_for('updateBooks',id=1),
            data = dict(book_name="updateTest",author_name="updateTest",pages=321,genre="updateTest")
        )
        assert Books.query.filter_by(book_name="updateTest").first().book_id ==1
        assert len(Books.query.all()) == 1

    def test_review_update(self):
        response = self.client.post(
            url_for('updateReviews',id=1),
            data = dict(book_id=1,rating="5",review="updateTest")
        )
        assert Reviews.query.filter_by(book_id=1).first().review_id ==1
        assert len(Reviews.query.all()) == 1

class TestDelete(TestBase):
    def test_book_delete(self):
        response = self.client.get(
            url_for('deleteBooks',id=1),
            data = dict(book_name="Test",author_name="Test",pages=123,genre="Test")
        )
        assert len(Books.query.all()) == 1

    def test_review_delete(self):
        response = self.client.get(
            url_for('deleteReviews',id=1),
            data = dict(book_id=1,rating="1",review="Test")
        )
        assert len(Books.query.all()) == 1

    
        