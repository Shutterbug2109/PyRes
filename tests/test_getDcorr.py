import unittest
import numpy as np
from funcs.getDcorr import getDcorr  # Replace 'your_module' with the actual module name where getDcorr is defined

class TestGetDcorr(unittest.TestCase):

    def test_predefined_image(self):
        # Test with a predefined image
        im = np.random.rand(100, 100)
        r = np.linspace(0, 1, 50)
        Ng = 10
        kcMax, A0, d0, d = getDcorr(im, r, Ng)
        
        self.assertIsInstance(kcMax, float)
        self.assertIsInstance(A0, float)
        self.assertIsInstance(d0, np.ndarray)
        self.assertIsInstance(d, np.ndarray)
        self.assertEqual(d0.shape, (len(r),))
        self.assertEqual(d.shape, (len(r), 2 * Ng + 1))

    def test_non_square_image(self):
        # Test with a non-square image
        im = np.random.rand(80, 100)
        kcMax, A0, d0, d = getDcorr(im)
        self.assertIsInstance(kcMax, float)
        self.assertIsInstance(A0, float)

    def test_varying_r_and_Ng(self):
        # Test with varying 'r' and 'Ng'
        im = np.random.rand(100, 100)
        r = np.linspace(0, 0.5, 30)
        Ng = 5
        kcMax, A0, d0, d = getDcorr(im, r, Ng)
        self.assertEqual(d0.shape, (len(r),))
        self.assertEqual(d.shape, (len(r), 2 * Ng + 1))

if __name__ == '__main__':
    unittest.main()
