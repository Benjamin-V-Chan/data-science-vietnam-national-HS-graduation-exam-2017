# Pseudocode:
# - import pandas, os
# - define feature_engineering(df)
#     - compute total_score as sum of key score columns
#     - compute math_lit_diff as difference
#     - return df with new features
# - in main:
#     - create outputs/ if needed
#     - read outputs/processed_data.csv
#     - apply feature_engineering
#     - save as outputs/features_data.csv
# - guard main
