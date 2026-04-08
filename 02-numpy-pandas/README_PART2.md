## 🎯 Learning Objectives

### After Completing NumPy Module:

**Core Skills:**
- ✅ Create NumPy arrays dari berbagai sources
- ✅ Perform vectorized operations (no loops!)
- ✅ Index dan slice arrays efficiently
- ✅ Manipulate array shapes (reshape, transpose, flatten)
- ✅ Aggregate dan compute statistics
- ✅ Understand broadcasting rules
- ✅ Perform matrix operations

**ML-Ready Skills:**
- ✅ Represent datasets as arrays
- ✅ Normalize and standardize data
- ✅ Implement basic ML operations (dot products, activations)
- ✅ Handle multi-dimensional data (images, batches)
- ✅ Efficiently process large datasets

### After Completing Pandas Module:

**Core Skills:**
- ✅ Load data dari CSV, Excel, JSON
- ✅ Explore data (head, info, describe)
- ✅ Select dan filter data
- ✅ Handle missing values
- ✅ Group dan aggregate data
- ✅ Merge datasets
- ✅ Create pivot tables

**ML-Ready Skills:**
- ✅ Clean messy real-world data
- ✅ Feature engineering
- ✅ Encode categorical variables
- ✅ Split data for training/testing
- ✅ Prepare data for ML models

---

## 🚀 Cara Memulai

### 1. Install Requirements

```bash
# Verify installations:
python -c "import numpy; print('NumPy version:', numpy.__version__)"
python -c "import pandas; print('Pandas version:', pandas.__version__)"

# If not installed:
pip install numpy pandas

# Or with Anaconda:
conda install numpy pandas
```

**Expected output:**
```
NumPy version: 1.21.x or higher
Pandas version: 1.3.x or higher
```

---

### 2. Start Jupyter Notebook

```bash
cd machine-learning/02-numpy-pandas
jupyter notebook
```

Browser akan open otomatis.

---

### 3. Learning Path

**Recommended sequence:**

#### Week 1-2: NumPy Mastery

```
Day 1-2: Array Creation & Basic Operations
├─ Read tutorial sections
├─ Run all example code
├─ Observe outputs
└─ Complete Exercise 1

Day 3-4: Indexing, Slicing & Boolean Indexing
├─ Practice different indexing methods
├─ Master boolean filtering
├─ Create sample filters
└─ Complete Exercise 2

Day 5-6: Shape Manipulation & Math Operations
├─ Practice reshaping arrays
├─ Learn aggregation functions
├─ Understand axis parameter
└─ Complete Exercise 3

Day 7: Broadcasting & Review
├─ Master broadcasting rules
├─ Review all exercises
├─ Do Final Exercise (ML data prep)
└─ Validate all answers

Weekend: Mini Project
└─ Build simple data pipeline using NumPy
```

#### Week 3-4: Pandas DataFrames (when available)

```
Day 1-2: DataFrames & Data Loading
Day 3-4: Selection & Filtering
Day 5-6: Cleaning & Missing Data
Day 7: Review & Practice
Weekend: EDA Project
```

---

## 📝 Prerequisites

### Required (Must Complete First):

✅ **01-python-basics** module
- Variables & data types
- Lists, dictionaries, tuples
- Loops (for, while)
- Functions
- List comprehensions

**Why:** NumPy builds on these concepts. Without solid Python basics, NumPy will be confusing.

---

### Recommended Skills:

- Basic math (arithmetic, averages, percentages)
- Matrix concept (rows & columns)
- Comfortable with Python syntax

**Note:** Tidak perlu advanced math! Basic understanding cukup.

---

### Self-Check - Ready for NumPy?

Can you do these WITHOUT looking up:

- [ ] Create Python list: `my_list = [1, 2, 3, 4, 5]`
- [ ] Access elements: `my_list[0]`, `my_list[-1]`
- [ ] Loop through list: `for item in my_list:`
- [ ] List comprehension: `[x**2 for x in my_list]`
- [ ] Write function with return value

**If yes to all → Start NumPy!**
**If struggling → Review Python basics first**

---

## 💡 Tips untuk Sukses

### 1. **Think in Arrays, Not Loops** 🔄→⚡

**Beginner mindset:**
```python
# Process each element individually
result = []
for x in data:
    result.append(x * 2)
```

**NumPy mindset:**
```python
# Process all at once
result = data * 2  # Vectorized!
```

**Practice:** Whenever tempted to write loop, ask "Can I vectorize this?"

---

### 2. **Print Shapes Frequently** 📐

Arrays beda shape = different meaning. Always check!

