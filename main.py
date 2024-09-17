from flask import Flask, make_response, jsonify
from teste import Dados

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!!!'


@app.route('/inicio', methods=['GET'])
def teste():
    return make_response(
        jsonify(
            Dados
        )
    ) 

app.run(port=10000, host='0.0.0.0')
