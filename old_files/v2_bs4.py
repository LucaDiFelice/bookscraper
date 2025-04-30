from bs4 import BeautifulSoup
import lxml
import requests

url = []
page = []
soup = []
i = 0
#url = "https://www.baseball-reference.com/players/a/"
#age = requests.get(url)
#soup = BeautifulSoup(page.text, "lxml")
#print(page)
#print(soup)

for letter in range(97, 123, 1):
    url.append("https://www.baseball-reference.com/players/" + chr(letter))
    page.append(requests.get(url[i]))
    soup.append(BeautifulSoup(page[i].text, features="html.parser"))
    i += 1


def find_player(player_name):
    all_names = []
    names = soup.find("div", class_="section_content", id="div_players_")
    for name in names.find_all("a"):
        all_names.append(name.text)
    if player_name in all_names:
        print("yes")
    else:
        print("no")
        
find_player("Beriiit Adams")


