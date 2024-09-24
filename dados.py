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


def load_transpose_data(link, ano, quantidade):
    base = pd.read_csv(link, sep=';', encoding = 'utf8')
    base = base.melt(id_vars=['id', 'control', 'produto'], var_name='ano', value_name='quantidade')
    base['ano'] = base['ano'].astype(int)
    if ano is not None:
      base.query(f'ano == {ano}', inplace=True)
    if quantidade is not None:
      base.query(f'quantidade > {quantidade}', inplace=True)
    base = json.loads(base.to_json(orient='records'))
    #base = json.dumps(base, ensure_ascii=, indent=4)   
    return base



#for elemento in load_transpose_data(link):
#    print(elemento)