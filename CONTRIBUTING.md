# 🤝 Contributing to Machine Learning Tutorials

Terima kasih telah ingin berkontribusi! Repository ini bertujuan menjadi **best resource** untuk belajar Machine Learning dengan penjelasan detail dan clarity maksimal.

---

## 🎯 Philosophy Kami

### 1. **Clarity First** 📖
Keterangan tertulis > Code examples. Student harus **understand concept** dulu sebelum lihat code.

### 2. **No Assumptions** 🚫
JANGAN assume student sudah tahu sesuatu. Define everything, explain everything.

### 3. **ML Connection** 🤖  
SETIAP tutorial harus explicitly connect ke Machine Learning. "Kenapa ML engineer perlu tahu ini?"

### 4. **Real-World Focus** 🌍
Contoh harus dari real ML scenarios, bukan toy examples yang tidak relevan.

---

## 📝 Types of Contributions

### 1. Adding New Tutorial

**Steps:**
1. Read [TUTORIAL_TEMPLATE.md](TUTORIAL_TEMPLATE.md) **THOROUGHLY**
2. Create Jupyter notebook following template structure
3. Add module `README.md` (following format in existing modules)
4. Update main `README.md` with new tutorial
5. Test all code
6. Submit PR with description

**Required elements:**
- [ ] Introduction section explaining why this topic matters
- [ ] Every topic has: "Apa itu", "Tentang apa", "Mengapa penting"
- [ ] Analogies for complex concepts (minimum 2 per topic)
- [ ] ML use cases (minimum 3 per tutorial)
- [ ] Exercises with hints (minimum 1 per section)
- [ ] Summary recap at end
- [ ] All code tested and working

### 2. Improving Existing Tutorial

**What to improve:**
- Add keterangan untuk section yang masih kurang penjelasan
- Add analogies untuk clarify difficult concepts
- Add ML use cases yang lebih relevant
- Fix errors or broken code
- Improve exercise quality
- Add visual aids (ASCII diagrams, emoji diagrams)

**Steps:**
1. Identify section that needs improvement
2. Follow [TUTORIAL_TEMPLATE.md](TUTORIAL_TEMPLATE.md) format
3. Make changes
4. Test if code still works
5. Submit PR explaining what improved

### 3. Adding Resources

**Updates to README files:**
- Additional learning resources
- Relevant articles/videos
- Practice platforms
- Cheatsheets

**Steps:**
1. Verify resource is high quality
2. Add brief description (jangan hanya link)
3. Categorize properly
4. Submit PR

### 4. Fixing Bugs/Errors

**Found error?**
1. Open issue describing:
   - Where (file, cell number if notebook)
   - What's wrong
   - Expected vs actual behavior
2. If you can fix: Submit PR referencing issue
3. If not sure: Just report issue, maintainers will fix

---

## 📋 Contribution Guidelines

### Code Style

**Python:**
- Follow PEP 8 style guide
- Use descriptive variable names (no `x`, `y` unless in math context)
- Add comments explaining WHY, not just WHAT
- Keep functions under 20 lines when possible

**Example:**
```python
# ❌ BAD
def f(x):
    return x**2

# ✅ GOOD  
def calculate_squared_values(input_array):
    """
    Square all elements in array for feature engineering.
    
    Args:
        input_array: NumPy array of numeric values
    Returns:
        Array with all values squared
    """
    return input_array ** 2
```

### Markdown Style

- Use proper headers (`##`, `###`, not `**Bold as header**`)
- One blank line before/after headers
- Use code fences with language: ````python`
- Use emoji for visual scanning (but don't overuse)
- Break long paragraphs (max 4-5 lines)

### Cell Structure (Notebooks)

**Markdown cells:**
- Start each section with explanation cell
- Use proper header levels
- Include emoji for section types (📖, 🎯, 💡)

**Code cells:**
- One concept per cell (don't cram multiple unrelated operations)
- Print outputs with explanatory messages
- Use cell like "paragraphs" in essay

**Example structure:**
```
[Markdown] Section intro with "Apa itu"
[Markdown] "Tentang apa ini"
[Markdown] "Mengapa penting"
[Code] Example 1
[Markdown] Explanation of output
[Code] Example 2
[Markdown] Exercise
[Code] Exercise solution space
```

### Commit Messages

Use clear, descriptive messages:

```bash
# ❌ BAD
git commit -m "update"
git commit -m "fix"

