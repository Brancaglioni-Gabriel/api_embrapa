import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


def get_link(site):
    conectar = requests.get(site)
    conteudo = conectar.content
    soup = BeautifulSoup(conteudo, 'html.parser')
    caminho = soup.find('a', class_="footer_content").get('href')
    if caminho[0:4] != 'http':
        link = 'http://vitibrasil.cnpuv.embrapa.br/' + caminho
    else:
        link = caminho
    return link


def load_transpose_data(link, sep, id, ano, quantidade):
    base = pd.read_csv(link, sep=sep, encoding = 'utf8')
    names = base.columns
    vars = []
    for n in names:
        if n.isnumeric() == False:
            vars.append(n)
    base = base.melt(id_vars=vars, var_name='ano', value_name='quantidade')
    base['ano'] = base['ano'].astype(int)
    if id is not None:
      base.query(f'id == {id}', inplace=True)
    if ano is not None:
      base.query(f'ano == {ano}', inplace=True)
    if quantidade is not None:
      base.query(f'quantidade > {quantidade}', inplace=True)
    base = json.loads(base.to_json(orient='records')) 
    return base


def load_transpose_data_double(link, sep, id, ano, quilos, valor):
    base = pd.read_csv(link, sep=sep, encoding = 'utf8')
    base.rename(columns={'Id':'id', 'País':'pais'}, inplace=True)
    principal = ['id','pais']
    colunas = []
    for n in base.columns:
        if n.isnumeric() == True:
            colunas.append(n)
    colunas_kg = principal + colunas
    base_kg = base[colunas_kg].melt(id_vars=principal, var_name='ano', value_name='quilos')
    base_valor = base.drop(colunas, axis=1)
    base_valor.columns = base_valor.columns.str.replace('.1', '')
    base_valor = base_valor.melt(id_vars=principal, var_name='ano', value_name='valor')
    base = base_kg.merge(base_valor)
    base['ano'] = base['ano'].astype(int)
    if id is not None:
      base.query(f'id == {id}', inplace=True)
    if ano is not None:
      base.query(f'ano == {ano}', inplace=True)
    if quilos is not None:
      base.query(f'quilos > {quilos}', inplace=True)
    if valor is not None:
      base.query(f'valor > {valor}', inplace=True)
    base = json.loads(base.to_json(orient='records')) 
    return base
