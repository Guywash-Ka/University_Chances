from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, FieldList
from wtforms.validators import DataRequired
from subjects import *


class LoginForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    # recaptcha = RecaptchaField()
    submit = SubmitField('Войти')


class CheckForm(FlaskForm):
    score = IntegerField('Сумма ваших баллов по трём экзаменам:', validators=[DataRequired()])
    submit = SubmitField('Проверить вероятность поступления')
    submit_test = SubmitField('Пройти выбранные экзамены')
    select = SelectField('Предметы', choices=[(i, i) for i in subjects.keys()])
    submit_subject = SubmitField('Выбрать')


class TestForm(FlaskForm):
    username = StringField('Ваш ответ:')
    submit_next = SubmitField('Следующий вопрос', description='Next')
    submit_back = SubmitField('Предыдущий вопрос', description='Previous')
    submit_end = SubmitField('Закончить тест', description='End')
    submit_to_main = SubmitField('Вернуться на главную страницу')


class RegisterForm(FlaskForm):
    email = StringField('Почта*', validators = [DataRequired()])
    password = PasswordField('Пароль*', validators = [DataRequired()])
    password_again = PasswordField('Повторите пароль*', validators = [DataRequired()])
    surname = StringField('Фамилия*', validators=[DataRequired()])
    name = StringField('Имя*', validators = [DataRequired()])
    age = IntegerField('Возраст*', validators = [DataRequired()])
    about = StringField("О себе")
    remember_me = BooleanField('Запомнить меня')
    # recapcha = RecaptchaField()
    submit = SubmitField('Подтвердить')


class SuccessForm(FlaskForm):
    submit_back = SubmitField('Вернуться на главную страницу')