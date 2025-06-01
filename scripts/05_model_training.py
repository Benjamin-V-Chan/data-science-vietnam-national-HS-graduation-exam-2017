# Pseudocode:
# - import pandas, os, joblib, json, and sklearn tools
# - define train_model(df)
#     - split features/target (total_score)
#     - set up GridSearchCV on RandomForestRegressor
#     - fit on training set
#     - save best_estimator to outputs/model/model.pkl
#     - save best_params and best_score to outputs/model/metrics.json
# - in main:
#     - create outputs/model/ if needed
#     - read outputs/features_data.csv
#     - call train_model
# - guard main
