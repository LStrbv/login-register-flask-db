"""Routes for home, login and register."""
from forms import LoginForm, RegisterForm
from UsersDatabase import UsersDatabase
from flask_login import login_user
from flask import Flask, render_template, request, redirect, url_for, flash
import secrets
secret_key = secrets.token_hex(16)


app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key


@app.route('/')
def home():
    """Welcome users to the page."""
    return render_template('home.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Return login form."""
    form = LoginForm()
    username = form.username.data
    password = form.password.data
    user = UsersDatabase(username, password)
    if form.validate_on_submit():
        if user.exists_user() and user.check_password(password):
            login_user(user)
            users_list = user.users_list()
            return render_template('user.html', name=username, list=users_list)
        flash('Chybné jméno nebo heslo')
        return redirect(url_for('login', title='Přihlášení'))
    return render_template('login.html', form=form, title='Přihlášení')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Return registration form."""
    form = RegisterForm()
    
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = UsersDatabase(username, password)
        existing_user = user.query.filter_by(username=form.username.data).first()
        if existing_user is None:
            user.add_user()
            user.set_password(form.password.data)
            login_user(user)
            return redirect(url_for('user'))
        flash('Uživatel s tímto jménem už existuje.')
    return render_template('register.html', form=form, title='Registrace')


if __name__ == "__main__":
    app.run(debug=True)
