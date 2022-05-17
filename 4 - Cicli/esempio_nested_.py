##
# Scrivere codice per ottenre come output questa sequenza
'''
abcd
efgh
ilmn
'''
s = "abcdefghilmn" # Stringa lunga 12 elementi volgiamo stamprle in 3 righe con 4 colonne

# Mettiamo le costanti fuori dai cicli così sono più facili da cambiare
k = 0
H = 3 # Righe
W = 4 # Colonne
# Sappiamo che s[0]=a e s[len(s)-1]=n

for i in range(H):
    for j in range (W): # Vogliamo passare dai due indici i e j ad un solo indice che mi consente di accedere a tutti gli elementi
        print(s[k], end="") # Indice che ci consente di accedere alla riga
        k = k + 1
    print("")

# Il for interno cicla più velocemente del for esterno
'''
i j k
0 0 0
0 1 1
0 2 2
0 3 3
1 0 4
1 1 5
1 2 6
1 3 7
2 0 8
2 1 9
2 2 10
2 3 11

La relazione matematica che consente di legare i,j,k è: k = 4 * i + j = W * i + j 
W è la dimensione della colonna

Se abbiamo una matirce che deriva dalla trasposizione di un vettore, 
il vettore è lineare ma lo trattiamo come se fosse una matrice.
Il vettore s è lineare e con i due for annidati vogliamo accedere in modo matriciale
'''

k = 0
H = 3
W = 4

for i in range(H):
    for j in range(W):
        k = W * i + j
        print(s[k], end="") # Indice che ci consente di accedere alla riga
        #k=k+1 qui la incremento dopo perchè prima deve essere uguale a zero
    print("")

# Con questi esempi non ancora tocchiamo le notazioni per matrici che vedremo prossimamente
