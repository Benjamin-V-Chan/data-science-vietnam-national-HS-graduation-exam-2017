# Pseudocode:
# - import pandas, os, joblib, matplotlib.pyplot
# - define plot_actual_vs_pred(df)
#     - load model
#     - predict on df features
#     - scatter actual vs predicted
#     - save to outputs/figures/actual_vs_pred.png
# - in main:
#     - create outputs/figures/ if needed
#     - read outputs/features_data.csv
#     - call plot_actual_vs_pred
# - guard main
