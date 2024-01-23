import unittest
import numpy as np
from funcs.getRadAvg import getRadAvg  

class TestGetRadAvg(unittest.TestCase):


    def test_invalid_input(self):
        # Test with an invalid (non-2D) input
        im = np.random.rand(10, 10, 3)
        with self.assertRaises(ValueError):
            getRadAvg(im)

if __name__ == '__main__':
    unittest.main()
