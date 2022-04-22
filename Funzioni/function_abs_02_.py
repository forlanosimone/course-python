## Calcolo il valore assoluto du un float
# @param x valore da valutare
# @return valore assoluto di x

def abs_f(x): #abs_f nome univoco altrimenti abs crea ambiguità
    if(x>=0):
        return x
    else:
        return -x

#posso utilizzare una funzione con valore di ritorno nullo per formattare il testo in un certo modo
def log_message(messaggio):
    print("-------------------")
    print(messaggio)
    print("-------------------")

#print(log_message(abs_f(float(input("inserisci un numero...")))))

def main():
    log_message(abs_f(float(input("inserisci un numero..."))))
    log_message("ciao")

main()
#la funzione main() ha lo scopo di essere il primo punto in ingresso nel momento in cui ho avviato il mio programma