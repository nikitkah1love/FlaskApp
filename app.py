from flask import Flask, render_template
from markupsafe import escape
from flask import request

app = Flask(__name__, template_folder='templates')


def do_the_login():
    pass

def show_the_login_form():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greetings')
def greetings():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
