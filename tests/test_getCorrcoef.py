import unittest
import numpy as np
from funcs.getCorrcoef import getCorrcoef  # Replace 'your_module' with the actual module name where getCorrcoef is defined

class TestGetCorrcoef(unittest.TestCase):

    def test_correlation_with_constants(self):
        # Test correlation with provided normalization constants
        I1 = np.array([1+1j, 2+2j, 3+3j])
        I2 = np.array([2+1j, 3+2j, 4+3j])
        c1 = 5
        c2 = 10
        expected_cc = np.sum(np.real(I1 * np.conj(I2))) / (c1 * c2)
        expected_cc = np.floor(1000 * expected_cc) / 1000
        result = getCorrcoef(I1, I2, c1, c2)
        self.assertAlmostEqual(result, expected_cc)

    def test_correlation_without_constants(self):
        # Test correlation without provided normalization constants
        I1 = np.array([1+1j, 2+2j, 3+3j])
        I2 = np.array([2+1j, 3+2j, 4+3j])
        c1 = np.sqrt(np.sum(np.abs(I1)**2))
        c2 = np.sqrt(np.sum(np.abs(I2)**2))
        expected_cc = np.sum(np.real(I1 * np.conj(I2))) / (c1 * c2)
        expected_cc = np.floor(1000 * expected_cc) / 1000
        result = getCorrcoef(I1, I2)
        self.assertAlmostEqual(result, expected_cc)

    

if __name__ == '__main__':
    unittest.main()
