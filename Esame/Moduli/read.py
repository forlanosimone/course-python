'''
Questo modulo contiene diverse funzione per la lettura e apertura di file, 
immagini o input in base alla funzione scelta.
'''
# Importo le librerie
import sys
import cv2 as cv
import matplotlib.pyplot as plt

def read_int(str_x):
    "Questa funzione permette di prendere in input un numero intero, in caso di valore errato ci sarà un'eccezione."
    letto = False # Condizione
    while not letto:
        try:
            res = int(input(str_x))
            letto = True
        except ValueError as err:
            print(err)
    return res


def read_txt(PATH_file):
    "Questa funzione permette di leggere un file e ritornare una lista, con il nome delle immagini all'interno del file." 
    try:
        file = open(PATH_file, "r") # Apro il file in modalità di lettura
    except IOError:
        print(f'il file non esiste, controllare PATH_file {PATH_file}')
        sys.exit(1)
    
    # Operazione di lettura
    riga = file.read()
    riga_splitted = riga.split("\n")

    # Operazione di chiusura
    file.close()

    return riga_splitted

def read_img(PATH_img, nome):
    "Questa funzione permette di aprire un'immagine... "
    # Operazione di lettura
    img = cv.imread(f'{PATH_img}{nome}', cv.IMREAD_GRAYSCALE) # Conversione immagine in scala di grigi
    #img = cv.imread(f'{PATH_img}{nome}')
    #img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    print(cv.haveImageReader(f'{PATH_img}{nome}')) # Restituisce true se l'immagine specificata può essere decodificata da OpenCV
    # Eccezione
    if (img is None):
        raise ValueError("L'immagine non esiste, controllare PATH_img e l'immagine")
      
    return img

if(__name__ == "__main__"):
    print("voglio fare il test...")
    PATH_img = ".\\Esame\\immagini\\"
    PATH_file = ".\\Esame\\image.txt"
    riga_splitted = read_txt(PATH_file)
    read_img(PATH_img, riga_splitted)

