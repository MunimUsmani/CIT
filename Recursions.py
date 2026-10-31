# Recursion in Python

Recursion is when a **function calls itself** to solve a smaller version of the same problem.

> **Before you start:** this lesson uses only functions, variables, conditions, `return` and scope. Examples that need lists or string slicing are saved for the end, in [After Lists & Strings](#after-lists--strings), so you can teach them later.

## Table of Contents

- [What is Recursion?](#what-is-recursion)
- [The Two Parts of Every Recursive Function](#the-two-parts-of-every-recursive-function)
- [Example 1: Factorial](#example-1-factorial)
- [Simple Examples](#simple-examples)
- [Real-World Examples](#real-world-examples)
- [Math Examples](#math-examples)
- [Recursion vs Loops](#recursion-vs-loops)
- [Common Mistakes](#common-mistakes)
- [Challenge Problems](#challenge-problems)
- [Key Tips](#key-tips)
- [After Lists & Strings](#after-lists--strings)
- [What's Next](#whats-next)

---

## What is Recursion?

Imagine standing between two mirrors. You see smaller and smaller reflections of yourself, again and again.

Recursion works the same way: the same thing happens **inside itself**, over and over, until a **stop condition** is reached. That stop condition is called the **base case**.

### Stairs analogy

You are on the 5th floor and want to reach the ground floor.

| Question | Meaning in recursion |
|----------|----------------------|
| "Am I on the ground floor?" If yes, stop. | **Base case** |
| "No? Take one step down and ask again." | **Recursive case** |

---

## The Two Parts of Every Recursive Function

Every recursive function needs both of these:

| Part | Job |
|------|-----|
| **Base case** | Tells the function **when to stop** |
| **Recursive case** | Makes the problem **smaller** and calls the function again |

### Template

```python
def recursive_function(input):
    # BASE CASE: when to stop
    if input_meets_stop_condition:
        return simple_result

    # RECURSIVE CASE: make the problem smaller and call yourself
    return combine_result_with_recursive_function(smaller_input)
```

---

## Example 1: Factorial

The factorial of a number `n` (written `n!`) is the product of every whole number from `n` down to 1.

```text
5! = 5 × 4 × 3 × 2 × 1 = 120
```

Notice that `5! = 5 × 4!`. Factorial is defined using a smaller factorial, which makes it a perfect fit for recursion. We stop at `0! = 1`.

```python
def factorial(n):
    if n == 0:                      # base case
        return 1
    return n * factorial(n - 1)     # recursive case

print(factorial(5))
```

Output:

```text
120
```

### Dry run of `factorial(4)`

Recursion happens in **two phases**.

**Phase 1: Going down.** The function keeps calling itself until it reaches the base case.

```text
factorial(4)  →  4 * factorial(3)
factorial(3)  →  3 * factorial(2)
factorial(2)  →  2 * factorial(1)
factorial(1)  →  1 * factorial(0)
factorial(0)  →  base case reached, returns 1
```

**Phase 2: Coming back up.** Each call receives the answer from the call below it and returns its own result.

```text
factorial(0) returns 1
factorial(1) returns 1 × 1 = 1
factorial(2) returns 2 × 1 = 2
factorial(3) returns 3 × 2 = 6
factorial(4) returns 4 × 6 = 24
```

> **Analogy:** like a stack of plates. You must wait for the top plates to be dealt with before you can finish the ones at the bottom.

---

## Simple Examples

### Countdown

Print numbers from `n` down to 1, then a message.

```python
def countdown(n):
    if n == 0:
        print("Blast off!")
        return
    print(n)
    countdown(n - 1)

countdown(3)
```

Output:

```text
3
2
1
Blast off!
```

### Sum from 1 to N

```python
def sum_to_n(n):
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)

print(sum_to_n(5))
```

Output:

```text
15
```

The calls unfold like this: `5 + (4 + (3 + (2 + 1)))`.

### Print a stars pattern

```python
def print_stars(n):
    if n == 0:
        return
    print("*" * n)
    print_stars(n - 1)

print_stars(4)
```

Output:

```text
****
***
**
*
```

---

## Real-World Examples

### Count the digits of a phone number

Each call removes the last digit (using `// 10`) and adds 1 to the count.

```python
def count_digits(number):
    number = abs(number)

    if number < 10:         # one digit left (this also covers 0)
        return 1
    return 1 + count_digits(number // 10)

print(count_digits(3001234567))
```

Output:

```text
10
```

### Compound interest

Each year the amount grows by the interest rate. Each call handles one year.

```python
def compound_interest(principal, years, rate=0.05):
    if years == 0:
        return principal
    new_amount = principal * (1 + rate)
    return compound_interest(new_amount, years - 1, rate)

print(round(compound_interest(1000, 3), 2))
```

Output:

```text
1157.62
```

### Distribute pizza slices

Each person takes an equal share of what is left. The last person gets whatever remains.

```python
def distribute_slices(total_slices, people):
    if people == 1:
        return total_slices

    slices_per_person = total_slices // people
    remaining_slices = total_slices - slices_per_person

    print("Person gets", slices_per_person, "slices")
    return distribute_slices(remaining_slices, people - 1)

last = distribute_slices(10, 3)
print("Last person gets", last, "slices")
```

Output:

```text
Person gets 3 slices
Person gets 3 slices
Last person gets 4 slices
```

### Reading tracker

How many pages will you read in total if you read the same number each day?

```python
def pages_read_total(pages_per_day, days):
    if days == 0:
        return 0
    return pages_per_day + pages_read_total(pages_per_day, days - 1)

print(pages_read_total(20, 5))
```

Output:

```text
100
```

---

## Math Examples

### Fibonacci

Each number is the sum of the two numbers before it: `0, 1, 1, 2, 3, 5, 8, ...`

This function calls itself **twice** each time, which makes it a little harder to follow.

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(7):
    print(fibonacci(i))
```

Output:

```text
0
1
1
2
3
5
8
```

### Sum of digits and digital root

`sum_digits` adds up every digit of a number. The digital root keeps doing that until only one digit is left.

```python
def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)

def digital_root(n):
    if n < 10:
        return n
    return digital_root(sum_digits(n))

print(sum_digits(1234))
print(digital_root(9875))
```

Output:

```text
10
2
```

For `9875`: 9+8+7+5 = 29, then 2+9 = 11, then 1+1 = 2.

### Reverse a number

Each call takes off the last digit and adds it to the end of the new number.

```python
def reverse_number(n, reversed_n=0):
    if n == 0:
        return reversed_n

    last_digit = n % 10
    reversed_n = reversed_n * 10 + last_digit

    return reverse_number(n // 10, reversed_n)

print(reverse_number(1234))
```

Output:

```text
4321
```

---

## Recursion vs Loops

Anything you can do with recursion you can also do with a loop.

```python
# Recursion
def sum_to_n(n):
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)

# Loop
def sum_to_n_loop(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total
```

| | Recursion | Loop |
|---|-----------|------|
| Style | Elegant and short for some problems | Simple and direct |
| Good for | Trees, nested structures, divide and conquer | Counting, repeating a fixed number of times |
| Risk | Very large inputs can cause a `RecursionError` (stack overflow) | Very low |

Python stops a recursive function after about 1000 calls. You will see why when we learn the **call stack**.

---

## Common Mistakes

### 1. Forgetting the base case

Without a base case, the function never stops.

```python
def countdown_broken(n):
    print(n)
    countdown_broken(n - 1)     # never stops!
```

Python eventually raises `RecursionError: maximum recursion depth exceeded`.

### 2. Not making the problem smaller

Every recursive call must move **closer** to the base case.

```python
def countdown_broken(n):
    if n == 0:
        return
    print(n)
    countdown_broken(n)         # n never changes, so it never reaches 0
```

### 3. Forgetting `return` on the recursive call

```python
def sum_to_n_broken(n):
    if n == 1:
        return 1
    n + sum_to_n_broken(n - 1)  # missing return: the answer is thrown away
```

This function returns `None` for every `n` except 1.

---

## Challenge Problems

Try each one yourself first. Click **Solution** to check.

### Easy

**1. `count_steps(stairs)`**: return how many steps it takes to climb `stairs` stairs, one step at a time.

<details>
<summary>Solution</summary>

```python
def count_steps(stairs):
    if stairs == 0:
        return 0
    return 1 + count_steps(stairs - 1)

print(count_steps(5))   # 5
```

</details>

**2. `birthday_countdown(days)`**: print how many days are left, ending with "Happy Birthday!".

<details>
<summary>Solution</summary>

```python
def birthday_countdown(days):
    if days == 0:
        print("Happy Birthday!")
        return
    print(days, "days left")
    birthday_countdown(days - 1)

birthday_countdown(3)
```

Output:

```text
3 days left
2 days left
1 days left
Happy Birthday!
```

</details>

**3. `total_allowance(amount, weeks)`**: return the total allowance you will receive after `weeks` weeks.

<details>
<summary>Solution</summary>

```python
def total_allowance(amount, weeks):
    if weeks == 0:
        return 0
    return amount + total_allowance(amount, weeks - 1)

print(total_allowance(50, 4))   # 200
```

</details>

### Medium

**4. `decimal_to_binary(n)`**: convert a whole number to binary (returned as text). *Hint: divide by 2 and use the remainder.*

<details>
<summary>Solution</summary>

```python
def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_to_binary(n // 2) + str(n % 2)

print(decimal_to_binary(10))   # 1010
```

</details>

**5. `gcd(a, b)`**: find the greatest common divisor using Euclid's algorithm. *Hint: `gcd(a, b)` is the same as `gcd(b, a % b)`. Stop when `b` is 0.*

<details>
<summary>Solution</summary>

```python
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))   # 6
```

</details>

---

## Key Tips

1. Find the **smallest possible input**. That is your base case.
2. **Trust the process.** Assume the recursive call works, and just use its answer.
3. **Draw it out** on paper (going down, then coming back up).
4. **Always confirm** the base case exists and is reachable.
5. Practice a little every day.

---

## After Lists & Strings

> These examples need **lists**, **slicing** (`lst[1:]`), or other topics that come later. Come back to this section once those are taught.

### Reverse a string

```python
def reverse(s):
    if len(s) == 0:
        return s
    return reverse(s[1:]) + s[0]

print(reverse("python"))   # nohtyp
```

### Palindrome check

```python
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("level"))    # True
print(is_palindrome("python"))   # False
```

### Print each character

```python
def print_chars(word):
    if not word:
        return
    print(word[0])
    print_chars(word[1:])

print_chars("Hi!")
```

### Sum of list elements

```python
def list_sum(lst):
    if not lst:
        return 0
    return lst[0] + list_sum(lst[1:])

print(list_sum([1, 2, 3, 4]))   # 10
```

### Find the maximum in a list

```python
def find_max(lst):
    if len(lst) == 1:
        return lst[0]

    max_of_rest = find_max(lst[1:])
    return lst[0] if lst[0] > max_of_rest else max_of_rest

print(find_max([3, 9, 2, 7]))   # 9
```

### Binary search

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

numbers = [1, 3, 5, 7, 9, 11]
print(binary_search(numbers, 7, 0, len(numbers) - 1))   # 3
```

### Password character check

```python
def check_password_strength(password, index=0):
    if index >= len(password):
        return True

    char = password[index]
    if not (char.isalnum() or char in "!@#$%"):
        return False

    return check_password_strength(password, index + 1)

print(check_password_strength("Pass@123"))   # True
print(check_password_strength("Pass 123"))   # False
```

### Flatten a nested list

```python
def flatten_list(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

print(flatten_list([1, [2, 3], [4, [5]]]))   # [1, 2, 3, 4, 5]
```

### Shopping cart total (nested lists)

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

print(calculate_cart_total([10, [5, 5], 20]))   # 40
```

### Folder size calculator (tree-style recursion)

```python
def folder_size(structure):
    if isinstance(structure, (int, float)):
        return structure

    total_size = 0
    for item in structure:
        total_size += folder_size(item)
    return total_size

print(folder_size([10, [20, 30], [5, [15]]]))   # 80
```

### Family tree age sum

Each member is `[age, [children]]`.

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

family = [60, [[35, [[8], [5]]], [32]]]
print(family_age_sum(family))   # 140
```

### Roll the dice until you get a 6

Uses the `random` module and f-strings.

```python
import random

def roll_until_six(rolls=0):
    rolls += 1
    result = random.randint(1, 6)
    print(f"Roll {rolls}: Got {result}")

    if result == 6:
        print(f"Got 6 in {rolls} rolls!")
        return rolls

    return roll_until_six(rolls)

roll_until_six()
```

### Optimizing with memoization

Plain Fibonacci repeats the same work many times. Memoization stores answers in a dictionary so each value is calculated only once.

```python
memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

print(fib(50))   # 12586269025
```

---

## What's Next

Continue with **[Call Stack](callstack.md)** to see exactly what Python does in memory when a function calls itself, and why too many calls cause a `RecursionError`.
