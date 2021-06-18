import pandas as pd
import musicbrainzngs as mb

#get genres from musicbrainz
#read more https://musicbrainz.org/doc/MusicBrainz_API

mb.auth('your username', 'your password')
mb.set_useragent("Your use for the apie", "1.0", "your email")
mb.set_rate_limit(limit_or_interval= 2,new_requests= 1)

# import dataset
df = pd.read_csv("WithID-Data.csv")

def get_tags(id):
    try:
        tags = mb.get_artist_by_id(id, includes=["tags"])['artist']["tag-list"]
        return [tag['name'] for tag in tags]
    except:
        pass

df["tags"] = df.apply(lambda row: get_tags(row['test']), axis=1)


rocklist = ["symphonic rock", "jazz-rock", "heartland rock", "rap rock", "garage rock", "folk-rock", "roots rock", "adult alternative pop rock", "rock roll", "punk rock", "arena rock", "pop-rock", "glam rock", "southern rock", "indie rock", "funk rock", "country rock", "piano rock", "art rock", "rockabilly", "acoustic rock", "progressive rock", "folk rock", "psychedelic rock", "rock & roll", "blues rock", "alternative rock", "rock and roll", "soft rock", "rock and indie", "hard rock", "pop/rock", "pop rock", "rock", "classic pop and rock", "psychedelic", "british psychedelia", "punk", "metal", "heavy metal"]
altlist = ["adult alternative pop rock", "alternative rock", "alternative metal", "alternative", "lo-fi indie", "indie", "indie folk", "indietronica", "indie pop", "indie rock", "rock and indie"]
electlist = ["dance and electronica", "electro house", "electronic", "electropop", "progressive house", "hip house", "house", "eurodance", "dancehall", "dance"]
soullist = ["psychedelic soul", "deep soul", "neo-soul", "neo soul", "southern soul", "smooth soul", "blue-eyed soul", "soul"]
classlist = ["classical", "orchestral", "film soundtrack", "composer"]
poplist = ["country-pop", "latin pop", "classical pop", "pop-metal", "orchestral pop", "instrumental pop", "indie pop", "sophisti-pop", "pop punk", "pop reggae", "britpop", "traditional pop", "power pop", "sunshine pop", "baroque pop", "synthpop", "art pop", "teen pop", "psychedelic pop", "folk pop", "country pop", "pop rap", "pop soul", "pop and chart", "dance-pop", "pop", "top 40"]
hiphoplist= ["conscious hip hop", "trap", "east coast hip hop", "hardcore hip hop", "west coast hip hop", "hiphop", "southern hip hop", "hip-hop", "hip hop", "gangsta rap", "rapper", "rap"]
discolist = ["disco"]
swinglist = ["swing"]
folklist = ["contemporary folk", "folk"]
countrylist =["country rock", "country-pop", "country pop", "contemporary country", "country"]
jazzlist =  ["vocal jazz", "jazz", "jazz-rock"]
rellist = ["christian", "christmas music", "gospel"]
blueslist =["delta blues", "rock blues", "urban blues", "electric blues", "acoustic blues", "soul blues", "country blues", "jump blues", "classic rock. blues rock", "jazz and blues", "piano blues", "british blues", "british rhythm & blues", "rhythm and blues", "blues", "blues rock", "rhythm & blues"]
reggaelist = ["reggae fusion", "roots reggae", "reggaeton", "pop reggae", "reggae", "soul and reggae"]
rblist = ["rhythm and blues", "contemporary rnb", "contemporary r&b", "rnb", "rhythm & blues","r&b", "contemporary r b"]
genrelist = ["rock", "alternative", "electric", "soul", "classical", "pop", "r&b", "hip-hop", "disco", "swing","folk", "country", "jazz", "religious", "blues", "reggae"]

mylist = ['1', '60s', '80s', 'metal', 'garage rock', 'adult alternative pop rock', 'electric blues', 'swing', 'disco','roots reggae']

def genre(list):
    try:
        rock = [i if i not in rocklist else 'rock' for i in list]
    except:
        pass
    try:
        alt = [i if i not in altlist else 'alternative' for i in rock]
    except:
        pass
    try:
        elec = [i if i not in electlist else 'electric' for i in alt]
    except:
        pass
    try:
        sou = [i if i not in soullist else 'soul' for i in elec]
    except:
        pass
    try:
        clas = [i if i not in classlist else 'classical' for i in sou]
    except:
        pass
    try:
        pop = [i if i not in poplist else 'pop' for i in clas]
    except:
        pass
    try:
        hip = [i if i not in hiphoplist else 'hip-hop' for i in pop]
    except:
        pass
    try:
        dis = [i if i not in discolist else 'disco' for i in hip]
    except:
        pass
    try:
        swi = [i if i not in swinglist else 'swing' for i in dis]
    except:
        pass
    try:
        fol = [i if i not in folklist else 'folk' for i in swi]
    except:
        pass
    try:
        cou = [i if i not in countrylist else 'country' for i in fol]
    except:
        pass
    try:
        jaz = [i if i not in jazzlist else 'jazz' for i in cou]
    except:
        pass
    try:
        rel = [i if i not in rellist else 'religious' for i in jaz]
    except:
        pass
    try:
        blu = [i if i not in blueslist else 'blues' for i in rel]
    except:
        pass
    try:
        rb = [i if i not in rblist else 'r&b' for i in blu]
    except:
        pass
    try:
        reg = [i if i not in reggaelist else 'reggae' for i in rb]
    except:
        pass
    try:  # delete dupes and delete if not in genrelist
        comp = [i for i in reg if i in genrelist]
    except:
        pass
    try:
        res = []
        [res.append(i) for i in comp]
        return res
    except:
        return "not found"

df["genre"] = df.apply(lambda row: genre(row['tags']), axis=1)


import collections

def count(row):
    a_counter = collections.Counter(row)
    most_common = a_counter.most_common(1)
    print(most_common)

df["genres"] = df.apply(lambda row: genre(row['genre']), axis=1)

#save to csv
df.to_csv('your file')
