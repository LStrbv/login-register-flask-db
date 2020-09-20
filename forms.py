"""Import sign up and login forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField 
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
            Length(min=3, message='Heslo musí obsahovat nejméně 3 znaky!'),
        ]
    )

    picture = StringField(
        'Profilový obrázek-url',
        validators=[
            DataRequired(),
        ],
    )
    confirm_password = PasswordField(
        'Potvrď heslo',
        validators=[
            DataRequired(),
            EqualTo('password', message='Hesla se musí shodovat!')
        ]
    )
    signup = SubmitField('Registrovat')
