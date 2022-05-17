##
# Metodo babilonese 
# Metodo per l'identificazione della soluzione della radice quadrata (soluzione ricorsiva)
'''
Utilizziamo un ciclo while perché non sappiamo il numero di cicli da effettuare
il criterio di arresto dell'algoritmo è dato dalla valutazione di un errore epsiolon.

Vado a definire un epsilon valutano la differenza tra valore iniziale e il valore calcolato
differenza in modulo di |x_new e x_old| se è minore di una certa tolleranza allora abbiamo 
avuto il numero con la tolleranza richiesta

while(abs(xn-xnl) < e(epsilon)) => stop (esco dal while)

1° passo 
Chido input all'utente possiamo scrivere alpha per mantenere una notaizone matematica altrimenti utilizziamo la variabile a
2° passo 
Verifichiamo che il numero sia positivo alpha>0
3° passo 
Inizializzo le variabili per l'algoritmo
4° passo 
Algoritmo => x_new = 0.5 * (x_old + alpha / x_old)

'''
import sys # Importo libreria di sistema per il massimo dell'errore

while(True): # Possiamo chiedere in modo iterativo all'utente di inserire un numero positivo
    alpha = float(input("Inserisci il numero per il quale calcolare la radice quadrata:")) 
    # Chiedo input all'utente e metto il float altrimenti è una stringa
    # Metto un if iniziale per controllare che il numero sia > di zero

    if (alpha > 0):
        break # Il break interrompe il ciclo mentre exit esce dal programma
    else:
        print("inserisci un numero positivo")

# Questo ciclo while può essere fatto anche con una Bool Statement
'''
isNegative = True
while(isNegative):
    alpha = float(input("inserisci il numero per il quale calcolare la radice quadrata"))
    if(alpha>0):
        isNegative=False #lavorare con isPositive era poco intuitivo per questo utilizziamo isPositive
    else:
        print("inserisci un numero positivo")
'''

# Inizializziamo le variabili
x_new = 0.0 # Valore attuale
x_old = alpha # Valore precedente, lo mettiamo uguale ad alpha (può essere anche alpha/0.5)
n = 1
N_ITER_MAX = 30 # Inizializziamo il valore arbitrario delle iterazione
epsilon = 1e-3 # Errore obiettivo (0,001)
err = sys.float_info.max # Errore inizile => valore massimo codificabile tramite il float presente in Python
#err = abs(x_new - x_old) # Come errore inizile posso usare anche questo

# Il numero di iterazioni non è dicibili anicipatamente per questo usiamo il while e non il for
while(err > epsilon and n < N_ITER_MAX): 
    # Fino a quando l'errore è maggiore di epsilon il while viene ripetuto, con and aggiungo un critetrio sul numero di iterazioni (se ci sto mettendo troppo mi fermo) 
    # and blocca quando almeno una delle 2 è verificata mentre con or continui con l'algoritmo
    x_new = 0.5*(x_old + alpha / x_old) 
    # (0.5) o (1/2) o (/2.0) è diverso
    # mettendo 1/2 è presa come divisione intera e non va molto bene (perché alcuni numeri possono non avere una rappresentazione esatta in una determinata base)
    
    err = abs(x_new - x_old) # Calcolo errore, lo calcolo con i valori attuali (dopo algoritmo x_new...), se lo faccio prima introduco un ritardo
    x_old = x_new # Il valore nuovo dipende dal valore precedente (andiamo ad aggiornare x_old)
    n = n+1 # Incremetno il numero di iterazioni
    print("iterazione numero:", n,"e il valore è:", x_new) # Stampo iterazioni e valori
    
    # Questo if lo abbiamo messo nella condizione del while con l'and
    #if(n>N_ITER_MAX): # Se n è maggiore usciamo dal ciclo
        #break # Fermo il ciclo

print("Il risultato è", x_new) # Stampo iterazione e valore

# Nel caso di Run and Debug sulla sinistra nella finestra di WATCH possiamo inserire espressioni che non modificano il codice
# Inserendo opportune espressioni possiamo fare delle considerazioni guardando l'evoluzione del programma
# Più il numero è grande e più iterazioni serivranno per la convergenza dell'algoritmo
