from flask import Flask, make_response, jsonify, Response, render_template, request
from teste import Dados
import requests
from bs4 import BeautifulSoup
import dados
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/{tipo}', methods=['GET'])
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
    ano = request.args.get('ano', default=None)
    quantidade = request.args.get('quantidade', default=None)
    link = dados.single_page()
    resultado = dados.load_transpose_data(link, ano, quantidade)
    print(type(resultado))
    resultado = json.dumps(resultado, ensure_ascii=False)
    print(type(resultado))
    return resultado

app.run(port=10000, host='0.0.0.0', debug=True)
