from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = "https://www.scrapethissite.com/pages/simple/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# Países
result = soup.find_all('h3', class_="country-name")

paises = list()

for i in result:
	paises.append(i.text.replace('\n', ' ').replace('\r', '').strip())

# Capital
result = soup.find_all('span', class_="country-capital")

capitales = list()

for i in result:
	capitales.append(i.text)

# Población
result = soup.find_all('span', class_="country-population")

poblacion = list()

for i in result:
	poblacion.append(i.text)

# area
result = soup.find_all('span', class_="country-area")

area = list()

for i in result:
	area.append(i.text)

# Generación DataFrame
df = pd.DataFrame({'País': paises, 'Capital': capitales, 'Población': poblacion, 'Área (km2)': area})

df.to_csv('scraping_paises.csv', index = False, encoding = 'utf-8-sig')