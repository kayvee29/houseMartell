from flask import Flask, jsonify, request, render_template
import json
from textblob import TextBlob
from classes import calculation

app = Flask(__name__)

@app.route("/", methods=['GET'])

def homepage(name=None):
    return render_template('home.html')

@app.route("/signup", methods=['GET'])

def signup(name=None):
    return render_template('signup.html')

@app.route("/translate", methods=['GET'])

def translate(name=None):
    return render_template('translate.html')

@app.route("/calculation", methods=['POST'])
def get_tasks():
    print(type(request.json))
    if request.json['method'] == 'addition':
        return "result: {}".format(str(calculation.calc.add(request.json['a'],request.json['b'])))
    elif request.json['method'] == 'subtraction':
        return "result: {}".format(str(calculation.calc.sub(request.json['a'],request.json['b'])))
    elif request.json['method'] == 'multiply':
        return "result: {}".format(str(calculation.calc.mul(request.json['a'],request.json['b'])))
    elif request.json['method'] == 'division' and request.json['b'] != 0:
        return "result: {}".format(str(calculation.calc.div(request.json['a'],request.json['b'])))
    elif request.json['method'] not in methods:
        return "Calculation method is wrong"
    elif request.json['b']:
        return "B Cannot be zero"

@app.route("/sentiment", methods=['POST'])
def sentiment():
    # w = Word(request.json['word'])
    blob = TextBlob(request.json['sentence'])
    # print(str(blob.sentiment))
    return str(blob.sentiment)

@app.route("/language", methods=['POST'])
def language():
    # w = Word(request.json['word'])
    blob = TextBlob(request.json['sentence'])
    # print(str(blob.sentiment))
    return str(blob.translate(from_lang=request.json['fromlang'], to =request.json['tolang']))

@app.route("/langui/", methods=['POST'])
def langui():
    # w = Word(request.json['word'])
    blob = TextBlob(request.form.get('sent'))
    # blob = TextBlob(request.form['sentence'])
    return str(blob.translate(from_lang='en', to=request.form.get('lang')))
    # print(str(blob.sentiment))
    # return str(blob.translate(from_lang='en', to =request.form['language']))

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0')
