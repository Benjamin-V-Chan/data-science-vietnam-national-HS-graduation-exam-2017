import pandas as pd
import os
import joblib
import matplotlib.pyplot as plt

def plot_actual_vs_pred(df):
    model = joblib.load("outputs/model/model.pkl")
    X = df.drop(columns=["student_id","province","total_score"])
    preds = model.predict(X)
    plt.figure()
    plt.scatter(df["total_score"], preds)
    plt.xlabel("Actual Total Score")
    plt.ylabel("Predicted Total Score")
    plt.tight_layout()
    plt.savefig("outputs/figures/actual_vs_pred.png")

def main():
    os.makedirs("outputs/figures", exist_ok=True)
    df = pd.read_csv("outputs/features_data.csv")
    plot_actual_vs_pred(df)

if __name__ == "__main__":
    main()
