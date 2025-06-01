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

## Usage

1. **Setup the Project:**

   * Clone the repository.
   * Ensure you have Python installed.
   * Install required dependencies using the requirements.txt file.

     ```bash
     pip install -r requirements.txt
     ```

2. **Data Ingestion:**

   ```bash
   python scripts/01_data_ingest.py
   ```

   This loads `data/2017.csv` and saves it as `outputs/raw_data.csv`.

3. **Data Preprocessing:**

   ```bash
   python scripts/02_data_preprocessing.py
   ```

   This reads `outputs/raw_data.csv`, imputes missing values, drops duplicates, and writes `outputs/processed_data.csv`.

4. **Exploratory Data Analysis:**

   ```bash
   python scripts/03_exploratory_data_analysis.py
   ```

   Generates descriptive statistics (`eda_summary.csv`), a correlation matrix (`correlation_matrix.csv`), a heatmap (`outputs/figures/correlation_heatmap.png`), and histograms for each numeric column (`outputs/figures/<subject>_hist.png`).

5. **Feature Engineering:**

   ```bash
   python scripts/04_feature_engineering.py
   ```

   Reads `outputs/processed_data.csv`, creates `total_score` and `math_lit_diff` features, and saves `outputs/features_data.csv`.

6. **Model Training:**

   ```bash
   python scripts/05_model_training.py
   ```

   Loads `outputs/features_data.csv`, splits into training/testing sets, runs GridSearchCV on a `RandomForestRegressor`, saves the best model at `outputs/model/model.pkl`, and writes best parameters and score to `outputs/model/metrics.json`.

7. **Model Evaluation:**

   ```bash
   python scripts/06_model_evaluation.py
   ```

   Loads the trained model, predicts on the full dataset, computes MSE and R², and writes metrics to `outputs/model/eval_metrics.txt`.

8. **Visualization:**

   ```bash
   python scripts/07_visualization.py
   ```

   Plots actual vs. predicted total scores and saves the figure as `outputs/figures/actual_vs_pred.png`.

## Requirements

* Python 3.7 or higher
* pandas
* scikit-learn
* matplotlib
* joblib

Install all dependencies with:

```bash
pip install -r requirements.txt
```

## Acknowledgments

* **Dataset Name:** Vietnam National HS Graduation Exam - 2017
* **Dataset Author:** ume
* **Dataset Source:** [https://www.kaggle.com/datasets/invictus169/vietnam-national-hs-graduation-exam-2017](https://www.kaggle.com/datasets/invictus169/vietnam-national-hs-graduation-exam-2017)