```python
import numpy as np

arr = np.random.rand(100, 10)
print(f"Shape: {arr.shape}")  # (100, 10)
print(f"Dimensions: {arr.ndim}")  # 2
print(f"Size: {arr.size}")  # 1000

# After operations:
reshaped = arr.reshape(10, 100)
print(f"New shape: {reshaped.shape}")  # (10, 100)
```

**Habit:** Add `print(arr.shape)` whenever debugging!

---

### 3. **Use .shape to Understand Errors** 🐛

**Common error:**
```
ValueError: operands could not be broadcast together with shapes (100,10) (100,)
```

**Debug strategy:**
```python
print(f"A shape: {A.shape}")  # (100, 10)
print(f"B shape: {B.shape}")  # (100,)
# Aha! Shapes don't match for operation

# Fix: Reshape B
B_reshaped = B.reshape(-1, 1)  # (100, 1)
result = A + B_reshaped  # Works!
```

---

### 4. **Experiment in Small Examples** 🧪

Don't test on big data!

```python
# Bad: Testing on real dataset
big_data = np.random.rand(10000, 1000)  # Slow to debug!

# Good: Test on small sample
small_sample = np.array([[1, 2], [3, 4]])  # Easy to verify
# Try operation
result = small_sample * 2
print(result)  # Can see if correct

# Once working, scale to big data
```

---

### 5. **Read Documentation** 📖

NumPy docs are excellent! When stuck:

```python
# In Jupyter:
np.mean?  # Show documentation
# or
help(np.mean)

# Online:
# numpy.org/doc/stable/reference/generated/numpy.mean.html
```

---

### 6. **Compare with Python Equivalents** 🔄

Understand what NumPy does by comparing with Python:

```python
# Python way:
python_list = [1, 2, 3, 4, 5]
mean_python = sum(python_list) / len(python_list)

# NumPy way:
numpy_array = np.array([1, 2, 3, 4, 5])
mean_numpy = np.mean(numpy_array)

# Same result, but NumPy is cleaner and faster!
```

---

## 🔗 Additional Resources

### Official Documentation:

