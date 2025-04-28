from bs4 import BeautifulSoup
import requests

url = "https://www.mlb.com/stats/"
page = requests.get(url)
soup = BeautifulSoup(page.text, features="html.parser")

players = "https://www.mlb.com/players"
player_page = requests.get(players)
player_soup = BeautifulSoup(player_page.text, features="html.parser")

def verify_player():
    player_data = player_soup.find("div", class_="section_wrapper", id="all_players_")
    print(player_data)

def top_player(stat_type):
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
    for player in all_players:
        player_name = player.find("a", class_="bui-link")
        player_stat = player.find('td', {'data-col': stat_column[stat_type]})
        print(player_name["aria-label"])
        print(player_stat.text)
        print("")

#top_player("HR")
verify_player()