# 📊 Datasets untuk Pembelajaran

Folder ini berisi dataset yang digunakan untuk praktek machine learning.

## 🗂️ Dataset List

### 1. Iris Dataset
- **File:** `iris.csv`
- **Size:** ~5KB
- **Samples:** 150
- **Features:** 4 (petal length, petal width, sepal length, sepal width)
- **Target:** 3 classes (setosa, versicolor, virginica)
- **Use Case:** Classification

### 2. Titanic Dataset
- **File:** `titanic.csv`
- **Size:** ~60KB
- **Samples:** 891
- **Features:** 11 (age, sex, class, fare, etc.)
- **Target:** Survived (0/1)
- **Use Case:** Binary Classification

### 3. Housing Prices
- **File:** `housing.csv`
- **Size:** ~1.4MB
- **Samples:** 20,640
- **Features:** 8 (location, size, rooms, etc.)
- **Target:** Median house value
- **Use Case:** Regression

## 📥 Download Datasets

Dataset dapat didownload dari:

### Scikit-learn Built-in Datasets
```python
from sklearn.datasets import load_iris, load_wine, load_breast_cancer
```

### Kaggle
- [Titanic Dataset](https://www.kaggle.com/c/titanic/data)
- [House Prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
- [MNIST](https://www.kaggle.com/datasets/oddrationale/mnist-in-csv)

### UCI Machine Learning Repository
- [https://archive.ics.uci.edu/ml/index.php](https://archive.ics.uci.edu/ml/index.php)

## 🔒 .gitignore

Dataset besar (>100MB) tidak di-commit ke git. Download secara lokal jika diperlukan.

## 📝 Usage Example

```python
import pandas as pd

# Load dataset
df = pd.read_csv('datasets/iris.csv')

# Explore
print(df.head())
print(df.info())
```

## ⚠️ Data Ethics

- Gunakan dataset hanya untuk pembelajaran
- Perhatikan lisensi dan copyright
- Jaga privacy jika menggunakan data real
