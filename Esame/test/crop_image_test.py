##
#

import unittest
import cv2 as cv

class test_roi (unittest.Testcase):
    print("Voglio fare il test...")
    print("Inserisci le coordinate del punto Top Left e del punto Bottom Right per\
            la creazione del bouding box.")
    PATH_IMG = ".\\Esame\\immagini\\DSCF0336.jpg"
    img = cv.imread(PATH_IMG, cv.IMREAD_GRAYSCALE)

if __name__ == "__main__":
    unittest.main()
