from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')

def hello_world():
    return render_template('index.html')
    # return 'Hi!'

if __name__ == '__main__':
    app.run(debug=True)
