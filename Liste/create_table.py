## creare una tabella con dimensione specificata dall'utente
# richiedere numero di righe e numero di colonne

n_righe = int(input("Inserisci il numero di righe:"))

n_colonne = int(input("Inserisci il numero di colonne:"))

tabella = [] # andiamo ad inizializzare una lista vuota

for i in range(n_righe):
    tabella.append([0] * n_colonne)

print("La tabella è formata da" + str(len(tabella)) + "righe", "e da", len(tabella[0]), "colonne")

print("ciao")