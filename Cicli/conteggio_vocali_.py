#############################################################################
##### CONTARE VOCALI IN UNA STRINGA #########################################
#############################################################################

stringa="hello world"
count_vocali=0
#per contare ho bisogno di un contatore
for carattere in stringa:
    print(carattere)
    if(carattere=="a" or carattere=="e" or carattere=="i" or carattere=="o" or carattere=="u"):
        count_vocali=count_vocali+1

print("Numero delle vocali:",count_vocali)

#questo codice non è ottimo provaimo con due for annidati

#############################################################################
#############################################################################

stringa="hello world"
vocali="aeiou"
count_vocali=0

for carattere in stringa:
    for vocale in vocali:
        if(carattere==vocale):
            count_vocali=count_vocali+1

print("Numero delle vocali:",count_vocali)

#potremi migliorare ancora un po' l'efficienza di questo codice fermando il ciclo una volta trovata la vocale
#per esempio in hello world una volta trovata la e continua a fare le iterazioni
#questa cosa è possibile vederla in Debug una volta trovata la vocale e l'algoritmo continua a iterare su volcali
#questa cosa è inutile e può essere risolta spezzando il ciclo con il break

#############################################################################
#############################################################################

stringa="hello world"
vocali="aeiou"
count_vocali=0

for carattere in stringa:
    for vocale in vocali:
        if(carattere==vocale):
            count_vocali=count_vocali+1
            break #riduce le iterazioni

print("Numero delle vocali:",count_vocali)


###########################################################################
########### CONTEGGIO ITERAZIONI ##########################################
###########################################################################

#andiamo a contare le iteraioni aggiungendo un contatore per le vocali

stringa="hello world"
vocali="aeiou"
count_vocali=0
iterations=0

for carattere in stringa:
    for vocale in vocali:
        iterations+=1 #ci entrerò il numero di volte della lunghezza della stringa moltiplicato per le vocali (5)
        if(carattere==vocale):
            count_vocali+=1

print("N° iterazioni:", iterations,"\nN° vocali:", count_vocali)


#possibilità di utilizzare notazione compatta per esprimente operazione di incremento, decremento, moltiplicazione o divisione
#notazione compatta

# iterations += 1  ==>  iterations = iterations + 1
# iterations -= 1  ==>  iterations = iterations - 1
# iterations *= 2  ==>  iterations = iterations * 2
# iterations /= 2  ==>  iterations = iterations / 2