from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    # recaptcha = RecaptchaField()
    submit = SubmitField('Войти')


class CheckForm(FlaskForm):
    score = IntegerField('Ваш балл:', validators=[DataRequired()])
    submit = SubmitField('Проверить')
    submit_test = SubmitField('Перейти к тесту')


class TestForm(FlaskForm):
    username = StringField('Ответ')
    submit_next = SubmitField('Далее', description='Next')
    submit_back = SubmitField('Назад', description='Previous')
    submit_end = SubmitField('Закончить тест', description='End')
    submit_to_main = SubmitField('Вернуться назад')


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
    submit_back = SubmitField('Вернуться назад')