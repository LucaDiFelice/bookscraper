from bs4 import BeautifulSoup
import requests

#url = []
#page = []
#soup = []
i = 0
url = "https://www.baseball-reference.com/players/a/"
page = requests.get(url)
soup = BeautifulSoup(page.text, features="html.parser")
print(soup)

#for letter in range(97, 123, 1):
    #url.append("https://www.baseball-reference.com/players/" + chr(letter))
    #page.append(requests.get(url[i]))
    #soup.append(BeautifulSoup(page[i].text, features="html.parser"))
    #i += 1

names = soup.find("div", class_="section_content", id="div_players_")
print(names)


