#imbd puanı en yüksek 250 filmi listeleme
from bs4 import BeautifulSoup
import requests
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, "html.parser")
list = soup.find("tbody", {"class":"lister-list"}).find_all("tr")

for tr in list:
    title = tr.find("td", {"class":"titleColumn"}).find("a").text
    rating = tr.find("td", {"class": "ratingColumn imdbRating"}).find("strong").text
    print(title, rating)
