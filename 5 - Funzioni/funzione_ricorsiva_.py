##
# Funzione che richiama se stessa all'interno
# Volglio calcoalre la molitiplicazione dei primi n numeri (fattoriale)

# Fattoriale con il for
n = int(input("inserisci il numero:"))
fattoriale = 1 # Valore che ci interessa => sarà il risultato dell'operazione
#fattoraile=n
#se inizializzo fattoriale=1 dovrei fare (i) crescenti se inizializzo fattoriale=n dovrei fare (i) decrescente
#se inizializzassi fattoraile=0 sarà sempre zero quindi la condizione di innesco è sbagliata

for i in range(1, n+1): # Attenzione alle condizioni di bordo
    #print(i) possiamo metterlo in WATCH
    fattoriale = fattoriale * i
print("il fattoriale è:", fattoriale)

'''
In questo modo il fattoriale è fatto sotto forma iterativa
Possiamo pensare di farlo sotto forma ricorsiva (richiamando una funzione)
Una funzione che chiamerà se stessa fino a quando non esce

Per ritornare il valore abbiamo bisogno di return n*fatt(n-1)
5*fatt(4)
4*fatt(3)
3*fatt(2)
2*fatt(1)
1*fatt(0)
0*fatt(n-1)

Se n=0 allora return 1 altrimenti return n*fatt(n-1)
'''

# Fattoriale sotto forma ricorsiva
x = int(input("inserisci il numero:"))

def fatt(x):
    if(x <= 0):
        return 1
    else:
        return x * fatt(x-1)

fattoriale_ricorsivo = fatt(x)
print("il fattoriale è:", fattoriale_ricorsivo)

'''
Proviamo a simulare il codice, in questo modo sarà più chiaro anche lo stack
Supponimao di iniziare con 5 => fatt(5)

fatt(0) ==> return 1
fatt(1) ==> return 1 * fatt(0)
fatt(2) ==> return 2 * fatt(1)
fatt(3) ==> return 3 * fatt(2)
fatt(4) ==> return 4 * fatt(3)
fatt(5) ==> return 5 * fatt(5-1) 

In questo caso n non è <=0 allora rintornerebbe x*fatt(x-1)

Parto da fatt(5) poi ho bisogno di fatt(4) ... e così via fino a fatt(0) ==> return 1
Vado ad impilare tutte le funzioni, per fattoriali molto grandi potrei andare in stack overflow

Troppe funzioni che si annidano possono portare all'errore di stack overflow
Questa cosa può essere osservata nel Debug in CALL STACK verranno impilate molte funzioni 
che saranno cancellate solo quando arriveremo al risultato

Molte volte una funzione ricorsiva può essere convertita in un for
Una funzione ricorsiva può incorrere in errori di stack overflow per numeri grandi
'''
