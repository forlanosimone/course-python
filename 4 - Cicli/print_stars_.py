##
# Stampa 3 volte la sequenza di 4 asterischi ****

# Questo funziona ma noi volgiamo ottenterlo con un ciclo for
print("****")
print("****")
print("****")

# Utilizzando un ciclo for
for i in range(3): # Posso mettere anche range(0,3)
    print("****")

# Utilizzando due cicli for annidati (nested)
for i in range(3):
    for j in range(4):
        print("*",end="") 
# Se scrivo print("*") tutti gli asterischi sono su una colonna perché il comando print() 
# di default ha il new line (mettere il mouse su print() per vedere la documentazione)
# Se non voglio andare a capo per ogni asterisco (new line) vado a mettere print("*",end="")
# In questo modo verrà stampato tutto su una riga

# Vado a stampare il print("/n") per andare a capo 
for i in range(3):
    for j in range(4):
        print("*",end="")
    print("\n")
# Con print("\n") vado a capo 2 volte perchè il comando print() di default ha il new line

# Vado a togliere il \n lasciamo print("")
for i in range(3):
    for j in range(4):
        print("*",end="")
    print("") # Messo per togliere un a capo

# Un altro modo per stmapre questa sequenza è con la variabile di appoggio
# Vedere esempio_matrici_.py