##
# Andiamo a costruire la classe persona

from codicefiscale import codicefiscale

class persona:
    _id = 1000000 # _ mi indica che è una variabile privata
    def __init__(self, nome = "", cognome = "?", data_nascita = "?", sesso = "?", luogo_nascita= "?"):      # Definisco il costruttore e alcuni attributi default
        persona._id += 1 # Viene incrementato ogni volta che creo un oggetto
        self._id = "S" + str(persona._id) # Matricolo con S
        self.nome = nome                  # Variabili di istanza
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.sesso = sesso
        self.luogo_nascita = luogo_nascita
        self.cf = " "

    def get_nome(self):
        return self.nome
    def get_cognome(self):
        return self.cognome
    def get_sesso(self):
        return self.sesso
    def get_id(self):
        return self._id
    def set_nome(self, nome):   # Il nome del parametro "nome" deve riflettere il nome del parametro di istanza
        self.nome = nome        # Scrivendo self.nome mi riferisco alla variabile di instanza
    def set_cognome(self, cognome):
        self.cognome = cognome
    def get_cognome_nome(self, reverse = False):
        if(reverse == False):                           # Se reverse = false
            return (self.cognome + "|" + self.nome)     # Se voglio ritornare cognome | nome con una funzione
        else:
            return (self.nome + "|" + self.cognome)     # Se reverse = true
    def calcola_cf(self):
        self.cf = codicefiscale.encode(surname = self.cognome, name = self.nome, sex = self.sesso, birthdate = self.data_nascita, birthplace = self.luogo_nascita)
    def get_cf(self):
        return self.cf
    # Overloading, quando uso == richiamo la funzione __eq__
    def __eq__(self, rhsValue): # Se (self, me stesso._id) è uguale all'altro terimne di paragone._id ritorna True
        return(self._id == rhsValue._id)

# Abbiamo create dei metodi che possono essere usati esternamente con la classe persona

# Subclass
class studente(persona): # Gli altri metodi li prendo dalla classe persona
    def __init__(self, anno_iscrizione):
        super().__init__() # Chiamo il costruttore della super classe persona per inizializzare le variabili
        self._anno_iscrizione = anno_iscrizione

# Subclass
class studente_Triennale(studente): # Dai genitori ereditiamo gli altri metodi
    def __init__(self):
        super().__init__() # Chiamo il costruttore della classe studente
        self.tipo = "Triennale"

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

# Esempio Subclass
from Classi.persona import studente
from Classi.persona import persona
s = studente("2020") # è richiesto l'anno di iscrizione
s.

'''
