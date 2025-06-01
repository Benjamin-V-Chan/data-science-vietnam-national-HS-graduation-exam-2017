import pandas as pd
import os
import matplotlib.pyplot as plt

def eda(df):
    df.describe().to_csv("outputs/eda_summary.csv")
    corr = df.select_dtypes(include=["number"]).corr()
    corr.to_csv("outputs/correlation_matrix.csv")
    plt.figure()
    plt.imshow(corr, interpolation="nearest")
    plt.colorbar()
    plt.xticks(range(len(corr)), corr.columns, rotation=90)
    plt.yticks(range(len(corr)), corr.columns)
    plt.tight_layout()
    plt.savefig("outputs/figures/correlation_heatmap.png")
    for col in df.select_dtypes(include=["number"]).columns:
        plt.figure()
        df[col].hist()
        plt.title(col)
        plt.savefig(f"outputs/figures/{col}_hist.png")

def main():
    os.makedirs("outputs/figures", exist_ok=True)
    df = pd.read_csv("outputs/processed_data.csv")
    eda(df)

if __name__ == "__main__":
    main()
