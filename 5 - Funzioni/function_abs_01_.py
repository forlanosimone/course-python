## Calcolo il valore assoluto du un float
# @param x valore da valutare
# @return valore assoluto di x

def abs_f(x): #abs_f nome univoco altrimenti abs crea ambiguità
    if(x>=0):
        return x
    else:
        return -x

#le varibili all'interno della funzione sono locali e non globali (vedere Debug)
#se volgio fare il test

def main():
    numero=float(input("inserisci un numero...")) #cast da str a float
    print("il valore assoluto è:", abs_f(numero))

main() #in questo modo invoco la funzione

#la funzione main() ha lo scopo di essere il primo punto in ingresso nel momento in cui ho avviato il mio programma

#nel Debug c'è il call stack (stack=impilare)
#lo stack è una tipologia di struttura dati che ha un criterio particolare (LIFO)
#struttura a coda => logica di tipo FIFO
#FIFO=First In First Out, gli elemnti si accodano e il primo inserito è il primo ad uscire

#la logica di gestione dello stack è di tipo LIFO => Last In First Out
#in una pila non possiamo tolgiere la base ma si tologno pirma quelli sopra

#stack overflow error => sono state attivate troppe funzioni e non entrano più nella pila
#lo stack è qualcosa che cresce e diminusice in base al numero di funzione che nello stesso istante temporale sono attive