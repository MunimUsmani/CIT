# 📋 Lists in Python — Beginner's Guide

A step-by-step introduction to lists: what they are, how to create them, how to read and change their items, and how to use them with loops, conditions and functions.

## The Lists & Tuples Series

Teach these files in this order:

| Order | File | Topic |
|:---:|---|---|
| 1 | **lists.md** (you are here) | What lists are, creating, reading, changing, looping |
| 2 | [indexing_slicing.md](indexing_slicing.md) | Indexing and slicing in depth |
| 3 | [list_methods.md](list_methods.md) | `append`, `pop`, `insert`, `remove`, `sort` and every other method |
| 4 | [tuples.md](tuples.md) | Tuples and how they differ from lists |

## Table of Contents

1. [Why Do We Need Lists?](#1-why-do-we-need-lists)
2. [Creating Lists](#2-creating-lists)
3. [Accessing Items with an Index](#3-accessing-items-with-an-index)
4. [Changing Items](#4-changing-items)
5. [Checking if an Item Exists](#5-checking-if-an-item-exists)
6. [Looping Through a List](#6-looping-through-a-list)
7. [Lists with Loops and Conditions](#7-lists-with-loops-and-conditions)
8. [Lists and Functions](#8-lists-and-functions)
9. [Two Names, One List](#9-two-names-one-list)
10. [Nested Lists](#10-nested-lists)
11. [Practice Problems](#11-practice-problems)
12. [Summary](#12-summary)

---

# 1. Why Do We Need Lists?

Imagine you want to store the marks of five students. With only variables, you would write this:

```python
mark1 = 85
mark2 = 92
mark3 = 78
mark4 = 90
mark5 = 66

print(mark1)
print(mark2)
print(mark3)
print(mark4)
print(mark5)
```

**Output:**

```text
85
92
78
90
66
```

This is slow to write, and it gets worse with 100 students. A **list** stores many values in **one variable**:

```python
marks = [85, 92, 78, 90, 66]
print(marks)
```

**Output:**

```text
[85, 92, 78, 90, 66]
```

> **Analogy: a row of numbered lockers.** The whole row has one name (`marks`). Each locker holds one value and has a number, starting from **0**, not 1.

A list is an **ordered collection** of items. It keeps the order you gave it, and it can be changed after it is created.

---

# 2. Creating Lists

Use square brackets `[ ]` and separate the items with commas.

```python
numbers = [10, 20, 30, 40]
names = ["Ali", "Sara", "Bilal"]
mixed = ["Ali", 15, 3.5, True]
empty = []

print(numbers)
print(names)
print(mixed)
print(empty)
```

**Output:**

```text
[10, 20, 30, 40]
['Ali', 'Sara', 'Bilal']
['Ali', 15, 3.5, True]
[]
```

A list can hold any data type, even a mix of types.

### Useful basics

```python
fruits = ["apple", "banana", "cherry"]

print(type(fruits))
print(len(fruits))
```

**Output:**

```text
<class 'list'>
3
```

- `type()` tells us it is a `list`.
- `len()` tells us **how many items** are in the list.

### Making a list from `range`

```python
numbers = list(range(1, 6))
print(numbers)

evens = list(range(2, 11, 2))
print(evens)
```

**Output:**

```text
[1, 2, 3, 4, 5]
[2, 4, 6, 8, 10]
```

---

# 3. Accessing Items with an Index

Every item has a position number called an **index**. **The first item is at index 0.**

```text
Positive index:     0        1         2        3        4
                 +--------+---------+--------+--------+--------+
fruits =         | apple  | banana  | cherry | mango  | grape  |
                 +--------+---------+--------+--------+--------+
Negative index:    -5       -4        -3       -2       -1
```

```python
fruits = ["apple", "banana", "cherry", "mango", "grape"]

print(fruits[0])
print(fruits[2])
print(fruits[4])
```

**Output:**

```text
apple
cherry
grape
```

### Negative indexes count from the end

`-1` is the last item, `-2` is the second from last, and so on.

```python
fruits = ["apple", "banana", "cherry", "mango", "grape"]

print(fruits[-1])
print(fruits[-2])
```

**Output:**

```text
grape
mango
```

### Going outside the list

If the index does not exist, Python raises an `IndexError`.

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[3])
```

**Error:**

```text
IndexError: list index out of range
```

The list has 3 items, so the valid indexes are `0, 1, 2`. The last valid index is always `len(list) - 1`.

> Indexing and slicing are explained fully in [indexing_slicing.md](indexing_slicing.md).

---

# 4. Changing Items

Lists are **mutable**, which means we can change them after creating them. Assign a new value to an index.

```python
marks = [85, 92, 78]

marks[1] = 95
print(marks)

marks[0] = marks[0] + 5
print(marks)
```

**Output:**

```text
[85, 95, 78]
[90, 95, 78]
```

---

# 5. Checking if an Item Exists

Use `in` and `not in`. They give `True` or `False`.

```python
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
print("mango" in fruits)
print("mango" not in fruits)
```

**Output:**

```text
True
False
True
```

This works well with `if`:

```python
fruits = ["apple", "banana", "cherry"]

if "apple" in fruits:
    print("We have apples!")
else:
    print("No apples today.")
```

**Output:**

```text
We have apples!
```

---

# 6. Looping Through a List

## 6.1 Loop through the items

The most common way. `item` takes each value in turn.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("I like", fruit)
```

**Output:**

```text
I like apple
I like banana
I like cherry
```

> **Analogy: school attendance.** The teacher goes through the register and checks every student one by one.

## 6.2 Loop through the indexes

Use `range(len(list))` when you need the **position** as well.

```python
fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(i, "->", fruits[i])
```

**Output:**

```text
0 -> apple
1 -> banana
2 -> cherry
```

## 6.3 Bonus: `enumerate()`

`enumerate()` gives you the index **and** the item together.

```python
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
    print(i, "->", fruit)
```

**Output:**

```text
0 -> apple
1 -> banana
2 -> cherry
```

## Which one should I use?

| Situation | Use |
|---|---|
| You only need the values | `for item in my_list:` |
| You need the position, or need to change items | `for i in range(len(my_list)):` |
| You need both and want cleaner code | `for i, item in enumerate(my_list):` |

---

# 7. Lists with Loops and Conditions

Everything you learned about variables, conditions and loops works with lists.

### Sum of all items

```python
numbers = [4, 8, 15, 16, 23, 42]

total = 0
for n in numbers:
    total = total + n

print("Total:", total)
```

**Output:**

```text
Total: 108
```

### Count the items that match a condition

```python
marks = [85, 42, 78, 35, 90, 66]

passed = 0
for m in marks:
    if m >= 50:
        passed = passed + 1

print("Students who passed:", passed)
```

**Output:**

```text
Students who passed: 4
```

### Find the largest item

```python
numbers = [12, 45, 7, 89, 23]

biggest = numbers[0]
for n in numbers:
    if n > biggest:
        biggest = n

print("Biggest:", biggest)
```

**Output:**

```text
Biggest: 89
```

### Build a new list with `append()`

`append()` adds an item to the **end** of a list. Start with an empty list and add to it.

```python
numbers = [1, 2, 3, 4, 5, 6]

evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)

print(evens)
```

**Output:**

```text
[2, 4, 6]
```

> All the list methods, including `append()`, are explained in [list_methods.md](list_methods.md).

---

# 8. Lists and Functions

A list can be passed into a function and a function can return a value calculated from a list.

```python
def average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total / len(numbers)

marks = [80, 90, 70]
print(average(marks))
```

**Output:**

```text
80.0
```

### A function can change the original list

Remember scope? A function cannot reassign a global variable. But a list is **mutable**, so a function can change the list it was given.

```python
def add_bonus_item(items):
    items.append("bonus")      # changes the ORIGINAL list

my_list = ["a", "b"]
add_bonus_item(my_list)
print(my_list)
```

**Output:**

```text
['a', 'b', 'bonus']
```

But **reassigning** the parameter does not change the original:

```python
def reset(items):
    items = []                 # makes a NEW local list; the original is untouched

my_list = [1, 2, 3]
reset(my_list)
print(my_list)
```

**Output:**

```text
[1, 2, 3]
```

**Why?** Inside the function, `items` is a local name pointing to the **same list**. `items.append(...)` changes that list itself. `items = []` only points the local name at a new empty list.

---

# 9. Two Names, One List

Assigning a list to another variable does **not** copy it. Both names point to the **same** list.

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
print(b)
```

**Output:**

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

Changing `b` also changed `a`, because they are the same list. To make a real copy, use `.copy()` (see [list_methods.md](list_methods.md)).

```python
a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)
print(b)
```

**Output:**

```text
[1, 2, 3]
[1, 2, 3, 4]
```

---

# 10. Nested Lists

A list can contain other lists. This is useful for tables and grids.

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(grid[0])
print(grid[1][2])
```

**Output:**

```text
[1, 2, 3]
6
```

`grid[1][2]` means: take row `1`, then take item `2` inside that row.

```text
            col 0  col 1  col 2
row 0   [     1      2      3  ]
row 1   [     4      5      6  ]   <- grid[1][2] is 6
row 2   [     7      8      9  ]
```

### Looping through a nested list

```python
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in grid:
    for item in row:
        print(item, end=" ")
    print()
```

**Output:**

```text
1 2 3 
4 5 6 
7 8 9 
```

---

# 11. Practice Problems

Try each one yourself first. Click **Solution** to check your answer.

### Q1. Create a list

Create a list of 5 of your favorite foods. Print the list and the number of items in it.

<details>
<summary>Solution</summary>

```python
foods = ["pizza", "biryani", "burger", "pasta", "samosa"]

print(foods)
print(len(foods))
```

**Output:**

```text
['pizza', 'biryani', 'burger', 'pasta', 'samosa']
5
```

</details>

### Q2. First and last

Using the list from Q1, print the first and the last item.

<details>
<summary>Solution</summary>

```python
foods = ["pizza", "biryani", "burger", "pasta", "samosa"]

print(foods[0])
print(foods[-1])
```

**Output:**

```text
pizza
samosa
```

</details>

### Q3. Change an item

Change the second item of the list to `"Karahi"` and print the list.

<details>
<summary>Solution</summary>

```python
foods = ["pizza", "biryani", "burger", "pasta", "samosa"]

foods[1] = "Karahi"
print(foods)
```

**Output:**

```text
['pizza', 'Karahi', 'burger', 'pasta', 'samosa']
```

</details>

### Q4. Loop and print

Print each item as `I like ___`.

<details>
<summary>Solution</summary>

```python
foods = ["pizza", "biryani", "burger"]

for food in foods:
    print("I like", food)
```

**Output:**

```text
I like pizza
I like biryani
I like burger
```

</details>

### Q5. Print with positions

Print each item along with its index, like `0 -> pizza`.

<details>
<summary>Solution</summary>

```python
foods = ["pizza", "biryani", "burger"]

for i in range(len(foods)):
    print(i, "->", foods[i])
```

**Output:**

```text
0 -> pizza
1 -> biryani
2 -> burger
```

</details>

### Q6. Sum

Calculate and print the sum of `[4, 8, 15, 16, 23, 42]` using a loop.

<details>
<summary>Solution</summary>

```python
numbers = [4, 8, 15, 16, 23, 42]

total = 0
for n in numbers:
    total = total + n

print(total)
```

**Output:**

```text
108
```

</details>

### Q7. Count even numbers

Count how many even numbers are in `[3, 8, 12, 5, 6, 9, 10]`.

<details>
<summary>Solution</summary>

```python
numbers = [3, 8, 12, 5, 6, 9, 10]

count = 0
for n in numbers:
    if n % 2 == 0:
        count = count + 1

print(count)
```

**Output:**

```text
4
```

</details>

### Q8. Does it exist?

Check whether `"Sara"` is in the list `["Ali", "Sara", "Bilal"]`. Print `Found` or `Not found`.

<details>
<summary>Solution</summary>

```python
names = ["Ali", "Sara", "Bilal"]

if "Sara" in names:
    print("Found")
else:
    print("Not found")
```

**Output:**

```text
Found
```

</details>

### Q9. Function: average

Write a function `average(numbers)` that **returns** the average of a list. Test it with `[10, 20, 30, 40]`.

<details>
<summary>Solution</summary>

```python
def average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total / len(numbers)

print(average([10, 20, 30, 40]))
```

**Output:**

```text
25.0
```

</details>

### Q10. Function: find the biggest

Write a function `find_max(numbers)` that **returns** the largest number without using `max()`. Test it with `[12, 45, 7, 89, 23]`.

<details>
<summary>Solution</summary>

```python
def find_max(numbers):
    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest

print(find_max([12, 45, 7, 89, 23]))
```

**Output:**

```text
89
```

</details>

### Q11 (Challenge). Squares list

Create a new list containing the squares of the numbers 1 to 5 using a loop and `append()`.

<details>
<summary>Solution</summary>

```python
squares = []

for i in range(1, 6):
    squares.append(i * i)

print(squares)
```

**Output:**

```text
[1, 4, 9, 16, 25]
```

</details>

### Q12 (Challenge). Predict the output

What will this print? Think first, then check.

```python
a = [1, 2, 3]
b = a
b[0] = 99
print(a)
```

<details>
<summary>Solution</summary>

```python
a = [1, 2, 3]
b = a
b[0] = 99
print(a)
```

**Output:**

```text
[99, 2, 3]
```

`a` and `b` are the same list, so changing `b[0]` also changes `a`.

</details>

---

# 12. Summary

| Idea | Example |
|---|---|
| Create a list | `fruits = ["apple", "banana"]` |
| Count the items | `len(fruits)` |
| First item | `fruits[0]` |
| Last item | `fruits[-1]` |
| Change an item | `fruits[1] = "mango"` |
| Check membership | `"apple" in fruits` |
| Loop over items | `for fruit in fruits:` |
| Loop with positions | `for i in range(len(fruits)):` |
| Add to the end | `fruits.append("grape")` |
| Copy a list | `fruits.copy()` (not `b = a`) |

**Next:** [Indexing and Slicing](indexing_slicing.md)
