##
# apro il file 
file = open("F:\\Università\\Magistrale\\1°Ciclo\\Fondamenti di Informatica\\Codici Python\\Eccezioni\\dati.txt")

# operazione di lettura della prima riga
riga = str(file.readline()) # riga di intestazione
print(riga)

# creiamo la lista che contiene il risultato (avrà N elementi con N = numero delle colonne)
riga_splitted = riga.split("\t") # la prima riga sarà acc_x e acc_y separati dal tabulatore (\t)
N = len(riga_splitted)
lista_somma = [0] * N # inizializzo la lista a zero e poi la moltiplico per N

# facciamo la somma delle due colonne andando a sommare le righe e aggiornando la lista_somma
while(riga != ""): # fino a quando la riga è diversa dalla stringa vuota
    riga = str(file.readline())
    riga_splitted = riga.split("\t") # la funzine split ci ritorna una stringa
    if(len(riga_splitted) == N): # se la lunghezza di quello che ho separato è pari ad N continuo altrimenti ignoro, ci potrebbero essere righe corrotte
        for i in range(N):
            lista_somma[i] += float(riga_splitted[i]) # faccio il cast da stringa a float e partendo da i=0 sommo il valore
print("lista somma")
# stampiamo il risultato
print(lista_somma) # si instaura un errore perché alcuni numeri hanno una rappresentazione periodica (approssimazioni numeriche)
# si può risolvere con un operazione di round

# operazione di chiusura
file.close()

########################################################################
########################################################################
##
# per fare la media ho bisogno del numero di righe quindi di un contatore

# apro il file 
file = open("F:\\Università\\Magistrale\\1°Ciclo\\Fondamenti di Informatica\\Codici Python\\Eccezioni\\dati.txt")

# operazione di lettura della prima riga
riga = str(file.readline()) # riga di intestazione

# creiamo la lista che contiene il risultato (avrà N elementi con N = numero delle colonne)
riga_splitted = riga.split("\t") # la prima riga sarà acc_x e acc_y separati dal tabulatore (\t)
N = len(riga_splitted)
lista_somma = [0] * N

n_elementi = 0 # contatore

while(riga != ""):
    riga = str(file.readline())
    riga_splitted = riga.split("\t")
    if(len(riga_splitted) == N):
        n_elementi += 1
        for i in range(N):
            lista_somma[i] += float(riga_splitted[i])

lista_media = [0] * N # qui inizializzo con una lista piena di zeri
for i in range(N):
    lista_media[i] = lista_somma[i] / n_elementi
print("lista media")
print(lista_media)

lista_media = list(lista_somma) # qui inizilizzo lista_media con i valori di lista_somma realizzando una copia
for i in range(N):
    lista_media[i] /= n_elementi
print(lista_media)

# operazione di chiusura
file.close()