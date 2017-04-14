from app import app, db
from flask_script import Manager, prompt_bool

from models import User


manager = Manager(app)

@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username="bob", email="bob@mail.com"))
    db.session.add(User(username="john", email="john@mail.com"))
    db.session.commit()
    print("Initialized the database")

@manager.command
def dropdb():
    if prompt_bool(
        "Are you sure you want to lose all your data"
    ):
        db.drop_all()
        print("Dropped the db!")

if __name__ == "__main__":
    manager.run()