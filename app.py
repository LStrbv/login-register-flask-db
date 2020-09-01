"""Routes for home, login and register."""
from forms import LoginForm, RegisterForm
from UsersDatabase import UsersDatabase
#import pomocny_slovnik
from flask import Flask, render_template, request, redirect, url_for, flash
import secrets
secret_key = secrets.token_hex(16)


app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key


@app.route('/')
def home():
    """Welcome users to the page."""
    return render_template('home.html')

""" @app.route('/user')
def user():
    return render_template('user.html')
 """
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Return login form."""
    form = LoginForm()
    username = form.username.data
    user = UsersDatabase(username, 'banan')
    #if form.validate_on_submit():
    if user.exists_user():
        return render_template('user.html', name=username)
    else:
        flash('Uživatel neexistuje')
        return render_template('login.html', form=form, title='Přihlášení')
        
    return render_template('login.html', form=form, title='Přihlášení')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Return registration form."""
    form = RegisterForm()
    return render_template('register.html', form=form, title='Registrace')


if __name__ == "__main__":
    app.run(debug=True)
