##
# Esempi fi statement
x = int(input("inserisci un numero...")) # Metto int per trasformare le stringa in interno

if(x < 0):
    x = -x
    print("inverto il valore...")
print("abs(x)=", x) # Mettendo il print() dentro l'if lo eseguo solo se l'istruzione if(x<0) è verificata
# Per cambiare indentazione si utilizza TAB => mentre per <= TAB+shif o backspace

# Se vogliamo mettere al posto di x (abs(x)) il valore iniziale inserito
x = int(input("inserisci un numero..."))

if(x < 0):
    print("abs(%d)="%(x), -x)
    x = -x
else: # Questo ramo viene verificato se e solo se la condizione dell'if non è verificata
    print("abs(%d)="%(x), x)


# C'è del codice ripetuto, ci sono 2 print()
# Utilizzando un solo print()
x = int(input("inserisci un numero..."))

if(x < 0):
    y = -x # Ci interessa tenere x (valore inserito) per questo utlizzo y=-x
else: # Senza else avrei problemi con x>0
    y = x
print("abs(%d)= %d"%(x,y))
