from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me')
    recaptcha = RecaptchaField()
    submit = SubmitField('submit')


class CheckForm(FlaskForm):
    username = StringField('Ваш балл:', validators=[DataRequired()])
    submit = SubmitField('Проверить')