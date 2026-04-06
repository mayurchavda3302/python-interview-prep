# 📘 Python Interview Questions — Complete Practice Bank
### Junior Developer | 1 Year Experience | ~100+ Questions

> Solve 3–5 daily. Write code first, then check. Always test edge cases.

---

# 🔤 SECTION 1: STRINGS

> **Tip:** Master slicing, `in`, `.count()`, `.replace()`, `collections.Counter`

---

### Q1. Reverse a String
**Input:** `"Hello"`
**Output:** `"olleH"`
**Methods to try:** Slicing `[::-1]`, loop, `reversed()`

---

### Q2. Check if String is a Palindrome
**Input:** `"madam"` → `True` | `"hello"` → `False`
**Edge cases:** Empty string, single char, uppercase mix

---

### Q3. Count Vowels and Consonants
**Input:** `"programming"`
**Output:** Vowels: `3`, Consonants: `8`

---

### Q4. First Non-Repeating Character
**Input:** `"aabbcde"` → `"c"` | `"aabb"` → `None`
**Hint:** Use `OrderedDict` or loop with `count()`

---

### Q5. Remove Duplicate Characters (Keep Order)
**Input:** `"aabbcc"` → `"abc"` | `"banana"` → `"ban"`
**Hint:** Use `dict.fromkeys()` or a seen set

---

### Q6. Check if Two Strings are Anagrams
**Input:** `"listen"`, `"silent"` → `True`
**Input:** `"hello"`, `"world"` → `False`
**Hint:** Sort both or use Counter

---

### Q7. Longest Substring Without Repeating Characters
**Input:** `"abcabcbb"` → `3` (`"abc"`)
**Input:** `"bbbbb"` → `1`
**Hint:** Sliding window + set

---

### Q8. Count Character Frequency
**Input:** `"aabbc"` → `{'a': 2, 'b': 2, 'c': 1}`
**Hint:** Use `collections.Counter` or manual dict

---

### Q9. Replace Spaces with `%20`
**Input:** `"Mr John Smith"` → `"Mr%20John%20Smith"`
**Methods:** `.replace()`, manual loop

---

### Q10. Check if String is a Rotation of Another
**Input:** `"waterbottle"`, `"erbottlewat"` → `True`
**Hint:** Check if s2 is in s1+s1

---

### Q11. Find All Substrings of a String
**Input:** `"abc"` → `["a", "ab", "abc", "b", "bc", "c"]`

---

### Q12. String Compression
**Input:** `"aabcccdd"` → `"a2b1c3d2"`
**Edge case:** If compressed is longer, return original

---

### Q13. Reverse Words in a Sentence
**Input:** `"Hello World"` → `"World Hello"`
**Input:** `"  spaces  here  "` → handle extra spaces

---

### Q14. Check if String Contains Only Digits
**Input:** `"12345"` → `True` | `"123a5"` → `False`
**Methods:** `.isdigit()`, manual loop, regex

---

### Q15. Find the Most Frequent Character
**Input:** `"aabbccca"` → `'c'`

---

# 📚 SECTION 2: LISTS

> **Tip:** Practice in-place operations, two-pointer, and sorting tricks

---

### Q16. Find Maximum and Minimum in a List
**Input:** `[3, 1, 9, 4]` → Max: `9`, Min: `1`
**Try:** Without built-in `max()`/`min()`

---

### Q17. Find Second Largest Number
**Input:** `[10, 20, 4, 45, 99]` → `45`
**Edge case:** List with all same elements

---

### Q18. Remove Duplicates from List (Preserve Order)
**Input:** `[1, 1, 2, 3, 2]` → `[1, 2, 3]`

---

### Q19. Find All Pairs with Given Sum
**Input:** `[1, 5, 3, 2, 4]`, target=`5`
**Output:** `[(1,4), (3,2)]`

---

### Q20. Rotate List Left by K positions
**Input:** `[1,2,3,4,5]`, k=`2` → `[3,4,5,1,2]`

---

### Q21. Rotate List Right by K positions
**Input:** `[1,2,3,4,5]`, k=`2` → `[4,5,1,2,3]`

---

### Q22. Flatten a Nested List (One Level)
**Input:** `[[1,2],[3,4],[5]]` → `[1,2,3,4,5]`

---

### Q23. Flatten a Deeply Nested List (Recursive)
**Input:** `[1,[2,[3,[4]]],5]` → `[1,2,3,4,5]`

