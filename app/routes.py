from app import app
from flask import render_template, request, jsonify
import requests
import os

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/add_message', methods=['POST'])
def add_message():
    message = request.form['message']
    return render_template('message.html', message=message)


@app.route("/forward", methods=['POST'])
def forward():
    message = request.form['message']

    os.environ['HTTPS_PROXY'] = 'https://USbCNuvYx9zAXGEK6o5nFVUE:e46973c6-e6aa-4a40-acf4-39ea148e7be0@tntfavjljdc.SANDBOX.verygoodproxy.com:8080'
    res = requests.post('https://echo.apps.verygood.systems/post',
                        json={'message': message},
                        verify='/Users/maryburak/dev/vsg_task/app/cert.pem')

    res = res.json()
    return render_template('forward.html', response=res)
