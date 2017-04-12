import os
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import BookmarkForm


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = b'\x9cCp\xddMW\x04\xda\x08\xe1\xc5\xf3\xef{"\xd5!f\xbf\x8e\xf3\xd64!'
# import os
# os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
db = SQLAlchemy(app)


from forms import BookmarkForm
import models


# Fake login
def logged_in_user():
    return models.User.query.filter_by(username="bob").first()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks=models.Bookmark.newest(5))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        bm = models.Bookmark(url=url, description=description)
        db.session.add(bm)
        db.session.commit()
        flash("Stored bookmark: '{}'".format(description))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error():
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
