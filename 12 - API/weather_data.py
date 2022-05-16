##
# Io sono il Client e interrogo il server
# API (Application Programming Interface) formato da end point e query string (stringa per fare ricerca)
# I dati possono ritornare in JSON, XML o HTML

# Nel JSON i dati sono memorizzati come chiave:valore
# L'XML è un linguaggio marcato simile all'HTML
# Per visalizzare meglio i JSON possiamo utilizzare JSONLint (sito)

import json
import requests # Ci permettere di chiedere al server
from secret import key

URL = "https://api.openweathermap.org/data/2.5/weather?appid=" + key + "=Guardiagrele,IT"
# Nell'url se al posto di weather mettiamo forecast avremo le previsioni

payload = {}
headers = {}

response = requests.request("GET", URL, headers=headers, data=payload)

print(response.text)

decoded =  json.loads(response.text) # Deserializza una stringa in un python object

print("decoded text")
print(decoded)
