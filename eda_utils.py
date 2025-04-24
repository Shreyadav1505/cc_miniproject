import pandas as pd

def load_data(path="E:/3rd_year_prac/CC/minipro3/data/credit_card_transactions.csv"):
    df = pd.read_csv(path)
    return df

def clean_data(df):
    # Fill or drop missing values
    df = df.dropna()  # Or use df.fillna(method='ffill')
    return df

def explore_data(df):
    return {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes,
        "missing": df.isnull().sum(),
        "summary": df.describe()
    }
