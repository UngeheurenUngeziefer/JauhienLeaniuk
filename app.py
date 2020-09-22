from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def home(name=None):
	return render_template('home.html', name=home)

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
