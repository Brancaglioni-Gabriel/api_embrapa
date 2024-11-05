#baixando bibliotecas, a biblioteca dados é referente as funções que a api chama 
from flask import Flask, make_response, jsonify, Response, render_template, request
import requests
from bs4 import BeautifulSoup
import dados
import json


#iniciando o app
app = Flask(__name__)


#primeira rota que contem a documentação
@app.route('/')
def document():
    return render_template('index.html')


#rota da pagina de Produção, retorna dados ou passa a opções de variaveis que é possivel usar como parametros
@app.route('/production', methods=['GET'])
def production():
    site = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'
    link = dados.get_link(site)
    id = request.args.get('id', default=None)
    ano = request.args.get('ano', default=None)
    quantidade = request.args.get('quantidade', default=None)
    resultado = dados.load_transpose_data(link, ';', id, ano, quantidade)
    resultado = json.dumps(resultado, ensure_ascii=False, indent=4)
    return resultado


# rota da pagina de processamento, pagina tem sub-opções por isso o ifs
@app.route('/process/<option>', methods=['GET'])
def process(option):
    sep = '\t'
    if option == 'viniferas':
        site = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03'
        sep = ';'
    elif option == 'americanas':
        site = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_03'
    elif option == 'mesa':
        site = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_03'
    elif option == 'semclass':
        site = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_03'
    else:
        return 'Opção invalida, favor consultar a documentação!'
    link = dados.get_link(site)
    id = request.args.get('id', default=None)
    ano = request.args.get('ano', default=None)
    quantidade = request.args.get('quantidade', default=None)
    resultado = dados.load_transpose_data(link, sep, id, ano, quantidade)
    resultado = json.dumps(resultado, ensure_ascii=False, indent=4)
    return resultado


#rota de comercialização, passa dados ou lista de id e anos dos dados
@app.route('/comercial', methods=['GET'])
def comercial():
    site = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04'
    link = dados.get_link(site)
    id = request.args.get('id', default=None)
    ano = request.args.get('ano', default=None)
    quantidade = request.args.get('quantidade', default=None)
    resultado = dados.load_transpose_data(link, ';', id, ano, quantidade)
    resultado = json.dumps(resultado, ensure_ascii=False, indent=4)
    return resultado


#rota da pagina de importação, essa pagina chama uma função diferente das outras paginas porque tem 2 colunas com valores
@app.route('/import/<option>', methods=['GET'])
def importation(option):
    if option == 'mesa':
        site = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05'
    elif option == 'espumante':
        site = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_05'
    elif option == 'fresca':
        site = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_05'
    elif option == 'passas':
        site = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_05'
    elif option == 'suco':
        site = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_05&opcao=opt_05'
    else:
        return 'Opção invalida, favor consultar a documentação!'
    link = dados.get_link(site)
    id = request.args.get('id', default=None)
    ano = request.args.get('ano', default=None)
    quilos = request.args.get('quilos', default=None)
    valor = request.args.get('valor', default=None)
    resultado = dados.load_transpose_data_double(link, ';', id, ano, quilos, valor)
    resultado = json.dumps(resultado, ensure_ascii=False, indent=4)
    return resultado


#rota da pagina de exportação, essa pagina chama uma função diferente das outras paginas porque tem 2 colunas com valores
@app.route('/export/<option>', methods=['GET'])
def export(option):
    if option == 'mesa':
        site = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_06'
    elif option == 'espumante':
        site = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_02&opcao=opt_06'
    elif option == 'fresca':
        site = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_03&opcao=opt_06'
    elif option == 'suco':
        site = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_04&opcao=opt_06'
    else:
        return 'Opção invalida, favor consultar a documentação!'
    link = dados.get_link(site)
    id = request.args.get('id', default=None)
    ano = request.args.get('ano', default=None)
    quilos = request.args.get('quilos', default=None)
    valor = request.args.get('valor', default=None)
    resultado = dados.load_transpose_data_double(link, ';', id, ano, quilos, valor)
    resultado = json.dumps(resultado, ensure_ascii=False, indent=4)
    return resultado


app.run(port=10000, host='0.0.0.0', debug=False)
