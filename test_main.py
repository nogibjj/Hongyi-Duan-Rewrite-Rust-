from main import *
import pandas as pd

df = None
try:
    df = pd.read_excel("Project-Management-Sample-Data.xlsx")
except FileNotFoundError:
    pass
x = df['Days Required']
print(x.describe())

def test_df_exists():
    assert df is not None, "DataFrame was not loaded, check if it exists."
    
def test_mean():
    assert round(get_mean(x), 5) == round(x.mean(), 5)

def test_median():
    assert round(get_median(x), 5) == round(x.median(), 5)

def test_std():
    assert round(get_std(x), 5) == round(x.std(), 5)

if __name__ == "__main__":
    test_df_exists()
    test_mean()
    test_median()
    test_std()
    get_plot()
