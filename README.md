# api_embrapa
 API feita para o primeiro modulo da pós tech da FIAP, e está temporariamente hospedada no render.

 A API puxa dados do site da "http://vitibrasil.cnpuv.embrapa.br/" onde temos informações sobre a quantidade de uvas processadas, produção e comercialização de vinhos, suco e derivados provenientes do Rio Grande do Sul

 Para utilização da API favor consultar a pagina https://api-embrapa.onrender.com/ que é o arquivo .html que consta na pasta templates, essa documentação foi feita no Google Colab baixado o arquivo 'ipynb' e convertido em HTML pelo comando abaixo também no Google Colab
 
 !jupyter nbconvert --execute --to html "file_name.ipynb"

 Sobre a API temos dois arquivos .py o 'main' onde temos as rotas das apis e quais funções são chamadas em cada rota e o arquivos 'dados' onde temos as funções que fazem a extração e a transformação desses dados.

 Observando a estrutura do site da embrapa, optou-se por não fazer a leitura dos dados no html da pagina, mas a leitura via html do link de download desses dados.

 Para extração e transformação dos dados utilizamos a biblioteca requests que capta os dados, depois a BeautifulSoup que lê o html e fornece o link de download dos dados, pandas para transformar os dados em um dataframe e fazer filtros nos dados de acordo com os parametros passados na url posteriormente, após isso utilizamos a json para formatar os dados visando facilitar a iteração dos dados por quem for consumir a API. (toda esse codigo se encontra no arquivos dados.py)

 A API foi montada utilizando Flask e é basicamente a definição da rota, checagem dos parametros passados e atravês de condições chama as determinadas funções para retornarem os dados. (esse codigo se encontra no arquivo main.py)
