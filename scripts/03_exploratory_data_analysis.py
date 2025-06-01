# Pseudocode:
# - import pandas, os, matplotlib.pyplot
# - define eda(df)
#     - save df.describe() to outputs/eda_summary.csv
#     - compute corr matrix, save to outputs/correlation_matrix.csv
#     - plot and save heatmap in outputs/figures/
#     - for each numeric column, plot histogram to outputs/figures/
# - in main:
#     - create outputs/figures/ if needed
#     - read outputs/processed_data.csv
#     - run eda(df)
# - guard main