---

### Q24. Move All Zeros to End
**Input:** `[0,1,0,3,12]` → `[1,3,12,0,0]`
**Constraint:** Do it in-place

---

### Q25. Find Missing Number (1 to N)
**Input:** `[1,2,4,5,6]` → `3`
**Hint:** Use sum formula: `n*(n+1)/2`

---

### Q26. Find All Duplicates in a List
**Input:** `[1,2,3,2,4,3]` → `[2, 3]`

---

### Q27. Merge Two Sorted Lists
**Input:** `[1,3,5]`, `[2,4,6]` → `[1,2,3,4,5,6]`

---

### Q28. Kadane's Algorithm — Maximum Subarray Sum
**Input:** `[-2,1,-3,4,-1,2,1,-5,4]` → `6` (subarray: `[4,-1,2,1]`)

---

### Q29. Count Occurrences of Each Element
**Input:** `[1,2,2,3,3,3]` → `{1:1, 2:2, 3:3}`

---

### Q30. Sort List Without Using sort()
**Practice:** Bubble sort, Selection sort — understand the logic

---

### Q31. Find Intersection of Two Lists
**Input:** `[1,2,3,4]`, `[3,4,5,6]` → `[3,4]`

---

### Q32. Split List into Chunks of Size N
**Input:** `[1,2,3,4,5,6,7]`, n=`3` → `[[1,2,3],[4,5,6],[7]]`

---

# 📦 SECTION 3: DICTIONARY

---

### Q33. Count Frequency of Elements in a List
**Input:** `[1,2,2,3,3,3]` → `{1:1, 2:2, 3:3}`

---

### Q34. Merge Two Dictionaries
**Input:** `{'a':1}`, `{'b':2}` → `{'a':1, 'b':2}`
**Methods:** `{**d1, **d2}`, `.update()`, `|` operator (Python 3.9+)

---

### Q35. Sort Dictionary by Value (Ascending & Descending)
**Input:** `{'a':3, 'b':1, 'c':2}` → `{'b':1, 'c':2, 'a':3}`

---

### Q36. Find Key with Maximum Value
**Input:** `{'a':10, 'b':30, 'c':20}` → `'b'`

---

### Q37. Invert a Dictionary (Swap Keys and Values)
**Input:** `{'a':1, 'b':2}` → `{1:'a', 2:'b'}`

---

### Q38. Group Anagrams Together
**Input:** `["eat","tea","tan","ate","nat","bat"]`
**Output:** `[["eat","tea","ate"],["tan","nat"],["bat"]]`

---

### Q39. Two Sum Using Hashmap
**Input:** `[2,7,11,15]`, target=`9` → `[0,1]`
**Hint:** Store `{value: index}` while iterating

---

### Q40. Remove Keys with None Values
**Input:** `{'a':1, 'b':None, 'c':3}` → `{'a':1, 'c':3}`

---

### Q41. Check if Two Dicts are Equal
**Input:** `{'a':1, 'b':2}`, `{'b':2, 'a':1}` → `True`

---

### Q42. Nested Dictionary — Access and Update
**Input:** `{'person': {'name': 'Alice', 'age': 25}}`
**Task:** Update age to 26

---

# 🔗 SECTION 4: SETS

---

### Q43. Remove Duplicates from a List Using Set
**Input:** `[1,1,2,3,2]` → `{1,2,3}`

---

### Q44. Find Intersection of Two Lists
**Input:** `[1,2,3]`, `[2,3,4]` → `{2,3}`

---

### Q45. Find Union of Two Lists
**Input:** `[1,2,3]`, `[3,4,5]` → `{1,2,3,4,5}`

---

### Q46. Find Difference (Elements in A but not B)
**Input:** `{1,2,3,4}`, `{3,4,5}` → `{1,2}`

---

### Q47. Check if One Set is Subset of Another
**Input:** `{1,2}`, `{1,2,3,4}` → `True`

---

### Q48. Symmetric Difference (Elements in Either but not Both)
**Input:** `{1,2,3}`, `{3,4,5}` → `{1,2,4,5}`

---

# ⚙️ SECTION 5: FUNCTIONS + LAMBDA + COMPREHENSIONS

---

### Q49. Fibonacci — Iterative
**Input:** `n=7` → `[0,1,1,2,3,5,8]`

---

### Q50. Fibonacci — Recursive
**Input:** `n=6` → `8`
**Edge case:** n=0 → 0, n=1 → 1

