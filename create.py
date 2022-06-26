from application import db
from application.models import ToDos

db.drop_all()
db.create_all()
'''
sample_todo = ToDos(
    task = "Sample todo",
    completed = False
)
db.session.add(sample_todo)
'''
db.session.commit()