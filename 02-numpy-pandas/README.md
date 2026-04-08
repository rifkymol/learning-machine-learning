# 🔢 NumPy & Pandas - Data Manipulation for Machine Learning

Welcome to modul 2! Di sini Anda akan belajar **NumPy** dan **Pandas** - dua library yang **ABSOLUTELY ESSENTIAL** untuk data science dan machine learning.

---

## 🎯 Mengapa NumPy & Pandas?

### The Big Picture:

```
Your ML Journey:
Raw Data → [NumPy/Pandas] → Clean Data  → [scikit-learn] → ML Model
            ^^^^^^^^^^^^^^
            YOU ARE HERE!
```

**80% of ML work adalah data preparation!** NumPy dan Pandas adalah tools utama untuk ini.

---

## 🔢 NumPy - Numerical Python

### Apa itu NumPy?

**NumPy** adalah library untuk **numerical computing** di Python. Core-nya adalah **ndarray** (N-dimensional array) - struktur data super cepat untuk handle numeric data.

### Analogi Sederhana:

**Python Lists:**
```python
# Python list - flexible tapi lambat
data = [1, 2, 3, 4, 5]  
```
- Can store mixed types (numbers, strings, objects)
- Slow untuk mathematical operations
- No built-in math operations

**NumPy Arrays:**
```python
# NumPy array - fast & specialized
import numpy as np
data = np.array([1, 2, 3, 4, 5])
```
- Homogeneous (semua elemen same type)
- 100x faster untuk large data
- Built-in mathematical operations
- Vectorized operations (no loops needed!)

---

### Mengapa NumPy Penting untuk ML?

#### 1. **Speed** ⚡

**Comparison:**
```python
import numpy as np
import time

# Python lists (SLOW)
start = time.time()
python_list = list(range(1000000))
python_squared = [x**2 for x in python_list]
print(f"Python: {time.time() - start:.4f}s")  # ~0.15s

# NumPy (FAST!)
start = time.time()
numpy_array = np.arange(1000000)
numpy_squared = numpy_array ** 2
print(f"NumPy: {time.time() - start:.4f}s")   # ~0.002s
```

**NumPy is 50-100x faster!** For large datasets, this difference is critical.

---

#### 2. **Vectorization** - No More Loops! 🔥

**Traditional way (Python lists):**
```python
# Add two lists element-wise (SLOW & VERBOSE)
a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]
result = []
for i in range(len(a)):
    result.append(a[i] + b[i])
# result = [11, 22, 33, 44, 55]
```

**NumPy way (vectorized):**
```python
# Same operation - clean & fast!
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])
result = a + b  # That's it!
# array([11, 22, 33, 44, 55])
```

**Benefits:**
- ✅ Lebih readable
- ✅ Less code
- ✅ Faster execution
- ✅ Less bugs (no loop index errors)

---

#### 3. **Foundation for Everything ML** 🏗️

Semua ML libraries build on top of NumPy:

```python
# scikit-learn expects NumPy arrays
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)  # X_train & y_train are NumPy arrays

# TensorFlow/PyTorch can convert from NumPy
import tensorflow as tf
tensor = tf.constant(numpy_array)  # Convert NumPy → TensorFlow

# Pandas built on NumPy
import pandas as pd
df = pd.DataFrame(numpy_array)  # NumPy → Pandas
```

**Translation:** Tidak bisa ML tanpa NumPy!

---

### Real ML Use Cases:

**1. Representing Data:**
```python
# Image data: 28x28 pixel image
image = np.array([[...]])  # Shape: (28, 28)

# Batch of images: 100 images
batch = np.array([[...]])  # Shape: (100, 28, 28)

# Dataset: 1000 samples, 10 features each
X = np.array([[...]])  # Shape: (1000, 10)
```

**2. Matrix Operations (Neural Networks!):**
```python
# Weights matrix
W = np.array([[w11, w12], [w21, w22]])

# Input vector
X = np.array([x1, x2])

# Forward pass (matrix multiplication)
output = np.dot(W, X)  # This is how neural networks work!
```

**3. Statistical Operations:**
```python
# Dataset statistics
mean = np.mean(data)
std = np.std(data)

# Normalize data (common preprocessing)
normalized = (data - mean) / std
```

---

## 🐼 Pandas - Python Data Analysis

### Apa itu Pandas?

**Pandas** adalah library untuk **data manipulation and analysis**. Core structure: **DataFrame** (think Excel spreadsheet, but programmable!)

