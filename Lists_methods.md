# 🛠️ List Methods in Python

Every list method explained with examples: adding items, removing items, searching, sorting and copying. This file also explains the differences students most often mix up, like `append` vs `extend` and `pop` vs `remove` vs `del`.

> **Series:** [lists.md](lists.md) → [indexing_slicing.md](indexing_slicing.md) → **list_methods.md** (you are here) → [tuples.md](tuples.md)

## Table of Contents

1. [Overview of All Methods](#1-overview-of-all-methods)
2. [Where Is `push`?](#2-where-is-push)
3. [Adding Items](#3-adding-items)
4. [Removing Items](#4-removing-items)
5. [Searching in a List](#5-searching-in-a-list)
6. [Sorting and Reversing](#6-sorting-and-reversing)
7. [Copying a List](#7-copying-a-list)
8. [Handy Built-in Functions](#8-handy-built-in-functions)
9. [Common Mistakes](#9-common-mistakes)
10. [Stack Example: Undo Button](#10-stack-example-undo-button)
11. [Practice Problems](#11-practice-problems)
12. [Cheat Sheet](#12-cheat-sheet)

---

# 1. Overview of All Methods

A **method** is a function that belongs to an object. We call it with a dot: `my_list.append(5)`.

| Method | What it does | Returns | Changes the list? |
|---|---|---|:---:|
| `append(x)` | Adds `x` to the **end** | `None` | Yes |
| `insert(i, x)` | Inserts `x` **at index `i`** | `None` | Yes |
| `extend(other)` | Adds **every item** of another list | `None` | Yes |
| `remove(x)` | Removes the **first** item equal to `x` | `None` | Yes |
| `pop(i)` | Removes and **returns** the item at index `i` (last item if no `i`) | The removed item | Yes |
| `clear()` | Removes **all** items | `None` | Yes |
| `index(x)` | Position of the first `x` | An `int` | No |
| `count(x)` | How many times `x` appears | An `int` | No |
| `sort()` | Sorts the list **in place** | `None` | Yes |
| `reverse()` | Reverses the list **in place** | `None` | Yes |
| `copy()` | Makes a separate copy | A new list | No |

> **Important:** most methods that change a list return `None`. They change the list itself. Never write `my_list = my_list.sort()`.

---

# 2. Where Is `push`?

Students who have seen other languages (like JavaScript) often ask about `push`.

**Python has no `push()` for lists.** The Python method that does the same job is **`append()`**.

| Idea | JavaScript | Python |
|---|---|---|
| Add to the end | `push(x)` | `append(x)` |
| Remove from the end | `pop()` | `pop()` |

So in Python: **`append()` is your push, and `pop()` is your pop.** Together they let a list work like a stack (see [section 10](#10-stack-example-undo-button)).

---

# 3. Adding Items

## 3.1 `append()`: add one item to the end

```python
fruits = ["apple", "banana"]

fruits.append("cherry")
print(fruits)

fruits.append("mango")
print(fruits)
```

**Output:**

```text
['apple', 'banana', 'cherry']
['apple', 'banana', 'cherry', 'mango']
```

> **Analogy: joining the back of a queue.** The new person always goes to the end.

## 3.2 `insert()`: add one item at a chosen position

`insert(index, item)` puts the item at that index and shifts the others to the right.

```python
fruits = ["apple", "banana", "cherry"]

fruits.insert(1, "mango")
print(fruits)

fruits.insert(0, "grape")
print(fruits)
```

**Output:**

```text
['apple', 'mango', 'banana', 'cherry']
['grape', 'apple', 'mango', 'banana', 'cherry']
```

`insert(0, x)` adds at the **front**.

## 3.3 `extend()`: add every item from another list

```python
fruits = ["apple", "banana"]
more = ["cherry", "mango"]

fruits.extend(more)
print(fruits)
```

**Output:**

```text
['apple', 'banana', 'cherry', 'mango']
```

## 3.4 `append()` vs `extend()`: the classic confusion

`append()` adds **one thing**. If that thing is a list, the whole list goes in as a **single item**.
`extend()` adds **each item** of the list separately.

```python
a = [1, 2, 3]
b = [1, 2, 3]

a.append([4, 5])
b.extend([4, 5])

print("append:", a)
print("extend:", b)
print(len(a), len(b))
```

**Output:**

```text
append: [1, 2, 3, [4, 5]]
extend: [1, 2, 3, 4, 5]
4 5
```

| | Result | Length |
|---|---|:---:|
| `a.append([4, 5])` | `[1, 2, 3, [4, 5]]` (a list inside a list) | 4 |
| `b.extend([4, 5])` | `[1, 2, 3, 4, 5]` | 5 |

## 3.5 The `+` operator

`+` joins two lists and gives a **new** list. The originals do not change.

```python
a = [1, 2, 3]
b = [4, 5]

c = a + b

print(c)
print(a)
print(b)
```

**Output:**

```text
[1, 2, 3, 4, 5]
[1, 2, 3]
[4, 5]
```

## Adding methods compared

| | Adds | Where | Changes original list? |
|---|---|---|:---:|
| `append(x)` | One item | End | Yes |
| `insert(i, x)` | One item | At index `i` | Yes |
| `extend(other)` | Many items | End | Yes |
| `a + b` | Many items | New list | No (makes a new list) |

---

# 4. Removing Items

## 4.1 `pop()`: remove by position and get the item back

`pop()` removes the **last** item and **returns** it, so you can use it.

```python
fruits = ["apple", "banana", "cherry"]

removed = fruits.pop()

print("Removed:", removed)
print("Left:", fruits)
```

**Output:**

```text
Removed: cherry
Left: ['apple', 'banana']
```

`pop(index)` removes the item at that index.

```python
fruits = ["apple", "banana", "cherry"]

removed = fruits.pop(0)

print("Removed:", removed)
print("Left:", fruits)
```

**Output:**

```text
Removed: apple
Left: ['banana', 'cherry']
```

> **Analogy: taking the top plate from a stack.** You remove it and you are holding it.

Popping from an empty list, or from an index that does not exist, raises an `IndexError`.

```python
empty = []

empty.pop()
```

**Error:**

```text
IndexError: pop from empty list
```

## 4.2 `remove()`: remove by value

`remove(x)` finds the **first** item equal to `x` and removes it. It does **not** return anything.

```python
fruits = ["apple", "banana", "cherry", "banana"]

fruits.remove("banana")
print(fruits)
```

**Output:**

```text
['apple', 'cherry', 'banana']
```

Only the **first** `"banana"` was removed. If the value is not in the list, you get a `ValueError`.

```python
fruits = ["apple", "banana"]

fruits.remove("mango")
```

**Error:**

```text
ValueError: list.remove(x): x not in list
```

A safe way is to check first:

```python
fruits = ["apple", "banana"]

if "mango" in fruits:
    fruits.remove("mango")
else:
    print("mango is not in the list")
```

**Output:**

```text
mango is not in the list
```

## 4.3 `del`: remove by index or slice

`del` is a Python keyword, not a method. It removes by index (or a slice) and returns nothing.

```python
numbers = [10, 20, 30, 40, 50]

del numbers[0]
print(numbers)

del numbers[1:3]
print(numbers)
```

**Output:**

```text
[20, 30, 40, 50]
[20, 50]
```

## 4.4 `clear()`: empty the whole list

```python
fruits = ["apple", "banana", "cherry"]

fruits.clear()
print(fruits)
```

**Output:**

```text
[]
```

## `pop` vs `remove` vs `del`: which one?

| | `pop(i)` | `remove(x)` | `del lst[i]` |
|---|---|---|---|
| Removes by | **Index** (default: last) | **Value** (first match) | **Index** or slice |
| Returns the removed item? | **Yes** | No | No |
| If it is not there | `IndexError` | `ValueError` | `IndexError` |
| Use when | You need the removed item | You know the value, not the position | You just want it gone by position |

```python
items = ["a", "b", "c", "d", "e"]

items.pop(1)       # removes "b" by position
items.remove("d")  # removes "d" by value
del items[0]       # removes "a" by position

print(items)
```

**Output:**

```text
['c', 'e']
```

---

# 5. Searching in a List

## 5.1 `index()`: where is it?

Returns the index of the **first** match.

```python
fruits = ["apple", "banana", "cherry", "banana"]

print(fruits.index("cherry"))
print(fruits.index("banana"))
```

**Output:**

```text
2
1
```

If the value is missing, `index()` raises a `ValueError`, so check with `in` first.

```python
fruits = ["apple", "banana", "cherry"]

if "mango" in fruits:
    print(fruits.index("mango"))
else:
    print("Not found")
```

**Output:**

```text
Not found
```

## 5.2 `count()`: how many times?

```python
numbers = [1, 2, 3, 2, 2, 5]

print(numbers.count(2))
print(numbers.count(9))
```

**Output:**

```text
3
0
```

## 5.3 `in`: does it exist?

```python
fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)
print("mango" in fruits)
```

**Output:**

```text
True
False
```

| You want to know | Use |
|---|---|
| **Is** it in the list? | `x in lst` |
| **Where** is it? | `lst.index(x)` |
| **How many** are there? | `lst.count(x)` |

---

# 6. Sorting and Reversing

## 6.1 `sort()`: sort the list itself

```python
numbers = [5, 2, 9, 1, 7]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)
```

**Output:**

```text
[1, 2, 5, 7, 9]
[9, 7, 5, 2, 1]
```

`sort()` works on strings too (alphabetical order).

```python
names = ["Sara", "Ali", "Bilal", "Fatima"]

names.sort()
print(names)
```

**Output:**

```text
['Ali', 'Bilal', 'Fatima', 'Sara']
```

## 6.2 `sorted()`: get a sorted copy

`sorted()` gives a **new sorted list** and leaves the original alone.

```python
numbers = [5, 2, 9, 1, 7]

new_list = sorted(numbers)

print(new_list)
print(numbers)
```

**Output:**

```text
[1, 2, 5, 7, 9]
[5, 2, 9, 1, 7]
```

| | `numbers.sort()` | `sorted(numbers)` |
|---|---|---|
| Changes the original? | **Yes** | **No** |
| Returns | `None` | A new sorted list |
| Use when | You do not need the old order | You want to keep the original |

## 6.3 `reverse()`: flip the order

```python
numbers = [1, 2, 3, 4, 5]

numbers.reverse()
print(numbers)
```

**Output:**

```text
[5, 4, 3, 2, 1]
```

`reverse()` flips the list itself. The slice `[::-1]` gives a **new** reversed list.

```python
numbers = [1, 2, 3, 4, 5]

backwards = numbers[::-1]

print(backwards)
print(numbers)
```

**Output:**

```text
[5, 4, 3, 2, 1]
[1, 2, 3, 4, 5]
```

> `reverse()` is **not** the same as sorting in descending order. It only flips whatever order is there.

```python
numbers = [3, 1, 2]

numbers.reverse()
print(numbers)
```

**Output:**

```text
[2, 1, 3]
```

---

# 7. Copying a List

Remember: `b = a` does **not** make a copy. Both names point to the same list.

```python
a = [1, 2, 3]
b = a

b.append(99)

print(a)
print(b)
```

**Output:**

```text
[1, 2, 3, 99]
[1, 2, 3, 99]
```

Use `copy()` (or the slice `[:]`) to get a separate list.

```python
a = [1, 2, 3]
b = a.copy()

b.append(99)

print(a)
print(b)
```

**Output:**

```text
[1, 2, 3]
[1, 2, 3, 99]
```

| Way | Result |
|---|---|
| `b = a` | **Same list** (an alias) |
| `b = a.copy()` | Separate copy |
| `b = a[:]` | Separate copy |

---

# 8. Handy Built-in Functions

These are not list methods. They are functions that take a list. They do not change it.

```python
numbers = [4, 8, 15, 16, 23, 42]

print(len(numbers))
print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers) / len(numbers))
```

**Output:**

```text
6
108
4
42
18.0
```

| Function | Meaning |
|---|---|
| `len(lst)` | Number of items |
| `sum(lst)` | Total of all (numeric) items |
| `min(lst)` | Smallest item |
| `max(lst)` | Largest item |

---

# 9. Common Mistakes

### Mistake 1: Saving the result of `sort()` or `append()`

These methods return `None`.

```python
numbers = [3, 1, 2]

numbers = numbers.sort()
print(numbers)
```

**Output:**

```text
None
```

The list was sorted, but then the name `numbers` was reassigned to `None`. Do this instead:

```python
numbers = [3, 1, 2]

numbers.sort()
print(numbers)
```

**Output:**

```text
[1, 2, 3]
```

The same applies to `append`, `extend`, `insert`, `remove`, `reverse` and `clear`.

### Mistake 2: Using `append` when you meant `extend`

```python
a = [1, 2]

a.append([3, 4])
print(a)
```

**Output:**

```text
[1, 2, [3, 4]]
```

You get a list **inside** the list. Use `extend()` to add the items individually.

### Mistake 3: Removing items from a list while looping over it

```python
numbers = [1, 2, 4, 6, 7]

for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)

print(numbers)
```

**Output:**

```text
[1, 4, 7]
```

We wanted only the odd numbers, but `4` is still there. When `2` was removed, the other items shifted left, so the loop skipped over `4`. Removing items while looping shifts the positions under the loop. The safe way is to **build a new list**:

```python
numbers = [1, 2, 4, 6, 7]

odds = []
for n in numbers:
    if n % 2 != 0:
        odds.append(n)

print(odds)
```

**Output:**

```text
[1, 7]
```

### Mistake 4: Thinking `b = a` copies the list

Use `b = a.copy()` instead. See [section 7](#7-copying-a-list).

---

# 10. Stack Example: Undo Button

A **stack** is "last in, first out", like a pile of plates. You add to the top and remove from the top.

A list works as a stack:

| Stack action | List method |
|---|---|
| **Push** (add on top) | `append()` |
| **Pop** (remove from top) | `pop()` |

Here is how an **undo** button works. Every action is pushed. Undo pops the most recent one.

```python
actions = []

actions.append("typed Hello")
actions.append("typed World")
actions.append("made text bold")
print("Actions:", actions)

undone = actions.pop()
print("Undo:", undone)

undone = actions.pop()
print("Undo:", undone)

print("Remaining:", actions)
```

**Output:**

```text
Actions: ['typed Hello', 'typed World', 'made text bold']
Undo: made text bold
Undo: typed World
Remaining: ['typed Hello']
```

---

# 11. Practice Problems

Try each one yourself first. Click **Solution** to check your answer.

### Q1. Build a list

Start with an empty list. Use `append()` to add three of your favorite movies, then print the list.

<details>
<summary>Solution</summary>

```python
movies = []

movies.append("Movie A")
movies.append("Movie B")
movies.append("Movie C")

print(movies)
```

**Output:**

```text
['Movie A', 'Movie B', 'Movie C']
```

</details>

### Q2. Add at the front

Add `"Start"` at the very beginning of `["middle", "end"]`.

<details>
<summary>Solution</summary>

```python
items = ["middle", "end"]

items.insert(0, "Start")
print(items)
```

**Output:**

```text
['Start', 'middle', 'end']
```

</details>

### Q3. Join two lists

Add all items of `[4, 5, 6]` to `[1, 2, 3]` so that one list holds `1` to `6`.

<details>
<summary>Solution</summary>

```python
a = [1, 2, 3]
b = [4, 5, 6]

a.extend(b)
print(a)
```

**Output:**

```text
[1, 2, 3, 4, 5, 6]
```

</details>

### Q4. Pop it

Remove the last item from `["red", "green", "blue"]`. Print the removed item and the list that is left.

<details>
<summary>Solution</summary>

```python
colors = ["red", "green", "blue"]

removed = colors.pop()

print("Removed:", removed)
print("Left:", colors)
```

**Output:**

```text
Removed: blue
Left: ['red', 'green']
```

</details>

### Q5. Remove by value

Remove `"banana"` from `["apple", "banana", "cherry"]`.

<details>
<summary>Solution</summary>

```python
fruits = ["apple", "banana", "cherry"]

fruits.remove("banana")
print(fruits)
```

**Output:**

```text
['apple', 'cherry']
```

</details>

### Q6. Sort in descending order

Sort `[5, 2, 9, 1, 7]` from largest to smallest.

<details>
<summary>Solution</summary>

```python
numbers = [5, 2, 9, 1, 7]

numbers.sort(reverse=True)
print(numbers)
```

**Output:**

```text
[9, 7, 5, 2, 1]
```

</details>

### Q7. Keep the original

Create a sorted version of `[5, 2, 9, 1, 7]` called `sorted_numbers` **without** changing the original list. Print both.

<details>
<summary>Solution</summary>

```python
numbers = [5, 2, 9, 1, 7]

sorted_numbers = sorted(numbers)

print(sorted_numbers)
print(numbers)
```

**Output:**

```text
[1, 2, 5, 7, 9]
[5, 2, 9, 1, 7]
```

</details>

### Q8. Count it

How many times does `3` appear in `[3, 1, 3, 4, 3, 5]`?

<details>
<summary>Solution</summary>

```python
numbers = [3, 1, 3, 4, 3, 5]

print(numbers.count(3))
```

**Output:**

```text
3
```

</details>

### Q9. Find the position

Print the index of `"mango"` in `["apple", "banana", "mango", "grape"]`. Check that it exists first.

<details>
<summary>Solution</summary>

```python
fruits = ["apple", "banana", "mango", "grape"]

if "mango" in fruits:
    print(fruits.index("mango"))
else:
    print("Not found")
```

**Output:**

```text
2
```

</details>

### Q10. Predict the output

What will this print? Think first, then check.

```python
a = [1, 2, 3]
a.append([4, 5])
print(len(a))

b = [1, 2, 3]
b.extend([4, 5])
print(len(b))
```

<details>
<summary>Solution</summary>

```python
a = [1, 2, 3]
a.append([4, 5])
print(len(a))

b = [1, 2, 3]
b.extend([4, 5])
print(len(b))
```

**Output:**

```text
4
5
```

`append` adds the whole list as one item, while `extend` adds each item.

</details>

### Q11 (Challenge). Remove the duplicates

Create a new list from `[1, 2, 2, 3, 1, 4, 3]` with the duplicates removed, keeping the original order. Use a loop, `in` and `append()`.

<details>
<summary>Solution</summary>

```python
numbers = [1, 2, 2, 3, 1, 4, 3]

unique = []
for n in numbers:
    if n not in unique:
        unique.append(n)

print(unique)
```

**Output:**

```text
[1, 2, 3, 4]
```

</details>

### Q12 (Challenge). Remove the even numbers

Create a new list that keeps only the odd numbers from `[1, 2, 3, 4, 5, 6, 7, 8]`. Do **not** remove items from the original while looping.

<details>
<summary>Solution</summary>

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

odds = []
for n in numbers:
    if n % 2 != 0:
        odds.append(n)

print(odds)
```

**Output:**

```text
[1, 3, 5, 7]
```

</details>

### Q13 (Challenge). Undo twice

Use a list as a stack. Push `"a"`, `"b"`, `"c"`, `"d"` one at a time. Then pop twice and print what you popped each time and what remains.

<details>
<summary>Solution</summary>

```python
stack = []

stack.append("a")
stack.append("b")
stack.append("c")
stack.append("d")

print("Popped:", stack.pop())
print("Popped:", stack.pop())
print("Remaining:", stack)
```

**Output:**

```text
Popped: d
Popped: c
Remaining: ['a', 'b']
```

</details>

### Q14 (Challenge). Function: top two

Write a function `top_two(numbers)` that **returns** the two largest numbers as a list, largest first. Do not change the original list. Test with `[5, 12, 8, 20, 3]`.

<details>
<summary>Solution</summary>

```python
def top_two(numbers):
    ordered = sorted(numbers, reverse=True)
    return ordered[:2]

data = [5, 12, 8, 20, 3]
print(top_two(data))
print(data)
```

**Output:**

```text
[20, 12]
[5, 12, 8, 20, 3]
```

</details>

---

# 12. Cheat Sheet

| I want to... | Use |
|---|---|
| Add one item to the end | `lst.append(x)` |
| Add one item at a position | `lst.insert(i, x)` |
| Add many items | `lst.extend(other)` |
| Remove the last item (and use it) | `lst.pop()` |
| Remove the item at an index (and use it) | `lst.pop(i)` |
| Remove an item by value | `lst.remove(x)` |
| Remove by index or slice | `del lst[i]` |
| Remove everything | `lst.clear()` |
| Find the position | `lst.index(x)` |
| Count occurrences | `lst.count(x)` |
| Check if it exists | `x in lst` |
| Sort the list itself | `lst.sort()` |
| Get a sorted copy | `sorted(lst)` |
| Flip the order | `lst.reverse()` or `lst[::-1]` |
| Make a copy | `lst.copy()` or `lst[:]` |

**Next:** [Tuples](tuples.md)
