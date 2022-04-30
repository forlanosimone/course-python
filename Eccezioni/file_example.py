##
# apro il file 
file = open("F:\\Università\\Magistrale\\1°Ciclo\\Fondamenti di Informatica\\Codici Python\\Eccezioni\\file_di_testo.txt")

# operazione di lettura
riga = str(file.readline())
print(riga)

# itero su riga_splitted per printare
riga_splitted = riga.split(";") # splitto la linea con il separatore (;) se il separatore era il tab dovevamo inserire (("\t"))
for item in riga_splitted:
    print(item)

# la prima riga è di intestazione
# posso fare direttamente il cast a float in una linea ma se la linea non è separata in elementi non va bene, bisogna separare gli elementi
riga = str(file.readline())
while(riga != ""):
    riga = str(file.readline())
    riga_splitted = riga.split(";")
    print(len(riga_splitted))

# operazione di chiusura
file.close()