---

### Q51. Factorial — Iterative + Recursive
**Input:** `5` → `120` | `0` → `1`

---

### Q52. Check if a Number is Prime
**Input:** `7` → `True` | `10` → `False`
**Optimize:** Check only up to `sqrt(n)`

---

### Q53. GCD of Two Numbers
**Input:** `12, 8` → `4`
**Methods:** Euclidean algorithm + `math.gcd()`

---

### Q54. LCM of Two Numbers
**Input:** `4, 6` → `12`
**Formula:** `lcm = a*b // gcd(a,b)`

---

### Q55. Lambda: Sort List of Dicts by a Key
**Input:** `[{'name':'Bob','age':25},{'name':'Alice','age':22}]`
**Output:** Sorted by age → Alice first

---

### Q56. Map: Square All Elements
**Input:** `[1,2,3,4]` → `[1,4,9,16]`

---

### Q57. Filter: Keep Only Even Numbers
**Input:** `[1,2,3,4,5,6]` → `[2,4,6]`

---

### Q58. Reduce: Find Product of All Elements
**Input:** `[1,2,3,4]` → `24`
**Hint:** Use `functools.reduce`

---

### Q59. List Comprehension: Squares of Even Numbers
**Input:** `range(1,11)` → `[4,16,36,64,100]`

---

### Q60. Dict Comprehension: Word Length Map
**Input:** `["apple","hi","banana"]` → `{'apple':5,'hi':2,'banana':6}`

---

### Q61. *args — Sum of Any Number of Arguments
```python
def total(*args): ...
total(1,2,3) → 6
total(5,10) → 15
```

---

### Q62. **kwargs — Print Key-Value Pairs
```python
def display(**kwargs): ...
display(name="Alice", age=22) → name: Alice, age: 22
```

---

# 🔁 SECTION 6: RECURSION

---

### Q63. Sum of Digits Using Recursion
**Input:** `1234` → `10`

---

### Q64. Reverse String Using Recursion
**Input:** `"hello"` → `"olleh"`

---

### Q65. Power of a Number (x^n) Using Recursion
**Input:** `2, 10` → `1024`

---

### Q66. Count Occurrences Using Recursion
**Input:** `[1,2,1,3,1]`, target=`1` → `3`

---

### Q67. Tower of Hanoi (Understand the Logic)
**Input:** `n=3` discs → print all moves
**Great for:** Recursion understanding in interviews

---

# 📂 SECTION 7: FILE HANDLING

---

### Q68. Read a File and Print All Lines
```python
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())
```

---

### Q69. Count Words, Lines, and Characters in a File
**Output:** Lines: 5, Words: 30, Characters: 180

---

### Q70. Find the Most Common Word in a File
**Hint:** Split → Counter → most_common(1)

---

### Q71. Write a List to a File (One Item Per Line)
**Input:** `["apple", "banana", "cherry"]`

---

### Q72. Append to an Existing File
```python
with open("file.txt", "a") as f:
    f.write("New line\n")
```

---

### Q73. Read a CSV File and Print as Dictionary
**Hint:** Use `csv.DictReader`

---

### Q74. Copy Content from One File to Another

---

# ⚠️ SECTION 8: EXCEPTION HANDLING

---

### Q75. Handle Division by Zero
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

### Q76. Handle Multiple Exceptions
```python
try:
    x = int("abc")
    y = 10 / 0
except ValueError:
    ...
except ZeroDivisionError:
    ...
```

---

### Q77. Use `finally` Block
**Concept:** `finally` always runs — use for cleanup (close file, DB connection)

---

### Q78. Create a Custom Exception Class
```python
class NegativeValueError(Exception):
    def __init__(self, value):
        super().__init__(f"Negative value not allowed: {value}")
```

---

### Q79. Raise an Exception Manually
```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
```

---

### Q80. Exception in a Loop — Continue After Error
**Task:** Loop over a list, skip items that cause errors

---

# 🧱 SECTION 9: OOP (Very Important — Always Asked)

---

### Q81. Create a Basic Class and Object
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

### Q82. Instance Variable vs Class Variable
```python
class Counter:
    count = 0              # class variable
    def __init__(self):
        Counter.count += 1
```

---

### Q83. Single Inheritance
```python
class Animal:
    def speak(self): ...

class Dog(Animal):
    def speak(self): return "Woof"
```

---

