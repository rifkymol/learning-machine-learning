# 🚨 Common Mistakes & How to Avoid Them

## 📖 Tentang Dokumen Ini

Dokumen ini compile **kesalahan umum** yang sering dibuat beginner saat belajar Python dan Machine Learning. Learn from others' mistakes - jangan repeat mereka!

**Format setiap section:**
- ❌ **Mistake:** Apa yang salah
- 🤔 **Why it happens:** Mengapa common  
- ✅ **Correct way:** Cara yang benar
- 💡 **Tip:** How to remember/avoid

---

## 🐍 PYTHON BASICS MISTAKES

### 1. Indentation Errors ❌

**Mistake:**
```python
# Salah - inconsistent indentation
def calculate_sum(a, b):
result = a + b  # ← No indentation!
    return result  # ← Too much indentation!
```

**Error you'll see:**
```
IndentationError: expected an indented block
```

**Why it happens:**
- Python uses indentation untuk define code blocks
- Mixing tabs dan spaces
- Not consistent dengan levels

**Correct way:**
```python
# Benar - consistent indentation (4 spaces)
def calculate_sum(a, b):
    result = a + b  # ← Indented properly
    return result   # ← Same level
```

**Tip:** 
- Use 4 spaces (Python convention)
- Configure editor untuk convert tabs → spaces
- In VS Code: Set "Tab Size" to 4

---

### 2. Forgetting Colons (:) ❌

**Mistake:**
```python
# Salah - missing colon
if age > 18
    print("Adult")

for i in range(10)
    print(i)

def greet(name)
    return f"Hello {name}"
```

**Error:**
```
SyntaxError: invalid syntax
```

**Why it happens:**
Coming from languages like Java/C++ yang tidak use colons

**Correct way:**
```python
# Benar - colons added
if age > 18:  # ← Colon here
    print("Adult")

for i in range(10):  # ← And here
    print(i)

def greet(name):  # ← And here
    return f"Hello {name}"
```

**Tip:** Remember - "if, for, while, def, class" always end with colon!

---

### 3. Using = Instead of == ❌

**Mistake:**
```python
# Salah - assignment instead of comparison
if age = 18:  # ← Assignment (=), not comparison
    print("Exactly 18")
```

**Error:**
```
SyntaxError: invalid syntax
```

**Why it happens:**
- `=` assigns value
- `==` compares value
- Easy to confuse

**Correct way:**
```python
# Benar - use == for comparison
if age == 18:  # ← Comparison (==)
    print("Exactly 18")

# Assignment (=) is different context:
age = 18  # ← This assigns value
```

**Tip:**
- `=` → "becomes" or "is assigned to"
- `==` → "equals" or "is equal to"
- `===` doesn't exist in Python (unlike JavaScript)

---

### 4. Modifying List While Iterating ❌

**Mistake:**
```python
# Salah - modifying list during iteration
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # ← Dangerous!

# Result: [1, 3, 5] - looks okay
# But: [1, 2, 2, 3, 4, 5] → [1, 2, 3, 5] - skips elements!
```

**Why it happens:**
Iterator gets confused when list size changes

**Correct way:**
```python
# Option 1: Create new list
numbers = [1, 2, 3, 4, 5]
odd_numbers = [num for num in numbers if num % 2 != 0]
# Result: [1, 3, 5]

# Option 2: Iterate over copy
numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:  # ← [:] creates copy
    if num % 2 == 0:
        numbers.remove(num)
```

**Tip:** Never modify collection you're iterating over. Use list comprehension instead!

---

### 5. Mutable Default Arguments ❌

**Mistake:**
```python
# Salah - mutable default argument
def add_item(item, my_list=[]):  # ← Dangerous!
    my_list.append(item)
    return my_list

# Unexpected behavior:
print(add_item(1))  # [1] ✓
print(add_item(2))  # [1, 2] ← Wait, what?!
print(add_item(3))  # [1, 2, 3] ← List persists!
```

**Why it happens:**
Default arguments evaluated ONCE when function defined, bukan every call

