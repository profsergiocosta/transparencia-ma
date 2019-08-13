import requests
from bs4 import BeautifulSoup as BS

def despesas_por_funcao (cod, ano):
    url = "http://www.transparencia.ma.gov.br/app/despesas/por-funcao/"+ano+"/funcao/"+cod+"?#lista"
    return extrai_despesas (url)

def despesas_total (ano):
    url = "http://www.transparencia.ma.gov.br/app/despesas/por-funcao/"+ano+"#lista"
    return extrai_despesas (url)

def extrai_despesas (url):
    response = requests.get(url)
    page = BS(response.text, 'lxml')
    table = page.find ('table')
    rows = table.find_all('tr')
    despesas = []
    for row in rows[1:]:
        cols =row.find_all("td")
        despesa = {}
        despesa["codigo"]  = cols[0].get_text().strip()
        despesa["nome"] = cols[1].find("a").get_text().strip()
        despesa["url_detalhe"] = cols[1].find("a").get('href')
        despesa["empenhado"] =  float (cols[2].get_text().strip().replace (".","").replace (",","."))
        despesa["liquidado"] =  float (cols[3].get_text().strip().replace (".","").replace (",","."))
        despesa["pago"] =  float (cols[4].get_text().strip().replace (".","").replace (",","."))
        despesas.append(despesa)

    return despesas