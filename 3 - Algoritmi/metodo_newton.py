##
# Trovare gli zeri della funzione risolve l'equazione f(x)=0
'''
Definito un intervallo, il programma calcola, attraverso il metodo di
Newton - Raphson, uno zero della funzione.
'''

import sys

# Definisco la funzione f di cui voglio conoscere lo zero in [a, b]
def f(x):
    return 4 * x**4 - 1.5 * x**3 + 6.0 * x**2 - 2.0 * x 
# Definisco la sua derivata df
# Python ha delle librerie di calcolo simbolico per eseguire le derivate
def df(x):        
    return 16 * x**3 - 4.5 * x**2 + 12.0 * x - 2.0 

def metodoNewtonRaphson(a, b, epsilon, N_ITER_MAX):
    # Chiedo input all'utente l'intervallo di ricerca dello zero
    #a = float(input("Inserire estremo sx intervallo: "))
    #b = float(input("Inserire estremo dx intervallo: "))

    # Inizializzo le variabili
    x_old = (a + b) / 2 #Prendo come inizio il valore medio tra gli estremi dell'intervallo
    x_new = 0.0

    # epsilon = float(input("Inserire epsilon, errore minimo: "))          
    
    n = 1 # Numero di iterazioni
    #N_ITER_MAX = int(input("Quante iterazioni devo fare al massimo:"))
    
    # Numero di iterazioni massime 
    err = sys.float_info.max # Definisco l'errore

    while(err > epsilon and n < N_ITER_MAX): # Finchè l'errore è maggiore di epsilon
        # E finchè il numero di iterazioni non è troppo elevato
        # Calcolo la nuova x_new
        x_new = x_old - (f(x_old) / df(x_old))
        
        err = abs(x_new - x_old) # Calcolo errore
        x_old = x_new                               
        # Al prossimo giro la nuova x di partenza sarà quella calcolata giro precedente
        n += 1 # Segno iterazione
        print(n, x_new)

    if x_new > a and x_new < b:
        print("Lo zero della funzione nell'intervallo [a, b] è: ", x_new)
    else:
        print("Lo zero della funzione non appartiene all'intervallo ed è: ", x_new)

# argv è una lista con gli argomenti che passo tramite riga di comando

#argv[1] --> a
#argv[2] --> b
#argv[3] --> epsilon
#argv[4] --> n_iter

if (len(sys.argv) == 5):
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        epsilon = float(sys.argv[3])
        n_iter = int(sys.argv[4])
        
        # Eccezioni
        if (epsilon <= 0):
            raise ValueError("Il valore di epsilon deve essere maggiore di zero")
        if (n_iter <= 0):
            raise ValueError("Il valore di n_iter deve essere maggiore di zero")
        metodoNewtonRaphson(a, b, epsilon, n_iter)
    except ValueError as err:
        print("eccezione di tipo value error...", str(err))
    except Exception as err:
        print("eccezione generica...", str(err)) 
else:
    print("Parametri non validi")
    print("Si usa facendo: metodoNewtonRaphson.py a b epsilon N_ITER_MAX")