### Q84. Multiple Inheritance
```python
class A: ...
class B: ...
class C(A, B): ...   # What is MRO here?
```
**Know:** MRO (Method Resolution Order) — use `C.__mro__`

---

### Q85. Multilevel Inheritance
```python
class GrandParent → Parent → Child
```

---

### Q86. Method Overriding
**Child class overrides a method of Parent class**

---

### Q87. Encapsulation — Private Variables
```python
class BankAccount:
    def __init__(self):
        self.__balance = 0       # private
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
```

---

### Q88. Polymorphism
**Same method name, different behavior**
```python
class Cat:
    def sound(self): return "Meow"
class Dog:
    def sound(self): return "Woof"
```

---

### Q89. Abstract Class
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass

class Circle(Shape):
    def area(self): return 3.14 * r * r
```

---

### Q90. Dunder / Magic Methods
```python
class Vector:
    def __init__(self, x, y): ...
    def __add__(self, other): ...    # v1 + v2
    def __str__(self): ...           # print(v1)
    def __len__(self): ...           # len(v1)
    def __eq__(self, other): ...     # v1 == v2
```

---

### Q91. @property Decorator in Class
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
```

---

### Q92. classmethod vs staticmethod
```python
class MyClass:
    @classmethod
    def from_string(cls, s): ...    # has access to class
    @staticmethod
    def helper(): ...               # no access to class or instance
```

---

# 🧠 SECTION 10: ADVANCED PYTHON

---

### Q93. Basic Decorator
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def say_hello(): print("Hello")
```

---

### Q94. Logger Decorator — Log Every Function Call
```python
import functools

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        return func(*args, **kwargs)
    return wrapper
```

---

### Q95. Timer Decorator — Measure Execution Time
```python
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Time: {time.time()-start:.4f}s")
        return result
    return wrapper
```

---

### Q96. Generator Function — yield vs return
```python
def count_up(n):
    for i in range(n):
        yield i

gen = count_up(5)
next(gen)   # 0
next(gen)   # 1
```
**Use case:** Reading large files line by line, infinite sequences

---

### Q97. Generator for Large File Processing
```python
def read_large_file(path):
    with open(path) as f:
        for line in f:
            yield line.strip()
```

---

### Q98. Custom Iterator Class
```python
class CountDown:
    def __init__(self, n): self.n = n
    def __iter__(self): return self
    def __next__(self):
        if self.n <= 0: raise StopIteration
        self.n -= 1
        return self.n + 1
```

---

### Q99. Closure — Function Remembers Outer Scope
```python
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
double(5)   # 10
```

---

### Q100. Simple Caching with Dictionary
```python
cache = {}
def fib(n):
    if n in cache: return cache[n]
    if n <= 1: return n
    cache[n] = fib(n-1) + fib(n-2)
    return cache[n]
```

---

### Q101. @lru_cache (Built-in Memoization)
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
```

---

# 🧪 SECTION 11: TRICKY / THEORY QUESTIONS

> These are almost always asked verbally. Know them cold.

---

### Q102. Mutable vs Immutable — with examples
- **Immutable:** int, float, str, tuple, bool, frozenset
- **Mutable:** list, dict, set
```python
a = [1,2,3]
b = a
b.append(4)
print(a)    # [1,2,3,4] — both point to same object!
```

---

### Q103. `is` vs `==`
```python
a = [1,2,3]
b = [1,2,3]
a == b    # True  (same value)
a is b    # False (different objects)
```

---

### Q104. Deep Copy vs Shallow Copy
```python
import copy
original = [[1,2],[3,4]]
shallow = copy.copy(original)      # inner lists still shared
deep = copy.deepcopy(original)     # fully independent
```

---

### Q105. Default Mutable Argument Bug
```python
# WRONG:
def add_item(item, lst=[]):
    lst.append(item)
    return lst

# RIGHT:
def add_item(item, lst=None):
    if lst is None: lst = []
    lst.append(item)
    return lst
```

---

### Q106. LEGB Rule (Scope in Python)
- **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in
```python
x = "global"
def outer():
    x = "enclosing"
    def inner():
        print(x)    # "enclosing" — not global
    inner()
```

---

### Q107. `global` and `nonlocal` Keywords
```python
count = 0
def increment():
    global count
    count += 1

def outer():
    x = 10
    def inner():
        nonlocal x
        x += 1
```

---

