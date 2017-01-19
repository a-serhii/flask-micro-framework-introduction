from flask import Flask, render_template, url_for

app = Flask(__name__)

class User:
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name

    def initials(self):
        return "{}. {}.".format(self.firstname[0], self.lastname[0])


@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html', title='It title in py-file',
                           user=User('Sergey', 'A')
                           )

@app.route('/add')
def add():
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
