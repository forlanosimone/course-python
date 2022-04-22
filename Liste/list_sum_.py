#fare la somma di una lista

a=[-1,1,2,3,4,5]

#1st versione
somma=0
#for con accesso tramite indice
for i in range(len(a)): #mettiamo range(len(a)) perchè solamente len(a) è un interno e non è  iterabile
    #print(i," ",a[i])
    somma+=a[i]
print("la somma della lista è:",somma)

#2nd versione
somma=0
#non occorre l'indice ma item è valorizzato attraverso lo scorrimento in modo automatico nella lista
for item in a: #al posso di item posso utilizzare anche i
    somma+=item
print("la somma della lista è:",somma)

#la 2nd versione ha lo svantaggio di non poter accedere in modo indicizzato nella lista
#item contiene il valore e non l'indice, se voglio accedere in modo puntutale e magari variado l'indice a seguito di qualche condizione è preferibile la 1st versione

somma=0
for i in range(len(a)): 
    somma+=a[i]
    if(a[1]==0): #se per qualche motivo devo avere queste condizioni nella logica della 2nd versione non lo posso fare
        i=i-2
        a[i]=3
print("la somma della lista è:",somma)
