# 🧠 Recursion in Python — Complete Beginner's Guide

A beginner-friendly guide to understanding recursion in Python through simple explanations, real-life analogies, code examples, dry runs, and practice problems.

---

# 1. What is Recursion?

**Recursion** is when a function calls itself to solve a smaller version of the same problem.

Instead of solving the entire problem at once, we break it into smaller problems until we reach a point where we can stop.

### Real-Life Analogy: Two Mirrors

Imagine standing between two mirrors.

You see smaller and smaller reflections of yourself.

That's similar to recursion: the same process repeats inside itself until a stopping condition is reached.

---

# 2. Basic Recursion Structure

Every recursive function needs **two important parts**:

1. **Base Case** → When to STOP.
2. **Recursive Case** → How to make the problem SMALLER.

### Template (Pseudocode)

```python
def recursive_function(input):

    # BASE CASE: When to stop
    if input_meets_stop_condition:
        return simple_result

    # RECURSIVE CASE: Make problem smaller
    return combine_result_with_recursive_function(smaller_input)
```

### Understanding the Two Parts

| Part | Purpose |
|---|---|
| Base Case | Stops the recursion |
| Recursive Case | Calls the same function again with a smaller problem |

### Real-Life Analogy: Walking Downstairs

- Base Case → Am I on the ground floor? Stop.
- Recursive Case → Take one step down and check again.

---

# 3. Base Case vs Recursive Case

**Base Case:**
- Defines when recursion should stop.
- Prevents infinite recursive calls.
- Returns a simple result.

**Recursive Case:**
- Calls the same function again.
- Makes the problem smaller.
- Moves toward the base case.

---

# 4. Understanding Recursion with Examples

## Example 1 — Countdown

Let's print numbers from 5 to 1 using recursion.

```python
def countdown(n):
    if n == 0:
        print("Blast off! 🚀")
        return

    print(n)
    countdown(n - 1)


countdown(5)
```

**Output:**

```text
5
4
3
2
1
Blast off! 🚀
```

**How it works:**

1. Prints 5 and calls countdown(4).
2. Prints 4 and calls countdown(3).
3. Continues until n becomes 0.
4. Prints Blast off and stops.

---

## Example 2 — Factorial (n!)

### What is factorial?

Factorial means multiplying a number by all positive integers smaller than it.

For example:

```text
5! = 5 × 4 × 3 × 2 × 1 = 120
```

Remember:

```text
0! = 1
```

### Recursive Code

```python
def factorial(n):
    if n == 0:          # Base Case
        return 1

    return n * factorial(n - 1)


print(factorial(5))
```

**Output:**

```text
120
```

### Dry Run of factorial(4)

**Going Down — Recursive Calls**

```text
factorial(4)
    → 4 * factorial(3)
        → 3 * factorial(2)
            → 2 * factorial(1)
                → 1 * factorial(0)
                    → return 1
```

**Coming Back Up — Returning Values**

```text
factorial(0) → 1
factorial(1) → 1 × 1 = 1
factorial(2) → 2 × 1 = 2
factorial(3) → 3 × 2 = 6
factorial(4) → 4 × 6 = 24
```

**Final Answer: 24**

### Visualization

```text
       GOING DOWN

       factorial(4)
             |
       factorial(3)
             |
       factorial(2)
             |
       factorial(1)
             |
       factorial(0)
             |
          BASE CASE
             |
             ↓

       COMING BACK UP

       factorial(0) = 1
       factorial(1) = 1
       factorial(2) = 2
       factorial(3) = 6
       factorial(4) = 24
```

### Key Idea

Recursion happens in two phases:

1. **Forward Phase:** Functions call themselves until the base case is reached.
2. **Backward Phase:** Returned values travel back through the previous function calls.

Think of stacking plates: you put plates on top of each other, but when removing them, you remove the top plate first.

---

# 5. More Recursion Examples

## Example 3 — Fibonacci Sequence

The Fibonacci sequence is a series where each number is the sum of the previous two numbers.

```text
0, 1, 1, 2, 3, 5, 8, 13, 21...
```

### Recursive Code

```python
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))
```

**Output:**

```text
8
```

---

## Example 4 — Sum of List Elements

Calculate the sum of all elements in a list using recursion.

```python
def list_sum(lst):
    if not lst:
        return 0

    return lst[0] + list_sum(lst[1:])


numbers = [10, 20, 30, 40]

print(list_sum(numbers))
```

**Output:**

```text
100
```

---

# 6. Common Interview Recursion Problems

## 6.1 Reverse a String

```python
def reverse(s):
    if len(s) == 0:
        return s

    return reverse(s[1:]) + s[0]


print(reverse("hello"))
```

**Output:**

```text
olleh
```

## 6.2 Palindrome Check

A palindrome is a word that reads the same forward and backward.

Examples: `madam`, `level`, `radar`.

```python
def is_palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1])


print(is_palindrome("madam"))
```

**Output:**

```text
True
```

## 6.3 Greatest Common Divisor (GCD)

