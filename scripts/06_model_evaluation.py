# Pseudocode:
# - import pandas, os, joblib, and sklearn.metrics
# - define evaluate_model(df)
#     - load model from outputs/model/model.pkl
#     - predict on df features
#     - compute mse and r2
#     - save to outputs/model/eval_metrics.txt
# - in main:
#     - create outputs/model/ if needed
#     - read outputs/features_data.csv
#     - call evaluate_model
# - guard main
