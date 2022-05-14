##
# Test della classe persona in persona.py

import unittest
from persona import persona

class test_persona(unittest.TestCase): # Con questa classe andiamo a testare la classe persona
    
    def setUp(self): # Metodo che già esiste e serve per creare un oggetto di esempio
        self.persona = persona() # self.persona è un oggetto di test
    
    def test_empty_fields(self): # Testiamo che il cognome di una persona vuota sia = a ?
        self.assertEqual(self.persona.get_cognome(),"?","Init error...")
        with self.assertRaises(ValueError): # Testiamo se solleva un'eccezione
            self.persona.calcola_cf() # Se ci sono campi vuoi si sollva un ValueError

if __name__ == '__main__':
    unittest.main()
