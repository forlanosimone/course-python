##
# Ho 4 sensori, come posso codificare i dati dei sensori?
# Non posso utilizzare un insieme perché se ho dati uguali ce ne sarà solo uno e l'ordine è casuale

# La chiave diventa il nome o il codice identificativo del sensore
temp_dict = {"sensore_1":23.4, "sensore_2":23.4, "sensore_3":7.8, "sensore_4":18.4}
print(temp_dict)

temp_dict["sensore_1"] += 0.1 # Posso incrementare il valore con la chiave
print(temp_dict)

# Aggiungo elementi
temp_dict["sensore_5"] = 17.8
print(temp_dict)

temp_dict["timestamp"] = "2022/05/08 18:08:10"
print(temp_dict)
print(type(temp_dict["timestamp"]))

import time
print(time.time()) # Ritorna il numero di secondi passati dal 1 gennaio 1970
# è un flot perché ci sono i milliseconi ma possiamo metterlo nel dizionario

temp_dict["timestamp"] = time.time()
print(temp_dict)