**NumPy:**
- [NumPy User Guide](https://numpy.org/doc/stable/user/) - Comprehensive tutorial
- [NumPy Reference](https://numpy.org/doc/stable/reference/) - API documentation
- [NumPy for MATLAB Users](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html) - If you know MATLAB

**Pandas:**
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html) - Quick start
- [Pandas Cookbook](https://pandas.pydata.org/docs/user_guide/cookbook.html) - Common tasks

---

### Cheat Sheets:

- [NumPy Cheat Sheet (DataCamp)](https://www.datacamp.com/cheat-sheet/numpy-cheat-sheet-data-analysis-in-python)
- [Pandas Cheat Sheet (Pandas)](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [NumPy for MATLAB Users](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html)

---

### Interactive Tutorials:

- [NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
- [Kaggle: Pandas Mini-Course](https://www.kaggle.com/learn/pandas)
- [DataCamp: NumPy Tutorial](https://www.datacamp.com/tutorial/python-numpy-tutorial)

---

### Books:

**"Python for Data Analysis" by Wes McKinney** (creator of Pandas!)
- Comprehensive coverage of NumPy & Pandas
- Real-world examples
- Best practices
- [Free online version](https://wesmckinney.com/book/)

---

### Video Tutorials:

- **Keith Galli - NumPy Tutorial:** Clear explanations
- **Corey Schafer - Pandas Tutorial Series:** Step-by-step
- **StatQuest - Pandas Playlist:** Visual learner friendly

---

### Practice Platforms:

- **[HackerRank - NumPy](https://www.hackerrank.com/domains/python)** - Graded exercises
- **[Kaggle Datasets](https://www.kaggle.com/datasets)** - Real datasets to practice
- **[LeetCode - Array Problems](https://leetcode.com/)** - Algorithm practice

---

## 🚨 Common Mistakes to Avoid

### 1. **Forgetting To Import** ❌

```python
# Wrong
arr = array([1, 2, 3])  # NameError!

# Correct
import numpy as np
arr = np.array([1, 2, 3])
```

**Tip:** Always start notebook dengan import cell!

---

### 2. **Modifying Arrays In-Place Accidentally** ❌

```python
a = np.array([1, 2, 3])
b = a  # NOT a copy! b points to same memory
b[0] = 99
print(a)  # [99, 2, 3] - a changed too!

# Correct - make copy:
b = a.copy()
b[0] = 99
print(a)  # [1, 2, 3] - a unchanged ✅
```

---

### 3. **Confusing Axis Parameter** ❌

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# axis=0: down the rows (column-wise)
np.sum(arr, axis=0)  # [5, 7, 9]

# axis=1: across columns (row-wise)
np.sum(arr, axis=1)  # [6, 15]
```

**Mnemonic:** 
- axis=0 → "**compress rows**" → result has shape (columns,)
- axis=1 → "**compress columns**" → result has shape (rows,)

---

### 4. **Not Checking Data Types** ❌

```python
# Integer division in NumPy:
arr = np.array([1, 2, 3])
result = arr / 2
print(result)  # [0.5, 1.0, 1.5] ✅ Float result

# But:
arr_int = np.array([1, 2, 3], dtype=int)
result_int = arr_int / 2  
print(result_int)  # Still [0.5, 1.0, 1.5] in Python 3 ✅

# Explicit type:
print(arr.dtype)  # Always check!
```

---

### 5. **Using Python Loops on Large Arrays** ❌

```python
# Slow (1000x slower!):
result = []
for x in big_array:
    result.append(x ** 2)

# Fast (vectorized):
result = big_array ** 2
```

**Rule:** If you write `for` loop on NumPy array, pause and think "Can I vectorize?"

---

## 📊 Progress Tracking

### Module Checklist:

#### NumPy Basics:
- [ ] Understand arrays vs lists
- [ ] Create arrays (zeros, ones, arange, random)
- [ ] Indexing & slicing proficiency
- [ ] Boolean indexing mastery
- [ ] Reshape & transpose arrays
- [ ] Compute statistics (mean, std, etc.)
- [ ] Understand broadcasting
- [ ] Matrix multiplication
- [ ] Complete all exercises with validation ✅

#### Pandas DataFrames (when available):
- [ ] Load CSV/Excel files
- [ ] Explore data (head, info, describe)
- [ ] Select columns & rows
- [ ] Filter with conditions
- [ ] Handle missing values
- [ ] Group & aggregate
- [ ] Merge datasets
- [ ] Feature engineering basics

---

### Skills Self-Assessment:

Rate yourself (1-5) after module completion:

| Skill | Rating | Notes |
|-------|--------|-------|
| Array creation | __/5 | |
| Indexing & slicing | __/5 | |
| Vectorization | __/5 | |
| Broadcasting | __/5 | |
| Reshaping | __/5 | |
| Aggregations | __/5 | |
| Matrix operations | __/5 | |

**Target:** All ≥ 3 before moving to next module

---

## 🎯 Next Steps

### After NumPy Module:

**Option 1: Continue with Pandas** (Recommended)
- Wait for `02_pandas_dataframes.ipynb` release
- Or explore Pandas independently using resources above

**Option 2: Build NumPy Project**
Examples:
- Image processing (load image as array, apply filters)
- Simple linear regression from scratch
- Data normalization pipeline
- Matrix calculator

**Option 3: Start ML Prep**
- Review `03-data-visualization` (when available)
- Or jump to basic ML algorithms prep

---

### After Complete NumPy & Pandas:

You're ready for:
- ✅ Data Visualization (Matplotlib, Seaborn)
- ✅ Machine Learning Fundamentals
- ✅ Real Kaggle datasets analysis
- ✅ Building ML pipelines

---

## 🤝 Need Help?

### When Stuck:

1. **Read error message carefully** - Usually self-explanatory
2. **Print shapes** - `print(arr.shape)` solves 50% of errors
3. **Check documentation** - `np.function_name?` in Jupyter
4. **Google the exact error** - Stack Overflow has answer 99%
5. **Ask in community** - Reddit r/learnpython, Discord servers

---

### Common Questions:

**Q: NumPy vs Pandas - which to learn first?**
A: NumPy! Pandas built on NumPy. Understanding NumPy makes Pandas easier.

**Q: Do I need to memorize all functions?**
A: No! Understand concepts, Google syntax when needed. Cheat sheets helpful.

**Q: How long until fluent?**
A: 2-4 weeks with daily practice. Fluency comes from building projects.

**Q: Can I skip NumPy and just use Pandas?**
A: Technically yes, but NumPy understanding makes you much better data scientist.

---

## 🏆 Achievement Unlocked!

Once you complete this module, you'll have:

- ✅ Mastered NumPy arrays - foundation of all ML
- ✅ Can process data 100x faster than pure Python
- ✅ Ready to handle real datasets
- ✅ Prepared for ML algorithms
- ✅ Skill used by data scientists worldwide

**Congratulations on choosing to invest in this skill!** 🚀

---

*"In data science, NumPy is your best friend. Get to know it well!"*

---

**Ready? Open `01_numpy_basics.ipynb` and start learning!** 📘

*Last updated: April 8, 2026*
