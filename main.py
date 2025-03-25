from flask import Flask, url_for, request

app = Flask(__name__)


@app.route("/")
def page1():
    return "Миссия Колонизация Марса"


@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    phrases = ["Человечество вырастает из детства.",

               "Человечеству мала одна планета.",

               "Мы сделаем обитаемыми безжизненные пока планеты.",

               "И начнем с Марса!",

               "Присоединяйся!", ]
    return "<br>".join(phrases)


@app.route("/image_mars")
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='images/mars.jpg')}">
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


@app.route("/promotion_image")
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='images/mars.jpg')}">
                    <div class="alert alert-secondary">Человечество вырастает из детства.</div>
                    <div class="alert alert-success">"Человечеству мала одна планета."</div>
                    <div class="alert alert-secondary">Мы сделаем обитаемыми безжизненные пока планеты.</div>
                    <div class="alert alert-warning">И начнем с Марса!</div>
                    <div class="alert alert-danger">Присоединяйся!</div>
                  </body>
                </html>"""


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        professions = ["инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач",
                       "инженер по терраформированию", "климатолог", "специалист по радиационной защите", "астрогеолог",
                       "гляциолог", "инженер жизнеобеспечения", "метеоролог", "оператор марсохода", "киберинженер",
                       "штурман", "пилот дронов"]
        checkbox = lambda i, x: f"""<div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="p{i}" name="accept{i}">
                                        <label class="form-check-label" for="p{i}">{x.capitalize()}</label>
                                    </div>"""
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h3>на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="name" class="form-control" placeholder="Введите имя" name="name">
                                    <input type="surname" class="form-control" placeholder="Введите фамилию" name="surname">
                                    <br>
                                    <input type="email" class="form-control" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="form-group form-check">Какие у Вас есть профессии</label>
                                        {" ".join([checkbox(j, i) for j, i in enumerate(professions)])}
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <br>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
