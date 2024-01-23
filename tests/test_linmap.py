import unittest
import numpy as np
from funcs.linmap import linmap  

class TestLinmap(unittest.TestCase):

    def test_basic_functionality(self):
        # Basic functionality test
        val = np.array([0, 128, 255])
        rsc = linmap(val, 0, 255, 0, 1)
        expected = np.array([0, 0.50196078, 1])
        np.testing.assert_array_almost_equal(rsc, expected, decimal=5)


    def test_boundary_values(self):
        # Test with boundary values
        val = np.array([10, 20, 30])
        rsc = linmap(val, 10, 30, 0, 1)
        expected = np.array([0, 0.5, 1])
        np.testing.assert_array_almost_equal(rsc, expected, decimal=5)

    def test_out_of_range_values(self):
        # Test with out-of-range values
        val = np.array([-10, 10, 100])
        rsc = linmap(val, 0, 50, 0, 1)
        expected = np.array([0, 0.2, 1])  # Clamped values at 0 and 1
        np.testing.assert_array_almost_equal(rsc, expected, decimal=5)

    def test_empty_input(self):
        # Test with an empty array
        val = np.array([])
        rsc = linmap(val, 0, 255, 0, 1)
        expected = np.array([])
        np.testing.assert_array_equal(rsc, expected)

if __name__ == '__main__':
    unittest.main()
