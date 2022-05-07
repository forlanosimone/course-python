##
# In numpy gli operatori si comportano normalmente come in Mathlab mentre nelle liste è diverso

# LISTE
print("Liste")
a_list = [1,2,3]
b_list = [1,2,3]
c_list = a_list + b_list # Nelle liste l'operatore somma è un operatore di append
print(c_list)

# Moltiplicazione di liste -> Concatenzaione
print(a_list*4)

# ARRAY NUMPY, possiamo manipolare facilmento gli array
print("Libreria NumPy")
import numpy as np # Al posto di np posso scrivere tutto (np - acronimo di numpy)

a = np.arange(3)
b = np.arange(3)
print(a)
print(a[1]) # Possimao accedere agli elementi come nelle liste
print(type(a))

c = a + b # Con Numpy possiamo fare le somme come su MathLab
print(c)

# Moltiplicazione
print(a*4)

a = [1,2,3] # Lista
print(type(a))

a = np.array([1,2,3]) # Array NumPy
# a = np.array(1,2,3) # SBAGLIATO
print(type(a))

print(a.dtype) # Andiamo a controllare il tipo  

# NumPy può gestire anche i numeri complessi

