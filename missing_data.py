

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd


#now you have to install selenium at first and I am using chrome browser to 
#scrape data using selenium. first you need to specify the path of chromedriver
#which is in my case in download folder
path = #'C:/Users/tanay/Downloads/chromedriver' this is my path in windows
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
#driver.get(web) it will open your browser
#driver.quit() will close your browser
def get_misssing_data(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'

    driver.get(web)
    matches = driver.find_elements(by='xpath', value='//td[@align="right"]/.. | //td[@style="text-align:right;"]/..')#inspect data from website using dev tool
    # matches = driver.find_elements(by='xpath', value='//tr[@style="font-size:90%"]')

    home = []
    score = []
    away = []

    for match in matches:
        home.append(match.find_element(by='xpath', value='./td[1]').text)
        score.append(match.find_element(by='xpath', value='./td[2]').text)
        away.append(match.find_element(by='xpath', value='./td[3]').text)

    dict_football = {'home': home, 'score': score, 'away': away}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year
    time.sleep(2)
    return df_football


years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]
#ignoring data from 2022 which is ongoing
fifa = [get_misssing_data(year) for year in years]
driver.quit()
df_fifa = pd.concat(fifa, ignore_index=True)
df_fifa.to_csv("fifa_worldcup_missing_data.csv", index=False)
