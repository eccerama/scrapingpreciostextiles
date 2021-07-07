import requests
import pandas as pd
from bs4 import BeautifulSoup

url='https://jackiesmith.com.ar/collections/the-dear-family'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup)

producto = soup.find_all('div', class_='grid-product__title grid-product__title--body')
precio = soup.find_all('span', class_='mw-price')
#precio2 = precio.strip()

listaProducto= []
listaPrecio=[]

for x in producto:
    listaProducto.append(x.text)
    
for y in precio:
    listaPrecio.append((y.text)),

    
precatalogo = {'producto':listaProducto, 'precio':listaPrecio}

catalogo=pd.DataFrame(precatalogo)

catalogo.to_csv('catalogo_JackieSmith.csv',index=False)
catalogo
