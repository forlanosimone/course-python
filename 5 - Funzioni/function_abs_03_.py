## 
# Calcolo il valore assoluto di un float
# @param x valore da valutare
# @return valore assoluto di x

def abs_f(x): 
    if(x >= 0):
        return x
    else:
        return -x

# Se ho un messaggio vuoto viene verificata la condizione dell'if
# Così le istruzioni in log_message non vengno eseguite perchè c'è il return che ci fa uscire

def log_message(messaggio):
    if(messaggio == ""):
        return # return interrompe la funzione e ci fa tornare dal chimante
    print("-------------------")
    print(messaggio)
    print("-------------------")

def main(): # Funzione chiamante
    log_message(abs_f(float(input("inserisci un numero..."))))
    log_message("") # Messaggio vuoto

main()