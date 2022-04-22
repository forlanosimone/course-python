##
# lista 1d
list_1 = [0, 1, 2]
print(list_1)
print(type(list_1))

# creo una lista 2d
list_2 = [
    [0, 1, 2],
    [3, 4, 5]
    ]
print(len(list_2))      # ci ritorna il numero di righe
print(len(list_2[0]))   # se accedo al primo elemento posso vedere la dimensione sulle colonne
print(list_2)
print(type(list_2))

# per stampare la matrice
for i in range(len(list_2)):        # i si utilizza per le righe
    for j in range(len(list_2[0])):
        print(list_2[i][j], end=" ")         # prima si estare la sottolista e poi tutti gli elementi
    print()                                  # sto stampando una str vuota per andare a capo