# ✅ GOOD
git commit -m "Add keterangan detail untuk NumPy broadcasting section"
git commit -m "Fix IndexError in pandas filtering example"
git commit -m "Add 3 ML use cases for list comprehensions"
```

Format: `[Action] [What] for [Where]`
- Add, Update, Fix, Remove, Refactor, etc.
- Specific change
- Which section/file

---

## 🔍 Review Process

### Before Submitting PR

**Self-review checklist:**
- [ ] Read your own tutorial as if you're student
- [ ] Every code block has explanation before AND after
- [ ] No jargon without definition
- [ ] ML connection is explicit
- [ ] All code tested (run all cells)
- [ ] No typos (run spellcheck)
- [ ] Follows TUTORIAL_TEMPLATE.md structure
- [ ] Markdown renders correctly
- [ ] Links work

### PR Description Template

```markdown
## Type of Change
- [ ] New tutorial
- [ ] Improving existing tutorial
- [ ] Fix bug/error
- [ ] Add resources
- [ ] Update documentation

## Description
[Describe what you changed and why]

## Motivation
[Why is this change needed? What problem does it solve?]

## Changes Made
- Change 1
- Change 2
- Change 3

## Checklist
- [ ] Followed TUTORIAL_TEMPLATE.md
- [ ] All code tested
- [ ] Added keterangan for all topics
- [ ] ML use cases included
- [ ] Exercises included (if new tutorial)
- [ ] Updated relevant README files

## Screenshots (if applicable)
[If changing UI/output, include before/after screenshots]
```

### Maintainer Review

Maintainers will check:
1. **Clarity** - Can beginner understand without prior knowledge?
2. **Completeness** - All mandatory sections present?
3. **ML Relevance** - Connected to ML explicitly?
4. **Code Quality** - Working, well-commented, clean?
5. **Consistency** - Follows repo standards?

Feedback will be provided via PR comments. Address comments and update PR.

---

## 🎓 Tutorial Quality Standards

### Mandatory Elements

Every tutorial section MUST have:

1. **"Apa itu [Konsep]?"** ✅
   - Clear definition (2-3 sentences)
   - Key characteristics listed
   
2. **"Tentang apa ini?"** ✅
   - Context (why it exists)
   - Problem it solves
   - Real-world analogy
   
3. **"Mengapa penting untuk ML?"** ✅
   - Explicit ML connection
   - Minimum 3 use cases with code
   - Libraries that use it

### Quality Checklist

**Content:**
- [ ] Concepts explained before code
- [ ] Analogies for difficult concepts
- [ ] Progression: simple → complex
- [ ] Examples are relevant to ML
- [ ] Common mistakes addressed
- [ ] Pro tips included

**Code:**
- [ ] All code executable
- [ ] Outputs shown and explained
- [ ] Comments explain intent
- [ ] Variable names descriptive
- [ ] Edge cases mentioned

**Exercises:**
- [ ] Clear requirements
- [ ] Hints provided
- [ ] Expected outcome stated
- [ ] Appropriate difficulty

---

## 🚀 Getting Started

### First-Time Contributors

**Step 1: Understand the format**
1. Read [TUTORIAL_TEMPLATE.md](TUTORIAL_TEMPLATE.md)
2. Look at existing notebooks that follow template:
   - `02-numpy-pandas/01_numpy_basics.ipynb`
   - `01-python-basics/01_python_fundamentals.ipynb`

**Step 2: Pick a task**

**Easy first contributions:**
- Add analogies to existing topics
- Improve exercise descriptions
- Add ML use cases to examples
- Fix typos or broken links
- Add comments to code

**Medium contributions:**
- Add new section to existing tutorial
- Improve explanation for difficult topic
- Create better exercises

**Advanced contributions:**
- Create entire new tutorial
- Design new module

**Step 3: Set up**
```bash
# Fork repository
# Clone your fork
git clone https://github.com/YOUR_USERNAME/learning-machine-learning.git
cd learning-machine-learning

# Create branch
git checkout -b feature/your-feature-name

# Make changes
# ...

# Commit
git add .
git commit -m "Your descriptive message"

# Push
git push origin feature/your-feature-name

