import unittest
import numpy as np
from funcs.loadData import load_data  
from PIL import Image
import os

class TestLoadData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a dummy image for testing
        cls.test_img_path = "test_image.png"
        img = Image.new("RGB", (10, 10), "red")
        img.save(cls.test_img_path)

    @classmethod
    def tearDownClass(cls):
        # Clean up: remove the created test image
        os.remove(cls.test_img_path)

    def test_load_data_with_path(self):
        # Test loading data with a given path
        im = load_data(self.test_img_path)
        self.assertIsNotNone(im)
        self.assertEqual(im.shape, (10, 10, 3, 1))  # Adjusted expected shape

    

if __name__ == '__main__':
    unittest.main()
