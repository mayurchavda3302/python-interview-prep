# Python String & Collection Utilities Guide

## 1. Slicing (String/List Slicing)

### Use:

Extract a part of a string or list using index positions.

### Syntax:

```python
data[start:end:step]
```

### Example:

```python
text = "Hello World"

print(text[0:5])     # Hello
print(text[6:])      # World
print(text[::-1])    # dlroW olleH (reverse string)
```

### Use Cases:

* Get substring
* Reverse string
* Skip characters

---

## 2. `in` Keyword

### Use:

Check if a value exists inside a string, list, tuple, etc.

### Example:

```python
text = "Hello World"

print("Hello" in text)   # True
print("Hi" in text)      # False
```

### Use Cases:

* Searching
* Condition checks

---

## 3. `.count()`

### Use:

Count how many times a value appears.

### Example:

```python
text = "banana"

print(text.count("a"))   # 3
print(text.count("na"))  # 2
```

### Use Cases:

* Frequency counting
* Pattern occurrence

---

## 4. `.replace()`

### Use:

Replace one substring with another.

### Example:

```python
text = "Hello World"

new_text = text.replace("World", "Python")
print(new_text)   # Hello Python
```

### Use Cases:

* Clean text
* Modify strings
* Data preprocessing

---

## 5. `collections.Counter`

### Use:

Count frequency of elements in a list or string.

### Example:

```python
from collections import Counter

text = "banana"

counter = Counter(text)
print(counter)
# Output: {'b': 1, 'a': 3, 'n': 2}

print(counter['a'])  # 3
```

### Use Cases:

* Frequency analysis
* Finding most common elements

---

## Combined Example

```python
from collections import Counter

text = "hello world"

# slicing
print(text[:5])  # hello

# in
print("world" in text)  # True

# count
print(text.count("l"))  # 3

# replace
print(text.replace("world", "python"))  # hello python

# counter
print(Counter(text))
```

---

## Summary Table

| Feature      | Purpose               |
| ------------ | --------------------- |
| Slicing      | Extract parts of data |
| `in`         | Check existence       |
| `.count()`   | Count occurrences     |
| `.replace()` | Replace text          |
| `Counter`    | Frequency dictionary  |

---
