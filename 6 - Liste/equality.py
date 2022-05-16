##
# You can use the == operator to compare whether two lists have the same elements, in the same order.
# date due liste verificare se sono uguali
# ritorna True se uguali (stessi elementi nella stessa posizione)
# else ritorna False
# Questa è una funzione che evita l'utilizzo dell'operatore ==

def compare_list(list1, list2):
    #confrontare elemento per elemento, posso prima confrontare se hanno la stessa lunghezza
    if(len(list1) != len(list2)):
        return False # a priori faccio questo controllo
    # visto che le due liste hanno stessa dimensione itero sugli elementi
    # se tutti gli elementi sono uguali nel giusto ordine allora le liste sono uguali
    for i in range(len(list1)):
        if(list1[i] != list2[i]):
            return False
    return True
