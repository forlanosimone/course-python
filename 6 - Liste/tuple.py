##
# definiamo una tupla e vediamo che non è possibile modificarla

a = ("pippo", 2, "simone", 7)
print(a)
print(type(a))

# per poter accedere alla tupla possiamo fare sempre così ma non possiamo modificare il valore
print(a[0])

print(a*2) # ma posso fare operazioni e possiamo accederci mediante indici

a[0] = "simone" # è immutabile
