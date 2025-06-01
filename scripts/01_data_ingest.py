import pandas as pd
import os

def load_data(path="data/2017.csv"):
    return pd.read_csv(path)

def main():
    os.makedirs("outputs", exist_ok=True)
    df = load_data()
    df.to_csv("outputs/raw_data.csv", index=False)

if __name__ == "__main__":
    main()
