from application import app, db
from application.models import ToDos
from application.forms import TaskForm
from flask import redirect, url_for, render_template, request

@app.route('/')
def about():
    return render_template("about.html")