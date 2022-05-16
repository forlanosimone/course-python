##
# Esempio d'uso di modulo.py per la somma

import modulo as mdl
#from modulo import differenza, somma # Se ci interessa importare una sola funzione possiamo fare così e poi bisogna chiamare solo la funzione senza modulo (mdl.somma)

a = int(input("inserisci il numero..."))
b = int(input("inserisci il numero..."))

somma = mdl.somma(a,b)
print("la somma è " + str(somma))
print("la differenza è " + str(mdl.differenza(a,b)))