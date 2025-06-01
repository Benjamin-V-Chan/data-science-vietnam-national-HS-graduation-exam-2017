# Pseudocode:
# - import pandas, os and SimpleImputer
# - define preprocess(df)
#     - identify numeric columns
#     - impute missing numeric values with mean
#     - drop duplicates
#     - return cleaned df
# - in main:
#     - create outputs/ if needed
#     - read outputs/raw_data.csv
#     - preprocess it
#     - save as outputs/processed_data.csv
# - guard main
