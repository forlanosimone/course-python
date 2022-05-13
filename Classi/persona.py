##
# Andiamo a costruire la classe persona

class persona:
    _id = 1000000 # _ mi indica che è una variabile privata
    def __init__(self, cognome = "", sesso = "?"):      # Definisco il costruttore e alcuni attributi default
        persona._id += 1 # Viene incrementato ogni volta che creo un oggetto
        self._id = "S" + str(persona._id) # Matricolo con S
        self.nome = ""                                  # Variabili di instanza
        self.cognome = cognome
        self.data_nascita = ""
        self.sesso = sesso

    def get_nome(self):
        return self.nome
    def get_cognome(self):
        return self.cognome
    def get_sesso(self):
        return self.sesso
    def get_id(self):
        return self._id
    def set_nome(self, nome):   # Il nome del parametro "nome" deve riflettere il nome del parametro di instanza
        self.nome = nome        # Scrivendo self.nome mi riferisco alla variabile di instanza
    def set_cognome(self, cognome):
        self.cognome = cognome
    def get_cognome_nome(self, reverse = False):
        if(reverse == False):                           # Se reverse = false
            return (self.cognome + "|" + self.nome)     # Se voglio ritornare cognome | nome con una funzione
        else:
            return (self.nome + "|" + self.cognome)     # Se reverse = true

# Abbiamo create dei metodi che possono essere usati esternamente con la classe persona

'''
# Da terminale
from Classi.persona import persona

p = persona()
p.get_nome()

p.set_nome("simone")
p.get_nome()

# Altro esempio
p1 = persona(cognome = "Forlano") # Posso inserire direttamente dal costruttore senza seguire l'ordine
p1.get_cognome()

# Altro esempio
p2 = persona()
p2.get_sesso() # Posso inserire un valore di default dal costruttore

# Altro esempio
p3 = persona("Forlano","M") # Se non scrivo il tipo di attributo verrà seguito l'ordine nel costruttore
p3.get_cognome()

# Altro esempio, con conteggio degli oggetti
p1 = persona()
p1.get_id()
p2 = persona()
p2.get_id()
p3 = persona()
p3.get_id()

'''
