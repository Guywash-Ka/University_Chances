from flask import Flask, redirect, render_template, request
from data import db_session
from data.users import User
from flask_form import LoginForm, CheckForm, RegisterForm, TestForm
from datetime import datetime
from flask_login import login_user, LoginManager, login_required, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init('db/abi.sqlite')
login_manager = LoginManager()
login_manager.init_app(app)


QUESTION_NUMBER = 1 #номер задания

# def add_users():
#     session = db_session.create_session()
#     user = session.query(users.User).filter(users.User.id == 1).first()
#     news = users.News(title="Вторая новость", content="Пока блог!",
#             user=user, is_private=False)
#     session.add(news)
#     session.commit()


@app.route("/")
def index():
    return redirect('/check_chances')


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form, message="Пароли не совпадают")
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form, message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
            about=form.about.data,
            created_date=datetime.now()
        )
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        login_user(user, remember=form.remember_me.data)
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html', message="Неправильный логин или пароль", form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/success/<points>')
def success(points):
    return render_template('success.html', score=points)


@app.route('/check_chances', methods=['GET', 'POST'])
def check_chances():
    form = CheckForm()
    if form.validate_on_submit():
        if form.submit.data:
            if not 0 <= int(form.score.data) <= 500:
                return render_template('check.html', title='Проверка баллов', form=form,
                                    wrong_number=True)
            else:
                return redirect('/success/{}'.format(form.score.data))
        elif form.submit_test.data:
            return redirect('/test')
    if form.submit_test.data:
            return redirect('/test')
    return render_template('check.html', title='Проверка баллов', form=form, wrong_number=False)


@app.route('/test', methods=['GET', 'POST'])
def test():
    global QUESTION_NUMBER
    form = TestForm()
    if form.validate_on_submit():
        if form.submit_back.data:
            if QUESTION_NUMBER != 1:
                QUESTION_NUMBER -= 1
        elif form.submit_next.data:
            QUESTION_NUMBER += 1
        return render_template('test.html', title='Тест', form=form, number=QUESTION_NUMBER)
    return render_template('test.html', title='Тест', form=form, number=QUESTION_NUMBER)


def main():
    app.run(port=8080)


if __name__ == '__main__':
    main()
