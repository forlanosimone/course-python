## 
# Creare una tabella con dimensione specificata dall'utente
# Richiedere numero di righe e numero di colonne

# Funzione per stampare una matrice
def print_2d_list(list_data):
    for i in range(len(list_data)): # i si utilizza per le righe
        for j in range(len(list_data[0])):
            print(list_data[i][j], end=" ") # Prima si estare la sottolista e poi tutti gli elementi
        print() # Sto stampando una str vuota per andare a capo

n_righe = int(input("Inserisci il numero di righe:"))

n_colonne = int(input("Inserisci il numero di colonne:"))

tabella = [] # Andiamo ad inizializzare una lista vuota

for i in range(n_righe):
    tabella.append([0] * n_colonne)

print("La tabella è formata da " + str(len(tabella)) + " righe" + "e da " + str(len(tabella[0])) + " colonne")

print(tabella) # Non va bene, scrive anche le parentesi
print_2d_list(tabella) # Scriviamo la tabella con la funzione definita
