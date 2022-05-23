'''
Questo modulo permette di definire una regione di interesse (ROI) all'interno di 
un'immagine, andando a definire le coordinate del punto Top-Left e le coordinate
del punto Bottom-Right.
'''
def roi(img):
    print("Inserisci le coordinate del punto Top Left e del punto Bottom Right per la creazione del bouding box.")
    try:    
        start_x = 2800 #int(input("inserisci start_x (Es.2800):"))
        start_y = 600 #int(input("inserisci start_y (Es.600):"))
        stop_x = 3300 #int(input("inserisci stop_x (Es.3300):"))
        stop_y = 1000 #int(input("inserisci stop_y (Es.1000):"))
    except ValueError:
        print("Si possono inserire solo numeri interi")
    # Prima la y (righe) poi x (colonne)
    roi_img = img[start_y:stop_y ,start_x:stop_x]
    
    return roi_img