**Correct way:**
```python
# Benar - use None as default
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []  # ← Fresh list each call
    my_list.append(item)
    return my_list

# Expected behavior:
print(add_item(1))  # [1] ✓
print(add_item(2))  # [2] ✓
print(add_item(3))  # [3] ✓
```

**Tip:** NEVER use mutable objects (list, dict, set) as default arguments. Use None instead.

---

### 6. Not Returning Value from Function ❌

**Mistake:**
```python
# Salah - function doesn't return
def calculate_total(prices):
    total = sum(prices)
    # ← Missing return!

result = calculate_total([10, 20, 30])
print(result)  # None ← Not what we wanted!
```

**Why it happens:**
Forgetting return statement - function returns None by default

**Correct way:**
```python
# Benar - explicit return
def calculate_total(prices):
    total = sum(prices)
    return total  # ← Return the value

result = calculate_total([10, 20, 30])
print(result)  # 60 ✓
```

**Tip:** If function computes something, make sure to `return` it!

---

## 🔢 NUMPY MISTAKES

### 7. Using Python Loops on NumPy Arrays ❌

**Mistake:**
```python
# Salah - slow loop
import numpy as np
arr = np.random.rand(1000000)

# DON'T do this:
result = []
for x in arr:
    result.append(x ** 2)  # Takes seconds...
```

**Why it happens:**
Thinking in Python lists, not NumPy arrays

**Correct way:**
```python
# Benar - vectorized operation
arr = np.random.rand(1000000)
result = arr ** 2  # 100x faster!
```

**Tip:** If you write `for` loop on NumPy array, pause! Can you vectorize?

---

### 8. Not Checking Array Shapes ❌

**Mistake:**
```python
# Salah - ignoring shapes
a = np.random.rand(100, 10)
b = np.random.rand(100)

result = a + b  # Works, but is it what you wanted?
```

**Error (sometimes):**
```
ValueError: operands could not be broadcast together...
```

**Why it happens:**
Not understanding broadcasting rules

**Correct way:**
```python
# Benar - check shapes first
a = np.random.rand(100, 10)
b = np.random.rand(100)

print(f"a.shape: {a.shape}")  # (100, 10)
print(f"b.shape: {b.shape}")  # (100,)

# Reshape if needed:
b_reshaped = b.reshape(-1, 1)  # (100, 1)
result = a + b_reshaped  # Now explicit!
```

**Tip:** ALWAYS print shapes when debugging: `print(arr.shape)`

---

### 9. Array Copying Pitfall ❌

**Mistake:**
```python
# Salah - not a copy!
a = np.array([1, 2, 3])
b = a  # ← NOT a copy, just another reference!

b[0] = 999
print(a)  # [999, 2, 3] ← a changed too!
```

**Why it happens:**
Assignment creates reference, not copy

**Correct way:**
```python
# Option 1: Explicit copy
a = np.array([1, 2, 3])
b = a.copy()  # ← Real copy

b[0] = 999
print(a)  # [1, 2, 3] ← a unchanged ✓
print(b)  # [999, 2, 3] ← b changed ✓

# Option 2: Use np.copy()
b = np.copy(a)
```

**Tip:** When modifying array, always ask: "Do I need a copy?"

---

### 10. Confusing axis Parameter ❌

**Mistake:**
```python
# Salah - confused about axis
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Want sum per row, but:
row_sums = np.sum(arr, axis=0)  # ← Wrong axis!
print(row_sums)  # [5, 7, 9] ← Column sums!
```

**Why it happens:**
axis parameter is confusing - axis=0 means "along rows" not "of rows"

**Correct way:**
```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Sum per row (across columns):
row_sums = np.sum(arr, axis=1)  # ← axis=1
print(row_sums)  # [6, 15] ✓

# Sum per column (across rows):
col_sums = np.sum(arr, axis=0)  # ← axis=0
print(col_sums)  # [5, 7, 9] ✓
```

**Tip:**
- axis=0: "compress rows" → result shape loses row dimension
- axis=1: "compress columns" → result shape loses column dimension
- Or just try both and see which makes sense!

---

## 🐼 PANDAS MISTAKES

### 11. Modifying DataFrame Copy ❌

