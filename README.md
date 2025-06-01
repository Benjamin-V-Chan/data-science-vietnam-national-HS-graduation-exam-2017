# data-science-vietnam-national-HS-graduation-exam-2017

## Project Overview

This project performs end-to-end data science and modeling on the 2017 Vietnam National High School Graduation Exam (NHGE) dataset. The goal is to ingest, preprocess, analyze, engineer features, train a predictive model, evaluate its performance, and visualize results. All scripts are modular, reusable, and organized for clarity.

## Folder Structure

```
project-root/
├── data/                    # Raw dataset folder
│   └── 2017.csv             # Original NHGE dataset file
├── scripts/                 # Python scripts for each step
│   ├── 01_data_ingest.py
│   ├── 02_data_preprocessing.py
│   ├── 03_exploratory_data_analysis.py
│   ├── 04_feature_engineering.py
│   ├── 05_model_training.py
│   ├── 06_model_evaluation.py
│   └── 07_visualization.py
├── outputs/                 # Generated outputs
│   ├── raw_data.csv         # Raw data copy
│   ├── processed_data.csv   # Cleaned data
│   ├── eda_summary.csv      # Descriptive statistics
│   ├── correlation_matrix.csv
│   ├── features_data.csv    # Data with engineered features
│   ├── model/               # Model artifacts and metrics
│   │   ├── model.pkl
│   │   ├── metrics.json
│   │   └── eval_metrics.txt
│   └── figures/             # Plots and visualizations
│       ├── correlation_heatmap.png
│       ├── <subject>_hist.png
│       └── actual_vs_pred.png
└── requirements.txt         # Python dependencies
```

