import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import date

url = 'https://www.pciconcursos.com.br/concursos/'
extracted_links = []
today = date.today().strftime('%Y%m%d')
data=[]
filename = 'links_' + today + '.csv'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
getlinks = soup.find_all('a')
for link in getlinks:
    if('https://www.pciconcursos.com.br/noticias/' in link.get('href', [])):
        response = requests.get(link.get('href'))
        extracted_links.append(link['href'])
        data.append({'link': link['href'], 'date': today})
        if len(extracted_links) %10 == 0:
            print(f"{len(extracted_links)} and collecting")

df = pd.DataFrame(data)
df.to_csv(filename, index=False)




