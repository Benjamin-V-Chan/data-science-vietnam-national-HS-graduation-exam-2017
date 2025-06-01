import pandas as pd
import os
from sklearn.impute import SimpleImputer

def preprocess(df):
    numeric = df.select_dtypes(include=["number"]).columns
    imputer = SimpleImputer(strategy="mean")
    df[numeric] = imputer.fit_transform(df[numeric])
    return df.drop_duplicates()

def main():
    os.makedirs("outputs", exist_ok=True)
    df = pd.read_csv("outputs/raw_data.csv")
    df_clean = preprocess(df)
    df_clean.to_csv("outputs/processed_data.csv", index=False)

if __name__ == "__main__":
    main()
