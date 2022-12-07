# -*- coding: utf-8 -*-
"""

@author: tanay



pip install bs4
pip install lxml
pip install requests
pip install pandas
"""
import pandas as pd
from bs4 import BeautifulSoup
import requests

#For Data from a single Fifa
"""
web = 'https://en.wikipedia.org/wiki/2014_FIFA_World_Cup'
response = requests.get(web)
content = response.text
soup = BeautifulSoup(content, 'lxml')
matches = soup.find_all('div', class_='footballbox')
home = []
score = []
away = []
for match in matches:
    home.append(match.find('th', class_='fhome').get_text())
    score.append(match.find('th', class_='fscore').get_text())
    away.append(match.find('th', class_='faway').get_text())
dict_football = {'home': home, 'score': score, 'away': away}
df_football = pd.DataFrame(dict_football)
df_football['year'] =2014
df_football.to_csv("fifa_worldcup_historical_data.csv", index=False)
"""
#For fetching record from 1930 to 2018
def get_matches(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    response = requests.get(web)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    matches = soup.find_all('div', class_='footballbox')
    home = []
    score = []
    away = []
    for match in matches:
        home.append(match.find('th', class_='fhome').get_text())
        score.append(match.find('th', class_='fscore').get_text())
        away.append(match.find('th', class_='faway').get_text())
    dict_football = {'home': home, 'score': score, 'away': away}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] =year
    return df_football
years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]

fifa = [get_matches(year) for year in years]

df_fifa = pd.concat(fifa, ignore_index=True)


df_fifa.to_csv("fifa_worldcup_historical_data.csv", index=False)

# fixture
df_fixture = get_matches(2022)
df_fixture.to_csv('fifa_worldcup_fixture.csv', index=False)