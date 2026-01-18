import requests
import json
import sys

if len(sys.argv) !=2:
    sys.exit() 
    
response = requests.get('https://itunes.apple.com/search?entity=song&limit=50&term='+sys.argv[1])
 
print(response)
o = response.json()
print(o)
for result in o["results"]:
    print(result["trackName"])