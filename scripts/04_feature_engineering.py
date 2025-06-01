import pandas as pd
import os

def feature_engineering(df):
    df["total_score"] = df[
        ["mathematics","literature","english","combined_natural_sciences","combined_social_sciences"]
    ].sum(axis=1)
    df["math_lit_diff"] = df["mathematics"] - df["literature"]
    return df

def main():
    os.makedirs("outputs", exist_ok=True)
    df = pd.read_csv("outputs/processed_data.csv")
    df_fe = feature_engineering(df)
    df_fe.to_csv("outputs/features_data.csv", index=False)

if __name__ == "__main__":
    main()
