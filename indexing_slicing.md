# 🔪 Indexing and Slicing in Python

How to pick a **single item** (indexing) or a **piece** of a list (slicing). This is one of the most important skills in Python. It works the same way on lists, tuples and strings.

> **Series:** [lists.md](lists.md) → **indexing_slicing.md** (you are here) → [list_methods.md](list_methods.md) → [tuples.md](tuples.md)

## Table of Contents

1. [Positions: What Is an Index?](#1-positions-what-is-an-index)
2. [Indexing: Getting One Item](#2-indexing-getting-one-item)
3. [Slicing: Getting a Piece](#3-slicing-getting-a-piece)
4. [Leaving Out the Start or the Stop](#4-leaving-out-the-start-or-the-stop)
5. [Negative Numbers in Slices](#5-negative-numbers-in-slices)
6. [The Step](#6-the-step)
7. [Slicing Never Raises an IndexError](#7-slicing-never-raises-an-indexerror)
8. [A Slice Is a New List](#8-a-slice-is-a-new-list)
9. [Changing a List with Slices (Bonus)](#9-changing-a-list-with-slices-bonus)
10. [Cheat Sheet of Common Slices](#10-cheat-sheet-of-common-slices)
11. [Common Mistakes](#11-common-mistakes)
12. [Works on Tuples and Strings Too](#12-works-on-tuples-and-strings-too)
13. [Practice Problems](#13-practice-problems)
14. [Summary](#14-summary)

---

# 1. Positions: What Is an Index?

Every item in a list has a position number called its **index**. There are two ways to count:

- **Positive index:** starts at `0` from the **front**.
- **Negative index:** starts at `-1` from the **back**.

```text
Positive index:     0        1         2        3        4
                 +--------+---------+--------+--------+--------+
fruits =         | apple  | banana  | cherry | mango  | grape  |
                 +--------+---------+--------+--------+--------+
Negative index:    -5       -4        -3       -2       -1
```

| Item | Positive index | Negative index |
|---|:---:|:---:|
| apple | 0 | -5 |
| banana | 1 | -4 |
| cherry | 2 | -3 |
| mango | 3 | -2 |
| grape | 4 | -1 |

For a list with `n` items:

- The first index is **`0`** (or `-n`).
- The last index is **`n - 1`** (or `-1`).

---

# 2. Indexing: Getting One Item

Put the index inside square brackets right after the list name.

```python
fruits = ["apple", "banana", "cherry", "mango", "grape"]

print(fruits[0])
print(fruits[1])
print(fruits[4])
```

**Output:**

```text
apple
banana
grape
```

### Negative indexing

Negative indexes are the easy way to reach the end of a list.

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

### Two ways to get the last item

```python
fruits = ["apple", "banana", "cherry", "mango", "grape"]

print(fruits[len(fruits) - 1])
print(fruits[-1])
```

**Output:**

```text
grape
grape
```

Both give `grape`. `fruits[-1]` is shorter and the one people use. It also keeps working when the list grows or shrinks.

### The `IndexError`

Asking for an index that does not exist is an error.

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[3])
```

**Error:**

```text
IndexError: list index out of range
```

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[-4])
```

**Error:**

```text
IndexError: list index out of range
```

For a list with `n` items, the valid indexes are from **`-n`** to **`n - 1`**. Anything outside that range raises `IndexError`.

### An index gives you the item itself

```python
fruits = ["apple", "banana", "cherry"]

item = fruits[1]
print(item)
print(type(item))
```

**Output:**

```text
banana
<class 'str'>
```

---

# 3. Slicing: Getting a Piece

A **slice** takes a **piece** of a list. The syntax is:

```text
list[start : stop]
```

- **`start`** is the first index to include.
- **`stop`** is where to stop. **The item at `stop` is NOT included.**

```python
fruits = ["apple", "banana", "cherry", "mango", "grape"]

print(fruits[1:4])
```

**Output:**

```text
['banana', 'cherry', 'mango']
```

This gives indexes `1`, `2` and `3`. Index `4` is not included.

### Memory trick: think of cuts between the items

Imagine the numbers as **cuts** between the items, not as the items themselves.

```text
   +-------+--------+--------+--------+-------+
   | apple | banana | cherry | mango  | grape |
   +-------+--------+--------+--------+-------+
   0       1        2        3        4       5
```

`fruits[1:4]` means: cut at `1`, cut at `4`, and take everything **between** the cuts. That is `banana`, `cherry`, `mango`.

### Handy rules

- Start is **included**, stop is **excluded**.
- The number of items you get is **`stop - start`**. For `[1:4]`, that is `4 - 1 = 3` items.
- `list[a:b]` followed by `list[b:c]` always joins up with no gaps and no overlap.

```python
fruits = ["apple", "banana", "cherry", "mango", "grape"]

print(fruits[0:2])
print(fruits[2:5])
```

**Output:**

```text
['apple', 'banana']
['cherry', 'mango', 'grape']
```

### Indexing vs slicing: the big difference

| | Example | What you get |
|---|---|---|
| **Index** | `fruits[1]` | One **item** (`'banana'`) |
| **Slice** | `fruits[1:2]` | A **list** (`['banana']`) |

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[1])
print(fruits[1:2])
```

**Output:**

```text
banana
['banana']
```

---

# 4. Leaving Out the Start or the Stop

If you leave out `start`, Python starts at the beginning. If you leave out `stop`, Python goes to the end.

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[:3])
print(numbers[2:])
print(numbers[:])
```

**Output:**

```text
[10, 20, 30]
[30, 40, 50, 60]
[10, 20, 30, 40, 50, 60]
```

| Slice | Meaning |
|---|---|
| `numbers[:3]` | From the start up to (not including) index 3. The **first 3 items** |
| `numbers[2:]` | From index 2 to the end |
| `numbers[:]` | The whole list (a copy) |

---

# 5. Negative Numbers in Slices

Negative numbers work in slices too. They count from the end.

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[-3:])
print(numbers[:-1])
print(numbers[1:-1])
print(numbers[-4:-1])
```

**Output:**

```text
[40, 50, 60]
[10, 20, 30, 40, 50]
[20, 30, 40, 50]
[30, 40, 50]
```

| Slice | Meaning |
|---|---|
| `numbers[-3:]` | The **last 3 items** |
| `numbers[:-1]` | Everything **except the last** item |
| `numbers[1:-1]` | Everything **except the first and last** items |
| `numbers[-4:-1]` | From the 4th from last up to (not including) the last |

> **Remember:** `stop` is still excluded, even with negative numbers. That is why `[:-1]` removes the last item.

---

# 6. The Step

A slice can have a third number, the **step**:

```text
list[start : stop : step]
```

The step says how many places to jump each time. The default step is `1`.

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[::2])
print(numbers[1::2])
print(numbers[::3])
print(numbers[2:8:2])
```

**Output:**

```text
[0, 2, 4, 6, 8]
[1, 3, 5, 7, 9]
[0, 3, 6, 9]
[2, 4, 6]
```

| Slice | Meaning |
|---|---|
| `numbers[::2]` | Every 2nd item, starting from the first |
| `numbers[1::2]` | Every 2nd item, starting from index 1 |
| `numbers[::3]` | Every 3rd item |
| `numbers[2:8:2]` | From index 2 up to 8, jumping by 2 |

### A negative step goes backwards

```python
numbers = [1, 2, 3, 4, 5]

print(numbers[::-1])
print(numbers[::-2])
print(numbers[4:1:-1])
```

**Output:**

```text
[5, 4, 3, 2, 1]
[5, 3, 1]
[5, 4, 3]
```

- `numbers[::-1]` is the classic way to **reverse** a list.
- With a negative step, `start` should be **bigger** than `stop`, because you are moving backwards. `numbers[4:1:-1]` starts at index 4 and goes down, stopping before index 1.

---

# 7. Slicing Never Raises an IndexError

Indexing outside the list is an error, but slicing outside the list is **safe**. Python just gives you what exists.

```python
numbers = [10, 20, 30]

print(numbers[1:100])
print(numbers[5:10])
print(numbers[2:1])
```

**Output:**

```text
[20, 30]
[]
[]
```

- `numbers[1:100]` gives everything from index 1 to the end.
- `numbers[5:10]` and `numbers[2:1]` give an empty list `[]`.

```python
numbers = [10, 20, 30]

print(numbers[5])
```

**Error:**

```text
IndexError: list index out of range
```

---

# 8. A Slice Is a New List

A slice makes a **copy**. Changing the slice does not change the original.

```python
numbers = [1, 2, 3, 4, 5]

piece = numbers[1:4]
piece[0] = 99

print(piece)
print(numbers)
```

**Output:**

```text
[99, 3, 4]
[1, 2, 3, 4, 5]
```

`numbers[:]` makes a full copy, which is different from `b = a`.

```python
a = [1, 2, 3]

b = a
c = a[:]

a.append(4)

print("b:", b)
print("c:", c)
```

**Output:**

```text
b: [1, 2, 3, 4]
c: [1, 2, 3]
```

- `b = a` → **same list** (changes show up in both).
- `c = a[:]` → a **separate copy**.

---

# 9. Changing a List with Slices (Bonus)

You can **replace** or **delete** a part of a list with a slice.

### Replace part of a list

```python
numbers = [1, 2, 3, 4, 5]

numbers[1:3] = [20, 30]
print(numbers)
```

**Output:**

```text
[1, 20, 30, 4, 5]
```

The replacement does not have to be the same length.

```python
numbers = [1, 2, 3, 4, 5]

numbers[1:3] = [99]
print(numbers)
```

**Output:**

```text
[1, 99, 4, 5]
```

### Delete part of a list

```python
numbers = [10, 20, 30, 40, 50]

del numbers[1:3]
print(numbers)
```

**Output:**

```text
[10, 40, 50]
```

---

# 10. Cheat Sheet of Common Slices

With `numbers = [10, 20, 30, 40, 50, 60, 70, 80]`:

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print("first 3      :", numbers[:3])
print("last 3       :", numbers[-3:])
print("all but last :", numbers[:-1])
print("all but first:", numbers[1:])
print("middle       :", numbers[1:-1])
print("every other  :", numbers[::2])
print("reversed     :", numbers[::-1])
print("copy         :", numbers[:])
```

**Output:**

```text
first 3      : [10, 20, 30]
last 3       : [60, 70, 80]
all but last : [10, 20, 30, 40, 50, 60, 70]
all but first: [20, 30, 40, 50, 60, 70, 80]
middle       : [20, 30, 40, 50, 60, 70]
every other  : [10, 30, 50, 70]
reversed     : [80, 70, 60, 50, 40, 30, 20, 10]
copy         : [10, 20, 30, 40, 50, 60, 70, 80]
```

| Goal | Slice |
|---|---|
| First `n` items | `lst[:n]` |
| Last `n` items | `lst[-n:]` |
| Everything except the last | `lst[:-1]` |
| Everything except the first | `lst[1:]` |
| Without first and last | `lst[1:-1]` |
| Every 2nd item | `lst[::2]` |
| Reverse | `lst[::-1]` |
| Copy | `lst[:]` |

---

# 11. Common Mistakes

### Mistake 1: Thinking the stop index is included

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:3])
```

**Output:**

```text
[20, 30]
```

This gives `[20, 30]`, **not** `[20, 30, 40]`. The item at index 3 is excluded.

### Mistake 2: Mixing up index and slice

```python
numbers = [10, 20, 30]

print(numbers[0])
print(numbers[0:1])
```

**Output:**

```text
10
[10]
```

The first is the **item** `10`. The second is a **list** `[10]`.

### Mistake 3: Counting from 1

The first item is index `0`. A list with 5 items has indexes `0` to `4`. Index `5` does not exist.

### Mistake 4: A negative step with the wrong order

```python
numbers = [1, 2, 3, 4, 5]

print(numbers[1:4:-1])
print(numbers[4:1:-1])
```

**Output:**

```text
[]
[5, 4, 3]
```

With a negative step you move backwards, so `start` must be bigger than `stop`. The first slice is empty because it cannot go from 1 to 4 backwards.

---

# 12. Works on Tuples and Strings Too

Indexing and slicing work exactly the same on tuples and strings. You will meet both of these soon, so learn the rules once and use them everywhere.

```python
word = "python"
colors = ("red", "green", "blue", "yellow")

print(word[0])
print(word[-1])
print(word[1:4])
print(word[::-1])

print(colors[1])
print(colors[1:3])
```

**Output:**

```text
p
n
yth
nohtyp
green
('green', 'blue')
```

---

# 13. Practice Problems

Try each one yourself first. Click **Solution** to check your answer.

Use this list for the first problems:

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
```

### Q1. First and last

Print the first item and the last item.

<details>
<summary>Solution</summary>

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[0])
print(numbers[-1])
```

**Output:**

```text
10
80
```

</details>

### Q2. Third item

Print the third item (remember: counting starts at 0).

<details>
<summary>Solution</summary>

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[2])
```

**Output:**

```text
30
```

</details>

### Q3. Second from last

Print the second item from the end using a negative index.

<details>
<summary>Solution</summary>

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[-2])
```

**Output:**

```text
70
```

</details>

### Q4. First three

Print the first three items as a list.

<details>
<summary>Solution</summary>

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[:3])
```

**Output:**

```text
[10, 20, 30]
```

</details>

### Q5. Last three

Print the last three items as a list.

<details>
<summary>Solution</summary>

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[-3:])
```

**Output:**

```text
[60, 70, 80]
```

</details>

### Q6. The middle

Print everything except the first and the last item.

<details>
<summary>Solution</summary>

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[1:-1])
```

**Output:**

```text
[20, 30, 40, 50, 60, 70]
```

</details>

### Q7. Every second item

Print every second item, starting from the first.

<details>
<summary>Solution</summary>

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[::2])
```

**Output:**

```text
[10, 30, 50, 70]
```

</details>

### Q8. Reverse

Print the list in reverse order without changing the original list.

<details>
<summary>Solution</summary>

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[::-1])
print(numbers)
```

**Output:**

```text
[80, 70, 60, 50, 40, 30, 20, 10]
[10, 20, 30, 40, 50, 60, 70, 80]
```

</details>

### Q9. Items from index 2 to index 5

Print the items at indexes 2, 3, 4 and 5.

<details>
<summary>Solution</summary>

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[2:6])
```

**Output:**

```text
[30, 40, 50, 60]
```

The stop must be `6` because the stop index is excluded.

</details>

### Q10. Predict the output

For `nums = [10, 20, 30, 40, 50, 60]`, work out what each line prints before checking.

```python
nums = [10, 20, 30, 40, 50, 60]

print(nums[2:5])
print(nums[:2])
print(nums[-2:])
print(nums[::3])
print(nums[4:1])
print(nums[3])
print(nums[3:4])
```

<details>
<summary>Solution</summary>

```python
nums = [10, 20, 30, 40, 50, 60]

print(nums[2:5])
print(nums[:2])
print(nums[-2:])
print(nums[::3])
print(nums[4:1])
print(nums[3])
print(nums[3:4])
```

**Output:**

```text
[30, 40, 50]
[10, 20]
[50, 60]
[10, 40]
[]
40
[40]
```

</details>

### Q11 (Challenge). Palindrome list

Write a function `is_palindrome_list(items)` that returns `True` if a list reads the same forwards and backwards. Test with `[1, 2, 3, 2, 1]` and `[1, 2, 3]`.

<details>
<summary>Solution</summary>

```python
def is_palindrome_list(items):
    return items == items[::-1]

print(is_palindrome_list([1, 2, 3, 2, 1]))
print(is_palindrome_list([1, 2, 3]))
```

**Output:**

```text
True
False
```

</details>

### Q12 (Challenge). Swap the halves

Write a function `swap_halves(items)` that takes a list with an even number of items and returns a new list with the second half first. For `[1, 2, 3, 4, 5, 6]` it should return `[4, 5, 6, 1, 2, 3]`.

<details>
<summary>Solution</summary>

```python
def swap_halves(items):
    middle = len(items) // 2
    return items[middle:] + items[:middle]

print(swap_halves([1, 2, 3, 4, 5, 6]))
```

**Output:**

```text
[4, 5, 6, 1, 2, 3]
```

</details>

---

# 14. Summary

| Idea | Example | Result for `[10, 20, 30, 40, 50]` |
|---|---|---|
| Index (from front) | `lst[0]` | `10` |
| Index (from back) | `lst[-1]` | `50` |
| Slice | `lst[1:4]` | `[20, 30, 40]` |
| From the start | `lst[:2]` | `[10, 20]` |
| To the end | `lst[3:]` | `[40, 50]` |
| Last 2 | `lst[-2:]` | `[40, 50]` |
| Step | `lst[::2]` | `[10, 30, 50]` |
| Reverse | `lst[::-1]` | `[50, 40, 30, 20, 10]` |

**Golden rules**

1. Indexes start at **0**.
2. `-1` is the **last** item.
3. In a slice, **start is included** and **stop is excluded**.
4. An index gives an **item**. A slice gives a **list**.
5. Slicing never raises an `IndexError`. Indexing can.

**Next:** [List Methods](list_methods.md)
