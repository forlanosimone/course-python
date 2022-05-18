##
# Test della classe persona in persona.py
# Andiamo a testare se il cognome è =?
# Se il metodo genera un'eccezione con un oggetto senza variabili
# Se il metodo calcola_cf è uguale al CF

import unittest
from persona import persona

class test_persona(unittest.TestCase): # Con questa classe andiamo a testare la classe persona
    
    def setUp(self): # Metodo che già esiste e serve per creare un oggetto di esempio
        self.persona = persona("simone") # self.persona è un oggetto di test con solo il nome
        self.persona_full_data = persona("simone","forlano","27-04-1997","M","guardiagrele")

    def test_empty_fields(self): # Testiamo che il cognome di una persona vuota sia = al ?
        self.assertEqual(self.persona.get_cognome(),"?","Init error...")
        with self.assertRaises(ValueError): # Testiamo se solleva un'eccezione
            self.persona.calcola_cf() # Se ci sono campi vuoti si sollva un ValueError
    
    def test_full_data(self):           
        self.persona_full_data.calcola_cf()
        self.assertEqual(self.persona_full_data.get_cf(), "FRLSMN97D27E243B", "CF error")

if __name__ == '__main__':
    unittest.main()

# Il test funziona e plotta OK perché non posso calcolare il CF senza avere gli attributi
# Mentre se testo persona_full_data confronto se il CF calcolato sia uguale a quello di test
