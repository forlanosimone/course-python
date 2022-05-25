##
# Testo che...

import unittest
import cv2 as cv
from crop_image import roi

class test_roi(unittest.TestCase): # Con questa classe andiamo a testare...
    def test_roi(self):
        PATH_IMG = ".\\Esame\\immagini\\DSCF0336.jpg"
        img = cv.imread(PATH_IMG, cv.IMREAD_GRAYSCALE)

        roi_img = roi(img)

        roi_img_test = img[800:1000 ,2000:2400]

        self.assertEqual(roi_img.all(), roi_img_test.all())

if __name__ == "__main__":
    unittest.main()
