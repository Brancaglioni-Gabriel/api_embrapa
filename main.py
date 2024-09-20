from flask import Flask, make_response, jsonify
from teste import Dados
import requests
from bs4 import BeautifulSoup
import dados


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!!!'


@app.route('/<tipo>', methods=['GET'])
def teste(tipo):
    if tipo != 'todos':
        return make_response(
            jsonify(
                Dados
            )
        )
    else:
        return 'Parametro invalido favor consultar a documentação' 


@app.route('/<tipo>/<sub_pagina>', methods=['GET'])
def teste_sub(tipo, sub_pagina):
    if tipo != 'todos' and sub_pagina != 'teste':
        return make_response(
            jsonify(
                Dados
            )
        )
    else:
        return 'Parametro invalido favor consultar a documentação' 


@app.route('/pagina1', methods=['GET'])
def valores():
    link = dados.single_page()
    resultado = dados.load_transpose_data(link)
    return make_response(
                resultado
        )


app.run(port=10000, host='0.0.0.0')
