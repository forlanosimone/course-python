"Questo modulo di esempio per la somma"

# Queste funzioni vengono caricate sempre, sia con "import modulo" che con "modulo.py"
from unittest import result


def somma(a_value, b_vale):
    "Questa funzione calcola la somma"
    return a_value + b_vale

def differenza(a_vale, b_value):
    "Questa funzione calcola la differenza"
    return a_vale - b_value

# Importando questo modulo dal terminale e scrivendo modulo.__doc__ ci verrà fornita la doc-string
# Importando Numpy e scrivendo np.__version__ ritornerà la versione

if(__name__ == "__main__"):
    # Se sono qui è perché sono stato lanciato come un normale script python
    print("Sto eseguendo il codice che si trova dentro al modulo...")
    print("Voglio fare il test...")
    # Effettuo un test
    expected_value = 3 # Risultato atteso
    input_values = [1, 2] # Valori noti in ingresso
    result_from_function = somma(input_values[0], input_values[1]) # Valore restituito dalla funzione

    # Effettuo controllo...
    if(expected_value == result_from_function):
        print("test PASSED")
    else:
        print("test NOT PASSED", expected_value, " got ", result_from_function )
else:
    # Se sono qui è perché qualcuno mi ha importato
    print(__name__)
