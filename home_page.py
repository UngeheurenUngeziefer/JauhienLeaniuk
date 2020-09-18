from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def home_page(name=None):
	return render_template('home_page.html', name=name)

@app.route('/my_projects')
def hello_world():
    return 'Here projects!'

with app.test_request_context():
    url_for('home_page')
    url_for('hello_world')
    url_for('static', filename='style.css')
    url_for('static', filename='menu.js')
