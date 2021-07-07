import requests
import pandas as pd
from bs4 import BeautifulSoup

url='https://www.carocuore.com/caro-cuore/pijamas/pijamas.html'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup)

producto = soup.find_all('h3', class_='nombre')
precio = soup.find_all('span', class_='price')
#precio2 = precio.strip()

listaProducto= []
listaPrecio=[]

for x in producto:
    listaProducto.append(x.text)
    
for y in precio:
    listaPrecio.append((y.text)),

    
precatalogo = {'producto':listaProducto, 'precio':listaPrecio}

#catalogo=pd.DataFrame(precatalogo)

#catalogo.to_csv('catalogo_Pijamas_CaroCuore.csv',index=False)
precatalogo
