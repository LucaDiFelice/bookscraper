from bs4 import BeautifulSoup
import requests

url = "https://www.mlb.com/stats/"
page = requests.get(url)
soup = BeautifulSoup(page.text, features="html.parser")

def top_player():
    stat_column = {
        "team": 1, 
        "G": 2, 
        "AB": 3, 
        "R": 4, 
        "H": 5, 
        "2B": 6,
        "3B": 7,
        "HR": 8,
        "RBI": 9,
        "BB": 10,
        "SO": 11,
        "SB": 12,
        "CS": 13,
        "AVG": 14,
        "OBP": 15,
        "SLG": 16,
        "OPS": 17,
    }
    all_players = soup.find("tbody", class_="notranslate")
    print(all_players.text)
    for player in all_players:
        player_name = player.find("a", class_="bui-link")
        player_stat = player.find('td', {'data-col': '2'})
        print(player_name["aria-label"])
        print(player_stat.text)
        print("")

top_player()

"""
players = soup.find("th", scope="row")
player = players.find("a", class_="bui-link")
"""