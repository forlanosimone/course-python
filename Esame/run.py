##
# Questo codice premette di...
# URL DBSCAN: https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#sphx-glr-auto-examples-cluster-plot-dbscan-py
# URL Adaptive Thresholding: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html

# Importo le librerie
import sys
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

from moduli import read, crop_image
from moduli.plt import plt_img

def main():
    # Definisco il path del file di testo e leggo i nomi delle immagini
    PATH_FILE = ".\\Esame\\image.txt"
    name_splitted = read.read_txt(PATH_FILE)

    # Definisco il path delle immagini
    PATH_IMG = ".\\Esame\\immagini\\"
    # Ripeto per tutte le immaigni
    for item in name_splitted:
        try:
            img = read.read_img(PATH_IMG, item)
        except ValueError as err:
            print(f'Eccezione di tipo value error per {item}\n{err}')
            sys.exit(1)

        # Plot immagine
        plt_img(img, "Immagine Originale")

        # Estrazione ROI (Region Of Interest)
        roi_img = crop_image.roi(img)

        # Plot ROI
        plt_img(roi_img, "Region of Interest")

        # Adaptive Thresholding
        BLOCK_SIZE = 21 # Dimensione di pixel vicini utilizzati per calcolare la soglia
        C = 6 # Costante sottratta dalla media

        th_adp = cv.adaptiveThreshold(roi_img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
                    cv.THRESH_BINARY, BLOCK_SIZE, C)
        th_adp_inv = cv.adaptiveThreshold(roi_img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
                    cv.THRESH_BINARY_INV, BLOCK_SIZE, C)

        # Erosione e dilatazione
        '''
        # Codice di prova non implementato
        kernel_1 = np.ones((3,3))
        kernel_2 = np.copy(kernel_1)
        kernel_2 [1,1] = 2
        th_filter = cv.dilate(th_adp, kernel_1)
        th_filter = cv.erode(th_adp, kernel_2)
        '''

        # Plot ROI con 2 valori
        titles = ["Valore grilli v=0", "Valore grilli v=255"]
        images = [th_adp, th_adp_inv]

        for i in range(2):
            plt.subplot(1,2,i+1),
            plt.imshow(images[i],'gray')
            plt.title(titles[i])
            plt.xticks([]),plt.yticks([])
            plt.colorbar(ticks=[0, 255], orientation='horizontal')
        plt.show(block = False)

        # Utente sceglie valore dei grilli
        v = -1
        while (v != 255 and v != 0):
            v = read.read_int("Inserisci valori grilli (0 o 255): ")
            if v == 255:
                th = th_adp_inv
            elif v == 0:
                th = th_adp
            else:
                print(f'Valore errore {v} diverso 255 o 0')

        # Plot immagine con valore scelto
        plt_img(th,f'Immagine v = {v}')

        # Matrice P con pixel che hanno valori pari a v
        coordinate = []  # Lista delle coordinate
        last_x, last_y = 0, 0  # Inizilizziamo a zero

        rows, cols = th.shape  # Calcoliamo righe e colonne

        # Itero su righe e colonne con due for per prendere le coordinate dei pixel uguali a v
        for x in range(cols):
            for y in range(rows):
                px = th[y, x]
                if px == v:
                    coordinate.append((y, x))
                last_x, last_y = x, y

        coordinate.append((last_y, last_x))
        P = np.array(coordinate)
        print("MATRICE DELLE COORDINATE")
        print(P)
        plt_img(th,"Confronta con matrice delle coordinate")

        # Algoritmo DBSCAN
        # eps -> distanza all'interno della quale ricercare i punti vicini
        EPS = 5 #int(input("inserisci eps (Es.2):"))

        # min_samples -> numero minimo di punti affinché si formi un cluster
        MIN_SAMPLES = 20 #int(input("inserisci min_samples (Es.5):"))

        db = DBSCAN(EPS, min_samples = MIN_SAMPLES).fit(P)
        labels = db.labels_

        # Numero di cluster nelle etichette, ignorando il rumore se presente.
        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
        n_noise = list(labels).count(-1)
        print(f'Numero di cluster stimati: {n_clusters}')
        print(f'Numero stimato di punti di disturbo: {n_noise}')

        # Matrice F
        F = np.full((rows, cols), -1)
       
        r,c = P.shape

        y = 0
        x = 0
        i = 0
        for x in range(c):
            for y in range(r):
                F [y,x] = labels[i] # Associo l'identificatore del cluster
                i += 1

main()