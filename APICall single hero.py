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
    number = random.randint(0, 2000)
    connection_url = url + "?limit=1&offset=" + str(number) + "&ts=" + timestamp + "&apikey=" + public_key + "&hash=" + md5digest
    return connection_url

while True:
    connection_url = dataOpvragen()
    response = requests.get(connection_url)
    jsontext = json.loads(response.text)
    # om de JSON leesbaar te printen...
    json_leesbaar = json.dumps(jsontext, sort_keys=True, indent=4)

    with open('apitext.json', 'w') as myfile:
        myfile.write(json_leesbaar)

    with open('Heroes.txt', 'w+', newline='') as file, open('Hero.json', 'w') as file2:
        for item in jsontext['data']['results']:
            if len((item['description'])) > 20:
                if int(item['comics']['available']) >= 3:
                    if int(item['series']['available']) >= 2:
                        if int(item['stories']['available']) >= 2:
                            print('hero gevonden')
                            file.write(item['name'] + ';' + str(item['description']) + '\n')
                            file.write('-----------------------Available Commics: ' + str(item['comics']['available']) + '-----------------------------\n')
                            all_comics = []
                            all_series = []
                            all_stories = []
                            for comics in item['comics']['items']:
                                all_comics.append({'name': comics['name']},)
                                file.write(comics['name'] + '\n')
                            file.write('-----------------------Available Series: ' + str(item['series']['available']) + '------------------------------\n')
                            for series in item['series']['items']:
                                file.write(series['name'] + '\n')
                                all_series.append({'name': series['name']}, )
                            file.write('-----------------------Available Stories: ' + str(item['stories']['available']) + '----------------------------\n')
                            for stories in item['stories']['items']:
                                file.write(stories['name'] + '\n')
                                all_stories.append({'name': stories['name']}, )
                            data = {'hero': {'name': item['name'], 'description': item['description'],
                                             'comics': {'appearances': item['comics']['available'], 'items': all_comics},
                                             'series': {'appearances': item['series']['available'], 'items': all_series},
                                             'stories': {'appearances': item['stories']['available'], 'items': all_stories
                                                         }
                                             }
                                    }
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
