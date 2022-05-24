'''
Questo modulo permette di definire una regione di interesse (ROI) all'interno di un'immagine,
andando a definire le coordinate del punto Top-Left e le coordinate del punto Bottom-Right.
'''

import cv2 as cv
from moduli.read import read_int

# @param img
# @return roi_img
def roi(img):
    "Questa funzione definisce una regione di interesse nell'immagine."
    print("Inserisci le coordinate del punto Top Left e del punto Bottom Right\
         per la creazione del bouding box.")
    #r,c = img.shape
    # start_x < stop_x e start_y < stop_y e che questi punti siano minori di tutta l'immagine
    STR_MAX_STP = True
    while STR_MAX_STP:
        try:
            start_x_pt = read_int("inserisci start_x (Es.2800):")
            start_y_pt = read_int("inserisci start_y (Es.600):")
            stop_x_pt = read_int("inserisci stop_x (Es.3300):")
            if start_x_pt > stop_x_pt:
                print(f'start_x deve essere < stop_x, {start_x_pt} non è < di {stop_x_pt}')
                raise ValueError
            stop_y_pt = read_int("inserisci stop_y (Es.1000):")
            if start_y_pt > stop_y_pt:
                print(f'start_y deve essere < stop_y, {start_y_pt} non è < di {stop_y_pt}')
                raise ValueError
            STR_MAX_STP = False
        except ValueError:
            STR_MAX_STP = True

    roi_img = img[start_y_pt:stop_y_pt ,start_x_pt:stop_x_pt] # Prima la y (righe) poi x (colonne)
 
    return roi_img


if __name__ == "__main__":
    print("Voglio fare il test...")
    print("Inserisci le coordinate del punto Top Left e del punto Bottom Right per\
         la creazione del bouding box.")
    PATH_IMG = ".\\Esame\\immagini\\DSCF0336.jpg"
    img = cv.imread(PATH_IMG, cv.IMREAD_GRAYSCALE)

    # start_x < stop_x e start_y < stop_y e che questi punti siano minori di tutta l'immagine

    STR_MAX_STP = True
    while STR_MAX_STP:
        try:
            start_x = read_int("inserisci start_x (Es.2800):")
            start_y = read_int("inserisci start_y (Es.600):")
            stop_x = read_int("inserisci stop_x (Es.3300):")
            if start_x > stop_x:
                print(f'start_x deve essere < stop_x, {start_x} non è < di {stop_x}')
                raise ValueError
            stop_y = read_int("inserisci stop_y (Es.1000):")
            if start_y > stop_y:
                print(f'start_y deve essere < stop_y, {start_y} non è < di {stop_y}')
                raise ValueError
            STR_MAX_STP = False
        except ValueError:
            STR_MAX_STP = True
