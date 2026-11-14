# 🗂️ Dictionaries and Sets in Python — Beginner's Guide

Learn how to store data as **key-value pairs** with dictionaries, how to store **unique items** with sets, and how to pick the right data structure for a problem. The lesson ends with a hands-on **student grade tracker** built with dictionaries.

> **Before you start:** this lesson builds on [lists](lists.md), [indexing and slicing](indexing_slicing.md), [list methods](list_methods.md) and [tuples](tuples.md), plus functions, loops and conditions.

## What You'll Learn

- Key-value pairs and dictionary operations
- Sets and their use cases
- Choosing the right data structure for a problem
- Hands-on: build a student grade tracker using dictionaries

## Table of Contents

**Part 1: Dictionaries**

1. [What Is a Dictionary?](#1-what-is-a-dictionary)
2. [Creating Dictionaries](#2-creating-dictionaries)
3. [Accessing Values](#3-accessing-values)
4. [Adding and Changing Items](#4-adding-and-changing-items)
5. [Removing Items](#5-removing-items)
6. [keys(), values() and items()](#6-keys-values-and-items)
7. [Looping Through a Dictionary](#7-looping-through-a-dictionary)
8. [Useful Dictionary Methods](#8-useful-dictionary-methods)
9. [Common Dictionary Patterns](#9-common-dictionary-patterns)
10. [Nested Dictionaries and Lists of Dictionaries](#10-nested-dictionaries-and-lists-of-dictionaries)
11. [Dictionaries and Functions](#11-dictionaries-and-functions)
12. [Common Dictionary Mistakes](#12-common-dictionary-mistakes)

**Part 2: Sets**

13. [What Is a Set?](#13-what-is-a-set)
14. [Creating Sets](#14-creating-sets)
15. [Adding and Removing Items](#15-adding-and-removing-items)
16. [Set Operations: Union, Intersection, Difference](#16-set-operations-union-intersection-difference)
17. [Where Sets Are Useful](#17-where-sets-are-useful)
18. [Common Set Mistakes](#18-common-set-mistakes)

**Part 3: Putting It Together**

19. [Choosing the Right Data Structure](#19-choosing-the-right-data-structure)
20. [Hands-On: Student Grade Tracker](#20-hands-on-student-grade-tracker)
21. [Practice Problems](#21-practice-problems)
22. [Summary](#22-summary)

---

# Part 1: Dictionaries

# 1. What Is a Dictionary?

A **list** finds items by **position** (`marks[0]`). That is awkward when the position has no meaning. Which index is Sara's mark?

A **dictionary** finds items by a **name**, called a **key**. Each key points to a **value**. Together they are a **key-value pair**.

> **Analogy: your phone's contact list.** You look up a **name** (the key) and get a **number** (the value). You do not look up "contact number 17".

> **Analogy: a real dictionary.** You look up a **word** (key) and get its **meaning** (value).

```text
   KEY        VALUE
 "name"   ->  "Ali"
 "age"    ->  15
 "city"   ->  "Karachi"
```

Compare the two ways to store one student:

```python
# With a list: what does student[1] mean? You have to remember.
student_list = ["Ali", 15, "Karachi"]
print(student_list[1])

# With a dictionary: the key says exactly what it is.
student_dict = {"name": "Ali", "age": 15, "city": "Karachi"}
print(student_dict["age"])
```

**Output:**

```text
15
15
```

---

# 2. Creating Dictionaries

Use curly brackets `{ }`. Write each pair as `key: value`, separated by commas.

```python
student = {"name": "Ali", "age": 15, "city": "Karachi"}
prices = {"apple": 120, "banana": 60, "mango": 200}
empty = {}

print(student)
print(prices)
print(empty)
print(type(student))
print(len(student))
```

**Output:**

```text
{'name': 'Ali', 'age': 15, 'city': 'Karachi'}
{'apple': 120, 'banana': 60, 'mango': 200}
{}
<class 'dict'>
3
```

`len()` gives the number of **pairs**.

### Rules for keys and values

| | Rule |
|---|---|
| **Keys** | Must be **unique**. Must be **immutable** (strings, numbers, tuples). |
| **Values** | Can be **anything**: numbers, strings, lists, even other dictionaries. Can repeat. |

```python
data = {
    "name": "Sara",
    "marks": [85, 90, 78],
    "address": {"city": "Lahore", "code": 54000},
    (24.86, 67.01): "Karachi coordinates"
}

print(data["marks"])
print(data["address"])
print(data[(24.86, 67.01)])
```

**Output:**

```text
[85, 90, 78]
{'city': 'Lahore', 'code': 54000}
Karachi coordinates
```

### Duplicate keys: the last one wins

```python
scores = {"Ali": 70, "Sara": 85, "Ali": 99}

print(scores)
```

**Output:**

```text
{'Ali': 99, 'Sara': 85}
```

### Dictionaries keep insertion order

Python remembers the order you added the pairs in. But you still do **not** use position numbers to read them. You use the keys.

---

# 3. Accessing Values

Put the **key** in square brackets.

```python
student = {"name": "Ali", "age": 15, "city": "Karachi"}

print(student["name"])
print(student["age"])
```

**Output:**

```text
Ali
15
```

### A missing key raises a `KeyError`

```python
student = {"name": "Ali", "age": 15}

print(student["phone"])
```

**Error:**

```text
KeyError: 'phone'
```

### `get()`: the safe way

`get(key)` returns `None` if the key is missing instead of crashing. You can also supply a **default** value.

```python
student = {"name": "Ali", "age": 15}

print(student.get("name"))
print(student.get("phone"))
print(student.get("phone", "Not available"))
```

**Output:**

```text
Ali
None
Not available
```

### `in`: does the key exist?

`in` checks the **keys**, not the values.

```python
student = {"name": "Ali", "age": 15}

print("name" in student)
print("phone" in student)
print("Ali" in student)
print("phone" not in student)
```

**Output:**

```text
True
False
False
True
```

```python
student = {"name": "Ali", "age": 15}

if "age" in student:
    print("Age is", student["age"])
else:
    print("No age stored")
```

**Output:**

```text
Age is 15
```

---

# 4. Adding and Changing Items

Use **the same syntax** for both. If the key exists, its value is **changed**. If it does not exist, a new pair is **added**.

```python
student = {"name": "Ali", "age": 15}

student["city"] = "Karachi"
print(student)

student["age"] = 16
print(student)

student["age"] = student["age"] + 1
print(student)
```

**Output:**

```text
{'name': 'Ali', 'age': 15, 'city': 'Karachi'}
{'name': 'Ali', 'age': 16, 'city': 'Karachi'}
{'name': 'Ali', 'age': 17, 'city': 'Karachi'}
```

| `d[key] = value` | What happens |
|---|---|
| Key does **not** exist | A new pair is **added** |
| Key **exists** | The value is **replaced** |

### Adding many pairs at once with `update()`

```python
student = {"name": "Ali", "age": 15}

student.update({"city": "Karachi", "grade": "A"})
print(student)

student.update({"age": 16})
print(student)
```

**Output:**

```text
{'name': 'Ali', 'age': 15, 'city': 'Karachi', 'grade': 'A'}
{'name': 'Ali', 'age': 16, 'city': 'Karachi', 'grade': 'A'}
```

---

# 5. Removing Items

## 5.1 `pop(key)`: remove a pair and get its value

```python
student = {"name": "Ali", "age": 15, "city": "Karachi"}

removed = student.pop("city")

print("Removed:", removed)
print(student)
```

**Output:**

```text
Removed: Karachi
{'name': 'Ali', 'age': 15}
```

You can give `pop()` a default so a missing key does not crash:

```python
student = {"name": "Ali", "age": 15}

print(student.pop("phone", "no phone"))
```

**Output:**

```text
no phone
```

## 5.2 `del`: remove a pair

```python
student = {"name": "Ali", "age": 15, "city": "Karachi"}

del student["age"]
print(student)
```

**Output:**

```text
{'name': 'Ali', 'city': 'Karachi'}
```

## 5.3 `popitem()`: remove the last pair added

```python
student = {"name": "Ali", "age": 15, "city": "Karachi"}

last = student.popitem()

print(last)
print(student)
```

**Output:**

```text
('city', 'Karachi')
{'name': 'Ali', 'age': 15}
```

It returns the removed pair as a **tuple** `(key, value)`.

## 5.4 `clear()`: remove everything

```python
student = {"name": "Ali", "age": 15}

student.clear()
print(student)
```

**Output:**

```text
{}
```

## Removing compared

| | Removes | Returns | If key missing |
|---|---|---|---|
| `pop(key)` | One pair by key | The **value** | `KeyError` (unless you give a default) |
| `del d[key]` | One pair by key | Nothing | `KeyError` |
| `popitem()` | The **last** pair | A `(key, value)` tuple | `KeyError` if empty |
| `clear()` | **Everything** | Nothing | n/a |

---

# 6. keys(), values() and items()

Three methods give you the parts of a dictionary.

```python
student = {"name": "Ali", "age": 15, "city": "Karachi"}

print(student.keys())
print(student.values())
print(student.items())
```

**Output:**

```text
dict_keys(['name', 'age', 'city'])
dict_values(['Ali', 15, 'Karachi'])
dict_items([('name', 'Ali'), ('age', 15), ('city', 'Karachi')])
```

| Method | Gives |
|---|---|
| `keys()` | All the keys |
| `values()` | All the values |
| `items()` | All the pairs, each as a **tuple** `(key, value)` |

Wrap them in `list()` if you want a normal list:

```python
student = {"name": "Ali", "age": 15, "city": "Karachi"}

print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))
```

**Output:**

```text
['name', 'age', 'city']
['Ali', 15, 'Karachi']
[('name', 'Ali'), ('age', 15), ('city', 'Karachi')]
```

### Useful with built-in functions

```python
prices = {"apple": 120, "banana": 60, "mango": 200}

print(len(prices))
print(sum(prices.values()))
print(max(prices.values()))
print(min(prices.values()))
```

**Output:**

```text
3
380
200
60
```

---

# 7. Looping Through a Dictionary

## 7.1 Loop through the keys (default)

```python
prices = {"apple": 120, "banana": 60, "mango": 200}

for fruit in prices:
    print(fruit)
```

**Output:**

```text
apple
banana
mango
```

## 7.2 Loop through the values

```python
prices = {"apple": 120, "banana": 60, "mango": 200}

for price in prices.values():
    print(price)
```

**Output:**

```text
120
60
200
```

## 7.3 Loop through keys **and** values

`items()` gives tuples, so we can **unpack** them (you learned this in the tuples lesson).

```python
prices = {"apple": 120, "banana": 60, "mango": 200}

for fruit, price in prices.items():
    print(fruit, "costs", price)
```

**Output:**

```text
apple costs 120
banana costs 60
mango costs 200
```

| I want... | Use |
|---|---|
| Only the keys | `for key in d:` |
| Only the values | `for value in d.values():` |
| Both | `for key, value in d.items():` |

---

# 8. Useful Dictionary Methods

| Method | What it does |
|---|---|
| `d.get(key, default)` | Read a value safely |
| `d.update(other)` | Add or change many pairs |
| `d.pop(key)` | Remove a pair and return its value |
| `d.popitem()` | Remove and return the last pair |
| `d.clear()` | Remove everything |
| `d.keys()` | All keys |
| `d.values()` | All values |
| `d.items()` | All `(key, value)` pairs |
| `d.copy()` | A separate copy |
| `d.setdefault(key, value)` | Add the key with `value` only if it is missing, then return its value |

### `copy()`

Just like lists, `b = a` does **not** copy a dictionary.

```python
a = {"x": 1}

b = a
c = a.copy()

a["x"] = 99

print("b:", b)
print("c:", c)
```

**Output:**

```text
b: {'x': 99}
c: {'x': 1}
```

### `setdefault()`

```python
student = {"name": "Ali"}

student.setdefault("age", 15)
student.setdefault("name", "Someone else")

print(student)
```

**Output:**

```text
{'name': 'Ali', 'age': 15}
```

---

# 9. Common Dictionary Patterns

## 9.1 Counting things (frequency)

A very common use: count how many times each item appears.

```python
votes = ["pizza", "burger", "pizza", "pasta", "pizza", "burger"]

counts = {}
for item in votes:
    if item in counts:
        counts[item] = counts[item] + 1
    else:
        counts[item] = 1

print(counts)
```

**Output:**

```text
{'pizza': 3, 'burger': 2, 'pasta': 1}
```

The same thing, shorter, using `get()` with a default of `0`:

```python
votes = ["pizza", "burger", "pizza", "pasta", "pizza", "burger"]

counts = {}
for item in votes:
    counts[item] = counts.get(item, 0) + 1

print(counts)
```

**Output:**

```text
{'pizza': 3, 'burger': 2, 'pasta': 1}
```

## 9.2 Finding the key with the biggest value

```python
scores = {"Ali": 85, "Sara": 92, "Bilal": 78}

best_name = ""
best_score = 0

for name, score in scores.items():
    if score > best_score:
        best_name = name
        best_score = score

print(best_name, best_score)
```

**Output:**

```text
Sara 92
```

## 9.3 Filtering into a new dictionary

```python
scores = {"Ali": 85, "Sara": 42, "Bilal": 78, "Fatima": 35}

passed = {}
for name, score in scores.items():
    if score >= 50:
        passed[name] = score

print(passed)
```

**Output:**

```text
{'Ali': 85, 'Bilal': 78}
```

## 9.4 Looking up a translation or a code

```python
days = {"Mon": "Monday", "Tue": "Tuesday", "Wed": "Wednesday"}

short = "Tue"

if short in days:
    print(short, "means", days[short])
else:
    print("Unknown day")
```

**Output:**

```text
Tue means Tuesday
```

---

# 10. Nested Dictionaries and Lists of Dictionaries

## 10.1 A dictionary inside a dictionary

```python
students = {
    "Ali": {"age": 15, "city": "Karachi"},
    "Sara": {"age": 14, "city": "Lahore"}
}

print(students["Ali"])
print(students["Ali"]["city"])
print(students["Sara"]["age"])
```

**Output:**

```text
{'age': 15, 'city': 'Karachi'}
Karachi
14
```

`students["Ali"]["city"]` means: get Ali's dictionary, then get `"city"` from it.

```python
students = {
    "Ali": {"age": 15, "city": "Karachi"},
    "Sara": {"age": 14, "city": "Lahore"}
}

for name, info in students.items():
    print(name, "is", info["age"], "and lives in", info["city"])
```

**Output:**

```text
Ali is 15 and lives in Karachi
Sara is 14 and lives in Lahore
```

## 10.2 A list inside a dictionary

```python
marks = {"Ali": [85, 90, 78], "Sara": [92, 88, 95]}

for name, scores in marks.items():
    print(name, "average:", sum(scores) / len(scores))

marks["Ali"].append(100)
print(marks["Ali"])
```

**Output:**

```text
Ali average: 84.33333333333333
Sara average: 91.66666666666667
[85, 90, 78, 100]
```

## 10.3 A list of dictionaries

This is how many programs store a table of records. Each dictionary is one row.

```python
students = [
    {"name": "Ali", "score": 85},
    {"name": "Sara", "score": 92},
    {"name": "Bilal", "score": 78}
]

for student in students:
    print(student["name"], "scored", student["score"])
```

**Output:**

```text
Ali scored 85
Sara scored 92
Bilal scored 78
```

---

# 11. Dictionaries and Functions

A dictionary can be passed into a function and returned from one.

```python
def average_score(grades):
    total = 0
    for score in grades.values():
        total = total + score
    return total / len(grades)

grades = {"Ali": 85, "Sara": 92, "Bilal": 78}
print(average_score(grades))
```

**Output:**

```text
85.0
```

Like lists, dictionaries are **mutable**, so a function can change the original:

```python
def add_student(grades, name, score):
    grades[name] = score

grades = {"Ali": 85}

add_student(grades, "Sara", 92)
print(grades)
```

**Output:**

```text
{'Ali': 85, 'Sara': 92}
```

No `global` keyword is needed, because the function is changing the dictionary itself, not reassigning a variable.

A function can also **return** a dictionary:

```python
def make_student(name, age):
    return {"name": name, "age": age}

s = make_student("Ali", 15)
print(s)
```

**Output:**

```text
{'name': 'Ali', 'age': 15}
```

---

# 12. Common Dictionary Mistakes

### Mistake 1: Reading a key that does not exist

```python
prices = {"apple": 120}

print(prices["mango"])
```

**Error:**

```text
KeyError: 'mango'
```

Use `get()` or check with `in` first.

### Mistake 2: Thinking a dictionary has index positions

```python
prices = {"apple": 120, "banana": 60}

print(prices[0])
```

**Error:**

```text
KeyError: 0
```

`0` is treated as a **key**, and there is no key `0`. Use the real key: `prices["apple"]`.

### Mistake 3: Using a list as a key

```python
data = {[1, 2]: "a list"}
```

**Error:**

```text
TypeError: unhashable type: 'list'
```

Keys must be immutable. Use a tuple `(1, 2)` instead.

### Mistake 4: Checking `in` for a value

```python
prices = {"apple": 120, "banana": 60}

print(120 in prices)
print(120 in prices.values())
```

**Output:**

```text
False
True
```

`in` checks the **keys**. To check values, use `.values()`.

### Mistake 5: Changing a dictionary while looping over it

```python
prices = {"apple": 120, "banana": 60}

for fruit in prices:
    prices[fruit + "2"] = 1
```

**Error:**

```text
RuntimeError: dictionary changed size during iteration
```

Loop over a **copy** (`list(prices)`) if you need to add or remove during the loop.

### Mistake 6: `{}` is an empty dictionary, not an empty set

```python
a = {}
b = set()

print(type(a))
print(type(b))
```

**Output:**

```text
<class 'dict'>
<class 'set'>
```

---

# Part 2: Sets

# 13. What Is a Set?

A **set** is a collection of **unique** items with **no order**.

- **No duplicates.** Adding something that is already there changes nothing.
- **No order, no index.** You cannot ask for "the first item".
- Items must be **immutable** (numbers, strings, tuples), just like dictionary keys.

> **Analogy: a bag of unique stickers.** If you get a second copy of a sticker, the bag still holds only one.

> **Analogy: today's attendance sheet.** Even if a student walks in twice, their name is counted once.

---

# 14. Creating Sets

Use curly brackets with items only (no colons), or the `set()` function.

```python
numbers = {1, 2, 3, 4}
colors = {"red", "green", "blue"}

print(numbers)
print(sorted(colors))
print(type(numbers))
print(len(colors))
```

**Output:**

```text
{1, 2, 3, 4}
['blue', 'green', 'red']
<class 'set'>
3
```

> Sets have no fixed order. Python may print a set's items in a different order than you wrote them, so this lesson uses `sorted()` to print sets of words.

### Duplicates disappear

```python
numbers = {1, 2, 2, 3, 3, 3}

print(numbers)
print(len(numbers))
```

**Output:**

```text
{1, 2, 3}
3
```

### Making a set from a list

```python
marks = [85, 90, 85, 70, 90, 100]

unique_marks = set(marks)

print(unique_marks)
print(len(unique_marks))
```

**Output:**

```text
{90, 100, 85, 70}
4
```

### The empty set

`{}` makes an empty **dictionary**. For an empty set, use `set()`.

```python
empty_dict = {}
empty_set = set()

print(type(empty_dict))
print(type(empty_set))
```

**Output:**

```text
<class 'dict'>
<class 'set'>
```

### Sets cannot be indexed or sliced

```python
numbers = {10, 20, 30}

print(numbers[0])
```

**Error:**

```text
TypeError: 'set' object is not subscriptable
```

### Checking membership

```python
fruits = {"apple", "banana", "cherry"}

print("apple" in fruits)
print("mango" in fruits)
print("mango" not in fruits)
```

**Output:**

```text
True
False
True
```

### Looping through a set

```python
numbers = {10, 20, 30}

for n in numbers:
    print(n)
```

**Output:**

```text
10
20
30
```

The order of the loop is not guaranteed, so do not depend on it.

---

# 15. Adding and Removing Items

## 15.1 `add()`: add one item

```python
fruits = {"apple", "banana"}

fruits.add("cherry")
fruits.add("apple")

print(sorted(fruits))
```

**Output:**

```text
['apple', 'banana', 'cherry']
```

`"apple"` was already there, so nothing changed.

## 15.2 `update()`: add many items

```python
numbers = {1, 2, 3}

numbers.update([3, 4, 5])
print(numbers)
```

**Output:**

```text
{1, 2, 3, 4, 5}
```

## 15.3 `remove()` vs `discard()`

Both remove an item. The difference is what happens when the item is **missing**.

```python
numbers = {1, 2, 3}

numbers.discard(99)
print(numbers)

numbers.remove(2)
print(numbers)
```

**Output:**

```text
{1, 2, 3}
{1, 3}
```

```python
numbers = {1, 2, 3}

numbers.remove(99)
```

**Error:**

```text
KeyError: 99
```

| | If the item exists | If the item is missing |
|---|---|---|
| `remove(x)` | Removes it | **`KeyError`** |
| `discard(x)` | Removes it | Does nothing (safe) |

## 15.4 `pop()` and `clear()`

`pop()` removes and returns **some** item (you cannot choose which, since sets have no order). `clear()` empties the set.

```python
numbers = {5}

item = numbers.pop()
print(item)
print(numbers)

numbers.add(7)
numbers.clear()
print(numbers)
```

**Output:**

```text
5
set()
set()
```

---

# 16. Set Operations: Union, Intersection, Difference

Sets are great for **comparing groups**. These operations work like the maths you may have seen in Venn diagrams.

```text
       A only        both        B only
    +-------------+---------+-------------+
    |    1    2   |  3   4  |   5    6    |
    +-------------+---------+-------------+
    |<--------- A --------->|
                  |<--------- B --------->|
```

With `a = {1, 2, 3, 4}` and `b = {3, 4, 5, 6}`:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:               ", a | b)
print("Intersection:        ", a & b)
print("Difference (a - b):  ", a - b)
print("Difference (b - a):  ", b - a)
print("Symmetric difference:", a ^ b)
```

**Output:**

```text
Union:                {1, 2, 3, 4, 5, 6}
Intersection:         {3, 4}
Difference (a - b):   {1, 2}
Difference (b - a):   {5, 6}
Symmetric difference: {1, 2, 5, 6}
```

| Operation | Operator | Method | Meaning |
|---|:---:|---|---|
| **Union** | `a \| b` | `a.union(b)` | Everything in **either** set |
| **Intersection** | `a & b` | `a.intersection(b)` | Only what is in **both** |
| **Difference** | `a - b` | `a.difference(b)` | In `a` but **not** in `b` |
| **Symmetric difference** | `a ^ b` | `a.symmetric_difference(b)` | In **one** set but **not both** |

### A real example: class clubs

```python
chess = {"Ali", "Sara", "Bilal", "Hina"}
music = {"Sara", "Hina", "Omar"}

print("In either club:   ", sorted(chess | music))
print("In both clubs:    ", sorted(chess & music))
print("Chess only:       ", sorted(chess - music))
print("In exactly one:   ", sorted(chess ^ music))
```

**Output:**

```text
In either club:    ['Ali', 'Bilal', 'Hina', 'Omar', 'Sara']
In both clubs:     ['Hina', 'Sara']
Chess only:        ['Ali', 'Bilal']
In exactly one:    ['Ali', 'Bilal', 'Omar']
```

### Subsets

```python
small = {1, 2}
big = {1, 2, 3, 4}
other = {8, 9}

print(small.issubset(big))
print(big.issuperset(small))
print(small.isdisjoint(other))
```

**Output:**

```text
True
True
True
```

| Method | `True` when |
|---|---|
| `a.issubset(b)` | Every item of `a` is also in `b` |
| `a.issuperset(b)` | `a` contains every item of `b` |
| `a.isdisjoint(b)` | `a` and `b` share **nothing** |

---

# 17. Where Sets Are Useful

## 17.1 Removing duplicates

```python
numbers = [1, 2, 2, 3, 3, 3, 4]

unique = list(set(numbers))

print(sorted(unique))
```

**Output:**

```text
[1, 2, 3, 4]
```

> A set does not keep order. If the order matters, use the loop from [list_methods.md](list_methods.md) (the "remove duplicates" challenge), or wrap the result in `sorted()`.

## 17.2 Counting unique items

```python
visitors = ["Ali", "Sara", "Ali", "Bilal", "Sara", "Ali"]

print("Total visits:", len(visitors))
print("Unique visitors:", len(set(visitors)))
```

**Output:**

```text
Total visits: 6
Unique visitors: 3
```

## 17.3 Finding common or missing items

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]

common = set(list1) & set(list2)
only_in_first = set(list1) - set(list2)

print(sorted(common))
print(sorted(only_in_first))
```

**Output:**

```text
[4, 5]
[1, 2, 3]
```

## 17.4 Fast membership testing

Checking `x in my_set` is very fast, even for huge sets. Checking `x in my_list` gets slower as the list gets longer, because Python has to look through the items one by one.

## 17.5 Detecting duplicates

```python
def has_duplicates(items):
    return len(items) != len(set(items))

print(has_duplicates([1, 2, 3, 4]))
print(has_duplicates([1, 2, 3, 2]))
```

**Output:**

```text
False
True
```

## Sets vs lists

| | **List** | **Set** |
|---|---|---|
| Brackets | `[ ]` | `{ }` |
| Duplicates | Allowed | **Not allowed** |
| Order | Kept | **Not kept** |
| Index / slice | Yes | **No** |
| Change items in place | Yes | No (but you can add and remove) |
| Best for | Ordered data, repeats | Unique items, comparing groups, fast `in` |

---

# 18. Common Set Mistakes

### Mistake 1: Expecting an order

Do not rely on the order of a set. If you need order, use a list (or `sorted()`).

### Mistake 2: Using `{}` for an empty set

`{}` is a dictionary. Use `set()`.

### Mistake 3: Putting a list inside a set

```python
data = {[1, 2], [3, 4]}
```

**Error:**

```text
TypeError: unhashable type: 'list'
```

Items must be immutable. Use tuples: `{(1, 2), (3, 4)}`.

```python
data = {(1, 2), (3, 4), (1, 2)}

print(len(data))
```

**Output:**

```text
2
```

### Mistake 4: Expecting `add()` to take several items

```python
numbers = {1, 2}

numbers.add(3, 4)
```

**Error:**

```text
TypeError: set.add() takes exactly one argument (2 given)
```

Use `update([3, 4])` to add many.

### Mistake 5: Expecting `remove()` to be safe

`remove()` raises a `KeyError` if the item is missing. Use `discard()` for a safe removal.

---

# Part 3: Putting It Together

# 19. Choosing the Right Data Structure

You now know four collections. How do you pick one?

| | **List** | **Tuple** | **Dictionary** | **Set** |
|---|---|---|---|---|
| Brackets | `[ ]` | `( )` | `{key: value}` | `{ }` |
| Ordered | Yes | Yes | Yes (insertion order) | **No** |
| Duplicates | Allowed | Allowed | Keys: **no**, values: yes | **No** |
| Can be changed | Yes | **No** | Yes | Yes |
| Access by | **Index** | **Index** | **Key** | Not possible (only `in`) |
| Example | `[85, 90, 78]` | `(24.8, 67.0)` | `{"Ali": 85}` | `{1, 2, 3}` |

### Ask yourself these questions

```text
Do I need to look things up by a NAME (a label)?
        YES  ->  Dictionary
        NO   ->  Do I only care that each item is UNIQUE (no repeats, no order)?
                      YES  ->  Set
                      NO   ->  Should the data NEVER change?
                                    YES  ->  Tuple
                                    NO   ->  List
```

### Scenarios

| Problem | Best choice | Why |
|---|---|---|
| Store the marks of a class in order | **List** | Ordered, can grow |
| Store the latitude and longitude of a place | **Tuple** | A fixed pair that should not change |
| Store each student's name and their score | **Dictionary** | Look up a score by name |
| Find which email addresses are repeated | **Set** | Duplicates disappear, quick `in` checks |
| Keep a to-do list where you add and remove tasks | **List** | Items change and order matters |
| Store days of the week | **Tuple** | Fixed values that never change |
| Count how many times each word appears | **Dictionary** | Word is the key, count is the value |
| Find students who are in both Maths and Science club | **Set** | Intersection (`&`) |
| Store a phone book | **Dictionary** | Look up a number by name |

### Mix them together

Real programs combine structures:

```python
class_data = {
    "Ali": {"marks": [85, 90, 78], "clubs": {"chess", "music"}, "location": (24.86, 67.01)},
    "Sara": {"marks": [92, 88, 95], "clubs": {"music"}, "location": (31.52, 74.35)}
}

ali = class_data["Ali"]

print(ali["marks"][0])
print(sorted(ali["clubs"]))
print(ali["location"][0])
```

**Output:**

```text
85
['chess', 'music']
24.86
```

This one object uses a **dictionary** (the records), a **list** (marks), a **set** (clubs) and a **tuple** (location).

---

# 20. Hands-On: Student Grade Tracker

We will build a grade tracker one step at a time. The data lives in a **dictionary**: the student's **name** is the key and the **score** is the value.

```text
{"Ali": 85, "Sara": 92, "Bilal": 78}
```

## Step 1: Store the grades

```python
grades = {}

grades["Ali"] = 85
grades["Sara"] = 92
grades["Bilal"] = 78

print(grades)
```

**Output:**

```text
{'Ali': 85, 'Sara': 92, 'Bilal': 78}
```

## Step 2: Show all students

```python
grades = {"Ali": 85, "Sara": 92, "Bilal": 78}

for name, score in grades.items():
    print(name, "->", score)
```

**Output:**

```text
Ali -> 85
Sara -> 92
Bilal -> 78
```

## Step 3: Turn a score into a letter grade

A function with `if / elif / else` and `return`:

```python
def get_letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(get_letter(95))
print(get_letter(72))
print(get_letter(40))
```

**Output:**

```text
A
C
F
```

## Step 4: Add, update and remove students

```python
def add_student(grades, name, score):
    grades[name] = score            # adds a new student OR updates an existing one

def remove_student(grades, name):
    if name in grades:
        grades.pop(name)
        return True
    return False

grades = {"Ali": 85, "Sara": 92}

add_student(grades, "Bilal", 78)
add_student(grades, "Ali", 88)
print(grades)

print(remove_student(grades, "Sara"))
print(remove_student(grades, "Zain"))
print(grades)
```

**Output:**

```text
{'Ali': 88, 'Sara': 92, 'Bilal': 78}
True
False
{'Ali': 88, 'Bilal': 78}
```

## Step 5: Statistics

```python
def class_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades.values()) / len(grades)

def top_student(grades):
    best_name = ""
    best_score = -1
    for name, score in grades.items():
        if score > best_score:
            best_name = name
            best_score = score
    return best_name, best_score

def lowest_student(grades):
    worst_name = ""
    worst_score = 101
    for name, score in grades.items():
        if score < worst_score:
            worst_name = name
            worst_score = score
    return worst_name, worst_score

grades = {"Ali": 85, "Sara": 92, "Bilal": 78}

print("Average:", class_average(grades))
print("Top:", top_student(grades))
print("Lowest:", lowest_student(grades))
```

**Output:**

```text
Average: 85.0
Top: ('Sara', 92)
Lowest: ('Bilal', 78)
```

Notice that `top_student` and `lowest_student` **return a tuple**, which you learned about in the tuples lesson.

## Step 6: A report with letter grades

```python
def get_letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def show_report(grades):
    print("----- Grade Report -----")
    for name, score in grades.items():
        print(name, "|", score, "|", get_letter(score))
    print("------------------------")

grades = {"Ali": 85, "Sara": 92, "Bilal": 78, "Fatima": 45}

show_report(grades)
```

**Output:**

```text
----- Grade Report -----
Ali | 85 | B
Sara | 92 | A
Bilal | 78 | C
Fatima | 45 | F
------------------------
```

## Step 7: Who passed? (using a set)

```python
grades = {"Ali": 85, "Sara": 92, "Bilal": 78, "Fatima": 45, "Omar": 30}

passed = set()
failed = set()

for name, score in grades.items():
    if score >= 50:
        passed.add(name)
    else:
        failed.add(name)

print("Passed:", sorted(passed))
print("Failed:", sorted(failed))
```

**Output:**

```text
Passed: ['Ali', 'Bilal', 'Sara']
Failed: ['Fatima', 'Omar']
```

## Complete program: Version A (runs on its own)

All the pieces together:

```python
# ===== Student Grade Tracker =====

def get_letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def add_student(grades, name, score):
    grades[name] = score

def remove_student(grades, name):
    if name in grades:
        grades.pop(name)
        return True
    return False

def class_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades.values()) / len(grades)

def top_student(grades):
    best_name = ""
    best_score = -1
    for name, score in grades.items():
        if score > best_score:
            best_name = name
            best_score = score
    return best_name, best_score

def show_report(grades):
    print("----- Grade Report -----")
    for name, score in grades.items():
        print(name, "|", score, "|", get_letter(score))
    print("------------------------")

# ----- Main program -----
grades = {}

add_student(grades, "Ali", 85)
add_student(grades, "Sara", 92)
add_student(grades, "Bilal", 78)
add_student(grades, "Fatima", 45)

show_report(grades)

print("Average:", class_average(grades))

name, score = top_student(grades)
print("Top student:", name, "with", score)

add_student(grades, "Fatima", 65)
print("Fatima improved to", grades["Fatima"])

remove_student(grades, "Bilal")
print("Students now:", list(grades.keys()))
```

**Output:**

```text
----- Grade Report -----
Ali | 85 | B
Sara | 92 | A
Bilal | 78 | C
Fatima | 45 | F
------------------------
Average: 75.0
Top student: Sara with 92
Fatima improved to 65
Students now: ['Ali', 'Sara', 'Fatima']
```

## Complete program: Version B (interactive menu)

This version uses `input()` and a `while` loop, so use a compiler that supports keyboard input.

```python
# ===== Student Grade Tracker (interactive) =====

def get_letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def show_report(grades):
    if len(grades) == 0:
        print("No students yet.")
        return
    print("----- Grade Report -----")
    for name, score in grades.items():
        print(name, "|", score, "|", get_letter(score))
    print("Average:", sum(grades.values()) / len(grades))

grades = {}

while True:
    print()
    print("1. Add or update a student")
    print("2. Remove a student")
    print("3. Show report")
    print("4. Look up a student")
    print("5. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Student name: ")
        score = int(input("Score (0-100): "))
        grades[name] = score
        print("Saved.")
    elif choice == "2":
        name = input("Student name: ")
        if name in grades:
            grades.pop(name)
            print("Removed.")
        else:
            print("Student not found.")
    elif choice == "3":
        show_report(grades)
    elif choice == "4":
        name = input("Student name: ")
        if name in grades:
            print(name, "has", grades[name], "->", get_letter(grades[name]))
        else:
            print("Student not found.")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.")
```

## Extension challenges

1. **Validation:** reject scores below 0 or above 100.
2. **Several subjects:** store each student's marks as a dictionary, like `{"Ali": {"Math": 85, "Science": 90}}`, and print each student's average.
3. **Rank list:** print students from highest to lowest score. (Hint: `sorted(grades.items(), key=...)` is advanced. Try repeatedly finding the top student and removing them from a **copy** instead.)
4. **Clubs:** add a set of clubs for each student, then print who is in both the chess and music clubs.

---

# 21. Practice Problems

Try each one yourself first. Click **Solution** to check your answer.

## Dictionary problems

### Q1. Create a dictionary

Create a dictionary about yourself with the keys `name`, `age` and `city`. Print it.

<details>
<summary>Solution</summary>

```python
me = {"name": "Ali", "age": 15, "city": "Karachi"}

print(me)
```

**Output:**

```text
{'name': 'Ali', 'age': 15, 'city': 'Karachi'}
```

</details>

### Q2. Read values safely

For `me = {"name": "Ali", "age": 15}`, print the age. Then use `get()` to read `"phone"` with the default `"Not available"`.

<details>
<summary>Solution</summary>

```python
me = {"name": "Ali", "age": 15}

print(me["age"])
print(me.get("phone", "Not available"))
```

**Output:**

```text
15
Not available
```

</details>

### Q3. Add and change

Starting from `me = {"name": "Ali", "age": 15}`, add an `email` key and change the age to 16.

<details>
<summary>Solution</summary>

```python
me = {"name": "Ali", "age": 15}

me["email"] = "ali@example.com"
me["age"] = 16

print(me)
```

**Output:**

```text
{'name': 'Ali', 'age': 16, 'email': 'ali@example.com'}
```

</details>

### Q4. Remove

Remove the key `"city"` from `{"name": "Ali", "city": "Karachi"}` using `pop()` and print what was removed.

<details>
<summary>Solution</summary>

```python
me = {"name": "Ali", "city": "Karachi"}

removed = me.pop("city")

print("Removed:", removed)
print(me)
```

**Output:**

```text
Removed: Karachi
{'name': 'Ali'}
```

</details>

### Q5. Loop

For `prices = {"apple": 120, "banana": 60, "mango": 200}`, print each item as `apple costs 120`.

<details>
<summary>Solution</summary>

```python
prices = {"apple": 120, "banana": 60, "mango": 200}

for fruit, price in prices.items():
    print(fruit, "costs", price)
```

**Output:**

```text
apple costs 120
banana costs 60
mango costs 200
```

</details>

### Q6. Total cost

Calculate the total of all the prices in `{"apple": 120, "banana": 60, "mango": 200}` using a loop.

<details>
<summary>Solution</summary>

```python
prices = {"apple": 120, "banana": 60, "mango": 200}

total = 0
for price in prices.values():
    total = total + price

print(total)
```

**Output:**

```text
380
```

</details>

### Q7. Most expensive item

Find and print the name of the most expensive item in the same dictionary.

<details>
<summary>Solution</summary>

```python
prices = {"apple": 120, "banana": 60, "mango": 200}

best_item = ""
best_price = 0

for item, price in prices.items():
    if price > best_price:
        best_item = item
        best_price = price

print(best_item, best_price)
```

**Output:**

```text
mango 200
```

</details>

### Q8. Does the student exist?

Write a function `find_grade(grades, name)` that **returns** the student's score, or the text `"Not found"` if the name is not in the dictionary. Test with `"Sara"` and `"Zain"`.

<details>
<summary>Solution</summary>

```python
def find_grade(grades, name):
    if name in grades:
        return grades[name]
    return "Not found"

grades = {"Ali": 85, "Sara": 92}

print(find_grade(grades, "Sara"))
print(find_grade(grades, "Zain"))
```

**Output:**

```text
92
Not found
```

</details>

### Q9. Count the votes

Count how many times each item appears in `["red", "blue", "red", "green", "red", "blue"]`.

<details>
<summary>Solution</summary>

```python
votes = ["red", "blue", "red", "green", "red", "blue"]

counts = {}
for v in votes:
    counts[v] = counts.get(v, 0) + 1

print(counts)
```

**Output:**

```text
{'red': 3, 'blue': 2, 'green': 1}
```

</details>

### Q10 (Challenge). Who passed?

Create a **new dictionary** that contains only the students with a score of 50 or more from `{"Ali": 85, "Sara": 42, "Bilal": 78, "Fatima": 35}`.

<details>
<summary>Solution</summary>

```python
scores = {"Ali": 85, "Sara": 42, "Bilal": 78, "Fatima": 35}

passed = {}
for name, score in scores.items():
    if score >= 50:
        passed[name] = score

print(passed)
```

**Output:**

```text
{'Ali': 85, 'Bilal': 78}
```

</details>

### Q11 (Challenge). Most common item

Using the vote counts from Q9, print the item with the most votes.

<details>
<summary>Solution</summary>

```python
votes = ["red", "blue", "red", "green", "red", "blue"]

counts = {}
for v in votes:
    counts[v] = counts.get(v, 0) + 1

winner = ""
most = 0
for item, count in counts.items():
    if count > most:
        winner = item
        most = count

print(winner, most)
```

**Output:**

```text
red 3
```

</details>

### Q12 (Challenge). Average per student

For `marks = {"Ali": [85, 90, 78], "Sara": [92, 88, 95]}`, print each student's average.

<details>
<summary>Solution</summary>

```python
marks = {"Ali": [85, 90, 78], "Sara": [92, 88, 95]}

for name, scores in marks.items():
    print(name, sum(scores) / len(scores))
```

**Output:**

```text
Ali 84.33333333333333
Sara 91.66666666666667
```

</details>

## Set problems

### Q13. Unique count

How many different numbers are in `[1, 2, 2, 3, 3, 3, 4]`?

<details>
<summary>Solution</summary>

```python
numbers = [1, 2, 2, 3, 3, 3, 4]

print(len(set(numbers)))
```

**Output:**

```text
4
```

</details>

### Q14. Remove duplicates

Remove the duplicates from `[5, 3, 5, 1, 3, 9]` and print the result as a sorted list.

<details>
<summary>Solution</summary>

```python
numbers = [5, 3, 5, 1, 3, 9]

unique = sorted(set(numbers))
print(unique)
```

**Output:**

```text
[1, 3, 5, 9]
```

</details>

### Q15. Add and discard

Start with `{1, 2, 3}`. Add `4`, then discard `1`, then try to discard `99` (it must not crash). Print the set.

<details>
<summary>Solution</summary>

```python
numbers = {1, 2, 3}

numbers.add(4)
numbers.discard(1)
numbers.discard(99)

print(numbers)
```

**Output:**

```text
{2, 3, 4}
```

</details>

### Q16. Common friends

Two students have these friends. Who are the friends they have **in common**?

```python
ali_friends = {"Sara", "Bilal", "Omar", "Hina"}
fatima_friends = {"Omar", "Hina", "Zain"}
```

<details>
<summary>Solution</summary>

```python
ali_friends = {"Sara", "Bilal", "Omar", "Hina"}
fatima_friends = {"Omar", "Hina", "Zain"}

print(sorted(ali_friends & fatima_friends))
```

**Output:**

```text
['Hina', 'Omar']
```

</details>

### Q17. Maths but not Science

Using the sets below, print the students who are in Maths but **not** in Science.

```python
maths = {"Ali", "Sara", "Bilal", "Hina"}
science = {"Sara", "Hina", "Omar"}
```

<details>
<summary>Solution</summary>

```python
maths = {"Ali", "Sara", "Bilal", "Hina"}
science = {"Sara", "Hina", "Omar"}

print(sorted(maths - science))
```

**Output:**

```text
['Ali', 'Bilal']
```

</details>

### Q18. Everyone

Using the same sets, print **everyone** who is in either class, and then **how many** students that is.

<details>
<summary>Solution</summary>

```python
maths = {"Ali", "Sara", "Bilal", "Hina"}
science = {"Sara", "Hina", "Omar"}

everyone = maths | science

print(sorted(everyone))
print(len(everyone))
```

**Output:**

```text
['Ali', 'Bilal', 'Hina', 'Omar', 'Sara']
5
```

</details>

### Q19 (Challenge). First duplicate

Write a function `first_duplicate(items)` that returns the first item that appears a second time, or `None` if there are no duplicates. Use a set. Test with `[3, 1, 4, 1, 5]` and `[1, 2, 3]`.

<details>
<summary>Solution</summary>

```python
def first_duplicate(items):
    seen = set()
    for item in items:
        if item in seen:
            return item
        seen.add(item)
    return None

print(first_duplicate([3, 1, 4, 1, 5]))
print(first_duplicate([1, 2, 3]))
```

**Output:**

```text
1
None
```

</details>

### Q20 (Challenge). Is it a subset?

Check whether all the required skills `{"python", "sql"}` are in the candidate's skills `{"python", "sql", "excel"}`. Print `Qualified` or `Not qualified`.

<details>
<summary>Solution</summary>

```python
required = {"python", "sql"}
candidate = {"python", "sql", "excel"}

if required.issubset(candidate):
    print("Qualified")
else:
    print("Not qualified")
```

**Output:**

```text
Qualified
```

</details>

## Choose the right data structure

### Q21. Which one would you use?

Pick **list**, **tuple**, **dictionary** or **set** for each task, and say why.

1. Store a person's name and their phone number so you can look up the number by name.
2. Store the colors of a traffic light: red, yellow, green (they never change).
3. Keep track of the unique usernames that have logged in today.
4. Store the scores of a game in the order they were played.
5. Count how many times each letter appears in a list of letters.

<details>
<summary>Solution</summary>

1. **Dictionary.** Look up the value (number) by a key (name).
2. **Tuple.** A fixed collection that never changes.
3. **Set.** Only unique items matter, and duplicates disappear automatically.
4. **List.** Order matters and new scores keep being added.
5. **Dictionary.** The letter is the key and the count is the value.

</details>

---

# 22. Summary

### Dictionaries

| Task | Code |
|---|---|
| Create | `d = {"name": "Ali", "age": 15}` |
| Read | `d["name"]` or `d.get("name", default)` |
| Add or change | `d["city"] = "Karachi"` |
| Check a key | `"name" in d` |
| Remove | `d.pop("age")` or `del d["age"]` |
| Keys / values / pairs | `d.keys()`, `d.values()`, `d.items()` |
| Loop with both | `for k, v in d.items():` |
| Count items | `counts[x] = counts.get(x, 0) + 1` |
| Number of pairs | `len(d)` |

### Sets

| Task | Code |
|---|---|
| Create | `s = {1, 2, 3}` (empty: `set()`) |
| Add / remove | `s.add(x)`, `s.discard(x)`, `s.remove(x)` |
| Check membership | `x in s` |
| Remove duplicates | `set(my_list)` |
| Union / intersection | `a \| b`, `a & b` |
| Difference | `a - b` |
| In exactly one | `a ^ b` |

### Remember

1. A dictionary looks things up by **key**, a list by **index**.
2. Keys must be **unique** and **immutable**.
3. `get()` and `in` protect you from a `KeyError`.
4. A set keeps only **unique** items and has **no order**.
5. `{}` is an empty **dictionary**. Use `set()` for an empty set.
6. Choose the structure that matches how you will use the data.