### Analogi:

- **Excel:**手動 click-click untuk filter, sort, calculate
- **Pandas:** Write code to do sama thing - automatable, reproducible, scalable

**Example:**
```
Excel: Click column → Sort A-Z → Filter > 100 → Apply
Pandas: df.sort_values('column').query('value > 100')
```

---

### Mengapa Pandas Penting untuk ML?

#### 1. **Handle Real-World Messy Data** 🧹

Real data tidak perfect. Pandas handles:

**Missing Values:**
```python
# Dataset with missing values
df = pd.DataFrame({
    'age': [25, None, 30, 45],
    'income': [50000, 60000, None, 70000]
})

# Handle missing data
df.fillna(df.mean())  # Fill with average
# atau
df.dropna()  # Remove rows with missing values
```

**Different Data Types:**
```python
# Mixed types in one structure
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],      # String
    'age': [25, 30, 35],                      # Integer
    'salary': [50000.0, 60000.5, 70000.25],  # Float
    'employed': [True, True, False]           # Boolean
})
```

---

#### 2. **Easy Data Exploration** 🔍

```python
# Load dataset
df = pd.read_csv('titanic.csv')

# Quick overview
df.head()         # First 5 rows
df.info()         # Data types, missing values
df.describe()     # Statistical summary
df.shape          # (rows, columns)

# Questions you can answer instantly:
df['age'].mean()                # Average age?
df['survived'].sum()            # How many survived?
df.groupby('class')['fare'].mean()  # Average fare by class?
```

**In Excel:** Would take many clicks!
**In Pandas:** One line of code!

---

#### 3. **Data Transformation** 🔄

**Common ML preprocessing:**

```python
# Feature engineering - create new features
df['family_size'] = df['sibsp'] + df['parch'] + 1

# Encoding categorical → numerical
df['sex_encoded'] = df['sex'].map({'male': 0, 'female': 1})

# Binning continuous → categorical
df['age_group'] = pd.cut(df['age'], bins=[0, 18, 35, 60, 100],
                         labels=['child', 'young', 'middle', 'senior'])

# Normalization
df['age_normalized'] = (df['age'] - df['age'].mean()) / df['age'].std()
```

---

#### 4. **Data Loading & Saving** 💾

Pandas reads/writes berbagai formats:

```python
# CSV (most common)
df = pd.read_csv('data.csv')
df.to_csv('cleaned_data.csv', index=False)

# Excel
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# JSON (API responses)
df = pd.read_json('api_response.json')

# SQL databases
import sqlite3
conn = sqlite3.connect('database.db')
df = pd.read_sql_query('SELECT * FROM users', conn)

# Parquet (efficient storage)
df.to_parquet('data.parquet')  # 10x smaller than CSV!
```

---

## 📚 Materi yang Akan Dipelajari

### Module 1: **NumPy Basics** 🔢

**Topics covered:**

#### 1.1 Creating Arrays

**Apa itu Creating Arrays?**

Creating arrays adalah proses **membuat struktur data NumPy array** dari berbagai sumber (Python lists, built-in functions, atau random values). Ini adalah langkah pertama dalam setiap operasi NumPy - tanpa array, tidak ada yang bisa dilakukan!

**Tentang apa ini?**

Topik ini mengajarkan berbagai cara untuk "membawa data" masuk ke dalam NumPy ecosystem:

1. **Dari data yang sudah ada** (Python lists) - convert data existing
2. **Generate dari scratch** (zeros, ones, arange) - create data patterns
3. **Random generation** (np.random) - create test data atau initialize values

Analogi: Seperti "import data" ke Excel - bisa dari file, bisa ketik manual, atau bisa generate pattern.

**Methods yang akan dipelajari:**
- From Python lists
- Built-in functions (`np.zeros`, `np.ones`, `np.arange`, `np.linspace`)
- Random arrays (crucial for ML!)

**Why important:**
- Initialize weights in neural networks (random)
- Create test datasets
- Generate data for simulations

**Examples:**
```python
# Random weights for neural network
weights = np.random.randn(784, 128)  # Layer 1: 784 inputs → 128 neurons

# Training data simulation
X_train = np.random.rand(1000, 10)  # 1000 samples, 10 features
y_train = np.random.randint(0, 2, 1000)  # Binary labels
```

**Estimated time:** 45 minutes

---

#### 1.2 Array Operations

