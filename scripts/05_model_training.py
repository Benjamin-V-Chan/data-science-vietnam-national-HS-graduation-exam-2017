import pandas as pd
import os
import joblib
import json
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor

def train_model(df):
    X = df.drop(columns=["student_id","province","total_score"])
    y = df["total_score"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    params = {"n_estimators":[100,200], "max_depth":[None,10,20]}
    grid = GridSearchCV(RandomForestRegressor(random_state=42), params, cv=5)
    grid.fit(X_train, y_train)
    joblib.dump(grid.best_estimator_, "outputs/model/model.pkl")
    with open("outputs/model/metrics.json","w") as f:
        json.dump({"best_params":grid.best_params_, "best_score":grid.best_score_}, f)

def main():
    os.makedirs("outputs/model", exist_ok=True)
    df = pd.read_csv("outputs/features_data.csv")
    train_model(df)

if __name__ == "__main__":
    main()
