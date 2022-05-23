##
# Test della classe point in point.py
# Andiamo a testare se ...
# Se il metodo genera un'eccezione con un oggetto senza variabili
# Se il metodo ... è uguale a ...

import unittest
from point import point

# Con questa classe andiamo a testare la classe point
class test_point(unittest.TestCase):

    def setUp(self): # Metodo che già esiste e serve per creare un oggetto di esempio
        self.point = point(20,30,40,50) # self.point è un oggetto di test con solo il nome
        self.point_full_data = point(20,30,40,50)

    def test_empty_fields(self): # Testiamo che start_y sia = 20
        self.assertEqual(self.point.start_y,20,"Init error...")
        #with self.assertRaises(ValueError): # Testiamo se solleva un'eccezione
            #self.point() # Se ci sono campi vuoti si sollva un ValueError

if __name__ == '__main__':
    unittest.main()
