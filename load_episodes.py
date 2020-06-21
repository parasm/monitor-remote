import requests
import os
from bs4 import BeautifulSoup
from typing import NamedTuple
import pickle

URLS = ["https://www1.couchtuner.page/series/what-we-do-in-the-shadows/"]

def load_episodes(URL):
    r = requests.get(URL)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    all_seasons_html = soup.find_all(class_="tvseason")
    episodes = []
    for season_html in all_seasons_html:
        all_links = season_html.find_all("a")
        episodes.append([str(link.get("href")) for link in all_links])
    series_name = str(soup.find(class_="breadcrumb").find(class_="active").string)
    num_seasons = len(episodes)
    print(series_name)
    #print(series_data)
    series_data = {"name": series_name, "num_seasons": num_seasons, "episodes": episodes}
    print(episodes)
    print("paras")
    series_name = series_name.replace(' ','_').replace(':','_')
    file_name = f"C:\\Users\\paras\Desktop\\ameliorate\\tv\\series_data\\{series_name.lower()}.txt"
    print(file_name)
    with open(file_name, "wb") as save_file:
        save_file.write(pickle.dumps(series_data))
        pickle.dump(series_data, save_file)
        #print()
for SERIES_URL in URLS:
    load_episodes(SERIES_URL)