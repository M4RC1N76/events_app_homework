from os import name
from flask import render_template, request
from app import app
from models.agenda import agenda, add_new_event
from models.event import Event


@app.route('/')
def index():
    return render_template('index.html', title='Home', agenda=agenda)

@app.route('/', methods=['POST'])
def add_event():
    print(request.form)
    new_event = Event(
        request.form['date'],
        request.form['name'],
        request.form['guest'],
        request.form['location'],
        request.form['description']
    )
    add_new_event(new_event)
    return render_template('index.html', title="Home", agenda=agenda)


