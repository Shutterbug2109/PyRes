import unittest
import numpy as np
from funcs.clamp import clamp  

class TestClamp(unittest.TestCase):

    def test_clamp_with_min_and_max(self):
        # Test clamping with both minval and maxval
        val = np.array([1, 2, 3, 4, 5])
        minval = 2
        maxval = 4
        expected = np.array([2, 2, 3, 4, 4])
        result = clamp(val, minval, maxval)
        np.testing.assert_array_equal(result, expected)

    def test_clamp_with_no_min(self):
        # Test clamping with no minval
        val = np.array([1, 2, 3, 4, 5])
        maxval = 4
        expected = np.array([1, 2, 3, 4, 4])
        result = clamp(val, None, maxval)
        np.testing.assert_array_equal(result, expected)

    def test_clamp_with_no_max(self):
        # Test clamping with no maxval
        val = np.array([1, 2, 3, 4, 5])
        minval = 2
        expected = np.array([2, 2, 3, 4, 5])
        result = clamp(val, minval, None)
        np.testing.assert_array_equal(result, expected)


    def test_clamp_with_empty_array(self):
        # Test clamping with an empty array
        val = np.array([])
        minval = 2
        maxval = 4
        expected = np.array([])
        result = clamp(val, minval, maxval)
        np.testing.assert_array_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
