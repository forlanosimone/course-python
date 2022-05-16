#calcolare lo zero di una funzione

def f(x): #definisco la funzione
    a=input("scrivi il valore di a:")
    b=input("scrivi il valore di b:")
    epsilon=input("inserisci soglia di arresto:")
    iterations=int(input("definisci il numero di iterazioni:"))

def df(x): #definisco la derivata della fuzione
    #python ha delle librerie di calcolo simbolico per eseguire le derivate

def newton_raphson(a,b,epsilon,iterations):
    x_new=x_old-f(x_old)/df(x_old)
    