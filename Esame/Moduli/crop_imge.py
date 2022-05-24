'''
Questo modulo permette di definire una regione di interesse (ROI) all'interno di 
un'immagine, andando a definire le coordinate del punto Top-Left e le coordinate
del punto Bottom-Right.
'''
from moduli.read import read_int
import cv2 as cv

def roi(img):
    "Questa funzione definisce una regione di interesse nell'immagine."
    print("Inserisci le coordinate del punto Top Left e del punto Bottom Right per la creazione del bouding box.")
    r,c = img.shape
    # start_x < stop_x e start_y < stop_y e che questi punti siano minori di tutta l'immagine
    condizione = True
    while (condizione):
        try:
            start_x = read_int("inserisci start_x (Es.2800):")
            start_y = read_int("inserisci start_y (Es.600):")
            stop_x = read_int("inserisci stop_x (Es.3300):")
            if(start_x > stop_x):
                    print(f'start_x deve essere < stop_x, {start_x} non è < di {stop_x}')
                    raise ValueError
            stop_y = read_int("inserisci stop_y (Es.1000):")
            if(start_y > stop_y):
                    print(f'start_y deve essere < stop_y, {start_y} non è < di {stop_y}')
                    raise ValueError
            condizione = False
        except ValueError:
            condizione = True

    
    roi_img = img[start_y:stop_y ,start_x:stop_x] # Prima la y (righe) poi x (colonne)
    
    return roi_img

if(__name__ == "__main__"):
    print("Voglio fare il test...")
    print("Inserisci le coordinate del punto Top Left e del punto Bottom Right per la creazione del bouding box.")
    PATH_img = ".\\Esame\\immagini\\DSCF0336.jpg"
    img = cv.imread(PATH_img, cv.IMREAD_GRAYSCALE)
    r,c = img.shape

    # start_x < stop_x e start_y < stop_y e che questi punti siano minori di tutta l'immagine
  
    condizione = True
    while (condizione):
        try:
            start_x = read_int("inserisci start_x (Es.2800):")
            start_y = read_int("inserisci start_y (Es.600):")
            stop_x = read_int("inserisci stop_x (Es.3300):")
            if(start_x > stop_x):
                    print(f'start_x deve essere < stop_x, {start_x} non è < di {stop_x}')
                    raise ValueError
            stop_y = read_int("inserisci stop_y (Es.1000):")
            if(start_y > stop_y):
                    print(f'start_y deve essere < stop_y, {start_y} non è < di {stop_y}')
                    raise ValueError
            condizione = False
        except ValueError:
            condizione = True
