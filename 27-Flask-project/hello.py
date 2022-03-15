from flask import Flask
from flask import request
from logging.config import dictConfig
from flask import abort

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'ERROR',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

persons = [] 


@app.route('/piotr')
def piotr():
    return 'Pozdrowienia dla Piotra, World!'


@app.route('/')
def hello_all():
    app.logger.info("info")
    app.logger.error("error")
    app.logger.debug("debug")
    all = ''
    for p  in persons:
        all = all + ','+ p
    return 'Hello, '+all   

@app.route('/person/<name>' , methods=['POST'])
def add_person(name):
    persons.append(name)
    app.logger.info("Processing request /person/ "+ name + " Header imie: "+request.headers['imie'])
    return 'OK'   

@app.route('/person/<name>' , methods=['DELETE'])
def remove_person(name):
    persons.remove(name)
    app.logger.info("Processing request /person/"+ name + " Header imie: "+request.headers['imie'])
    return 'OK'   

@app.route('/error' , methods=['GET'])
def error():
    abort(401)   