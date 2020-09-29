from flask import Flask, url_for, render_template, request
from flask_babel import Babel, gettext, format_date
from babel import numbers, dates
from datetime import date, datetime, time

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
# app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)

@babel.localeselector
def get_locale():
    return 'be'
    #return request.accept_languages.best_match(['en', 'be', 'ru'])

@app.route('/')
def home(name=None):

    jauhien = gettext('Jaŭhien')

    sep_10 = date(2007, 9, 10)
    multilang_date = format_date(sep_10)

    format_dates = {'date': multilang_date}

    return render_template('home.html', name=home, format_dates=format_dates, jauhien=jauhien)

@app.route('/coding')
def coding():
    return render_template('coding.html', name=coding)

@app.route('/maps')
def maps():
    return render_template('maps.html', name=maps)

@app.route('/running')
def running():
    return render_template('running.html', name=running)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html', name=contacts)


with app.test_request_context():
    url_for('home')
    url_for('coding')
    url_for('maps')
    url_for('running')
    url_for('contacts')
    url_for('static', filename='home.css')

if __name__ == '__main__':
    app.run(debug=True)