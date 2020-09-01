"""Import sign up and login forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Uživatel', validators=[DataRequired()])
    password = PasswordField('Heslo', validators=[DataRequired()])
    submit = SubmitField('Přihlásit')


class RegisterForm(FlaskForm):
    """Register form."""

    username = StringField('Uživatel', validators=[DataRequired()])
    password = PasswordField(
        'Heslo',
        validators=[
            DataRequired(),
            Length(min=7, message='Heslo musí obsahovat nejméně 6 znaků.'),
        ]
    )
    confirm_password = PasswordField(
        'Potvrď heslo',
        validators=[
            DataRequired(),
            EqualTo('Heslo', message='Hesla se musí shodovat.')
        ]
    )
    signup = SubmitField('Registrovat')
