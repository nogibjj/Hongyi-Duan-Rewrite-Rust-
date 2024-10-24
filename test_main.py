from main import *
import numpy as np

def test_mean():
    assert round(get_mean(x), 5) == round(np.mean(x), 5)

def test_median():
    assert round(get_median(x), 5) == round(np.median(x), 5)

def test_std():
    assert round(get_std(x), 5) == round(np.std(x, ddof=1), 5)

if __name__ == "__main__":
    test_mean()
    test_median()
    test_std()

