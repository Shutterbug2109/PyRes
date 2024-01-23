import unittest
from funcs.resolution import calculate_resolution  # Replace 'your_module' with the actual module name where calculate_resolution is defined

class TestCalculateResolution(unittest.TestCase):

    def test_regular_values(self):
        # Test with regular values
        kc = 2.0
        pixel_size = 1.5
        expected_resolution = (2 * pixel_size) / kc * 1000  # in nano meters
        self.assertAlmostEqual(calculate_resolution(kc, pixel_size), expected_resolution)

    def test_zero_kc(self):
        # Test with kc equal to zero
        kc = 0
        pixel_size = 1.5
        with self.assertRaises(ZeroDivisionError):
            calculate_resolution(kc, pixel_size)

    def test_negative_values(self):
        # Test with negative values
        kc = -2.0
        pixel_size = 1.5
        expected_resolution = (2 * pixel_size) / kc * 1000  # in nano meters
        self.assertAlmostEqual(calculate_resolution(kc, pixel_size), expected_resolution)

    def test_large_values(self):
        # Test with large values
        kc = 1e6
        pixel_size = 1e3
        expected_resolution = (2 * pixel_size) / kc * 1000  # in nano meters
        self.assertAlmostEqual(calculate_resolution(kc, pixel_size), expected_resolution)

    def test_small_values(self):
        # Test with very small values
        kc = 1e-6
        pixel_size = 1e-3
        expected_resolution = (2 * pixel_size) / kc * 1000  # in nano meters
        self.assertAlmostEqual(calculate_resolution(kc, pixel_size), expected_resolution)

if __name__ == '__main__':
    unittest.main()
