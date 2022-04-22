x = int(input("inserisci un numero...")) #metto int per trasformare le stringa in interno

if (x < 0):
    x=-x
    print("inverto il valore...")
print("abs(x)=",x)#mettendo il print() dentro l'if lo esguso solo se l'istruzione if(x<0) è verificata
#per cambiare indentazione si utilizza TAB => mentre per <= TAB+shif o backspace

########################################################################################################
########################################################################################################

#se vogliamo mettere al posto di x (abs(x)) il valore iniziale inserito
x = int(input("inserisci un numero..."))

if (x < 0):
    print("abs(%d)="%(x),-x)
    x=-x
else: #questo ramo viene verificato se e solo se la condizione dell'if non è verificata
    print("abs(%d)="%(x),x)

#c'è del codice ripetuto, ci sono 2 print()

########################################################################################################
########################################################################################################

#utilizzando un solo print()
x = int(input("inserisci un numero..."))

if (x < 0):
    y=-x #ci interessa tenere x (valore inserito) per questo utlizzo y=-x
else: #senza else avrei problemi con x>0
    y=x
print("abs(%d)=%d"%(x,y))

########################################################################################################
########################################################################################################