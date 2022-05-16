#voglio stampare i primi 10 numeri partendo da zero
#utilizzando la varibile flag (variabile che può assumere True o False) 
#prima faccio la valutazione e poi incremento

a=0
condizione=True #variabile flag
while(condizione):
    if(a>=10): #valutazione
        condizione=False
    print(a)
    a=a+1 #incremento

###############################################################################################
print("########")
###############################################################################################
#prima vado ad incrementare e poi vado a valutare (posso ottenere lo stesso risulato modificando >= nell'if)

a=0
condizione=True
while(condizione):
    a=a+1 #incremento
    #print(a)
    if(a>=10): #valutazione
        condizione=False
    print(a)