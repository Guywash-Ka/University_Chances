from flask import Flask, redirect, render_template, request
from data import db_session
from data.users import User
from flask_form import LoginForm, CheckForm, RegisterForm, TestForm, SuccessForm
from datetime import datetime
from flask_login import login_user, LoginManager, login_required, logout_user
from subjects import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init('db/abi.sqlite')
login_manager = LoginManager()
login_manager.init_app(app)


CORRECT_ANSWERS = [chr(i) for i in range(32, 125)]
QUESTION_NUMBER = 1 #номер задания
ANSWERS = []
is_test = False
test_number = 1
subjects_needed = []


# def add_users():
#     session = db_session.create_session()
#     user = session.query(users.User).filter(users.User.id == 1).first()
#     news = users.News(title="Вторая новость", content="Пока блог!",
#             user=user, is_private=False)
#     session.add(news)
#     session.commit()
def check_answers(answers):
    global CORRECT_ANSWERS
    count = 0

    for i in range(len(CORRECT_ANSWERS)):
        if answers[i] == CORRECT_ANSWERS[i]:
            count += 1

    return count


def count_questions(arr):
    res = 0
    for i in arr:
        res += number_of_questions[i]
    print(res)
    return res


def numb_to_skip(test):
    if test == 1:
        return 0
    elif test == 2:
        return number_of_questions[subjects_needed[0]]
    return number_of_questions[subjects_needed[1]] + number_of_questions[subjects_needed[0]]


def make_option_list(arr):
    pass




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


@app.route('/success/<points>', methods=['GET', 'POST'])
def success(points):
    global is_test
    form = SuccessForm()
    if form.is_submitted():
        return redirect('/')
    if is_test:
        question_numbers = (number_of_questions[subjects_needed[0]], number_of_questions[subjects_needed[1]], number_of_questions[subjects_needed[2]])
    else:
        question_numbers = -100
    return render_template('success.html', form=form, score=points, points=is_test, answers=ANSWERS, correct_answers=CORRECT_ANSWERS, question_numbers=question_numbers, subjects=subjects_needed)


@app.route('/check_chances', methods=['GET', 'POST'])
def check_chances():
    global QUESTION_NUMBER
    global CORRECT_ANSWERS
    global ANSWERS
    global is_test
    global subjects_needed
    global test_number
    form = CheckForm()
    if form.submit_subject.data:
        return render_template('check.html', title='Проверка баллов', form=form, wrong_number=False, subj=subjects[request.form['select']])
    if form.validate_on_submit():
        if form.submit.data:
            if not 0 <= int(form.score.data) <= 500:
                return render_template('check.html', title='Проверка баллов', form=form,
                                    wrong_number=True, subj=subjects[request.form['select']])
            else:
                is_test = False
                return redirect('/success/{}'.format(form.score.data))
    if form.submit_test.data:
        QUESTION_NUMBER = 1
        is_test = False
        test_number = 1
        subjects_needed = subjects[request.form['select']]
        ANSWERS = ['' for i in range(count_questions(subjects_needed))]
        CORRECT_ANSWERS = correct_answers_dict[subjects_needed[0]] + correct_answers_dict[subjects_needed[1]] + correct_answers_dict[subjects_needed[2]]
        return redirect('/test')
    
    return render_template('check.html', title='Проверка баллов', form=form, wrong_number=False)


@app.route('/test', methods=['GET', 'POST'])
def test():
    global QUESTION_NUMBER
    global ANSWERS
    global is_test
    global test_number
    global subjects_needed

    form = TestForm()

    if form.validate_on_submit():
        ANSWERS[numb_to_skip(test_number) + QUESTION_NUMBER - 1] = form.username.data
        if form.submit_back.data:
            if QUESTION_NUMBER != 1:
                QUESTION_NUMBER -= 1
                form.username.data = ANSWERS[numb_to_skip(test_number) + QUESTION_NUMBER - 1]
        elif form.submit_next.data:
            if QUESTION_NUMBER != number_of_questions[subjects_needed[test_number - 1]]:
                QUESTION_NUMBER += 1
                form.username.data = ANSWERS[numb_to_skip(test_number) + QUESTION_NUMBER - 1]
        elif form.submit_end.data:
            test_number += 1
            is_test = True
            if test_number == 4:
                print(ANSWERS)
                return redirect('/success/{}'.format(check_answers(ANSWERS)))
            else:
                QUESTION_NUMBER = 1
                question_text = [i for i in range(100)]
                if subjects_needed[test_number - 1] == 'Математика':
                    question_text = questions_for_math
                return render_template('test.html', title=subjects_needed[test_number - 1], form=form, number=QUESTION_NUMBER, question=question_text[QUESTION_NUMBER - 1])
        elif form.submit_to_main.data:
            return redirect('/')
        question_text = [i for i in range(100)]
        if subjects_needed[test_number - 1] == 'Математика':
            question_text = questions_for_math
        return render_template('test.html', title=subjects_needed[test_number - 1], form=form, number=QUESTION_NUMBER, question=question_text[QUESTION_NUMBER - 1])
    question_text = [i for i in range(100)]
    if subjects_needed[test_number - 1] == 'Математика':
        question_text = questions_for_math
    return render_template('test.html', title=subjects_needed[test_number - 1], form=form, number=QUESTION_NUMBER, question=question_text[QUESTION_NUMBER - 1])


def main():
    app.run(port=8080)


if __name__ == '__main__':
    main()