**Apa itu Array Operations?**

Array Operations adalah **operasi matematika yang dilakukan pada SELURUH array sekaligus** tanpa perlu loop. NumPy melakukan operasi element-by-element secara otomatis (vectorization).

**Tentang apa ini?**

Bayangkan punya 1 juta angka dan ingin kalikan semuanya dengan 2:
- **Cara biasa:** Loop 1 juta kali (slow!)
- **Cara NumPy:** Satu operasi `array * 2` (instant!)

Topik ini cover:
1. **Basic arithmetic** (+, -, *, /) - operasi dasar pada seluruh array
2. **Universal functions (ufuncs)** - fungsi optimized (sin, cos, exp, log, sqrt)
3. **Broadcasting** - operasi pada arrays dengan shape berbeda

Ini adalah **inti kekuatan NumPy** - vectorization makes everything fast!

**Operations yang dipelajari:**
- Element-wise operations (+, -, *, /, **)
- Universal functions (ufuncs)
- Broadcasting rules

**Why important:**
- Data normalization
- Feature scaling
- Activation functions

**Examples:**
```python
# Normalize features to 0-1 range
X_normalized = (X - X.min()) / (X.max() - X.min())

# Apply sigmoid activation
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

activated = sigmoid(weighted_sum)
```

**Estimated time:** 1 hour

---

#### 1.3 Indexing & Slicing

**Apa itu Indexing & Slicing?**

**Indexing** adalah cara **mengakses elemen tertentu** dalam array (seperti mengambil 1 cell di Excel).
**Slicing** adalah cara **mengambil subset/potongan** array (seperti select range A1:D10 di Excel).

**Tentang apa ini?**

Dalam ML, Anda TIDAK PERNAH process seluruh dataset sekaligus. Anda selalu perlu:
- Ambil baris tertentu (sample tertentu)
- Ambil kolom tertentu (feature tertentu)  
- Filter data berdasarkan kondisi (data dengan nilai > threshold)
- Split data (training set vs test set)

Topik ini mengajarkan 4 cara akses data:

1. **Basic indexing:** `arr[2]` - akses by position
2. **Slicing:** `arr[1:5]` - ambil range
3. **Boolean indexing:** `arr[arr > 10]` - filter by condition (POWERFUL!)
4. **Fancy indexing:** `arr[[0, 2, 5]]` - akses multiple indices

Analogi: Seperti SQL `WHERE` clause, tapi untuk arrays!

**Techniques yang dipelajari:**
- Basic indexing
- Slicing (1D, 2D, 3D)
- Boolean indexing (SUPER USEFUL!)
- Fancy indexing

**Why important:**
- Select training/test data
- Filter outliers  
- Sample specific rows/columns

**Examples:**
```python
# Boolean indexing - filter data
high_income = data[data[:, 3] > 100000]  # People with income > 100k

# Training/test split concept
train_data = data[:800]   # First 800 samples
test_data = data[800:]    # Remaining samples

# Select features
X = data[:, :-1]  # All columns except last (features)
y = data[:, -1]   # Last column (target)
```

**Estimated time:** 1 hour

---

#### 1.4 Shape Manipulation

**Apa itu Shape Manipulation?**

Shape Manipulation adalah **mengubah dimensi/bentuk array TANPA mengubah data**-nya. Sama data, beda "packaging". 

Contoh: Array dengan 12 elemen bisa berbentuk:
- 1D: `(12,)` - single row
- 2D: `(3, 4)` - 3 rows, 4 columns
- 2D: `(4, 3)` - 4 rows, 3 columns  
- 3D: `(2, 2, 3)` - 2 matrices of 2x3

Semuanya contain 12 elements yang sama!

**Tentang apa ini?**

Machine learning models SANGAT PARTICULAR tentang input shape:
- Image classifier expects: `(batch_size, height, width, channels)`
- Dense layer expects: `(batch_size, features)`
- RNN expects: `(batch_size, timesteps, features)`

Wrong shape = ERROR! Jadi Anda HARUS bisa reshape data.

Operations yang dipelajari:

1. **Reshape** - ubah dimensions: `(12,) → (3, 4)`
2. **Flatten** - collapse ke 1D: `(3, 4) → (12,)`
3. **Transpose** - flip axes: `(3, 4) → (4, 3)`
4. **Expand dims** - tambah axis: `(3, 4) → (1, 3, 4)`

