import json
import hashlib
import time
import requests


public_key = "e236fca8413247cbbd3b6eab5a278226"
private_key = "52fd65bb2019b663e26f555526b943dcfc1d5b2d"
counter = 0
timestamp = str(time.time())
hash = hashlib.md5( (timestamp+private_key+public_key).encode('utf-8') )
md5digest = str(hash.hexdigest())

while True:
    url = "http://gateway.marvel.com:80/v1/public/characters"
    print(timestamp)
    connection_url = url+"?limit=100&offset="+ str(counter) + "&ts=" +timestamp+"&apikey="+public_key+"&hash="+md5digest

    response = requests.get(connection_url)
    jsontext = json.loads(response.text)

    # om de JSON leesbaar te printen...
    json_leesbaar = json.dumps(jsontext, sort_keys=True, indent=4)

    with open('apitext.json', 'w') as myfile:
        myfile.write(json_leesbaar)

    print("\nGevonden characters in comics:")
    # JSON-indeling kun je uit het geprinte resultaat halen of uit de Marvel docs!
    for item in jsontext['data']['results']:
        print(item['name'])

    print("\nGevonden characters in series:")
    # JSON-indeling kun je uit het geprinte resultaat halen of uit de Marvel docs!
    for item in jsontext['data']['results']:
        print(item['name'])

    with open('api_data.json', 'a') as file:
        for item in jsontext['data']['results']:
            if len((item['description'])) > 20:
                file.write(item['name'] + ' has the following description: ' + str(item['description']) + '\n')

    counter += 100
    if counter == 1500:
        break

#TODO: de while loop mooier maken, andere informatie uit API halen, informatie uit json file ordenen
