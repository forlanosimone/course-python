##
# Io sono il Client e interrogo il server
# API (Application Programming Interface) formato da end point e query string (stringa per fare ricerca)
# I dati possono ritornare in JSON, XML o HTML

# Nel JSON i dati sono memorizzati come chiave:valore
# L'XML è un linguaggio marcato simile all'HTML
# Per visalizzare meglio i JSON possiamo utilizzare JSONLint (sito)

import requests # Ci permettere di chiedere al server
import json

url = "https://api.openweathermap.org/data/2.5/weather?appid=fad12c2ca3c5d8596156d99d41ccfe0a&q=Guardiagrele,IT"
# Nell'url se al posto di weather mettiamo forecast avremo le previsioni

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

decoded =  json.loads(response.text) # Deserializza una stringa in un python object

print("decoded text")
print(decoded)

