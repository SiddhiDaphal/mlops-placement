import pandas as pd

def load_data():
    df = pd.read_csv("data/placement.csv")
    return df

def preprocess(df):
    X = df.drop("placed", axis=1)
    y = df["placed"]
    return X, y

if __name__ == "__main__":
    df = load_data()
    X, y = preprocess(df)

    print("Features:\n", X.head())
    print("\nTarget:\n", y.head())