import requests
from bs4 import BeautifulSoup
import pandas as pd


# function to scrape hot 100 data of wikipedia.
def get_year_end_songs(year):
    """Returns list of dicts containing song title, artist and chart number for all songs of given year"""

    url = 'https://en.m.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_' + str(year)
    r = requests.get(url)
    bs = BeautifulSoup(r.text, 'lxml')
    rows = bs.find('table').find_all('tr')
    songs = []
    for row in rows[1:]:
        cols = row.find_all(['td', 'th'])
        cols = [t.text.strip().strip('"') for t in cols]
        song = {}
        try:
            song['number'] = cols[0]
        except:
            song['number'] = None
        try:
            song['title'] = cols[1]
        except:
            song['title'] = None

        try:
            song['artist'] = cols[2]
        except:
            song['artist'] = None

        song['year'] = year
        songs.append(song)
    return (songs)

all_songs = []
for year in range(1965, 2021):
    all_songs.extend(get_year_end_songs(year))

df = pd.DataFrame(all_songs)

print(df[df.number=='Tie'])

df = df.drop(500)

df = df.reindex()

df.number = df.number.astype(int)

df.to_csv('billboard-year-end-wiki.csv')

# removes every songs above number 40
df = df[df.number < 41]

df.to_csv('billboard-year-end-wiki.csv')

#adapted from https://alexforrest.github.io/scraping-billboard-top-100-on-wikipedia.html



