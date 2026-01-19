import sys, requests, os
'''
from dotenv import load_dotenv
load_dotenv()
'''
API_KEY_COIN='ur apikey'



#precio=round(precio,4)
if len(sys.argv)!=2:
    print('Missing command-line argument')
    sys.exit(1)
try:
    cantidad=float(sys.argv[1])
    respuesta=requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey='+API_KEY_COIN)
    o=respuesta.json()

    precio=o["data"]

    precio=float(precio["priceUsd"])
except ValueError:
    print('Command line argument is not a number')
    sys.exit(1)
print(f'${cantidad*precio:,.4f}')

