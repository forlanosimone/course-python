##
# Fare la somma di una lista

a = [-1,1,2,3,4,5]

# 1st versione
somma = 0
# for con accesso tramite indice
for i in range(len(a)): # Mettiamo range(len(a)) perchè solamente len(a) è un interno e non è iterabile
    #print(i," ",a[i]) # Printiamo il valore di i, uno spazio " " e gli indici della lista
    somma +=a [i]
print("la somma della lista è:",somma)

# 2nd versione
somma = 0
# Non occorre l'indice ma item è valorizzato attraverso lo scorrimento in modo automatico nella lista
for item in a: # Al posso di item posso utilizzare anche i
    somma += item
print("la somma della lista è:",somma)

# La 2nd versione ha lo svantaggio di non poter accedere in modo indicizzato nella lista
# Item contiene il valore e non l'indice, se voglio accedere in modo puntutale e 
# variado l'indice a seguito di qualche condizione è preferibile la 1st versione

##
# Esempio
somma = 0
for i in range(len(a)): 
    somma += a[i]
    if(a[1] == 0): # Se per qualche motivo devo avere queste condizioni nella logica della 2nd versione non lo posso fare
        i = i - 2
        a[i] = 3
print("la somma della lista è:",somma)
