import pandas as pd
import os
import joblib
from sklearn.metrics import mean_squared_error, r2_score

def evaluate_model(df):
    model = joblib.load("outputs/model/model.pkl")
    X = df.drop(columns=["student_id","province","total_score"])
    y = df["total_score"]
    preds = model.predict(X)
    mse = mean_squared_error(y, preds)
    r2 = r2_score(y, preds)
    with open("outputs/model/eval_metrics.txt","w") as f:
        f.write(f"MSE: {mse}\nR2: {r2}")

def main():
    os.makedirs("outputs/model", exist_ok=True)
    df = pd.read_csv("outputs/features_data.csv")
    evaluate_model(df)

if __name__ == "__main__":
    main()
