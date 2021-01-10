"""Routes for home, login and register."""
from forms import LoginForm, RegisterForm
from UsersDatabase import UsersDatabase
from flask import Flask, render_template, redirect, url_for, flash, session, request
from flask_login import login_user, LoginManager, current_user, logout_user, login_required
import secrets
secret_key = secrets.token_hex(16)


app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key


login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.user_loader


usersDatabase = UsersDatabase()
@app.route('/')
def home():
    """Return home page."""
    return render_template('layout.html')


@app.route('/user')
@login_required
def user():
    """Return user profile page."""
    users = usersDatabase.load()
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
        username = form.username.data
        password = form.password.data
        user = usersDatabase.get_by_id(username)
        if user:
            if user.check_password(password):
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
    
    usersDatabase.remove_user(username)
    flash('Uživatel byl odstraněn.')
    return redirect(url_for('user'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Return signup page."""
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        picture = form.picture.data
        user = usersDatabase.get_by_id(username)
        if not user:
            user = usersDatabase.add_user(username, password, picture)
            login_user(user, remember=True)
            return redirect(url_for('user'))
        else:
            flash('Uživatel s tímto jménem už existuje.')
    return render_template('register.html', form=form)


@login_manager.user_loader
def load_user(username):
    """Check if user is logged-in upon page load."""
    return usersDatabase.get_by_id(username)

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
