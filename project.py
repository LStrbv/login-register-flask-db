from flask import Flask, render_template, url_for, GET, POST
from flask_wtf import FlaskForm
# from flask_login import LoginManager
from wtforms import StringField, PasswordField, SubmitField
import secrets
secret_key = secrets.token_hex(16)

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key


@app.route('/')
def home():
    """Welcome users to the page."""
    return render_template('home.html')


@app.route('/login', methods=[GET, POST])
def login():
    """Return login form."""
    form = SignInForm()
    return render_template('login.html', form=form)


@app.route('/register')
def registration():
    """Return registration form."""
    form = RegisterForm()
    return render_template('register.html', form=form)


class SignInForm(FlaskForm):
    """Define sign in form."""

    username = StringField('Uživatel')
    password = PasswordField('Heslo')
    submit = SubmitField('Přihlásit')


class RegisterForm(FlaskForm):
    """Define sign up form."""

    username = StringField('Uživatel')
    password = PasswordField('Heslo')
    signup = SubmitField('Registrovat')


if __name__ == "__main__":
    app.run(debug=True)
