'''
Questo modulo contiene diverse funzione per la lettura e apertura di file, 
immagini o input in base alla funzione scelta.
'''
# Importo le librerie
import sys
import cv2 as cv

# @param str_x stringa da far visualizzare all'utente
# @return res ritorna un intero
def read_int(str_x):
    "Questa funzione permette di prendere in input un numero intero,\
    in caso di valore errato ci sarà un'eccezione."
    letto = False # Condizione
    while not letto:
        try:
            res = int(input(str_x))
            letto = True
        except ValueError as err:
            print(err)
    return res

# @param PATH_FILE posizione del file
# @return name_splitted ritorna una lista con i nomi dei file
def read_txt(PATH_FILE):
    "Questa funzione permette di leggere un file e ritornare una lista,\
        con il nome delle immagini all'interno del file."
    try:
        file = open(PATH_FILE, "r") # Apro il file in modalità di lettura
    except IOError:
        print(f'il file non esiste, controllare PATH_file {PATH_FILE}')
        sys.exit(1)

    # Operazione di lettura
    riga = file.read()
    name_splitted = riga.split("\n")

    # Operazione di chiusura
    file.close()

    return name_splitted

# @param PATH_IMG posizione del file
# @param nome nome del file con estensione
# @return img ritorna un array
def read_img(PATH_IMG, nome):
    "Questa funzione permette di aprire un'immagine... "
    # Operazione di lettura e conversione immagine in scala di grigi
    img = cv.imread(f'{PATH_IMG}{nome}', cv.IMREAD_GRAYSCALE)
    #img = cv.imread(f'{PATH_img}{nome}')
    #img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Restituisce true se l'immagine specificata può essere decodificata da OpenCV
    print(cv.haveImageReader(f'{PATH_IMG}{nome}'))
    # Eccezione
    if img is None:
        raise ValueError("L'immagine non esiste, controllare PATH_img e l'immagine")

    return img


if __name__ == "__main__":
    print("voglio fare il test...")
    PATH_IMG = ".\\Esame\\immagini\\"
    PATH_FILE = ".\\Esame\\image.txt"
    riga_splitted = read_txt(PATH_FILE)
    read_img(PATH_IMG, riga_splitted)
