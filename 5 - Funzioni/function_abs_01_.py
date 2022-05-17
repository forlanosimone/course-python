## 
# Calcolo il valore assoluto di un float
# @param x valore da valutare
# @return valore assoluto di x

def abs_f(x): # abs_f nome univoco altrimenti abs crea ambiguità
    if(x >= 0):
        return x
    else:
        return -x

# Le varibili all'interno della funzione sono locali e non globali (vedere Debug)

def main():
    numero = float(input("inserisci un numero...")) # Cast da str a float
    print("il valore assoluto è:", abs_f(numero))

main() # In questo modo invoco la funzione
# La funzione main() ha lo scopo di essere il primo punto in ingresso nel momento in cui ho avviato il mio programma

'''
Nel Debug c'è il call stack (stack=impilare)
Lo stack è una tipologia di struttura dati che ha un criterio particolare (LIFO)
struttura a coda => logica di tipo FIFO (First In First Out)
gli elemnti si accodano e il primo inserito è il primo ad uscire

La logica di gestione dello stack è di tipo LIFO => Last In First Out
In una pila non possiamo tolgiere la base ma si tologno pirma quelli sopra

Stack overflow error => sono state attivate troppe funzioni e non entrano più nella pila
Lo stack è qualcosa che cresce e diminusice in base al numero di funzione che nello stesso istante temporale sono attive
'''