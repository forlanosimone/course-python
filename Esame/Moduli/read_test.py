##
# Testo che...

import unittest
from read import read_img

class test_read (unittest.TestCase):
    def test_read_img(self):
        PATH_IMG = ".\\Esame\\immagini\\hello"
        with self.assertRaises(ValueError):
            img = read_img(PATH_IMG, "hello")


if __name__ == "__main__":
    unittest.main()