**Mistake:**
```python
# Salah - modifying copy, not original
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3]})

# This doesn't modify df:
df['A'][0] = 999  # SettingWithCopyWarning!

print(df)  # Still [1, 2, 3] - unchanged!
```

**Warning:**
```
SettingWithCopyWarning: A value is trying to be set on a copy...
```

**Why it happens:**
Chained indexing creates temporary copy

**Correct way:**
```python
# Benar - use .loc or .iloc
df = pd.DataFrame({'A': [1, 2, 3]})

# Option 1: loc
df.loc[0, 'A'] = 999  # ← Direct access

# Option 2: at (faster for single value)
df.at[0, 'A'] = 999

print(df)  # [999, 2, 3] ✓
```

**Tip:** Always use `.loc[]` or `.iloc[]` untuk modify DataFrame!

---

### 12. Forgetting inplace Parameter ❌

**Mistake:**
```python
# Salah - expecting in-place modification
df = pd.DataFrame({'A': [3, 1, 2]})
df.sort_values('A')  # ← Returns NEW DataFrame
print(df)  # [3, 1, 2] ← Unchanged!
```

**Why it happens:**
Most Pandas methods return NEW DataFrame by default

**Correct way:**
```python
# Option 1: inplace=True
df = pd.DataFrame({'A': [3, 1, 2]})
df.sort_values('A', inplace=True) # ← Modify in place
print(df)  # [1, 2, 3] ✓

# Option 2: Reassign (preferred)
df = df.sort_values('A')  # ← Reassign
print(df)  # [1, 2, 3] ✓
```

**Tip:** Check documentation - does method return new DF or modify in-place?

---

## 🤖 MACHINE LEARNING MISTAKES

### 13. Training on All Data ❌

**Mistake:**
```python
# Salah - no train/test split
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)  # ← Training on ALL data
score = model.score(X, y)  # ← Testing on SAME data!
print(f"Accuracy: {score}")  # 99%! ← Misleading!
```

**Why it happens:**
Tidak understand konsep overfitting

**Correct way:**
```python
# Benar - proper train/test split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)  # ← Train on training set
score = model.score(X_test, y_test)  # ← Test on unseen data
print(f"Accuracy: {score}")  # More realistic score
```

**Tip:** ALWAYS split data! Never test on training data!

---

###14. Not Scaling Features ❌

**Mistake:**
```python
# Salah - features not scaled
data = np.array([[25, 50000],  # Age, Income
                 [30, 60000],
                 [35, 70000]])

# Some algorithms sensitive to scale
model.fit(data, labels)  # ← Income dominates!
```

**Why it happens:**
Not understanding feature scaling importance

**Correct way:**
```python
# Benar - scale features
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Now both features have similar scale
model.fit(data_scaled, labels)  # ← Better!
```

**Tip:** Scale features for: KNN, SVM, Neural Networks, Gradient Descent

---

### 15. Ignoring Class Imbalance ❌

**Mistake:**
```python
# Salah - imbalanced dataset ignored
# Dataset: 95% class 0, 5% class 1

model.fit(X, y)
accuracy = model.score(X_test, y_test)  # 95%!

# But model just predicts class 0 always!
```

**Why it happens:**
Not looking at class distribution

**Correct way:**
```python
# Check distribution first
print(pd.Series(y).value_counts())
# 0: 9500
# 1: 500  ← Imbalanced!

# Handle imbalance:
# Option 1: Use class_weight
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(class_weight='balanced')

# Option 2: Resampling
from imblearn.over_sampling import SMOTE
X_resampled, y_resampled = SMOTE().fit_resample(X, y)

# Option 3: Use better metrics
from sklearn.metrics import f1_score, precision_recall_curve
# Don't rely on accuracy alone!
```

**Tip:** For imbalanced data, look at precision, recall, F1 - not just accuracy!

---

## 💡 GENERAL LEARNING MISTAKES

### 16. Tutorial Hell ❌

**Mistake:**
- Watching tutorial after tutorial
- Never building anything yourself
- Always following along, never creating

**Why it happens:**
- Watching feels productive
- Building is harder (scary!)
- Tutorial gives false sense of understanding

