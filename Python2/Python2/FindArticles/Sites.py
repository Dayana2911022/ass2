import requests
from bs4 import BeautifulSoup
class findsites():
    def findArticle(self, crypto):
        url = "https://www.google.com/search?q=site%3Acoinmarketcap.com+alexandria+" + crypto
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        listOfLinks = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if "https://coinmarketcap.com/" in href:
                realLink = "https://www.google.com"+href
                listOfLinks.append(realLink)
        return listOfLinks