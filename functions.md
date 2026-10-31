# 🐍 Python Functions — Beginner's Guide

A practical lesson covering function definitions, parameters, `print()`, `return`, conditions, loops, variable scope, and practice problems.

## What You'll Learn

- What functions are and why we use them
- How to define and call functions
- How to use parameters and arguments
- The difference between `print()` and `return`
- How functions work with conditions and loops
- Local and global variable scope
- Practice problems from beginner to challenge level

## Table of Contents

1. [Function Basics](#function-basics)
2. [Examples: Step by Step](#examples-step-by-step)
3. [Variable Scope](#variable-scope)
4. [Practice Problems](#practice-problems)
5. [Quick Summary](#quick-summary)

---

## Function Basics

A **function** is a reusable block of code with a name.

| Syntax | Meaning |
|---|---|
| `def` | **Creates** (defines) a function |
| `name()` | **Calls** (runs) the function |

A function helps us write code once and reuse it whenever we need it.

> **Tip:** Run one example at a time if you want to focus on a particular concept. Put a `#` in front of the others to switch them off.

---

## Examples: Step by Step

### Step 1: A simple function

The simplest kind of function: no inputs and nothing sent back. `def` creates the function, and writing `say_hello()` runs it.

```python
def say_hello():
    print("Hello!")

say_hello()
```

Output:

```text
Hello!
```

### Step 2: Reusable - call it many times

A function is **reusable**. Write it once, then call it as many times as you like.

```python
say_hello()
say_hello()
say_hello()
```

Output:

```text
Hello!
Hello!
Hello!
```

### Step 3: Function with a parameter

A **parameter** lets us pass information into a function. Here `name` receives `"Ali"` the first time and `"Sara"` the second time.

```python
# A parameter is a variable that receives a value when we call the function.
def greet(name):
    print("Hello", name)

greet("Ali")
greet("Sara")
```

Output:

```text
Hello Ali
Hello Sara
```

### Step 4: Two parameters

A function can have more than one parameter. Separate them with commas.

```python
def show_sum(a, b):
    print(a, "+", b, "=", a + b)

show_sum(3, 4)
show_sum(10, 25)
```

Output:

```text
3 + 4 = 7
10 + 25 = 35
```

### Step 5: Introducing return

This is the big idea of the lesson. `print()` and `return` look similar, but they do different jobs:

| | What it does | Can you use the result later? |
|---|---|---|
| `print()` | **Shows** something on the screen | No |
| `return` | **Sends a value back** to where the function was called | Yes: store it, print it or calculate with it |

> **Analogy: a vending machine.** You press a button (call the function) and the machine gives you a snack (the return value) that you can keep and use.

```python
# print  -> SHOWS something on the screen. Nothing comes back.
# return -> SENDS a value BACK to the place where the function was called.
# Analogy: a vending machine. You press a button (call the function)
# and the machine gives you a snack (return value) that you can keep and use.
def add(a, b):
    return a + b

result = add(3, 4)       # the answer comes back and is stored in result
print(result)
print(add(10, 5))        # we can also print it directly
print(add(2, 3) * 10)    # and use it in a calculation: 5 * 10 = 50
```

Output:

```text
7
15
50
```

### Step 6: What if there is NO return?

If a function has no `return`, nothing comes back. Python gives you the special value `None`.

```python
def add_no_return(a, b):
    print(a + b)         # only shows the answer, does not send it back

x = add_no_return(3, 4)  # prints 7
print(x)                 # None -> nothing came back!
```

Output:

```text
7
None
```

### Step 7: Return + variables

A function can create its own variables and return them.

```python
def area_of_rectangle(length, width):
    area = length * width
    return area

print(area_of_rectangle(5, 3))
a1 = area_of_rectangle(4, 6)
print("Area:", a1)
```

Output:

```text
15
Area: 24
```

### Step 8: Return + conditions (True / False)

A function can return `True` or `False`. This is useful for yes/no questions like "is this number even?".

```python
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))
```

Output:

```text
True
False
```

### Step 9: Using the returned value in an if

Because `is_even(10)` returns `True` or `False`, we can use it directly inside an `if`.

```python
if is_even(10):
    print("10 is even")
```

Output:

```text
10 is even
```

### Step 10: Return different messages

A function can return different messages depending on a condition.

```python
def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

print(check_age(20))
print(check_age(12))
```

Output:

```text
Adult
Minor
```

### Step 11: Return ends the function immediately

`return` ends the function **immediately**. Any code after a `return` that runs is skipped, so the second `return` only happens if the `if` did not return.

```python
def positive_or_not(n):
    if n > 0:
        return "Positive"
    return "Not positive"    # runs only if the if above did not return

print(positive_or_not(5))
print(positive_or_not(-3))
```

Output:

```text
Positive
Not positive
```

### Step 12: If / elif / else with return

Use `if / elif / else` with `return` when there are more than two outcomes.

```python
def grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    else:
        return "C"

print(grade(85))
print(grade(65))
print(grade(30))
```

Output:

```text
A
B
C
```

### Step 13: Function with a loop inside

A function can have a loop inside it. This one prints a multiplication table for any number.

```python
def print_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

print_table(2)
print_table(5)
```

Output:

```text
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

### Step 14: Loop + variable + return

Combine a loop, a variable and `return` to calculate a total.

```python
def sum_to(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

print(sum_to(5))     # 15
print(sum_to(100))   # 5050
```

Output:

```text
15
5050
```

### Step 15: Loop + condition + return

Combine a loop, a condition and `return` to count things.

```python
def count_even(n):
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            count = count + 1
    return count

print(count_even(20))   # 10
```

Output:

```text
10
```

### Step 16: A function using another function

A function can call another function. Here `sum_of_squares` reuses `square`.

```python
def square(n):
    return n * n

def sum_of_squares(a, b):
    return square(a) + square(b)

print(sum_of_squares(3, 4))   # 9 + 16 = 25
```

Output:

```text
25
```

---

## Variable Scope

**Scope** means the place where a variable can be seen and used.

| Kind | Where it is created | Where it can be used |
|---|---|---|
| **Local variable** | Inside a function | Only inside that function |
| **Global variable** | Outside all functions | Everywhere (functions can read it) |
| **Parameter** | In the function's brackets | Only inside that function (it is local) |

### Scope Examples

### Step 17: Local variables

A variable created **inside** a function is **local**. It is born when the function starts and disappears when it ends.

> **Analogy: your private notebook inside your school bag.** Only you (the function) can read it. Nobody outside can.

> **Try it:** remove the `#` in front of `print(secret)` to see the `NameError`.

```python
# Scope = the place where a variable can be seen and used.
# A variable created INSIDE a function is LOCAL.
# It is born when the function starts and disappears when it ends.
# Analogy: your private notebook inside your school bag.
# Only you (the function) can see it. Nobody outside can read it.
def make_secret():
    secret = "I live only inside this function"
    print(secret)         # works: we are inside the function

make_secret()
# print(secret)           # ERROR (NameError): secret does not exist out here.
#                         # Remove the # at the start of the line to see it.
```

Output:

```text
I live only inside this function
```

### Step 18: Global variables

A variable created **outside** all functions is **global**. Any function can read it.

> **Analogy: the notice board in the school corridor.** Every classroom (function) can walk out and read it.

```python
# A variable created OUTSIDE all functions is GLOBAL.
# Analogy: the notice board in the school corridor.
# Every classroom (function) can walk out and READ it.
school_name = "Python Academy"

def welcome_student(name):
    print("Welcome", name, "to", school_name)   # reads the global variable

welcome_student("Ali")
welcome_student("Sara")
```

Output:

```text
Welcome Ali to Python Academy
Welcome Sara to Python Academy
```

### Step 19: Parameters are local too

Parameters are local too. They only exist inside their own function.

```python
# Parameters only exist inside their function.
def triple(n):
    return n * 3

print(triple(4))
# print(n)                # ERROR: n belongs to triple() only.
```

Output:

```text
12
```

### Step 20: Same name, different variables

If a function creates a variable with the **same name** as a global one, Python makes a brand new local variable. The global one stays unchanged.

```python
# If a function creates a variable with the SAME name as a global one,
# Python makes a brand new local variable. The global one stays unchanged.
level = 1                 # global

def change_level():
    level = 99            # NEW local variable, not the global one
    print("Inside function:", level)

change_level()
print("Outside function:", level)   # still 1
```

Output:

```text
Inside function: 99
Outside function: 1
```

### Step 21: Changing a global variable

A function can **read** a global freely, but it cannot **change** it by default. There are two ways around that:

1. The `global` keyword. It works, but use it sparingly because it makes code harder to follow.
2. **Better:** pass the value in and `return` the new value.

```python
# A function can READ a global freely, but it cannot CHANGE it by default.
points = 0

def add_point_broken():
    # points = points + 1   # ERROR (UnboundLocalError): Python thinks
    #                       # points is local here, but it has no value yet.
    pass

# Option 1: the global keyword. It works, but use it sparingly,
# because it makes code harder to follow.
def add_point_global():
    global points
    points = points + 1

add_point_global()
add_point_global()
print("Points (global keyword):", points)   # 2

# Option 2 (BETTER): pass the value in and RETURN the new value.
def add_point(current):
    return current + 1

points = add_point(points)
print("Points (with return):", points)      # 3
```

Output:

```text
Points (global keyword): 2
Points (with return): 3
```

### Step 22: Every call starts fresh

Local variables are created again every time the function runs, so they never remember the previous call.

```python
# Local variables are created again each time the function runs.
def counter_demo():
    count = 0
    count = count + 1
    return count

print(counter_demo())   # 1
print(counter_demo())   # 1 again, not 2! The old count was thrown away.
```

Output:

```text
1
1
```

### Scope Summary

| Kind | Think of it as |
|---|---|
| **Local** | A private notebook. Created inside a function and only usable inside it |
| **Global** | A notice board. Created outside functions and readable everywhere |

- To get information **out** of a function, use `return`.
- To get information **into** a function, use parameters.

---

## Practice Problems

The exercises go from simple functions to challenges that combine functions, conditions, loops and scope. Try each one yourself first, then click **Solution** to check your answer.

### Level 1: Simple functions (no parameters)

#### Q1

Create a function called `welcome()` that prints "Welcome to Python class". Call it 3 times.

<details>
<summary>Solution</summary>

```python
def welcome():
    print("Welcome to Python class")

welcome()
welcome()
welcome()
```

Output:

```text
Welcome to Python class
Welcome to Python class
Welcome to Python class
```

</details>

#### Q2

Create a function called `draw_line()` that prints 10 stars on one line. Call it twice.

<details>
<summary>Solution</summary>

```python
def draw_line():
    print("*" * 10)

draw_line()
draw_line()
```

Output:

```text
**********
**********
```

</details>

### Level 2: Parameters

#### Q3

Create a function called `say_name(name)` that prints "My name is ___". Call it with two different names.

<details>
<summary>Solution</summary>

```python
def say_name(name):
    print("My name is", name)

say_name("Ali")
say_name("Fatima")
```

Output:

```text
My name is Ali
My name is Fatima
```

</details>

#### Q4

Create a function called `show_square(n)` that **PRINTS** the square of n. Call it with 5 and 9.

<details>
<summary>Solution</summary>

```python
def show_square(n):
    print(n * n)

show_square(5)
show_square(9)
```

Output:

```text
25
81
```

</details>

#### Q5

Create a function called `repeat_word(word, times)` that prints the word that many times using a loop. Example: `repeat_word("Hi", 4)`

<details>
<summary>Solution</summary>

```python
def repeat_word(word, times):
    for i in range(times):
        print(word)

repeat_word("Hi", 4)
```

Output:

```text
Hi
Hi
Hi
Hi
```

</details>

### Level 3: return

#### Q6

Create a function called `multiply(a, b)` that **RETURNS** a * b. Print `multiply(6, 7)`.

<details>
<summary>Solution</summary>

```python
def multiply(a, b):
    return a * b

print(multiply(6, 7))
```

Output:

```text
42
```

</details>

#### Q7

Create a function called `double(n)` that **RETURNS** n * 2. Then store `double(8)` in a variable and print the variable.

<details>
<summary>Solution</summary>

```python
def double(n):
    return n * 2

answer = double(8)
print(answer)
```

Output:

```text
16
```

</details>

#### Q8

Create a function called `perimeter_of_rectangle(length, width)` that **RETURNS** 2 * (length + width). Print `perimeter_of_rectangle(5, 3)`.

<details>
<summary>Solution</summary>

```python
def perimeter_of_rectangle(length, width):
    return 2 * (length + width)

print(perimeter_of_rectangle(5, 3))
```

Output:

```text
16
```

</details>

#### Q9

Create a function called `total_cost(price, quantity)` that **RETURNS** the total. Use it to print the cost of 4 items priced at 50.

<details>
<summary>Solution</summary>

```python
def total_cost(price, quantity):
    return price * quantity

print(total_cost(50, 4))
```

Output:

```text
200
```

</details>

#### Q10

Without writing a new function, use `multiply()` from Q6 to calculate (2 * 3) * 4 in a single print line.

<details>
<summary>Solution</summary>

```python
print(multiply(multiply(2, 3), 4))
```

Output:

```text
24
```

</details>

### Level 4: return with conditions

#### Q11

Create a function called `is_positive(n)` that **RETURNS** True if n is greater than 0, otherwise False. Test with 5 and -2.

<details>
<summary>Solution</summary>

```python
def is_positive(n):
    if n > 0:
        return True
    else:
        return False

print(is_positive(5))
print(is_positive(-2))
```

Output:

```text
True
False
```

</details>

#### Q12

Create a function called `is_odd(n)` that **RETURNS** True if n is odd. Test with 7 and 10.

<details>
<summary>Solution</summary>

```python
def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False

print(is_odd(7))
print(is_odd(10))
```

Output:

```text
True
False
```

</details>

#### Q13

Create a function called `bigger(a, b)` that **RETURNS** the larger number. Test with (10, 4) and (3, 9).

<details>
<summary>Solution</summary>

```python
def bigger(a, b):
    if a > b:
        return a
    else:
        return b

print(bigger(10, 4))
print(bigger(3, 9))
```

Output:

```text
10
9
```

</details>

#### Q14

Create a function called `pass_or_fail(marks)` that **RETURNS** "Pass" if marks are 50 or more, otherwise "Fail". Test with 72 and 35.

<details>
<summary>Solution</summary>

```python
def pass_or_fail(marks):
    if marks >= 50:
        return "Pass"
    else:
        return "Fail"

print(pass_or_fail(72))
print(pass_or_fail(35))
```

Output:

```text
Pass
Fail
```

</details>

#### Q15

Create a function called `number_type(n)` that **RETURNS** "Positive", "Negative" or "Zero". Test with 8, -3 and 0.

<details>
<summary>Solution</summary>

```python
def number_type(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

print(number_type(8))
print(number_type(-3))
print(number_type(0))
```

Output:

```text
Positive
Negative
Zero
```

</details>

#### Q16

Create a function called `can_vote(age)` that **RETURNS** True if age is 18 or more. Then use it in an if statement to print "You can vote" or "You cannot vote" for age 20.

<details>
<summary>Solution</summary>

```python
def can_vote(age):
    return age >= 18

if can_vote(20):
    print("You can vote")
else:
    print("You cannot vote")
```

Output:

```text
You can vote
```

</details>

### Level 5: Functions with loops

#### Q17

Create a function called `countdown(n)` that prints numbers from n down to 1. Call `countdown(5)`.

<details>
<summary>Solution</summary>

```python
def countdown(n):
    for i in range(n, 0, -1):
        print(i)

countdown(5)
```

Output:

```text
5
4
3
2
1
```

</details>

#### Q18

Create a function called `sum_even(n)` that **RETURNS** the sum of all even numbers from 1 to n. Test with 10 (answer: 30).

<details>
<summary>Solution</summary>

```python
def sum_even(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total = total + i
    return total

print(sum_even(10))
```

Output:

```text
30
```

</details>

#### Q19

Create a function called `count_divisible(n, d)` that **RETURNS** how many numbers from 1 to n are divisible by d. Test with `count_divisible(50, 3)` (answer: 16).

<details>
<summary>Solution</summary>

```python
def count_divisible(n, d):
    count = 0
    for i in range(1, n + 1):
        if i % d == 0:
            count = count + 1
    return count

print(count_divisible(50, 3))
```

Output:

```text
16
```

</details>

#### Q20

Create a function called `factorial(n)` that **RETURNS** n! Example: 5! = 5 x 4 x 3 x 2 x 1 = 120. Test with 5.

<details>
<summary>Solution</summary>

```python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

print(factorial(5))
```

Output:

```text
120
```

</details>

### Level 6: Challenges (combining everything)

#### Q21 (Challenge)

Create a function called `is_prime(n)` that **RETURNS** True if n is prime, otherwise False. (A prime is only divisible by 1 and itself; numbers below 2 are not prime.) Test with 7, 10 and 2.

<details>
<summary>Solution</summary>

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(10))
print(is_prime(2))
```

Output:

```text
True
False
True
```

</details>

#### Q22 (Challenge)

Using `is_prime()` from Q21, create a function called `count_primes(n)` that **RETURNS** how many primes are between 1 and n. Test with 20 (answer: 8).

<details>
<summary>Solution</summary>

```python
def count_primes(n):
    count = 0
    for i in range(1, n + 1):
        if is_prime(i):
            count = count + 1
    return count

print(count_primes(20))
```

Output:

```text
8
```

</details>

#### Q23 (Challenge)

Create a function called `fizzbuzz(n)` that **RETURNS** "Fizz" if n is divisible by 3, "Buzz" if by 5, "FizzBuzz" if by both, otherwise n. Then use a loop from 1 to 15 to print `fizzbuzz(i)`.

<details>
<summary>Solution</summary>

```python
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

for i in range(1, 16):
    print(fizzbuzz(i))
```

Output:

```text
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

</details>

### Level 7: Scope

#### Q24

Predict the output **BEFORE** running. What do the two prints show? `x = 10` is global; the function creates its own `x = 5`.

<details>
<summary>Solution</summary>

```python
x = 10

def show_x():
    x = 5
    print(x)

show_x()
print(x)
# Answer: 5 (local x inside the function), then 10 (global x is unchanged).
```

Output:

```text
5
10
```

</details>

#### Q25

Create a global variable favorite_color = "blue". Create a function called `print_favorite()` that prints "My favorite color is ___" using the global variable. Call it.

<details>
<summary>Solution</summary>

```python
favorite_color = "blue"

def print_favorite():
    print("My favorite color is", favorite_color)

print_favorite()
```

Output:

```text
My favorite color is blue
```

</details>

#### Q26

Create a global variable score = 10. Create a function `add_bonus(s)` that **RETURNS** s + 5. Update score using the function, then print it (answer: 15).

<details>
<summary>Solution</summary>

```python
score = 10

def add_bonus(s):
    return s + 5

score = add_bonus(score)
print(score)
```

Output:

```text
15
```

</details>

#### Q27

Create a global variable counter = 0. Create a function `increase()` that adds 1 to counter using the global keyword. Call it 3 times, then print counter (answer: 3).

<details>
<summary>Solution</summary>

```python
counter = 0

def increase():
    global counter
    counter = counter + 1

increase()
increase()
increase()
print(counter)
```

Output:

```text
3
```

</details>

#### Q28 (Challenge)

Do Q27 again **WITHOUT** the global keyword. Create `increase_value(c)` that **RETURNS** c + 1, and use it 3 times with a variable called counter2 (answer: 3).

<details>
<summary>Solution</summary>

```python
def increase_value(c):
    return c + 1

counter2 = 0
counter2 = increase_value(counter2)
counter2 = increase_value(counter2)
counter2 = increase_value(counter2)
print(counter2)
```

Output:

```text
3
```

</details>

#### Q29 (Challenge)

Predict the output **BEFORE** running. Why isn't it 2? (Hint: think about local variables and what the function returns.)

<details>
<summary>Solution</summary>

```python
total_calls = 0

def add_one():
    total_calls = 1
    return total_calls

add_one()
add_one()
print(total_calls)
# Answer: 0. Inside add_one(), total_calls is a NEW local variable.
# The global total_calls is never changed, and the returned value is ignored.
```

Output:

```text
0
```

</details>

---

## Quick Summary

- Use **parameters** to pass information into a function.
- Use **`return`** to send a value back from a function.
- Use **`print()`** to display information on the screen.
- **Local** variables belong to the function where they are created.
- **Global** variables are created outside functions.
- Returning a new value is often clearer than changing a global variable.
