A=input() #in questo modo andremo ad inserire una stringa
B=input()
print(A+B) #concatenazione di stringhe
print("somma="+(A+B)) #con il + andremo a fare una concatenazione di stringhe (somma di stringhe)
#dobbiamo convertire l'intero in stringa
#print(type(int(B))) #possiamo forzare il tipo di variabile, è possibile passare dalla stringa al numero

A=int(input()) #definisco intero (prendi input e lo trasformi in intero)
B=int(input()) #type-casting operazione di casting = operazione di conversione
#print("somma="+(A+B)) #non posso sommare una stringa "somma=" con un intero (A+B)
print("somma="+str(A+B)) #convertiamo l'intero (A+B) in stinga 

print(type(A)) #per vedere il tipo di variabile (tipologia del dato)
#in Python non è obbligatorio definire il tipo di variabile e la variabile è dinamica può variare mentre in C no 