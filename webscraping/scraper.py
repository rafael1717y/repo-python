from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')
soup = BeautifulSoup(html.read(), 'html.parser')
#print(soup.prettify())
#print(soup.title)
#print(soup.div)

### só as classes com feature.
#divs = soup.find_all('div', {'class':'featured'})
#print(divs)

# Achar um div com a classe featured e o filho (h2)
#featured_header = soup.find('div', {'class':'featured'}).h2
#get_text retira o texto
#print(featured_header.get_text())

#for button in soup.find(attrs={'class': 'button button--primary'}):
#for button in soup.find(class_='button button--primary'):
#    print(button)

for link in soup.find_all('a'):
    print(link.get('href'))














