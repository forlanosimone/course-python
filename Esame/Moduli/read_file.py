##
#

def read_file(PATH_file):
    try:   
        file = open(PATH_file, "r") # Apro il file in modalità di lettura
    except IOError:
        print("il file non esiste")
        exit

    # Operazione di lettura
    riga = file.read()
    riga_splitted = riga.split("\n")

    # Operazione di chiusura
    file.close()
    return riga_splitted