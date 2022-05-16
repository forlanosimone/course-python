##
# Previsioni meteo Guardiagrele

import requests # Ci permettere di chiedere al server
import json
import numpy as np
import matplotlib.pyplot as plt
from secret import key

url = "https://api.openweathermap.org/data/2.5/forecast?appid=" + key + "=Guardiagrele,IT"
# Nell'url se al posto di weather mettiamo weather avremo il meteo in tempo reale

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

decoded =  json.loads(response.text) # Deserializza una stringa in un python object

print("decoded text")
print(decoded)

print(decoded["list"][0]["main"]["temp"]) # Se voglio sapere la temperatura

# 1 - Creare un array in NumPy che sia grande quanto il numero di elementi ritornato nella lista cioè len(decoded["list"] oppure decoded["cnt"])
N = int(decoded["cnt"])
data_temp = np.zeros((N,1))
print(data_temp)

# 2 - Inserire il valore della temperatura ciclando per ogni elemento della lista
for i in range(N):
    data_temp[i] = decoded["list"][i]["main"]["temp"] # Temperatura in Kelin

print(data_temp-273.15)

# 3 - Inserire il tempo
data_temp = np.zeros((N,2))
print(data_temp)

for i in range(N):
    #data_temp[i][0] = decoded["list"][i]["dt"] # Tempo assoluto espresso in secondi (epoch time)
    # Mettere un tempo relativo rispetto il primo elemento (conteggio l'incremento temporale)
    data_temp[i][0] = decoded["list"][i]["dt"] - decoded["list"][0]["dt"]
    data_temp[i][1] = decoded["list"][i]["main"]["temp"] # Temperatura in Kelin

print(data_temp)
# Il tempo sarà incrementato di 10800 secondi = 3 ore

# Se voglio fare il plot dei dati con Matplotlib
plt.plot(data_temp[:,0]/3600, data_temp[:,1]-273.15) # Seleziono la colonna 0 e la colonna 1
plt.show()