##
# Data una lista fare reverse [1 2 5 3 4] ---> [4 3 5 2 1] (swapping elements)

# Caso 1 -> lista dispari [1 2 3 4 5] non ha senso far lo swap dell'elemento centrale, devo fare 2 iterazioni con una lista con 5 elementi
# Caso 2 -> lista pari [1 2 3 4]

lista = [-1,-4,5,6,7]
#lista = [-1,-4,6,7]

lista_reversed = list(lista)

# Calcoliamo su quanti elementi andare ad iterare
if((len(lista)%2) == 0): # Il % indica il resto della divisione
    n_iter = len(lista) // 2-1
else:
    n_iter = len(lista) // 2

for i in range(n_iter):
    lista_reversed[i] = lista_reversed[len(lista_reversed)-1-i]
