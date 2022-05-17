##
# Calocolare il minimo e il massimo della lista

valori = [2, 4, 5, -5, 3, 9]

print(max(valori))
print(min(valori))

max_value = valori[0] # Variabili di appoggio
min_value = valori[0]

for item in valori:
    if(item > max_value):
        max_value = item
    if(item < min_value): # Mettondo elif il primo e il secondo if sono staccati con if vengono fatti prima uno e poi l'altro
        min_value = item

print("Il massimo è:", max_value, "Il minimo è:", min_value)
