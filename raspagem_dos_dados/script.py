import pandas
import requests
from bs4 import BeautifulSoup
import re 
import os


url = ("https://dadosabertos.bcb.gov.br/dataset/dolar-americano-usd-todos-os-boletins-diarios")

res = requests.get(url)

html_page = res.text

#print(html_page)

soup = BeautifulSoup(html_page, 'html.parser')
soup.prettify()
for link in soup.find_all('div', class_='notes embedded-content'):
    texto = (link.text)
    print(texto)
    
with open('texto.txt', 'w', encoding='utf-8') as file:
    for paragraph in texto:
        file.write(paragraph)
    
    
        
        


