##
# Apro il file 
file = open(".\\7 - Eccezioni e File\\file_di_testo.txt")

# Operazione di lettura
riga = str(file.readline())
print(riga)

# Itero su riga_splitted per printare
riga_splitted = riga.split(";") # splitto la linea con il separatore (;) se il separatore era il tab ("\t") (carattere di tabulazione) splitto in una lista che contiene le 3
for item in riga_splitted:
    print(item)

# La prima riga è di intestazione
# Posso fare direttamente il cast a float in una linea ma se la linea non è separata in elementi non va bene, bisogna separare gli elementi
riga = str(file.readline())
while(riga != ""): # Fino a quando la riga è diversa dalla stringa vuota
    riga = str(file.readline())
    riga_splitted = riga.split(";")
    print(len(riga_splitted))
    # Per verificare se lo split mi ha restituito il numero di elementi corretto devo verificare che la lunghezza della lista che è stata ritornata dallo split corrisponde al numero di colonne
    if(riga_splitted == 1):
        print("formato corretto...")
        # Lo split deve ritornare sempre il numero di colonne che mi aspetto

# Operazione di chiusura
file.close()