### Q108. List vs Tuple vs Set — When to Use Which
| Type | Ordered | Mutable | Duplicates | Use When |
|---|---|---|---|---|
| List | ✅ | ✅ | ✅ | Ordered, changeable collection |
| Tuple | ✅ | ❌ | ✅ | Fixed data, dict keys, unpacking |
| Set | ❌ | ✅ | ❌ | Uniqueness, membership tests |

---

### Q109. Python Memory Management (Basic)
- Python uses **reference counting** + **garbage collector**
- `id(obj)` returns memory address
- Small integers (-5 to 256) are cached/interned

---

### Q110. Generator vs List — Memory Difference
```python
# List — stores all in memory
squares_list = [x**2 for x in range(1000000)]

# Generator — computes one at a time
squares_gen = (x**2 for x in range(1000000))
```

---

### Q111. `__str__` vs `__repr__`
- `__str__` → for end users (readable)
- `__repr__` → for developers (unambiguous, used in debugger)

---

### Q112. `pass`, `continue`, `break` — Difference
```python
for i in range(5):
    if i == 2: pass       # does nothing, continues loop body
    if i == 3: continue   # skips rest of this iteration
    if i == 4: break      # exits loop entirely
```

---

# 🔥 SECTION 12: REAL INTERVIEW PROBLEMS

---

### Q113. Two Sum
**Input:** `[2,7,11,15]`, target=`9` → `[0,1]`
**Approach:** Hashmap O(n)

---

### Q114. Valid Parentheses
**Input:** `"()[]{}"` → `True` | `"(]"` → `False`
**Approach:** Stack

---

### Q115. Palindrome — Optimized (Two Pointer)
**Input:** `"racecar"` → `True`
```python
def is_palindrome(s):
    l, r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]: return False
        l += 1; r -= 1
    return True
```

---

### Q116. Longest Common Prefix
**Input:** `["flower","flow","flight"]` → `"fl"`
**Approach:** Zip + set, or sort + compare first/last

---

### Q117. Merge Intervals
**Input:** `[[1,3],[2,6],[8,10],[15,18]]`
**Output:** `[[1,6],[8,10],[15,18]]`
**Approach:** Sort + merge

---

### Q118. Top K Frequent Elements
**Input:** `[1,1,1,2,2,3]`, k=`2` → `[1,2]`
**Approach:** Counter + most_common(k)

---

### Q119. Find Duplicate in Array (Single Duplicate)
**Input:** `[1,3,4,2,2]` → `2`
**Approach:** Set or Floyd's algorithm

---

### Q120. Log File Analyzer — Count Error Types
```python
# Given a log file with lines like:
# "ERROR: disk full"
# "WARNING: low memory"
# Count occurrences of each log level
```

---

### Q121. URL Parser (Without urllib)
**Input:** `"https://www.example.com/path?name=Alice&age=22"`
**Extract:** scheme, domain, path, params

---

### Q122. FizzBuzz (Classic but still asked)
- Multiples of 3 → "Fizz"
- Multiples of 5 → "Buzz"
- Both → "FizzBuzz"
- Otherwise → number

---

### Q123. Balanced Brackets Check (Extended)
**Input:** `"{[()]}"` → `True` | `"[{]}"` → `False`

---

### Q124. Roman Numeral to Integer
**Input:** `"XIV"` → `14` | `"IX"` → `9`

---

### Q125. Count Islands (Concept Level)
**Input:** Grid of 0s and 1s — count connected regions of 1s
**Approach:** DFS/BFS on grid (good to explain even if not fully coded)

---

# 📌 DAILY PRACTICE TEMPLATE

Copy this for each question you solve:

```
Question: [Name]
Date: [Date]
Time taken: [X minutes]

Approach:
[Describe your thinking]

Code:
[Paste your solution]

Edge cases tested:
- [ ] Empty input
- [ ] Single element
- [ ] Negative numbers
- [ ] Duplicates

Mistakes made:
[Write what went wrong]

Optimized?
[ ] Yes — O(?) time, O(?) space
```

---

# ⏱️ Time Complexity Quick Reference

| Algorithm / Operation | Time |
|---|---|
| Access list by index | O(1) |
| Append to list | O(1) amortized |
| Search in list | O(n) |
| Search in set/dict | O(1) avg |
| Sort | O(n log n) |
| Binary search | O(log n) |

---

> 🏆 Complete every question here → You are ready for junior Python interviews.
> Remember: It's not about memorising — it's about thinking clearly under pressure.