##
# This program ...
# URL DBSCAN: https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#sphx-glr-auto-examples-cluster-plot-dbscan-py
# URL Adaptive Thresholding: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html

# Importo le librerie
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from point import point

# Apro il file
PATH_file = ".\\Esame\\image.txt"

try:   
    file = open(PATH_file)
except IOError:
    print("il file non esiste")
    #return -1

# Operazione di lettura
riga = str(file.readline())
#print(riga)

# Itero su riga_splitted
riga_splitted = riga.split(";") # splitto la linea con il separatore (;) se il separatore era il tab ("\t") (carattere di tabulazione) splitto in una lista che contiene le 3
for item in riga_splitted:
    print(item)

# Operazione di chiusura
file.close()

nome_1 = riga_splitted[0]
nome_2 = riga_splitted[1]

PATH_img = ".\\Esame\\"

try:
    img_1 = cv.imread(f'{PATH_img}{nome_1}', cv.IMREAD_GRAYSCALE)
    img_2 = cv.imread(f'{PATH_img}{nome_2}', cv.IMREAD_GRAYSCALE)
    print(img_1)
    print(img_2)
except IOError: # Vedere link su Elenco di lettura
    print("Errore: il file non esiste")
#plt.imshow(img_1)
#plt.show()
# plt.imshow(img_2, cmap="gray")
# plt.show()

# Estrazione ROI (Region Of Interest)
# Posso fare una classe point dove fornisco x e y o inserisco le coordinate in una lista e poi splitto?
start_x = (2800) #int(input("inserisci start_x:")) #2800
start_y = (800) #int(input("inserisci start_y:")) #800
stop_x = (3000) #int(input("inserisci stop_x:")) #3000
stop_y = (1000) #int(input("inserisci stop_y:")) #1000

roi_img = img_1[start_y:stop_y ,start_x:stop_x] # Prima la y (righe) poi x (colonne)

# CLASSE
#roi = point(input("scrivi start_x"),input("scrivi start_y"),input("scrivi stop_x"),input("scrivi stop_y"))
#roi_img = img_1[roi.get_start_y() : roi.get_stop_x() , roi.get_start_x() : roi.get_stop_x()]
#roi_img = img_1[roi.get_roi()]

# PLOT ROI
#plt.imshow(roi_img, cmap="gray")
#plt.show()

# Adaptive Thresholding
th1 = cv.adaptiveThreshold(roi_img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,5)
th2 = cv.adaptiveThreshold(roi_img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY_INV,11,2)
titles = ['1 - Adaptive Mean Thresholding', '0 - Adaptive Mean Thresholding Inv']
images = [th1, th2]

for i in range(2):
    plt.subplot(1,2,i+1),
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show(block=0)

v = int(input("Inserisi 0 o 1:"))

th = cv.adaptiveThreshold(roi_img,255,cv.ADAPTIVE_THRESH_MEAN_C, v,11,2)

# Matrice P con pixel che hanno valori pari a v
coordinate = []  # Lista delle coordinate
last_x, last_y = 0, 0  # Inizilizziamo a zero

rows, cols = th.shape  # Calcoliamo righe e colonne

# Itero su righe e colonne con due for
for x in range(rows):
    for y in range(cols):
        px = th[x, y]
        if px == 255:
                coordinate.append((y, x))
        last_x, last_y = x, y

coordinate.append((last_y, last_x))
#print(coordinate)
P = np.array(coordinate)
print(P)

#Matrice P n*2
#[y1, x1,
#y2, x2,
#…
#yN, xN]

# Algoritmo DBSCAN
#eps = int(input("inserisci eps:")) #2
#min_samples = int(input("inserisci min_samples:")) #5

#X = StandardScaler().fit_transform(P)
db = DBSCAN(eps = 2, min_samples = 5).fit(P)

# Plot
F = np.ones((rows, cols))

plt.imshow(F)
plt.show()
