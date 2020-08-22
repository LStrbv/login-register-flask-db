from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
import secrets
secret_key = secrets.token_hex(16)

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = secret_key


@app.route('/')
def home():
    """Welcome users to the page."""
    return render_template('home.html')


@app.route('/login')
def login():
    """Return login form."""
    form = SignUpForm()
    return render_template('login.html', form=form)


class SignUpForm(FlaskForm):
    """Define sign up form."""

    username = StringField('Uživatel')
    password = PasswordField('Heslo')
    submit = SubmitField('Přihlásit')


if __name__ == "__main__":
    app.run()
