#stampare 3 volte la sequenza di 4 asterischi ****

#questo funziona ma noi volgiamo ottenterlo con un ciclo for
print("****")
print("****")
print("****")

###########################################################
###########################################################

#utilizzando un ciclo for
for i in range(3): #posso mettere anche range(0,3)
    print("****")

###########################################################
###########################################################

#utilizzando due cicli for annidati (nested)

for i in range(3):
    for j in range(4):
        print("*",end="") #se scrivo print("*") tutti gli asterischi sono su una colonna perché il comando print() di default ha il new line (mettere il mouse su print() per vedere la documentazione)
#se non voglio andare a capo per ogni asterisco (new line) vado a mettere print("*",end="")
#in questo modo verrà stampato tutto su una riga

###########################################################
###########################################################

#vado a stampare il print("/n") per andare a capo 

for i in range(3):
    for j in range(4):
        print("*",end="")
    print("\n")

#con print("\n") vado a capo 2 volte perchè il comando print() di default ha il new line

###########################################################
###########################################################

#vado a togliere il \n lasciamo print("")

for i in range(3):
    for j in range(4):
        print("*",end="")
    print("") #messo per togliere un a capo

#un altro modo per stmapre questa sequenza è con la variabile di appoggio
#vedere esempio_matrici_.py