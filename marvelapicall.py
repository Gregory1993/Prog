import json
import hashlib
import time
import requests
import random

public_key = "e236fca8413247cbbd3b6eab5a278226"
private_key = "52fd65bb2019b663e26f555526b943dcfc1d5b2d"
counter = 0
timestamp = str(time.time())
hash = hashlib.md5( (timestamp+private_key+public_key).encode('utf-8') )
md5digest = str(hash.hexdigest())
url = "http://gateway.marvel.com:80/v1/public/characters"

def dataOpvragen():
    'Deze functie maakt een random url aan voor een random hero'
    number = random.randint(0, 2000)
    connection_url = url + "?limit=1&offset=" + str(number) + "&ts=" + timestamp + "&apikey=" + public_key + "&hash=" + md5digest
    return connection_url

# In een loop wordt de random hero gecheckt op een aantal criteria:
# Heeft de hero voldoende beschrijving en heeft de hero genoeg appearances om hints mee te maken.
while True:
    connection_url = dataOpvragen()
    response = requests.get(connection_url)
    jsontext = json.loads(response.text)
    # om de JSON leesbaar te printen
    json_leesbaar = json.dumps(jsontext, sort_keys=True, indent=4)

    with open('apitext.json', 'w') as myfile:
        myfile.write(json_leesbaar)

    with open('Hero.json', 'w') as file2:
        for item in jsontext['data']['results']:
            if len((item['description'])) > 20:  # hier wordt gekeken of de description bestaat en/of lang genoeg is.
                if int(item['comics']['available']) >= 3: # Hier wordt er gekeken of de hero in genoeg comics voor komt.
                    if int(item['series']['available']) >= 2: # Hier wordt er gekeken of de hero in geneog series voor komt.
                        if int(item['stories']['available']) >= 2: # Hier wordt er gekeken of de hero in genoeg stories voorkomt.
                            print('hero gevonden')
                            all_comics = []
                            all_series = []
                            all_stories = []
                            # De titels van alle comics, series en stories worden tijdelijk opgeslagen in een lijst.
                            for comics in item['comics']['items']:
                                all_comics.append({'name': comics['name']},)
                            for series in item['series']['items']:
                                all_series.append({'name': series['name']}, )
                            for stories in item['stories']['items']:
                                all_stories.append({'name': stories['name']}, )
                            # Nu wordt alle bruikbare data in een JSON formaat gezet.
                            data = {'hero': {'name': item['name'], 'description': item['description'],
                                             'comics': {'appearances': item['comics']['available'],
                                                        'items': all_comics},
                                             'series': {'appearances': item['series']['available'],
                                                        'items': all_series},
                                             'stories': {'appearances': item['stories']['available'],
                                                         'items': all_stories
                                                         }
                                             }
                                    }
                            # Om de naam niet weg te geven in de tip wordt deze hier weg gefilterd
                            heroName = data['hero']['name']
                            # Als de naam tekst tussen haakjes heeft wordt dit verwijderd
                            if '(' in heroName:
                                heroName = (heroName[:heroName.find('(') - 1])
                                if heroName in item['description']:
                                    descriptionFilter = item['description'].replace(heroName, '********')
                            elif heroName in item['description']:
                                descriptionFilter = item['description'].replace(heroName, '********')
                            else:
                                descriptionFilter = item['description']


                            print(heroName)
                            # De description wordt vervangen door de gefilterde description
                            data = {'hero': {'name': item['name'], 'description': descriptionFilter,
                                             'comics': {'appearances': item['comics']['available'], 'items': all_comics},
                                             'series': {'appearances': item['series']['available'], 'items': all_series},
                                             'stories': {'appearances': item['stories']['available'], 'items': all_stories
                                                         }
                                             }
                                    }
                            # Hier wordt de data uiteindelijk naar de file geschreven
                            json_data = json.dumps(data, indent=4)
                            file2.write(json_data)
                            counter += 1
                        else:
                            print('nieuwe hero')
                            continue
                    else:
                        print('nieuwe hero')
                        continue
                else:
                    print('nieuwe hero')
                    continue
            else:
                print('nieuwe hero')
                continue
    if counter == 1:
        break
