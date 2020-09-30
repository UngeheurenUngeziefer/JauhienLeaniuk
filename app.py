from flask import Flask, url_for, render_template, request, session, redirect
from flask_babel import Babel, gettext, format_date
from babel import numbers, dates
from datetime import date, datetime, time

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['LANGUAGES'] =  {
    'en': 'EN',
    'be': 'BE',
    'ru': 'RU',
}

app.secret_key = "super secret key"
# app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)

@app.route('/language=<language>')
def set_language(language=None):
    session['language'] = language
    return redirect(request.referrer)
    # return redirect(url_for('home'))

@app.context_processor
def inject_conf_var():
    return dict(CURRENT_LANGUAGE=session.get('language'))

@babel.localeselector
def get_locale():
    try:
        language = session['language']
    except KeyError:
        language = None
    if language is not None:
        return language
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())

# @babel.localeselector
# def get_locale():
#     return 'ru'
#     #return request.accept_languages.best_match(['en', 'be', 'ru'])

@app.route('/')
def home(name=None):
    return render_template('home.html', name=home)

@app.route('/coding')
def coding():

    september_30_2020 = date(2020, 9, 30)
    sep_30_2020 = format_date(september_30_2020)

    september_15_2020 = date(2020, 9, 15)
    sep_15_2020 = format_date(september_15_2020)

    july_29_2020 = date(2020, 7, 29)
    jul_29_2020 = format_date(july_29_2020)

    july_12_2020 = date(2020, 7, 12)
    jul_12_2020 = format_date(july_12_2020)

    july_5_2020 = date(2020, 7, 5)
    jul_5_2020 = format_date(july_5_2020)

    july_3_2020 = date(2020, 7, 3)
    jul_3_2020 = format_date(july_3_2020)

    june_24_2020 = date(2020, 6, 24)
    jun_24_2020 = format_date(june_24_2020)

    june_23_2020 = date(2020, 6, 23)
    jun_23_2020 = format_date(june_23_2020)

    june_18_2020 = date(2020, 6, 18)
    jun_18_2020 = format_date(june_18_2020)

    traven_29_2020 = date(2020, 5, 29)
    may_29_2020 = format_date(traven_29_2020)

    traven_3_2020 = date(2020, 5, 3)
    may_3_2020 = format_date(traven_3_2020)

    january_11_2020 = date(2020, 1, 11)
    jan_11_2020 = format_date(january_11_2020)

    december_10_2019 = date(2019, 12, 10)
    dec_10_2019 = format_date(december_10_2019)

    november_17_2019 = date(2019, 11, 17)
    nov_17_2019 = format_date(november_17_2019)

    format_dates = {'sep_30_2020': sep_30_2020, 
    'sep_15_2020': sep_15_2020, 'jul_12_2020': jul_12_2020,
    'jul_29_2020': jul_29_2020, 'jul_5_2020': jul_5_2020, 
    'jul_3_2020': jul_3_2020, 'jun_24_2020': jun_24_2020,
    'jun_23_2020': jun_23_2020, 'jun_18_2020': jun_18_2020,
    'may_29_2020': may_29_2020, 'may_3_2020': may_3_2020,
    'jan_11_2020': jan_11_2020, 'dec_10_2019': dec_10_2019,
    'nov_17_2019': nov_17_2019}

    return render_template('coding.html', name=coding, 
        format_dates=format_dates)

@app.route('/maps')
def maps():
    return render_template('maps.html', name=maps)

@app.route('/running')
def running():

    september_30_2020 = date(2020, 9, 25)
    sep_30_2020 = format_date(september_30_2020)
    september_30_2019 = date(2019, 9, 25)
    sep_30_2019 = format_date(september_30_2019)

    format_dates = {'sep_30_2020': sep_30_2020, 'sep_30_2019': sep_30_2019}

    return render_template('running.html', name=running, 
        format_dates=format_dates)

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
