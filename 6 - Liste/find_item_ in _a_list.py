##
# cercare un elemento all'inteno di una lista
##
# Creare una funzione che partendo dalla lista e da un elemento ritorni la posizione nella lista
# Ritorna -1 in caso di elemento non trovato

def look_into_list(list_data, key): # Chiave per poter accedere all'elemento desiderato
    for i in range(len(list_data)): # Con for i possiamo pensare di tornare indietro e contiene già il valore dell'indice all'interno
        if(key == list_data[i]):
            return i
    return -1 # Faccio return quando sono uscito dal for e non ho un match
    
def main():
    lenght_list = int(input("Inserisci la lunghezza della lista:"))
    list_data = []
    for i in range(lenght_list):
        list_data.append(int(input("Inserisci l'elemento:")))
        print(i+1)

    key = int((input("Inserisci una chiave:")))
    print("il valore è:",look_into_list(list_data, key))

main()


##
# Data una lista e una chiave creare una funzione che consenta di ritornare la posizione 
# della prima occorrenza, il numero di occorrenze della chiave nel caso di non matching ritorniamo (-1,0)

def look_into_list_and_count(list_data, key):
    count = 0
    posizione = -1
    for i in range(len(list_data)):
        if(key == list_data[i]):
           count += 1
           if(count == 1):
               posizione = i
    return (posizione, count)

value = [0, 0, 2, 3, 4, -1, 4, 5]
risultato = look_into_list_and_count(value, 4)
print("Posizione e Chiave:",risultato)
