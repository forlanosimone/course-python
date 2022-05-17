##
# Andiamo a vedere se value dopo la radice quadrata è uguale a value_restored

import math

value = 2.0
r = math.sqrt(value)
value_restored = r * r

# Vado a calcolare la differenza tra value e value_restored
delta = math.fabs(value - value_restored) # math.fabs serve per fare il valore assoluto di numeri float
# Serve il valore assoluto perché il delta potrebbe essere sia negativo che positivo

if(delta < 1e-3):
    print("sono uguali")
else:
    print("sono diversi")


# Se voglio mantenere il valore di delta perché mi servirà dopo
value = 2.0
r=math.sqrt(value)
value_restored = r * r

delta = value - value_restored

if(math.fabs(delta) < 1e-3): # In questo modo faccio il valore assoluto del delta nell'if
    print("sono uguali")
else:
    print("sono diversi")