Analogi: Seperti pack 12 telur - bisa 1 row of 12, atau 3 rows of 4, atau 2 boxes of 6. Same eggs, different arrangement!

**Operations yang dipelajari:**
- Reshape
- Flatten
- Transpose
- Expand dimensions

**Why important:**
- Prep data for models (models expect specific shapes)
- Transform features
- Batch processing

**Examples:**
```python
# Flatten image for neural network
image = np.array([[...]])  # Shape: (28, 28)
flat_image = image.flatten()  # Shape: (784,)

# Batch of images
batch = images.reshape(-1, 28, 28, 1)  # Add channel dimension

# Transpose features/samples
X_transposed = X.T  # From (samples, features) → (features, samples)
```

**Estimated time:** 45 minutes

---

#### 1.5 Mathematical Operations

**Apa itu Mathematical Operations?**

Mathematical Operations adalah **fungsi-fungsi matematika yang bekerja pada arrays** - dari operasi sederhana (sum, mean) sampai advanced (matrix multiplication, eigenvalues). 

Beda dengan Array Operations (topic 1.2) yang fokus pada element-wise ops, ini fokus pada **aggregate operations** dan **linear algebra**.

**Tentang apa ini?**

Dalam ML, hampir SEMUA algorithm adalah math operations:

**Statistics & Aggregations:**
- Calculate mean/std untuk normalization
- Find min/max untuk scaling
- Compute variance untuk feature analysis

**Linear Algebra:**
- Matrix multiplication = Neural network forward pass
- Dot product = Similarity calculation  
- Eigenvalues = PCA dimensionality reduction

Topik ini cover:

1. **Aggregations** - reduce array to single value (atau per-axis)
   - `sum()`, `mean()`, `std()`, `min()`, `max()`, `median()`
   
2. **Axis operations** - aggregate along specific dimension
   - Sum per row vs sum per column
   - Mean of each feature across samples
   
3. **Matrix operations** - linear algebra (the math behind ML!)
   - Dot product: `np.dot(A, B)`
   - Matrix multiply: `A @ B`
   - Inverse, determinant, eigenvalues

Analogi: Aggregations seperti "Total" di Excel. Matrix ops seperti solver di Excel, tapi much more powerful!

**Operations yang dipelajari:**
- Aggregations (sum, mean, std, min, max)
- Axis-wise operations
- Matrix multiplication (CRUCIAL!)
- Linear algebra operations

**Why important:**
- Statistics on datasets
- Matrix ops in neural networks
- Gradient calculations

**Examples:**
```python
# Dataset statistics
mean = np.mean(X, axis=0)  # Mean of each feature
std = np.std(X, axis=0)    # Std dev of each feature

# Standardize (zero mean, unit variance)
X_standardized = (X - mean) / std

# Neural network forward pass
output = np.dot(input_layer, weights) + bias
```

**Estimated time:** 1 hour

---

#### 1.6 Broadcasting

**Apa itu Broadcasting?**

Broadcasting adalah **set aturan otomatis** yang memungkinkan NumPy melakukan operasi pada arrays dengan **shapes yang berbeda** - tanpa perlu manually expand arrays.

Contoh simple:
```python
arr = np.array([1, 2, 3])  # Shape: (3,)
arr + 10  # → [11, 12, 13]
```

Kenapa bisa? NumPy automatically "broadcasts" scalar `10` menjadi `[10, 10, 10]` behind the scenes!

**Tentang apa ini?**

Broadcasting adalah "magic" yang makes NumPy code clean dan efficient. Tanpa broadcasting, Anda harus:

```python
# WITHOUT broadcasting (manual expansion):
scalar = 10
expanded = np.array([scalar, scalar, scalar])  # Repeat manually
result = arr + expanded

# WITH broadcasting (automatic):
result = arr + 10  # NumPy does expansion automatically!
```

Topik ini mengajarkan:

1. **Broadcasting rules** - kapan broadcasting works, kapan tidak
   - Rule 1: Dimensions compared from right to left
   - Rule 2: Compatible if dimensions equal OR one is 1
   
2. **Common patterns:**
   - Add scalar to array: `(100,) + scalar`
   - Add vector to matrix (row-wise): `(100, 10) + (10,)`
   - Add vector to matrix (column-wise): `(100, 10) + (100, 1)`
   
3. **Performance benefits** - avoid loops dan explicit copying

