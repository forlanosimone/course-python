#metodo babilonese => metodo per l'identificazione della soluzione della radice quadrata (soluzione ricorsiva)

#utilizziamo un ciclo while perché non sappiamo il numero di cicli da effettura
#il criterio di arresto dell'algoritmo è dato dalla valutazione di un errore epsiolon
#vado a definire un epsilon valutano la differenza tra valore iniziale e valore calcolato
#differenza in modulo di |x_new e x_old| se è minore di una certa tolleranza allora abbiamo avuto il numero con la tolleranza richiesta
#while(abs(xn-xnl)<e(epsilon)) => stop (esco dal while)

# 1° passo chido input all'utente possiamo scrivere alpha per mantenere una notaizone matematica altrimenti utilizziamo la variabile a
# 2° passo verifichiamo che il numero sia positivo alpha>0
# 3° passo inizializzo le variabili per l'algoritmo
# 4° passo algoritmo => x_new=0.5*(x_old+alpha/x_old)

import sys #importo libreria di sistema per il massimo dell'errore

while(True): #possiamo chiedere in modo iterativo all'utente di inserire un numero positivo
    alpha = float(input("Inserisci il numero per il quale calcolare la radice quadrata:")) #chiedo input all'utente metto il float altrimenti è una stringa
    #metto un if iniziale per controllare che il numero sia > di zero
    if (alpha>0):
        break #il break interrompe il ciclo mentre exit esce dal programma
    else:
        print("inserisci un numero positivo")

#questo ciclo while può essere fatto anche con una Bool Statement
# isNegative=True
# while(isNegative):
#     alpha = float(input("inserisci il numero per il quale calcolare la radice quadrata"))
#     if(alpha>0):
#         isNegative=False #lavorare con isPositive era poco intuitivo per questo utilizziamo isPositive
#     else:
#         print("inserisci un numero positivo")


#inizializziamo le variabili
x_new=0.0 #valore attuale
x_old=alpha #valore precedente, lo mettiamo uguale ad alpha (può essere anche alpha/0.5)
n=1
N_ITER_MAX=30 #inizializziamo il valore arbitrario delle iterazione
epsilon=1e-3 #errore obiettivo (0,001)
err=sys.float_info.max #errore inizile => valore massimo codificabile tramite il float presente in Python
#err=abs(x_new-x_old) #come errore inizile posso usare anche questo

#il numero di iterazioni non è dicibili anicipatamente per questo usiamo il while e non il for
while(err>epsilon and n<N_ITER_MAX): #fino a quando l'errore è maggiore di epsilon il while viene ripetuto, con and aggiungo un critetrio sul numero di iterazioni (se ci sto mettendo troppo mi fermo) 
    #and blocca quando almeno una delle 2 è verificata mentre con or continui con l'algoritmo
    x_new=0.5*(x_old+alpha/x_old) #(*0.5) o (*1/2) o (/2.0) è diverso, mettendo 1/2 è presa come divisione intera e non va molto bene (perché alcuni numeri possono non avere una rappresentazione esatta in una determinata base)
    err=abs(x_new-x_old) #calculate error (formula per calcolare l'errore) l'err lo calcolo con i valori attuali (dopo algoritmo x_new...), se lo faccio prima introduco un ritardo
    x_old=x_new #il valore nuovo dipende dal valore precedente (andiamo ad aggiornare x_old)
    n=n+1 #incremetno il numero di iterazioni
    print("iterazione numero:", n,"e il valore è:", x_new) #stampo iterazioni e valori
    
    #questo if lo abbiamo messo nella condizione del while con l'and
    #if(n>N_ITER_MAX): #se n è maggiore uscaimo dal ciclo
        #break #fermo il ciclo

print("Il risultato è", x_new) #stampo iterazione e valore

#Nel caso di Run and Debug sulla sinistra nella finestra di WATCH possiamo inserire espressioni che non modificano il codice
#inserendo opportune espressioni possiamo fare delle considerazioni guardando l'evoluzione del programma

#più il numero è grande e più iterazioni serivranno per la convergenza dell'algoritmo
