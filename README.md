# 📊 Data Mining Project
This project implements multiple data mining techniques including exploratory data analysis, **preprocessing, classification, regression, clustering, and association rule mining** on a real-world dataset.
```
# 📁 Project Structure

project/
│
├── data/
│   ├── raw/                # Original dataset
│   │   └── immo_data.csv
│   └── processed/          # Cleaned & split datasets
│       ├── train.csv
│       ├── val.csv
│       └── test.csv
│
├── notebooks/              # Jupyter notebooks for experiments
│   ├── eda_and_prep.ipynb
│   ├── classification.ipynb
│   ├── regression.ipynb
│   ├── clustering.ipynb
│   └── association_rule.ipynb
│
├── report/                 # Final report / documentation
├── download_data.py        # Script to download dataset
├── requirements.txt        # Python dependencies
├── .gitignore
└── README.md
```

# 🎯 Project Objectives
- Perform data exploration and preprocessing
- Build and evaluate:
    - Classification models
    - Regression models
    - Clustering algorithms
    - Association rule mining
- Extract meaningful insights from the dataset
# ⚙️ Setup Instructions
### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <data_mining>
```
### 2. Create virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
# 📥 Data
- Raw data is stored in:
```bash
data/raw/immo_data.csv
```
- Processed datasets:
```bash
data/processed/
```
If needed, run:
```bash
python download_data.py
```
# 🔍 Workflow
### 1. Data Exploration & Preprocessing
- **Notebook**: `eda_and_prep.ipynb`
- **Tasks**:
    - Handle missing values
    - Feature engineering
- Data normalization / encoding
- Train/validation/test split
### 2. Modeling
#### 📌 Classification
- **Notebook**: `classification.ipynb`
- **Example tasks**:
  - Predict categorical outcomes
  - Evaluate using accuracy, precision, recall and F1-score
#### 📌 Regression
- **Notebook**: `regression.ipynb`
- **Example tasks**:
    - Predict continuous values
    - Evaluate using RMSE, MAE and $R^2$.
#### 📌 Clustering
- **Notebook**: `clustering.ipynb`
- **Example tasks**:
    - Group similar data points
    - Use algorithms like K-Means / Hierarchical
#### *📌 Association Rule Mining
- **Notebook**: `association_rule.ipynb`
- **Example tasks**:
    - Discover relationships between features
    - Metrics: support, confidence, lift
# 📊 Results
- Key findings and visualizations are documented in:
    - Notebooks
    - `report/` directory
# 🧪 Reproducibility
- To reproduce results:
1. Run `eda_and_prep.ipynb`
2. Execute modeling notebooks in order:
    - classification
    - regression
    - clustering
    - association rules
# 📦 Dependencies
- Main libraries (see `requirements.txt`): Pandas, NumPy, scikit-learn, matplotlib / seaborn, mlxtend (for association rules)

# 👤 Author
**Name**: Phạm Thành Trí (2313621) - Trần Kiến Quốc (2312878) - Trương Nhật Thành (2313145)

**Course**: Data Mining (CO3029)

**Project Name**: Determinants of House Renting Decisions in Germany