**Correct way:**
```
Learning cycle:
1. Watch/read tutorial (30% time)
2. Code along (20% time)
3. Build YOUR project (50% time) ← Most important!

Example:
- Learn NumPy arrays → Build image filter from scratch
- Learn Pandas → Analyze your own data (expenses, fitness, etc.)
- Learn ML → Build model for problem YOU care about
```

**Tip:** Rule: For every 1 hour of tutorial, spend 1.5 hours building!

---

### 17. Not Reading Error Messages ❌

**Mistake:**
```
* Error appears *
"Oh no! Panic! Skip to next tutorial!"
```

**Why it happens:**
Error messages scary/intimidating

**Correct way:**
```
* Error appears *

1. READ the message carefully
2. Identify:
   - Error type (NameError, ValueError, etc.)
   - Line number
   - What was expected vs what was received
3. Google EXACT error message
4. Try fix suggested
5. If still stuck, ask for help WITH error message
```

**Example:**
```
IndexError: list index out of range
  File "main.py", line 5, in <module>
    print(my_list[10])
```

**Reading:**
- Error type: IndexError
- Line: 5
- Problem: Accessing index 10, but list too short

**Tip:** Errors are HELPFUL! They tell exactly what's wrong.

---

### 18. Not Taking Breaks❌

**Mistake:**
```
* Study 8 hours straight *
* Brain fried *
* Nothing sticks *
* Burn out *
```

**Why it happens:**
- Feel "I need to hurry"
- Think "More hours = faster learning"

**Correct way:**
```
Session structure:
├─ 25 min focus (Pomodoro)
├─ 5 min break (walk, water, stretch)
├─ Repeat 4x
└─ 30 min longer break

Daily:
├─ Study max 4-6 hours (with breaks)
├─ Sleep 7-8 hours (learning happens during sleep!)
└─ Exercise/outdoor time (brain needs oxygen!)

Weekly:
└─ Take 1-2 full rest days
```

**Tip:** Quality > Quantity. 2 focused hours > 6 unfocused hours!

---

## ✅ Mistake Prevention Checklist

### Before Running Code:

- [ ] Did I import necessary libraries?
- [ ] Are variable names spelled correctly?
- [ ] Do loops/functions have proper indentation?
- [ ] Did I include colons (:) after if/for/def?
- [ ] Am I using `==` for comparison (not `=`)?

### When Working with Arrays:

- [ ] Did I print shapes (`print(arr.shape)`)?
- [ ] Am I modifying original or copy?
- [ ] Can I vectorize instead of loop?
- [ ] Is axis parameter correct?

### When Building ML Models:

- [ ] Did I split train/test?
- [ ] Did I scale features if needed?
- [ ] Did I check class distribution?
- [ ] Am I testing on unseen data?
- [ ] Am I using appropriate metrics?

### When Learning:

- [ ] Am I building, not just watching?
- [ ] Did I take breaks today?
- [ ] Am I reading error messages?
- [ ] Did I ask for help when stuck (didn't waste hours)?

---

## 🎓 Quote Collection

**On Mistakes:**
> "I have not failed. I've just found 10,000 ways that won't work." - Thomas Edison

> "Mistakes are proof that you are trying."

> "The only real mistake is the one from which we learn nothing." - Henry Ford

**On Learning:**
> "Anyone who has never made a mistake has never tried anything new." - Albert Einstein

> "Programming isn't about what you know; it's about what you can figure out." - Chris Pine

---

## 🔄 Keep This Document Updated!

As you learn, add YOUR mistakes here:

```markdown
### [Your Mistake Number]: [Short Description] ❌

**Mistake:**
[Code that was wrong]

**Why it happened:**
[What you were thinking]

**Correct way:**
[Fixed code]

**Tip:**
[How to remember/avoid]
```

**Building this collection will:**
- Help you remember
- Help others learn from your experience
- Create personal reference

---

*"The expert in anything was once a beginner who refused to give up."*

**Keep learning! Keep making mistakes! Keep growing!** 🚀

---

*Last updated: April 8, 2026*