Kenapa penting? Makes code:
- ✅ **Cleaner** - no manual expansion
- ✅ **Faster** - no unnecessary copying
- ✅ **More readable** - intent clear

Analogi: Seperti Excel auto-fill - ketik formula di 1 cell, drag ke kolom lain, formula automatically adjust. Broadcasting does similar "auto-adjustment" for arrays!

**Concepts yang dipelajari:**
- Broadcasting rules
- Common patterns
- Avoiding explicit loops

**Why important:**
- Efficient operations on arrays of different shapes
- Clean code
- Performance optimization

**Examples:**
```python
# Add bias to each sample (no loop needed!)
X_with_bias = X + bias  # bias shape: (10,), X shape: (1000, 10)

# Normalize batch
normalized = (batch - mean) / std  # Works even if shapes differ!
```

**Estimated time:** 45 minutes

---

### Module 2: **Pandas DataFrames** 🐼 (Coming Soon)

**Topics:**

#### 2.1 Series & DataFrames

**Apa itu Series & DataFrames?**

**Series** adalah array 1D dengan **labels** (index). Think: single column di Excel dengan row labels.
**DataFrame** adalah table 2D dengan rows dan columns (keduanya punya labels). Think: entire Excel spreadsheet!

**Tentang apa ini?**

NumPy bagus untuk numerical arrays, tapi real-world data tidak sesimple array of numbers. Anda punya:
- Column names (features punya nama, bukan cuma index 0, 1, 2)
- Row labels (samples bisa punya ID)
- Mixed types (age=int, name=string, employed=bool dalam 1 table)
- Missing values (real data selalu ada yang missing!)

Pandas DataFrame adalah **NumPy array + metadata** - structure yang lebih rich!

**Methods yang dipelajari:**
- Creating DataFrames (from dict, lists, CSV)
- Column/row operations (add, delete, rename)
- Data types (checking dan converting types)

**Why important:** Foundation untuk semua data analysis di Python!

---

#### 2.2 Reading/Writing Data

**Apa itu Reading/Writing Data?**

Reading = **load data dari files** (CSV, Excel, JSON, database) ke Pandas DataFrame.
Writing = **save DataFrame kembali** ke files untuk sharing atau storage.

**Tentang apa ini?**

Dalam ML workflow, data JARANG sudah ada di script Anda. Data biasanya:
- From database (SQL query results)
- From files (CSV exports, Excel reports)
- From APIs (JSON responses)
- From web scraping (HTML tables)

Pandas bisa read/write 20+ formats! Ini adalah **gateway** untuk bring data into dan out of Python.

**Formats & techniques:**
- CSV, Excel, JSON (most common)
- Handling encodings (UTF-8, Latin-1)
- Parse dates (string → datetime)
- SQL databases, Parquet, HDF5

**Why important:** Can't do ML without data - need to load it first!

---

#### 2.3 Data Selection

**Apa itu Data Selection?**

Data Selection adalah **mengakses specific rows, columns, atau cells** dalam DataFrame. Pandas version dari NumPy indexing, tapi lebih powerful karena bisa use labels!

**Tentang apa ini?**

Ada 4 ways untuk select data di Pandas:
1. **Column selection:** `df['age']` - get column by name
2. **loc (label-based):** `df.loc[0:5, 'age']` - use labels
3. **iloc (position-based):** `df.iloc[0:5, 2]` - use integer positions
4. **Boolean indexing:** `df[df['age'] > 25]` - filter by condition

Confusion: kapan pakai `loc` vs `iloc`? Topic ini clarify!

**Techniques yang dipelajari:**
- loc vs iloc (crucial difference!)
- Filtering data (conditional selection)
- Boolean indexing (複雑な conditions)

**Why important:** 99% of Pandas work involves selecting subsets of data!

---

#### 2.4 Handling Missing Data

**Apa itu Missing Data?**

Missing data adalah **nilai yang tidak ada** dalam dataset - represented as `NaN` (Not a Number) atau `None`. Dalam Excel, ini adalah empty cells.

**Tentang apa ini?**

Real-world data SELALU messy! Missing values terjadi karena:
- Sensor failed (IoT data)
- User skip pertanyaan (survey data)
- Data lost (corrupted files)
- Not applicable (tidak semua field relevant untuk semua records)

Machine learning models **CANNOT handle NaN**! Model expects numbers, not "missing". Jadi Anda HARUS handle missing data dulu.

