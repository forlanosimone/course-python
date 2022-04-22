##
# cerca una stringa nella lista

friends = ["Bob", "Martino", "Topo", "Laika"]
n = friends.index(input())

print(n)

##
# se voglio fare la stessa cose senza usare index
# data una lista ed una parola chiave di ricerca
# ritornare la sua posizione
# ritornare -1 se non trovato

#1st method
def index_custom(list_data, word):

    for i in range(len(list_data)):
        if(list_data[i] == word):
            return i
    return -1

n = index_custom(friends, "Bob")
print(n)

#2st method
# def index_custom(list_data, word):
#     i=0
#     for item in list_data:
#         if(item == word):
#             return i
#         i+=1
#     return -1

# n = index_custom(friends, "Bob")
# print(n)