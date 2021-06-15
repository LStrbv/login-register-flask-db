"""Routes for home, login and register."""
from forms import LoginForm, RegisterForm
import secrets
from UsersDatabase import User
from db import db
from flask import Flask, render_template, redirect, url_for, flash, session, request
from flask_login import login_user, LoginManager, current_user, logout_user, login_required
secret_key = secrets.token_hex(16)


def register_extensions(app):
    db.init_app(app)


app = Flask(__name__)
register_extensions(app)
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.user_loader

""" usersDatabase = UsersDatabase() """
@app.route('/')
def home():
    """Return home page."""
    return render_template('layout.html')


@app.route('/user')
@login_required
def user():
    """Return user profile page."""
    users = User.query.all()
    return render_template('user.html', users=users)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """GET return registration form. POST requests validate and redirect user to home page."""
    # If user is logged in.
    if current_user.is_authenticated:
        return redirect(url_for('user'))

    form = LoginForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.check_password(password=form.password.data):
                login_user(user, remember=True)
                flash('Přihlášení proběhlo úspěšně.')
                return redirect(url_for('user'))
            else:
                flash('Chybné heslo')
                return redirect(url_for('login'))
        else:
            flash('Chybné jméno')
            return redirect(url_for('login'))
    return render_template('login.html', form=form, title='Přihlášení')


@app.route('/remove/<username>')
def remove(username):
    """Remove user."""
    user = User.query.filter_by(username=username).first()
    db.session.delete(user)
    db.session.commit()

    flash('Uživatel byl odstraněn.')
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Return signup page."""
    form = RegisterForm()
    if form.validate_on_submit():
        exist_user = User.query.filter_by(username=form.username.data).first()
        if not exist_user:
            user = User(
                username=form.username.data,
                password=form.password.data,
                picture=form.picture.data
            )
            user.set_password(password=form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            return redirect(url_for('user'))
        else:
            flash('Uživatel s tímto jménem už existuje.')
    return render_template('register.html', form=form)


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in upon page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@app.errorhandler(404)
def page_not_found(error):
    """Return when page doesnt exist."""
    return render_template('404.html'), 404


@app.route('/logout')
@login_required
def logout():
    """Logout user."""
    logout_user()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
