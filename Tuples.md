# 🔒 Tuples in Python — Beginner's Guide

Tuples are like lists that **cannot be changed**. This guide covers creating tuples, indexing and slicing, why they are immutable, unpacking, returning multiple values from functions, and when to choose a tuple instead of a list.

> **Series:** [lists.md](lists.md) → [indexing_slicing.md](indexing_slicing.md) → [list_methods.md](list_methods.md) → **tuples.md** (you are here)

## Table of Contents

1. [What Is a Tuple?](#1-what-is-a-tuple)
2. [Creating Tuples](#2-creating-tuples)
3. [Indexing and Slicing](#3-indexing-and-slicing)
4. [Tuples Are Immutable](#4-tuples-are-immutable)
5. [Tuple Methods and Functions](#5-tuple-methods-and-functions)
6. [Looping Through a Tuple](#6-looping-through-a-tuple)
7. [Tuple Unpacking](#7-tuple-unpacking)
8. [Returning Multiple Values from a Function](#8-returning-multiple-values-from-a-function)
9. [Lists of Tuples](#9-lists-of-tuples)
10. [Tuple vs List](#10-tuple-vs-list)
11. [Common Mistakes](#11-common-mistakes)
12. [Practice Problems](#12-practice-problems)
13. [Summary](#13-summary)

---

# 1. What Is a Tuple?

A **tuple** is an ordered collection of items, just like a list. The big difference is that **a tuple cannot be changed after it is created**. This is called being **immutable**.

> **Analogy: a locked list.** A list is a notebook where you can erase and rewrite. A tuple is a printed certificate. You can read it, but you cannot edit it.

Tuples are used for data that should **stay fixed**:

- A point on a map: `(24.86, 67.01)`
- A date: `(2026, 11, 7)`
- RGB colors: `(255, 0, 0)`
- A student record: `("Ali", 15, "Karachi")`

---

# 2. Creating Tuples

Use round brackets `( )` with items separated by commas.

```python
colors = ("red", "green", "blue")
point = (10, 20)
mixed = ("Ali", 15, 3.5, True)
empty = ()

print(colors)
print(point)
print(mixed)
print(empty)
print(type(colors))
```

**Output:**

```text
('red', 'green', 'blue')
(10, 20)
('Ali', 15, 3.5, True)
()
<class 'tuple'>
```

### The one-item tuple needs a comma

```python
not_a_tuple = (5)
a_tuple = (5,)

print(type(not_a_tuple))
print(type(a_tuple))
```

**Output:**

```text
<class 'int'>
<class 'tuple'>
```

`(5)` is just the number 5 in brackets. The **comma** is what makes a tuple, so a one-item tuple is written `(5,)`.

### Brackets are optional

```python
point = 10, 20, 30

print(point)
print(type(point))
```

**Output:**

```text
(10, 20, 30)
<class 'tuple'>
```

### Converting with `tuple()`

```python
numbers = tuple([1, 2, 3])
letters = tuple("abc")
evens = tuple(range(2, 11, 2))

print(numbers)
print(letters)
print(evens)
```

**Output:**

```text
(1, 2, 3)
('a', 'b', 'c')
(2, 4, 6, 8, 10)
```

---

# 3. Indexing and Slicing

Indexing and slicing work **exactly** like they do for lists. See [indexing_slicing.md](indexing_slicing.md) for all the rules.

```python
colors = ("red", "green", "blue", "yellow", "purple")

print(colors[0])
print(colors[-1])
print(colors[1:3])
print(colors[::2])
print(colors[::-1])
```

**Output:**

```text
red
purple
('green', 'blue')
('red', 'blue', 'purple')
('purple', 'yellow', 'blue', 'green', 'red')
```

```text
Positive index:     0        1        2         3         4
                 +--------+---------+--------+----------+----------+
colors =         |  red   |  green  |  blue  |  yellow  |  purple  |
                 +--------+---------+--------+----------+----------+
Negative index:    -5       -4        -3        -2         -1
```

A slice of a tuple is a **new tuple**.

---

# 4. Tuples Are Immutable

If you try to change a tuple, Python raises a `TypeError`.

```python
colors = ("red", "green", "blue")

colors[0] = "pink"
```

**Error:**

```text
TypeError: 'tuple' object does not support item assignment
```

```python
colors = ("red", "green", "blue")

colors.append("yellow")
```

**Error:**

```text
AttributeError: 'tuple' object has no attribute 'append'
```

Tuples have **no** `append`, `insert`, `remove`, `pop`, `sort` or `reverse` methods, because those all change the object.

### How to "change" a tuple

You cannot change it, but you can **make a new tuple**.

```python
colors = ("red", "green", "blue")

new_colors = colors + ("yellow",)

print(new_colors)
print(colors)
```

**Output:**

```text
('red', 'green', 'blue', 'yellow')
('red', 'green', 'blue')
```

Or convert it to a list, change the list, and convert it back:

```python
colors = ("red", "green", "blue")

temp = list(colors)
temp[0] = "pink"
temp.append("yellow")
colors = tuple(temp)

print(colors)
```

**Output:**

```text
('pink', 'green', 'blue', 'yellow')
```

```text
tuple  ->  list()  ->  change it  ->  tuple()
```

---

# 5. Tuple Methods and Functions

Tuples only have **two** methods, because they cannot be changed.

| Method | Meaning |
|---|---|
| `count(x)` | How many times `x` appears |
| `index(x)` | Position of the first `x` |

```python
numbers = (1, 2, 3, 2, 2, 5)

print(numbers.count(2))
print(numbers.index(3))
```

**Output:**

```text
3
2
```

These built-in functions and operators also work with tuples:

```python
numbers = (4, 8, 15, 16, 23, 42)

print(len(numbers))
print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(15 in numbers)
print(99 in numbers)
```

**Output:**

```text
6
108
4
42
True
False
```

### Sorting a tuple

Tuples have no `sort()`, but `sorted()` works and gives back a **list**.

```python
numbers = (5, 2, 9, 1)

result = sorted(numbers)

print(result)
print(tuple(result))
```

**Output:**

```text
[1, 2, 5, 9]
(1, 2, 5, 9)
```

### Joining and repeating

```python
a = (1, 2)
b = (3, 4)

print(a + b)
print(a * 3)
```

**Output:**

```text
(1, 2, 3, 4)
(1, 2, 1, 2, 1, 2)
```

---

# 6. Looping Through a Tuple

Loops work the same as with lists.

```python
colors = ("red", "green", "blue")

for color in colors:
    print(color)

for i in range(len(colors)):
    print(i, "->", colors[i])
```

**Output:**

```text
red
green
blue
0 -> red
1 -> green
2 -> blue
```

---

# 7. Tuple Unpacking

You can split a tuple into separate variables in one line. This is called **unpacking**.

```python
student = ("Ali", 15, "Karachi")

name, age, city = student

print(name)
print(age)
print(city)
```

**Output:**

```text
Ali
15
Karachi
```

The number of variables must match the number of items.

```python
student = ("Ali", 15, "Karachi")

name, age = student
```

**Error:**

```text
ValueError: too many values to unpack (expected 2)
```

### Swapping two variables

This is the famous Python trick. It uses a tuple behind the scenes.

```python
a = 10
b = 20

a, b = b, a

print(a, b)
```

**Output:**

```text
20 10
```

> Compare this with the older way that needed a temporary variable:
>
> ```python
> temp = a
> a = b
> b = temp
> ```

### Bonus: collecting the rest with `*`

```python
numbers = (1, 2, 3, 4, 5)

first, *middle, last = numbers

print(first)
print(middle)
print(last)
```

**Output:**

```text
1
[2, 3, 4]
5
```

---

# 8. Returning Multiple Values from a Function

A function can only `return` one thing, but that thing can be a **tuple**. When you write `return a, b`, Python returns the tuple `(a, b)`.

```python
def min_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]

    for n in numbers:
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n

    return smallest, largest

result = min_max([4, 9, 1, 7])
print(result)
print(type(result))
```

**Output:**

```text
(1, 9)
<class 'tuple'>
```

Unpack the result straight into variables:

```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 9, 1, 7])

print("Lowest:", low)
print("Highest:", high)
```

**Output:**

```text
Lowest: 1
Highest: 9
```

Another example, a function that returns both the sum and the average:

```python
def stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

t, a = stats([10, 20, 30])

print("Total:", t)
print("Average:", a)
```

**Output:**

```text
Total: 60
Average: 20.0
```

> This is also how `*args` will work later. The extra arguments arrive inside a **tuple**.

---

# 9. Lists of Tuples

A list of tuples is a common way to store records, like a table where each row is fixed but you can add or remove rows.

```python
students = [("Ali", 85), ("Sara", 92), ("Bilal", 78)]

for student in students:
    print(student[0], "scored", student[1])
```

**Output:**

```text
Ali scored 85
Sara scored 92
Bilal scored 78
```

With unpacking in the loop, the code reads much more clearly:

```python
students = [("Ali", 85), ("Sara", 92), ("Bilal", 78)]

for name, score in students:
    print(name, "scored", score)
```

**Output:**

```text
Ali scored 85
Sara scored 92
Bilal scored 78
```

### Finding the top scorer

```python
students = [("Ali", 85), ("Sara", 92), ("Bilal", 78)]

best_name = ""
best_score = 0

for name, score in students:
    if score > best_score:
        best_name = name
        best_score = score

print("Top scorer:", best_name, best_score)
```

**Output:**

```text
Top scorer: Sara 92
```

---

# 10. Tuple vs List

| | **List** | **Tuple** |
|---|---|---|
| Brackets | `[ ]` | `( )` |
| Can be changed (mutable)? | **Yes** | **No** (immutable) |
| Add / remove items | Yes | No |
| Methods | Many (`append`, `pop`, `sort`...) | Only `count` and `index` |
| Indexing and slicing | Yes | Yes |
| Loop through it | Yes | Yes |
| Use it for | Data that **changes** (a shopping list, scores) | Data that **stays fixed** (coordinates, dates, a record) |
| One-item version | `[5]` | `(5,)` |

### When to choose a tuple

- The values **should not change** (a point on a map, days of the week).
- You want to **return several values** from a function.
- You want to protect data from being changed by accident.

### When to choose a list

- You need to **add, remove or change** items.
- You will **sort** the data.
- The number of items is not known in advance.

---

# 11. Common Mistakes

### Mistake 1: Forgetting the comma in a one-item tuple

```python
a = (5)
b = (5,)

print(type(a))
print(type(b))
```

**Output:**

```text
<class 'int'>
<class 'tuple'>
```

### Mistake 2: Trying to change a tuple

```python
point = (10, 20)

point[0] = 15
```

**Error:**

```text
TypeError: 'tuple' object does not support item assignment
```

Make a new tuple instead: `point = (15, point[1])`.

### Mistake 3: Unpacking into the wrong number of variables

```python
point = (10, 20, 30)

x, y = point
```

**Error:**

```text
ValueError: too many values to unpack (expected 2)
```

### Mistake 4: Expecting `sorted()` to return a tuple

```python
numbers = (3, 1, 2)

print(sorted(numbers))
print(type(sorted(numbers)))
```

**Output:**

```text
[1, 2, 3]
<class 'list'>
```

`sorted()` always gives a list. Wrap it with `tuple(...)` if you need a tuple.

### Mistake 5: A tuple with a list inside can still change

The tuple itself is fixed, but a **list inside it** is still a list.

```python
data = ("Ali", [85, 90])

data[1].append(95)

print(data)
```

**Output:**

```text
('Ali', [85, 90, 95])
```

You still cannot replace the list with something else (`data[1] = [...]` is an error), but the list's own contents can change.

---

# 12. Practice Problems

Try each one yourself first. Click **Solution** to check your answer.

### Q1. Create a tuple

Create a tuple of three of your favorite colors and print it.

<details>
<summary>Solution</summary>

```python
colors = ("red", "blue", "green")

print(colors)
```

**Output:**

```text
('red', 'blue', 'green')
```

</details>

### Q2. Read items

For `("red", "green", "blue", "yellow")`, print the item at index 1 and the last item.

<details>
<summary>Solution</summary>

```python
colors = ("red", "green", "blue", "yellow")

print(colors[1])
print(colors[-1])
```

**Output:**

```text
green
yellow
```

</details>

### Q3. Slice a tuple

For `(10, 20, 30, 40, 50)`, print the first three items and the last two items.

<details>
<summary>Solution</summary>

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[:3])
print(numbers[-2:])
```

**Output:**

```text
(10, 20, 30)
(40, 50)
```

</details>

### Q4. What happens?

Try to change the first item of `(1, 2, 3)` to `99`. What error do you get?

<details>
<summary>Solution</summary>

```python
numbers = (1, 2, 3)

numbers[0] = 99
```

**Error:**

```text
TypeError: 'tuple' object does not support item assignment
```

Tuples are immutable, so they cannot be changed.

</details>

### Q5. Change it the safe way

Turn `("red", "green", "blue")` into `("pink", "green", "blue", "yellow")` by converting to a list and back.

<details>
<summary>Solution</summary>

```python
colors = ("red", "green", "blue")

temp = list(colors)
temp[0] = "pink"
temp.append("yellow")
colors = tuple(temp)

print(colors)
```

**Output:**

```text
('pink', 'green', 'blue', 'yellow')
```

</details>

### Q6. Unpack a record

Unpack `("Ali", 15, "Karachi")` into `name`, `age` and `city`, then print a sentence using all three.

<details>
<summary>Solution</summary>

```python
student = ("Ali", 15, "Karachi")

name, age, city = student

print(name, "is", age, "years old and lives in", city)
```

**Output:**

```text
Ali is 15 years old and lives in Karachi
```

</details>

### Q7. Swap

Swap the values of `x = 5` and `y = 9` in one line.

<details>
<summary>Solution</summary>

```python
x = 5
y = 9

x, y = y, x

print(x, y)
```

**Output:**

```text
9 5
```

</details>

### Q8. Count

How many times does `2` appear in `(2, 5, 2, 7, 2, 9)`?

<details>
<summary>Solution</summary>

```python
numbers = (2, 5, 2, 7, 2, 9)

print(numbers.count(2))
```

**Output:**

```text
3
```

</details>

### Q9. Function: return two values

Write a function `sum_and_product(a, b)` that returns **both** the sum and the product. Unpack the result and print it. Test with `4` and `5`.

<details>
<summary>Solution</summary>

```python
def sum_and_product(a, b):
    return a + b, a * b

total, product = sum_and_product(4, 5)

print("Sum:", total)
print("Product:", product)
```

**Output:**

```text
Sum: 9
Product: 20
```

</details>

### Q10. List of tuples

For `students = [("Ali", 85), ("Sara", 92), ("Bilal", 78)]`, print each student as `Name: score` and then print the average score.

<details>
<summary>Solution</summary>

```python
students = [("Ali", 85), ("Sara", 92), ("Bilal", 78)]

total = 0
for name, score in students:
    print(name + ":", score)
    total = total + score

print("Average:", total / len(students))
```

**Output:**

```text
Ali: 85
Sara: 92
Bilal: 78
Average: 85.0
```

</details>

### Q11 (Challenge). Only the even numbers

Write a function `evens_only(numbers)` that takes a tuple and **returns a new tuple** with only the even numbers. Test with `(1, 2, 3, 4, 5, 6)`.

<details>
<summary>Solution</summary>

```python
def evens_only(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return tuple(result)

print(evens_only((1, 2, 3, 4, 5, 6)))
```

**Output:**

```text
(2, 4, 6)
```

</details>

### Q12 (Challenge). Closest point to the origin

For `points = [(3, 4), (1, 1), (6, 8), (0, 2)]`, find the point closest to `(0, 0)`. Use `x * x + y * y` as the distance measure (no square root needed).

<details>
<summary>Solution</summary>

```python
points = [(3, 4), (1, 1), (6, 8), (0, 2)]

closest = points[0]
closest_dist = closest[0] * closest[0] + closest[1] * closest[1]

for x, y in points:
    dist = x * x + y * y
    if dist < closest_dist:
        closest = (x, y)
        closest_dist = dist

print(closest)
```

**Output:**

```text
(1, 1)
```

</details>

---

# 13. Summary

| Idea | Example |
|---|---|
| Create a tuple | `t = (1, 2, 3)` |
| One-item tuple | `t = (5,)` |
| Index | `t[0]`, `t[-1]` |
| Slice | `t[1:3]` |
| Immutable | `t[0] = 9` raises `TypeError` |
| Only two methods | `t.count(x)`, `t.index(x)` |
| Unpack | `a, b, c = t` |
| Swap | `a, b = b, a` |
| Return many values | `return total, average` |
| Convert | `list(t)` and `tuple(lst)` |

**Remember**

1. A tuple is a list that **cannot change**.
2. Indexing and slicing work **exactly the same** as lists.
3. A one-item tuple needs a **comma**.
4. Functions can return several values as a **tuple**.

**What's next:** Strings (they use the same indexing and slicing and are also immutable), then `*args`.

**Previous:** [List Methods](list_methods.md)