# Create PR on GitHub
```

**Step 4: Submit PR**
- Fill PR template completely
- Link related issues if any
- Wait for review
- Address feedback

---

## 💡 Tips for Quality Contributions

### Writing Clear Explanations

**DO:**
- ✅ Use simple words (prefer "change" over "modify", "use" over "utilize")
- ✅ Give analogies from everyday life
- ✅ Show "before and after" comparisons
- ✅ Connect to student's existing knowledge
- ✅ Use concrete examples before abstract concepts

**DON'T:**
- ❌ Use jargon without defining
- ❌ Assume prior knowledge
- ❌ Jump to advanced topics too fast
- ❌ Give examples without context
- ❌ Use passive voice excessively

### Creating Good Analogies

**Formula:** `[Complex concept] is like [Everyday thing] because [Shared property]`

**Examples:**
- "NumPy vectorization is like photocopier because both process everything at once instead of one by one"
- "Python dict is like phonebook because both let you look up values by name (key)"
- "Broadcasting is like Excel auto-fill because both automatically expand pattern to multiple cells"

**Good analogy:**
- From everyday experience (not another tech concept)
- Illustrates KEY property of concept
- Easy to visualize mentally
- Student can refer back to it

### ML Connection Examples

**Generic (weak):**
> "This is useful in ML"

**Specific (strong):**
> "In image classification, you'll reshape (batch_size, 28, 28) → (batch_size, 784) to flatten images before passing to dense layer. Do this 1000x per project!"

**Always specify:**
- WHEN in ML workflow (preprocessing? training? evaluation?)
- WHICH ML algorithms/libraries need it
- HOW OFTEN used (every project? occasionally?)
- WHAT breaks if you don't know it

---

## 🤔 Common Questions

### Q: Can I contribute if I'm still learning?
**A:** YES! Best contributors are often learners because you remember what's confusing. Your "beginner questions" help make tutorials clearer!

### Q: Do I need to be ML expert?
**A:** Not for most contributions! Improving explanations, adding analogies, fixing typos - all valuable regardless of ML expertise.

### Q: What if I'm not sure my contribution is good enough?
**A:** Submit anyway! Maintainers will give constructive feedback. All contributions improve through collaboration.

### Q: Can I contribute in Indonesian?
**A:** Most tutorials are bilingual (English + Indonesian), which is perfect! Both languages welcome.

### Q: How long should a tutorial be?
**A:** Quality > length. Rather have 5 pages with great explanations than 20 pages of unexplained code. See template for structure.

### Q: What if I disagree with existing content?
**A:** Open issue explaining your concern with specific example. If valid, maintainers will discuss best approach.

---

## 📞 Get Help

**Stuck or have questions?**

1. **Check existing resources first:**
   - [TUTORIAL_TEMPLATE.md](TUTORIAL_TEMPLATE.md)
   - [README.md](README.md)
   - Existing notebooks as examples

2. **Open GitHub Issue:**
   - Tag with `question` label
   - Be specific about what's unclear

3. **Contact maintainers:**
   - Via GitHub discussions
   - Reference which contribution you're planning

---

## 🙏 Recognition

Contributors will be:
- Listed in main README.md
- Credited in specific tutorials they improve
- Thanked in repository

Your contributions help thousands of learners! 🎉

---

## 📜 Code of Conduct

### Our Pledge

We are committed to providing a **welcoming, supportive, and harassment-free** environment for everyone, regardless of:
- Experience level (beginners welcome!)
- Technical background
- Language proficiency
- Location or timezone
- Any personal characteristic

### Expected Behavior

- ✅ Be respectful and constructive in feedback
- ✅ Assume good intentions
- ✅ Focus on what is best for learners
- ✅ Be patient with beginners
- ✅ Provide helpful, specific feedback
- ✅ Acknowledge others' contributions

### Unacceptable Behavior

- ❌ Harassment or discriminatory comments
- ❌ Personal attacks or insults
- ❌ Dismissing questions as "stupid" or "obvious"
- ❌ Gatekeeping ("you shouldn't learn ML if you don't know X")
- ❌ Plagiarism or claiming others' work

**Violations:** Report to maintainers. We take this seriously.

---

## 🎯 Final Words

**Remember:**

> "Good tutorial explains the code.  
> Great tutorial explains the WHY.  
> Excellent tutorial transforms understanding."

Your contributions make learning accessible to more people! Every:
- Analogy you add
- Explanation you clarify
- Example you improve
- Bug you fix

...helps someone understand better. **Thank you for contributing!** 🚀

---

*Last updated: April 8, 2026*
