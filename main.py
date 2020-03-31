from flask import Flask
from data import db_session
#from data import users
from flask import render_template
from flask_form import LoginForm
from flask import redirect
from flask_form import CheckForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


'''def add_users():
    session = db_session.create_session()
    user = session.query(users.User).filter(users.User.id == 1).first()
    news = users.News(title="Вторая новость", content="Пока блог!", 
            user=user, is_private=False)
    session.add(news)
    session.commit()'''


@app.route("/")
def index():
    return redirect('/check_chances')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success/<points>')
def success(points):
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                   integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                   crossorigin="anonymous">
                    <title>Привет, {}</title>
                  </head>
                  <body>
                    <h1>Твои шансы равны {}%!</h1>
                  </body>
                </html>'''.format('Абитуриент', points)


@app.route('/check_chances', methods=['GET', 'POST'])
def check_chances():
    form = CheckForm()
    if form.validate_on_submit():
        if form.username.data.isdigit():
            if not 0 <= int(form.username.data) <=500:
                return render_template('check.html', title='Проверка баллов', form=form, not_is_digit=False, wrong_number=True)
            else:
                return redirect('/success/{}'.format(form.username.data))
        else:
            return render_template('check.html', title='Проверка баллов', form=form, not_is_digit=True, wrong_number=False)
        
    return render_template('check.html', title='Проверка баллов', form=form, not_is_digit=False, wrong_number=False, empty=True)


def main():
    db_session.global_init("db/abi.sqlite")
    #add_users()
    app.run()


if __name__ == '__main__':
    main()