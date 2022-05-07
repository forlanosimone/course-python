##
# apro il file 
file = open("F:\\Università\\Magistrale\\1°Ciclo\\Fondamenti di Informatica\\Codici Python\\Eccezioni\\file_di_testo.txt")

# operazione di lettura
riga = str(file.readline())
print(riga)

# itero su riga_splitted per printare
riga_splitted = riga.split(";") # splitto la linea con il separatore (;) se il separatore era il tab ("\t") (carattere di tabulazione) splitto in una lista che contiene le 3
for item in riga_splitted:
    print(item)

# la prima riga è di intestazione
# posso fare direttamente il cast a float in una linea ma se la linea non è separata in elementi non va bene, bisogna separare gli elementi
riga = str(file.readline())
while(riga != ""): # fino a quando la riga è diversa dalla stringa vuota
    riga = str(file.readline())
    riga_splitted = riga.split(";")
    print(len(riga_splitted))
    # per verificare se lo split mi ha restituito il numero di elementi corretto devo verificare che la lunghezza della lista che è stata ritornata dallo split corrisponde al numero di colonne
    if(riga_splitted == 1):
        print("formato corretto...")
        # lo split deve ritornare sempre il numero di colonne che mi aspetto

# operazione di chiusura
file.close()