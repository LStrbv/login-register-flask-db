"""Routes for home, login and register."""
from forms import LoginForm, RegisterForm
from UsersDatabase import UsersDatabase
from flask import Flask, render_template, redirect, url_for, flash, session, request
from flask_login import login_user, LoginManager, current_user, logout_user
import secrets
secret_key = secrets.token_hex(16)


app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key


login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.user_loader


UsersDatabase = UsersDatabase()
@app.route('/')
def home():
    """Return home page."""
    return render_template('layout.html')


@app.route('/user')
def user():
    """Return user profile page."""
    return render_template('user.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Return login form."""
    form = LoginForm()
    username = form.username.data
    #if form.validate_on_submit():
    if UsersDatabase.exists_user(username):
        UsersDatabase.generate_password(password=form.password.data)
        login_user(UsersDatabase, remember=True)
        flash('Přihlášení proběhlo úspěšně.')
        users_list = UsersDatabase.users_list()
        return render_template('user.html', name=username, list=users_list)
    """flash('Chybné jméno nebo heslo')
    return redirect(url_for('login', title='Přihlášení')) """
    return render_template('login.html', form=form, title='Přihlášení')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Return registration form."""
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if UsersDatabase.exists_user(username) is not True:
            UsersDatabase.session.add_user(username, password)
            UsersDatabase.generate_password(password)
            login_user(UsersDatabase)
            return redirect(url_for('user'))
        flash('Uživatel s tímto jménem už existuje.')
    return render_template('register.html', form=form, title='Registrace')


@login_manager.user_loader
def load_user(id):
    """Check if user is logged-in upon page load."""
    return id

@app.errorhandler(404)
def page_not_found(error):
    """Return when page doesnt exist."""
    return render_template('404.html'), 404



if __name__ == "__main__":
    app.run(debug=True)
