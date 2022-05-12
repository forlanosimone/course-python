##
# Andiamo a costruire la classe persona

from numpy import False_


class persona:

    # Variabili di instanza
    nome = ""
    cognome = ""

    def get_nome(self):
        return self.nome
    def get_cognome(self):
        return self.cognome
    def set_nome(self, nome): # Il nome del parametro "nome" deve riflettere il nome del parametro di instanza
        self.nome = nome # Scrivendo self.nome mi riferisco alla variabile di instanza
    def set_cognome(self, cognome):
        self.cognome = cognome
    def get_cognome_nome(self, reverse = False):
        if(reverse == False): # Se reverse = false
            return (self.cognome + "|" + self.nome) # Se voglio ritornare cognome | nome con una funzione
        else:
            return (self.nome + "|" + self.cognome) # Se reverse = true

# Abbiamo create dei metodi che possono essere usati esternamente con la classe persona

'''
# Da terminale
from Classi.persona import persona

p = persona()
p.get_nome()

p.set_nome("simone")
p-get_nome()
'''
