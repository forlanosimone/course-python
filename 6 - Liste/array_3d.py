##
# gli array possono essere fatti da più di due dimensioni

# Array monodimensionale
a = [1,2]
print(a[0]) # Riesco ad acceere con un solo indice

# Array bidimensionale
a_2d = [[1,2], [3,4]]
print(a_2d[0][1]) # Riesco ad accedere con due indici

# Array tridimensionali
a_3d = [[[1,2,3], [1,2,4], [1,2,5]], [[-1,-2,-3],[-1,-2,-4],[-1,-2,-5]]]

print(len(a_3d))
print(len(a_3d[0]))
print(len(a_3d[0][0]))
print(a_3d[1][2][1]) # Riesco ad accedere con tre indici
