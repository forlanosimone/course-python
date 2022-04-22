## Calcolo il valore assoluto du un float
# @param x valore da valutare
# @return valore assoluto di x

def abs_f(x): 
    if(x>=0):
        return x
    else:
        return -x

#se ho un messaggio vuoto viene verificata la condizione dell'if
#così le istruzioni in log_message non vengno eseguite perchè c'è il return che ci fa uscire
def log_message(messaggio):
    if(messaggio==""): #se la messaggio è vuoto la riga 16/17/18 non verranno esegiute
        return #return interrompe la funzione e ci fa tornare dal chimante
    print("-------------------")
    print(messaggio)
    print("-------------------")

def main(): #funzione chiamante
    log_message(abs_f(float(input("inserisci un numero..."))))
    log_message("") #messaggio vuoto

main()