```python
def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


print(gcd(12, 8))
```

**Output:**

```text
4
```

## 6.4 Binary Search

Binary Search finds an element in a sorted list by repeatedly dividing the search area into halves.

```python
def binary_search(arr, target, left, right):

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)

    else:
        return binary_search(arr, target, mid + 1, right)


numbers = [10, 20, 30, 40, 50]

print(binary_search(numbers, 30, 0, len(numbers) - 1))
```

**Output:**

```text
2
```

---

# 7. Why Use Recursion?

Recursion makes certain problems easier to understand and solve.

It is particularly useful for:

- Trees
- Graphs
- Divide and conquer algorithms
- Nested lists and structures
- Backtracking problems
- File and folder traversal

### When NOT to Use Recursion

Recursion is not always the best solution.

- Large inputs can cause a recursion depth error.
- Recursive calls consume additional memory.
- Some problems are easier to solve using loops.
- Poorly designed recursion can repeat calculations unnecessarily.

---

# 8. Optimizing Recursion — Memoization

Memoization is a technique that stores previously calculated results so we don't have to calculate them again.

It is particularly useful for Fibonacci.

### Without Memoization

```python
def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)
```

The function repeatedly calculates the same values.

### With Memoization

```python
memo = {}

def fib(n):

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]


print(fib(10))
```

**Output:**

```text
55
```

---

# 9. Simple Recursion Practice Examples

## 9.1 Countdown

```python
def countdown(n):

    if n == 0:
        print("Blast off! 🚀")
        return

    print(n)
    countdown(n - 1)


countdown(5)
```

## 9.2 Sum from 1 to N

```python
def sum_to_n(n):

    if n == 1:
        return 1

    return n + sum_to_n(n - 1)


print(sum_to_n(5))
```

**Output:**

```text
15
```

## 9.3 Print Stars Pattern

```python
def print_stars(n):

    if n == 0:
        return

    print("*" * n)
    print_stars(n - 1)


print_stars(5)
```

**Output:**

```text
*****
****
***
**
*
```

## 9.4 Print Each Character

```python
def print_chars(word):

    if not word:
        return

    print(word[0])
    print_chars(word[1:])


print_chars("Python")
```

**Output:**

```text
P
y
t
h
o
n
```

---

# 10. Real-World Recursion Examples

## 10.1 Count Digits of a Number

```python
def count_digits(number):

    number = abs(number)

    if number < 10:
        return 1

    return 1 + count_digits(number // 10)


print(count_digits(12345))
```

**Output:**

```text
5
```

## 10.2 Compound Interest Recursively

```python
def compound_interest(principal, years, rate=0.05):

    if years == 0:
        return principal

    new_amount = principal * (1 + rate)

    return compound_interest(new_amount, years - 1, rate)


print(compound_interest(1000, 3))
```

## 10.3 Distribute Pizza Slices

Imagine distributing pizza slices among people one by one.

```python
def distribute_slices(total_slices, people):

    if people == 1:
        return total_slices

    slices_per_person = total_slices // people
    remaining_slices = total_slices - slices_per_person

    print(f"Person gets {slices_per_person} slices")

    return distribute_slices(remaining_slices, people - 1)


distribute_slices(12, 3)
```

## 10.4 Reading Tracker

```python
def pages_read_total(pages_per_day, days):

    if days == 0:
        return 0

    return pages_per_day + pages_read_total(pages_per_day, days - 1)


print(pages_read_total(20, 5))
```

**Output:**

```text
100
```

---

# 11. Interactive Recursion Examples

## 11.1 Roll Dice Until 6

```python
import random

def roll_until_six(rolls=0):

    rolls += 1

    result = random.randint(1, 6)

    print(f"Roll {rolls}: Got {result}")

    if result == 6:
        print(f"🎉 Got 6 in {rolls} rolls!")
        return rolls

    return roll_until_six(rolls)


roll_until_six()
```

## 11.2 Shopping Cart Total (Nested Lists)

```python
def calculate_cart_total(cart):

    if not cart:
        return 0

    item = cart[0]
    rest_of_cart = cart[1:]

    if isinstance(item, list):
        return calculate_cart_total(item) + calculate_cart_total(rest_of_cart)

    else:
        return item + calculate_cart_total(rest_of_cart)


cart = [100, 200, [50, 75], 150]

print(calculate_cart_total(cart))
```

**Output:**

```text
575
```

---

# 12. More Mathematical Recursion Problems

## 12.1 Digital Root

The digital root is calculated by repeatedly adding the digits of a number until only one digit remains.

Example:

```text
987
9 + 8 + 7 = 24
2 + 4 = 6
```

```python
def sum_digits(n):

    if n == 0:
        return 0

    return (n % 10) + sum_digits(n // 10)


def digital_root(n):

    if n < 10:
        return n

    return digital_root(sum_digits(n))


print(digital_root(987))
```

**Output:**

```text
6
```

## 12.2 Reverse a Number

