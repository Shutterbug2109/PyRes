import unittest
import numpy as np
from funcs.apodImRect import apodImRect  

class TestApodImRect(unittest.TestCase):

    def test_functionality(self):
        # Simple functionality test
        img = np.ones((10, 10))
        N = 2
        apodized_img, mask = apodImRect(img, N)
        self.assertEqual(apodized_img.shape, img.shape)
        self.assertEqual(mask.shape, img.shape)
        self.assertTrue(np.all(apodized_img <= 1))

    def test_input_types(self):
        # Test with 3D array with singleton dimension
        img = np.ones((10, 10, 1))
        N = 2
        apodized_img, mask = apodImRect(img, N)
        self.assertEqual(apodized_img.shape, (10, 10))
        self.assertEqual(mask.shape, (10, 10))


    def test_output_verification(self):
        img = np.ones((10, 10))
        N = 2
        apodized_img, mask = apodImRect(img, N)
        self.assertIsInstance(apodized_img, np.ndarray)
        self.assertIsInstance(mask, np.ndarray)


if __name__ == '__main__':
    unittest.main()
