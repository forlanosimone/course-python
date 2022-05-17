##
# Linguaggio case sensitive

A=3
a=2

print(A)
print(a)
# Case sensitive significa che ha una stretta dipendenza del modo in cui l'abbiamo scritta
# Quindi con MAIUSCOLO e minuscolo identifico cose in modo diverso

scelta = (input("vuoi continuare?"))

if(scelta.lower()=="y"):
    print("ho scelto si...")
else:
    print("ho scelto no...")
    