Topic ini mengajarkan:
1. **Detect:** Temukan where missing values are
2. **Decide:** Drop rows or fill (impute) values?
3. **Handle:** Execute chosen strategy

**Strategies yang dipelajari:**
- Detecting nulls (`isnull()`, `notnull()`)
- Filling strategies (mean, median, forward-fill, interpolate)
- Dropping vs imputing (trade-offs)

**Why important:** Missing data handling can make or break model performance!

---

#### 2.5 Basic Statistics

**Apa itu Basic Statistics (in Pandas)?**

Basic Statistics adalah **summarizing data** untuk understand distributions, relationships, dan patterns. Pandas makes this one-liner!

**Tentang apa ini?**

Before building model, Anda HARUS understand data Anda:
- What's average age? (central tendency)
- Age range? (spread)
- Distribution skewed? (shape)
- Correlation between features? (relationships)

This is **Exploratory Data Analysis (EDA)** - critical first step!

Topic ini cover:
1. **describe()** - instant statistical summary (count, mean, std, min, max, quartiles)
2. **groupby()** - split data by categories, analyze each group
3. **Aggregations** - custom summarizations

**Methods yang dipelajari:**
- describe() - quick overview
- groupby() - group-wise analysis (SQL `GROUP BY` in Pandas!)
- Aggregations (sum, mean, count, custom functions)

**Why important:** Can't build good model without understanding data first!

**Estimated time:** 1-2 weeks

---

### Module 3: **Advanced Data Manipulation** 🚀 (Coming Soon)

**Topics:**

#### 3.1 GroupBy Operations

**Apa itu GroupBy?**

GroupBy adalah **split-apply-combine pattern** - split data into groups, apply function ke each group, combine results. Ini adalah Pandas version dari SQL `GROUP BY`.

**Tentang apa ini?**

Sering Anda perlu answer questions seperti:
- Average salary **per department**?
- Total sales **per region**?
- Customer count **per age group**?

Pattern: "Calculate [aggregate] **per [category]**"

GroupBy workflow:
```
Data → Split by category → Apply function → Combine results
```

Contoh:
```
Titanic data:
Split by "class" (1st, 2nd, 3rd)
→ Calculate survival rate per class
→ Combine: {1st: 62%, 2nd: 47%, 3rd: 24%}
```

**Techniques yang dipelajari:**
- Split-apply-combine pattern
- Multiple aggregations (mean, sum, count at once)
- Custom functions (apply YOUR logic)

**Why important:** Most powerful Pandas feature for group-wise analysis!

---

#### 3.2 Merging & Joining

**Apa itu Merging & Joining?**

Merging/Joining adalah **combining multiple DataFrames** into one - matching rows based on common column(s). Pandas version dari SQL `JOIN`.

**Tentang apa ini?**

Real data jarang dalam 1 file. Biasanya tersebar:
- `customers.csv` - customer info
- `orders.csv` - order details  
- `products.csv` - product catalog

Untuk analysis, Anda perlu **combine** mereka: "Which customers ordered which products?"

Types of joins:
1. **Inner join** - only matching rows (intersection)
2. **Left join** - keep all from left, match from right
3. **Right join** - keep all from right, match from left
4. **Outer join** - keep all from both (union)

Analogi: Seperti VLOOKUP di Excel, tapi much more powerful!

**Methods yang dipelajari:**
- concat() - stack DataFrames vertically/horizontally
- merge() - join on columns (SQL-style)
- join() - join on index
- Different join types (inner, left, right, outer)

**Why important:** Real datasets always require combining multiple sources!

---

#### 3.3 Pivot Tables

**Apa itu Pivot Tables?**

Pivot table adalah **reshaping data** dari long format ke wide format (atau sebaliknya), dengan aggregation. Pandas version dari Excel Pivot Tables!

**Tentang apa ini?**

Same data bisa represented 2 ways:

**Long format** (tidy data):
```
| Person | Year | Revenue |
|--------|------|---------|
| Alice  | 2023 | 100     |
| Alice  | 2024 | 150     |
| Bob    | 2023 | 120     |
| Bob    | 2024 | 130     |
```

**Wide format** (pivot):
```
| Person | 2023 | 2024 |
|--------|------|------|
| Alice  | 100  | 150  |
| Bob    | 120  | 130  |
```

Different shapes, same data! Pivot transforms between them.

Use cases:
- Create summary reports
- Prepare data untuk visualization
- Match format expected by ML models

