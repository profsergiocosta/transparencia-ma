import requests
from bs4 import BeautifulSoup as BS

url = "http://www.transparencia.ma.gov.br/app/despesas/por-funcao/2019#lista"
page_response = requests.get(url)
page = BS(page_response.text, 'lxml')
table = page.find ('table')
print (table)
