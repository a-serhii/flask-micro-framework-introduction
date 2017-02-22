from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)
app.config['SECRET_KEY'] = b'\x9cCp\xddMW\x04\xda\x08\xe1\xc5\xf3\xef{"\xd5!f\xbf\x8e\xf3\xd64!'
# import os
# os.urandom(24)
bookmarks = []


def store_bookmark(url):
    bookmarks.append(dict(
        url=url,
        user='reindert',
        date=datetime.utcnow()
    ))


def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks=new_bookmarks(5))


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmark(url)
        app.logger.debug('stored url: ' + url)
        flash("Stored bookmark: '{}'".format(url))
        return redirect(url_for('index'))
    return render_template('add.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error():
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
