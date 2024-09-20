import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


def single_page():
    site = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'
    try:
        conectar = requests.get(site)
        conteudo = conectar.content
        soup = BeautifulSoup(conteudo, 'html.parser')
        caminho = soup.find('a', class_="footer_content").get('href')
        if caminho[0:4] != 'http':
            link = 'http://vitibrasil.cnpuv.embrapa.br/' + caminho
        else:
            link = caminho
        return link
    except ValueError:
        print('Erro pagina invalida')


def load_transpose_data(link):
    base = pd.read_csv(link, sep=';', encoding = 'utf8')
    base = base.melt(id_vars=['id', 'control', 'produto'], var_name='ano', value_name='quantidade')
    base_json = json.loads(base.to_json(orient='records', force_ascii=False))
    return base_json