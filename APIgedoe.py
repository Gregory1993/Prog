import json
import hashlib
import time
import requests


public_key = "e236fca8413247cbbd3b6eab5a278226"
private_key = "52fd65bb2019b663e26f555526b943dcfc1d5b2d"
timestamp = str(time.time())
hash = hashlib.md5( (timestamp+private_key+public_key).encode('utf-8') )
md5digest = str(hash.hexdigest())

url = "http://gateway.marvel.com:80/v1/public/characters"
connection_url = url+"?ts="+timestamp+"&apikey="+public_key+"&hash="+md5digest
print(connection_url)


response = requests.get(connection_url)
jsontext = json.loads(response.text)

# om de JSON leesbaar te printen...
print(json.dumps(jsontext, sort_keys=True, indent=4))
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

with open('api_data.json', 'w') as file:
    getal = 0
    for item in jsontext['data']['results']:
        file.write(item['name'] + '\n')
        file.write('Series\n')
        for a in jsontext['data']['results'][getal]['series']['items']:
            file.write(a['name'] + '\n')
            file.write('Stories\n')
        for b in jsontext['data']['results'][getal]['stories']['items']:
            file.write(b['name'] + '\n')
            file.write('Comics\n')
        for c in jsontext['data']['results'][getal]['comics']['items']:
            file.write(c['name'] + '\n')
        getal += 1
        file.write('\n')