```python
def reverse_number(n, reversed_n=0):

    if n == 0:
        return reversed_n

    last_digit = n % 10

    reversed_n = reversed_n * 10 + last_digit

    return reverse_number(n // 10, reversed_n)


print(reverse_number(12345))
```

**Output:**

```text
54321
```

## 12.3 Find Maximum in a List

```python
def find_max(lst):

    if len(lst) == 1:
        return lst[0]

    max_of_rest = find_max(lst[1:])

    return lst[0] if lst[0] > max_of_rest else max_of_rest


print(find_max([10, 45, 20, 90, 30]))
```

**Output:**

```text
90
```

---

# 13. Tree-Style Recursion

These examples demonstrate recursion with nested structures.

## 13.1 Folder Size Calculator

Imagine folders containing files and other folders.

```python
def folder_size(structure):

    if isinstance(structure, (int, float)):
        return structure

    total_size = 0

    for item in structure:
        total_size += folder_size(item)

    return total_size


folders = [100, [200, 300], [50, 75]]

print(folder_size(folders))
```

**Output:**

```text
725
```

## 13.2 Family Tree Age Sum

```python
def family_age_sum(member):

    if isinstance(member, (int, float)):
        return member

    age = member[0]

    children = member[1] if len(member) > 1 else []

    total_age = age

    for child in children:
        total_age += family_age_sum(child)

    return total_age


family = [50, [25, [10, 5], 20]]

print(family_age_sum(family))
```

---

# 14. Recursion Challenge Problems

Try solving these problems yourself before looking for solutions! Click **Solution** under each problem to check your answer.

## 🟢 Easy Level

### Challenge 1 — Count Steps

Write a recursive function that counts how many steps are left before reaching zero.

<details>
<summary>Solution</summary>

```python
def count_steps(stairs):

    if stairs == 0:
        return 0

    return 1 + count_steps(stairs - 1)


print(count_steps(5))
```

**Output:**

```text
5
```

</details>

### Challenge 2 — Birthday Countdown

Write a recursive function that prints how many days are left until a birthday, and finishes with a birthday message when the days reach zero.

<details>
<summary>Solution</summary>

```python
def birthday_countdown(days):

    if days == 0:
        print("🎉 Happy Birthday!")
        return

    print(f"{days} days left")

    birthday_countdown(days - 1)


birthday_countdown(5)
```

**Output:**

```text
5 days left
4 days left
3 days left
2 days left
1 days left
🎉 Happy Birthday!
```

</details>

### Challenge 3 — Total Allowance

Calculate the total allowance received over multiple weeks.

<details>
<summary>Solution</summary>

```python
def total_allowance(amount, weeks):

    if weeks == 0:
        return 0

    return amount + total_allowance(amount, weeks - 1)


print(total_allowance(500, 4))
```

**Output:**

```text
2000
```

</details>

## 🟡 Medium Level

### Challenge 4 — Check Password Characters

Check whether every character in a password is either a letter, number, or one of the allowed symbols.

<details>
<summary>Solution</summary>

```python
def check_password_strength(password, index=0):

    if index >= len(password):
        return True

    char = password[index]

    if not (char.isalnum() or char in "!@#$%"):
        return False

    return check_password_strength(password, index + 1)


print(check_password_strength("Hello@123"))
```

**Output:**

```text
True
```

</details>

### Challenge 5 — Decimal to Binary

Convert a decimal number into binary using recursion.

<details>
<summary>Solution</summary>

```python
def decimal_to_binary(n):

    if n == 0:
        return "0"

    if n == 1:
        return "1"

    return decimal_to_binary(n // 2) + str(n % 2)


print(decimal_to_binary(10))
```

**Output:**

```text
1010
```

</details>

### Challenge 6 — Flatten a Nested List

Convert a nested list into a single list.

<details>
<summary>Solution</summary>

```python
def flatten_list(nested):

    result = []

    for item in nested:

        if isinstance(item, list):
            result.extend(flatten_list(item))

        else:
            result.append(item)

    return result


numbers = [1, [2, 3], [4, [5, 6]]]

print(flatten_list(numbers))
```

**Output:**

```text
[1, 2, 3, 4, 5, 6]
```

</details>

---

# 15. Important Recursion Tips

When solving a recursion problem, always ask yourself these questions:

1. What is the smallest possible input?
2. When should the function stop?
3. How can I make the problem smaller?
4. Am I moving toward the base case?
5. What should the function return?

### Remember These Key Points

- Every recursive function needs a base case.
- Every recursive call should move toward the base case.
- Recursive functions can return values to previous calls.
- Recursion has a forward phase and a backward phase.
- Use dry runs to understand how recursive calls work.
- Use memoization when calculations are repeated.
- For very large inputs, consider iteration instead.

---

# 🎯 Final Takeaway

**Recursion = Base Case + Recursive Case**

The most important thing to understand is that a function doesn't just call itself randomly.

It breaks a problem into smaller versions of the same problem until it reaches a stopping point. Then the results travel back through the previous calls.
