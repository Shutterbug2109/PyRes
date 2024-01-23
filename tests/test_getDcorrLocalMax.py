import unittest
import numpy as np
from funcs.getDcorrLocalMax import getDcorrLocalMax  # Replace 'your_module' with the actual module name where getDcorrLocalMax is defined

class TestGetDcorrLocalMax(unittest.TestCase):

    def test_single_element(self):
        d = np.array([1])
        ind, A = getDcorrLocalMax(d)
        self.assertEqual(ind, 0)
        self.assertEqual(A, 1)

    def test_maximum_at_beginning(self):
        d = np.array([0.4, 0.3, 0.2, 0.1])
        ind, A = getDcorrLocalMax(d)
        self.assertEqual(ind, 0)
        self.assertEqual(A, 0.4)


    def test_all_identical_elements(self):
        d = np.array([0.2, 0.2, 0.2, 0.2])
        ind, A = getDcorrLocalMax(d)
        self.assertEqual(ind, 0)
        self.assertEqual(A, 0.2)

    def test_empty_array(self):
        d = np.array([])
        with self.assertRaises(IndexError):
            getDcorrLocalMax(d)

if __name__ == '__main__':
    unittest.main()
