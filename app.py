"""Routes for home, login and register."""
from forms import SignInForm, RegisterForm
from flask import Flask, render_template
import secrets
secret_key = secrets.token_hex(16)


app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key


@app.route('/')
def home():
    """Welcome users to the page."""
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Return login form."""
    form = SignInForm()
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Return registration form."""
    form = RegisterForm()
    return render_template('register.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

#
