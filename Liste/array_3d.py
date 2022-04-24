##
# gli array possono essere fatti da più di due dimensioni

# array monodimensionale
a = [1,2]
print(a[0]) # riesco ad acceere con un solo indice

# array bidimensionale
a_2d = [[1,2], [3,4]]
print(a_2d[0][1]) # riesco ad accedere con due indici

# array tridimensionali
a_3d = [[[1,2,3], [1,2,4], [1,2,5]], [[-1,-2,-3],[-1,-2,-4],[-1,-2,-5]]]

#print(len(a_3d))
#print(len(a_3d[0]))
#print(len(a_3d[0][0]))
print(a_3d[1][2][1]) # riesco ad accedere con tre indici 