**Operations yang dipelajari:**
- pivot() - reshape without aggregation
- pivot_table() - reshape + aggregate
- Wide vs long format (melt, stack, unstack)

**Why important:** Data often needs reshaping before analysis or modeling!

---

#### 3.4 String Operations

**Apa itu String Operations?**

String Operations adalah **text manipulation methods** untuk clean, extract, dan transform text data dalam DataFrames. Pandas `.str` accessor gives you string superpowers!

**Tentang apa ini?**

Text data selalu messy:
- "John Doe" vs "john doe" vs " John Doe " (case, whitespace)
- Extract email domain from "user@gmail.com"
- Clean phone numbers: "123-456-7890" → "1234567890"
- Check if text contains keyword

Pandas `.str` methods:
```python
df['name'].str.lower()  # Lowercase
df['email'].str.contains('@gmail')  # Check pattern
df['phone'].str.replace('-', '')  # Remove characters
```

**Text processing techniques:**
- String methods (lower, upper, strip, split, replace)
- Regular expressions (pattern matching)
- Text preprocessing (for NLP/ML)

**Why important:** Text data needs heavy cleaning before use in ML!

---

#### 3.5 Date/Time Handling

**Apa itu Date/Time Handling?**

Date/Time handling adalah **working with temporal data** - parsing dates, extracting components (year, month, day), calculating differences, resampling time series.

**Tentang apa ini?**

Time-based data adalah everywhere:
- Sales data (date of transaction)
- Sensor data (timestamp of reading)
- User activity logs (login/logout times)
- Stock prices (daily values)

Challenges:
- Dates stored as strings: "2024-01-15" → need parse to datetime
- Extract features: year, month, day of week (for ML!)
- Calculate duration: time between events
- Resample: daily data → monthly averages

**Operations yang dipelajari:**
- datetime operations (parsing, formatting)
- Time series (DateTimeIndex)
- Resampling (aggregate over time periods)
- Rolling windows (moving averages)

**Why important:** Time-based features often crucial for ML models!

**Estimated time:** 1-2 weeks

---

## ⏱️ Estimasi Waktu

### Module Completion Times:

| Module | Topics | Estimated Time | Difficulty |
|--------|--------|----------------|------------|
| NumPy Basics | Arrays, operations, indexing | 1-2 weeks | Medium |
| Pandas DataFrames | Data loading, cleaning | 1-2 weeks | Medium |
| Advanced Manipulation | Groupby, merge, pivot | 1-2 weeks | Medium-Hard |

### Weekly Schedule Example:

**Week 1: NumPy Foundations**
- Day 1-2: Array creation & operations
- Day 3-4: Indexing & slicing
- Day 5-6: Shape manipulation & math ops
- Day 7: Review & practice exercises

**Week 2: NumPy Mastery**
- Day 1-2: Broadcasting & advanced indexing
- Day 3-4: Linear algebra for ML
- Day 5-6: Mini ML project (data preprocessing)
- Day 7: Start Pandas

**Flexibility:** Adjust based on your pace!

---

## ✅ Exercise Validation

### Auto-Validation Available! 🎉

Every NumPy exercise sekarang punya **automatic validation** with instant feedback!

### How to Use:

**Step 1:** Work on exercise di `01_numpy_basics.ipynb`
```python
# Exercise 1: Create array with numbers 10-20
arr1 = np.arange(10, 21)  # Your solution
```

**Step 2:** Open `01_numpy_basics_SOLUTIONS.ipynb`

**Step 3:** Copy your solution to validation cell

**Step 4:** Run cell → Get feedback
```
✅ arr1 is a NumPy array
✅ arr1 has correct values: [10 11 12 13 14 15 16 17 18 19 20]
🎉 Perfect! Array created correctly!
```

### Example Feedback:

**Success:**
```
✅ Correct! arr1 has shape (4, 4)
✅ Great! All values are floats
✅ Excellent! Matrix multiplication works correctly
```

**Error with Hints:**
```
❌ arr1 should be 2D array, found 1D
💡 Hint: Use reshape() atau create with nested lists

❌ Expected shape (3, 4), got (4, 3)
💡 Hint: Check rows vs columns - (rows, columns)
```

**See:** [VALIDATION_GUIDE.md](../VALIDATION_GUIDE.md) for complete guide

---
- [Pandas Cheatsheet](https://www.datacamp.com/cheat-sheet/pandas-cheat-sheet-for-data-science-in-python)
