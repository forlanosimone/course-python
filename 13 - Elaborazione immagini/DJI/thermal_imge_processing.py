##
# Analisi difetti pannelli solari

# Importo le librerie
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# Leggo l'immagine
PATH_img = ".\\13 - Elaborazione immagini\\DJI\\DJI_0804.jpg"
img = cv.imread(PATH_img) # In questo modo l'immagine viene letta come RGB
#print(img[0,0]) # Vedo che tutti e 3 i canali hanno valori uguali

img_single_ch = img[:,:,0] # Prendo il canale 0

# Plotto l'immagine
plt.imshow(img_single_ch, cmap="gray")
plt.show()

# Extract AOI/ROI o Crop, AOI (Area Of Interest), ROI (Region Of Interest)
# Posso fare una classe point dove fornisco x e y
start_x = (90)
start_y = (34)
stop_x = (322)
stop_y = (218)

img_cut = img_single_ch[start_y:stop_y,start_x:stop_x]
plt.imshow(img_cut, cmap="gray")
plt.show()

# Istogramma
'''
Facciamo il reshape della matrice perché np.histogram 
ha bisogno di una flattened array
'''
# Calcolo il numero di elementi della matrice, posso farlo in diversi modi
(r,c) = img_cut.shape
n_elements = r * c
#n_elements = img_cut.size
#n_elements = img_cut.shape[0] * img_cut.shape[1]

flatten_img = np.reshape(img_cut,(n_elements,1))
counts, bins = np.histogram(flatten_img, bins=256, range=(0, 255))

plt.hist(bins[:-1], bins, weights=counts) # Istogramma non normalizzato
plt.show()

# Anslisi multimodale, somma di n gaussiane
# Fittinig (trova le gaussiane nell'istogramma) algoritmi di clustering

# Segmentazione tramite thresholding e poi binarizziamo l'immagine
img_defect = img_cut>200
plt.imshow(img_defect, cmap="gray") # Ottengo una matrice di vero o di falso
plt.show() # Possiamo calcolare l'area e la zona danneggiata

# Andiamo a calcolare l'area difettore delle celle danneggiate
# Con numpy.sum andiamo a fare la somma di tutti i valori della matrice
element_over_th = np.sum(img_defect)
ratio = element_over_th/n_elements
print(f'detected defect is {ratio}') # string literal
# Posso calcolari anche con un for senza utilizzare numpy.sum
count = 0
for i in range(r): # per goni riga
    for j in range(c):
        if (img_cut[i,j]>200):
            count += 1

print(f'calcolo con np.sum {element_over_th}; con ciclo {count}')
