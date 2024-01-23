import unittest
import numpy as np
from funcs.im2pol import im2pol  # Replace 'your_module' with the actual module name where im2pol is defined

class TestIm2Pol(unittest.TestCase):


    def test_large_image_exception(self):
        # Test with an image larger than max_resolution
        imC = np.random.rand(2000, 2000)
        with self.assertRaises(ValueError):
            im2pol(imC)


    def test_empty_image(self):
        # Test with an empty image
        imC = np.array([])
        with self.assertRaises(IndexError):
            im2pol(imC)

if __name__ == '__main__':
    unittest.main()
