##
# Voglio stampare i primi 10 numeri partendo da zero
# Utilizzando la varibile flag (variabile che può assumere True o False) 
# Prima faccio la valutazione e poi incremento

a = 0
condizione = True # Variabile flag
while(condizione):
    if(a >= 10): # Valutazione
        condizione = False
    print(a)
    a = a + 1 # Incremento

# Prima vado ad incrementare e poi vado a valutare
# Posso ottenere lo stesso risulato modificando >= nell'if
a = 0
condizione = True
while(condizione):
    a = a + 1 # Incremento
    #print(a)
    if(a >= 10): # Valutazione
        condizione=False
    print(a)
    