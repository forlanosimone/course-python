##
# Sommo due numeri con input dell'utente

A = input() # In questo modo andremo ad inserire una stringa
B = input()

print(A+B) # Concatenazione di stringhe

print("somma=" + (A+B)) # Con il + andremo a fare una concatenazione di stringhe (somma di stringhe)
# Dobbiamo convertire l'intero in stringa
print(type(int(B))) # Possiamo forzare il tipo di variabile, è possibile passare dalla stringa al numero

A = int(input()) # Definisco intero (prendi input e lo trasformo in intero)
B = int(input()) # Type-casting operazione di casting = operazione di conversione
#print("somma="+(A+B)) # Non posso sommare una stringa "somma=" con un intero (A+B)
print("somma=" + str(A+B)) # Convertiamo l'intero (A+B) in stinga 

print(type(A)) # Per vedere il tipo di variabile (tipologia del dato)
# In Python non è obbligatorio definire il tipo di variabile
# La variabile è dinamica può variare mentre nel linguaggio C questo non accade
