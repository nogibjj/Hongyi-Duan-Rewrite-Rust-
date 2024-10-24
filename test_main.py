import unittest
from main import get_mean, get_median, get_std
import numpy as np

class TestStatisticsFunctions(unittest.TestCase):
    
    def setUp(self):
        self.x = [i for i in range(1, 1000000)]
    
    def test_mean(self):
        self.assertAlmostEqual(get_mean(self.x), np.mean(self.x), places=5)
    
    def test_median(self):
        self.assertAlmostEqual(get_median(self.x), np.median(self.x), places=5)
    
    def test_std(self):
        self.assertAlmostEqual(get_std(self.x), np.std(self.x, ddof=1), places=5)

if __name__ == "__main__":
    unittest.main()

