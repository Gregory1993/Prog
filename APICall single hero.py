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

    with open('Heroes.txt', 'w+', newline='') as file:
        for item in jsontext['data']['results']:
            if len((item['description'])) > 20:
                print('hero gevonden')
                file.write(item['name'] + ';' + str(item['description']) + '\n')
                counter += 1
            else:
                print('nieuwe hero')
                continue
    if counter == 1:
        break
