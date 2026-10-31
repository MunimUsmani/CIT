🐍 Python Functions — Beginner's Guide
A practical lesson covering function definitions, parameters, print(), return, conditions, loops, variable scope, and practice problems.
What You'll Learn
- What functions are and why we use them
- How to define and call functions
- How to use parameters and arguments
- The difference between print() and return
- How functions work with conditions and loops
- Local and global variable scope
- Practice problems from beginner to challenge level
Table of Contents
1. Function Basics
2. Examples: Step by Step
3. Variable Scope
4. Practice Problems
Function Basics
A function is a reusable block of code with a name.
- def creates (defines) a function.
- name() calls (runs) a function.
- A function helps us write code once and reuse it whenever we need it.
For the examples below, run one example at a time if you want to focus on a particular concept.
Examples: Step by Step
Step 1: A simple function
def say_hello():
    print("Hello!")

say_hello()

Step 2: Reusable - call it many times
say_hello()
say_hello()
say_hello()

Step 3: Function with a parameter
# A parameter is a variable that receives a value when we call the function.
def greet(name):
    print("Hello", name)

greet("Ali")
greet("Sara")

Step 4: Two parameters
def show_sum(a, b):
    print(a, "+", b, "=", a + b)

show_sum(3, 4)
show_sum(10, 25)

Step 5: Introducing return
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

Step 6: What if there is NO return?
def add_no_return(a, b):
    print(a + b)         # only shows the answer, does not send it back

x = add_no_return(3, 4)  # prints 7
print(x)                 # None -> nothing came back!

Step 7: return + variables
def area_of_rectangle(length, width):
    area = length * width
    return area

print(area_of_rectangle(5, 3))
a1 = area_of_rectangle(4, 6)
print("Area:", a1)

Step 8: return + conditions (True / False)
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))

Step 9: Using the returned value in an if
if is_even(10):
    print("10 is even")

Step 10: return different messages
def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

print(check_age(20))
print(check_age(12))

Step 11: return ends the function immediately
def positive_or_not(n):
    if n > 0:
        return "Positive"
    return "Not positive"    # runs only if the if above did not return

print(positive_or_not(5))
print(positive_or_not(-3))

Step 12: if / elif / else with return
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

Step 13: Function with a loop inside
def print_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

print_table(2)
print_table(5)

Step 14: Loop + variable + return
def sum_to(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

print(sum_to(5))     # 15
print(sum_to(100))   # 5050

Step 15: Loop + condition + return
def count_even(n):
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            count = count + 1
    return count

print(count_even(20))   # 10

Step 16: A function using another function
def square(n):
    return n * n

def sum_of_squares(a, b):
    return square(a) + square(b)

print(sum_of_squares(3, 4))   # 9 + 16 = 25


Variable Scope
Scope means the place where a variable can be seen and used.
- Local variable: created inside a function; it is only available inside that function.
- Global variable: created outside functions; functions can read it.
- Parameters: values passed into a function; parameters are local to that function.
Scope Examples
Step 17: SCOPE - local variables
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

Step 18: SCOPE - global variables
# A variable created OUTSIDE all functions is GLOBAL.
# Analogy: the notice board in the school corridor.
# Every classroom (function) can walk out and READ it.
school_name = "Python Academy"

def welcome_student(name):
    print("Welcome", name, "to", school_name)   # reads the global variable

welcome_student("Ali")
welcome_student("Sara")

Step 19: Parameters are local too
# Parameters only exist inside their function.
def triple(n):
    return n * 3

print(triple(4))
# print(n)                # ERROR: n belongs to triple() only.

Step 20: Same name, different variables
# If a function creates a variable with the SAME name as a global one,
# Python makes a brand new local variable. The global one stays unchanged.
level = 1                 # global

def change_level():
    level = 99            # NEW local variable, not the global one
    print("Inside function:", level)

change_level()
print("Outside function:", level)   # still 1

Step 21: Changing a global variable
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

Step 22: Every call starts fresh
# Local variables are created again each time the function runs.
def counter_demo():
    count = 0
    count = count + 1
    return count

print(counter_demo())   # 1
print(counter_demo())   # 1 again, not 2! The old count was thrown away.

# Scope summary:
#   Local  -> created inside a function, only usable inside it (private notebook)
#   Global -> created outside functions, readable everywhere (notice board)
#   To get information OUT of a function, use return.
#   To get information INTO a function, use parameters.

Practice Problems
The following exercises are arranged from simple functions to challenges combining functions, conditions, loops, and scope. Each question is followed by its solution in the source lesson.
# ---------- PRACTICE PROBLEMS (task comment, then solution) ----------

# --- Level 1: Simple functions (no parameters) ---

# Q1: Create a function called welcome() that prints "Welcome to Python class".
#     Call it 3 times.
def welcome():
    print("Welcome to Python class")

welcome()
welcome()
welcome()


# Q2: Create a function called draw_line() that prints 10 stars on one line.
#     Call it twice.
def draw_line():
    print("*" * 10)

draw_line()
draw_line()


# --- Level 2: Parameters ---

# Q3: Create a function called say_name(name) that prints "My name is ___".
#     Call it with two different names.
def say_name(name):
    print("My name is", name)

say_name("Ali")
say_name("Fatima")


# Q4: Create a function called show_square(n) that PRINTS the square of n.
#     Call it with 5 and 9.
def show_square(n):
    print(n * n)

show_square(5)
show_square(9)


# Q5: Create a function called repeat_word(word, times) that prints the word
#     that many times using a loop. Example: repeat_word("Hi", 4)
def repeat_word(word, times):
    for i in range(times):
        print(word)

repeat_word("Hi", 4)


# --- Level 3: return ---

# Q6: Create a function called multiply(a, b) that RETURNS a * b.
#     Print multiply(6, 7).
def multiply(a, b):
    return a * b

print(multiply(6, 7))


# Q7: Create a function called double(n) that RETURNS n * 2.
#     Then store double(8) in a variable and print the variable.
def double(n):
    return n * 2

answer = double(8)
print(answer)


# Q8: Create a function called perimeter_of_rectangle(length, width) that
#     RETURNS 2 * (length + width). Print perimeter_of_rectangle(5, 3).
def perimeter_of_rectangle(length, width):
    return 2 * (length + width)

print(perimeter_of_rectangle(5, 3))


# Q9: Create a function called total_cost(price, quantity) that RETURNS the
#     total. Use it to print the cost of 4 items priced at 50.
def total_cost(price, quantity):
    return price * quantity

print(total_cost(50, 4))


# Q10: Without writing a new function, use multiply() from Q6 to calculate
#      (2 * 3) * 4 in a single print line.
print(multiply(multiply(2, 3), 4))


# --- Level 4: return with conditions ---

# Q11: Create a function called is_positive(n) that RETURNS True if n is
#      greater than 0, otherwise False. Test with 5 and -2.
def is_positive(n):
    if n > 0:
        return True
    else:
        return False

print(is_positive(5))
print(is_positive(-2))


# Q12: Create a function called is_odd(n) that RETURNS True if n is odd.
#      Test with 7 and 10.
def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False

print(is_odd(7))
print(is_odd(10))


# Q13: Create a function called bigger(a, b) that RETURNS the larger number.
#      Test with (10, 4) and (3, 9).
def bigger(a, b):
    if a > b:
        return a
    else:
        return b

print(bigger(10, 4))
print(bigger(3, 9))


# Q14: Create a function called pass_or_fail(marks) that RETURNS "Pass" if
#      marks are 50 or more, otherwise "Fail". Test with 72 and 35.
def pass_or_fail(marks):
    if marks >= 50:
        return "Pass"
    else:
        return "Fail"

print(pass_or_fail(72))
print(pass_or_fail(35))


# Q15: Create a function called number_type(n) that RETURNS "Positive",
#      "Negative" or "Zero". Test with 8, -3 and 0.
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


# Q16: Create a function called can_vote(age) that RETURNS True if age is 18
#      or more. Then use it in an if statement to print "You can vote" or
#      "You cannot vote" for age 20.
def can_vote(age):
    return age >= 18

if can_vote(20):
    print("You can vote")
else:
    print("You cannot vote")


# --- Level 5: Functions with loops ---

# Q17: Create a function called countdown(n) that prints numbers from n down
#      to 1. Call countdown(5).
def countdown(n):
    for i in range(n, 0, -1):
        print(i)

countdown(5)


# Q18: Create a function called sum_even(n) that RETURNS the sum of all even
#      numbers from 1 to n. Test with 10 (answer: 30).
def sum_even(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total = total + i
    return total

print(sum_even(10))


# Q19: Create a function called count_divisible(n, d) that RETURNS how many
#      numbers from 1 to n are divisible by d.
#      Test with count_divisible(50, 3) (answer: 16).
def count_divisible(n, d):
    count = 0
    for i in range(1, n + 1):
        if i % d == 0:
            count = count + 1
    return count

print(count_divisible(50, 3))


# Q20: Create a function called factorial(n) that RETURNS n!
#      Example: 5! = 5 x 4 x 3 x 2 x 1 = 120. Test with 5.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

print(factorial(5))


# --- Level 6: Challenges (combining everything) ---

# Q21 (Challenge): Create a function called is_prime(n) that RETURNS True if
#     n is prime, otherwise False. (A prime is only divisible by 1 and itself;
#     numbers below 2 are not prime.) Test with 7, 10 and 2.
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


# Q22 (Challenge): Using is_prime() from Q21, create a function called
#     count_primes(n) that RETURNS how many primes are between 1 and n.
#     Test with 20 (answer: 8).
def count_primes(n):
    count = 0
    for i in range(1, n + 1):
        if is_prime(i):
            count = count + 1
    return count

print(count_primes(20))


# Q23 (Challenge): Create a function called fizzbuzz(n) that RETURNS "Fizz"
#     if n is divisible by 3, "Buzz" if by 5, "FizzBuzz" if by both,
#     otherwise n. Then use a loop from 1 to 15 to print fizzbuzz(i).
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


# --- Level 7: Scope ---

# Q24: Predict the output BEFORE running. What do the two prints show?
#      x = 10 is global; the function creates its own x = 5.
x = 10

def show_x():
    x = 5
    print(x)

show_x()
print(x)
# Answer: 5 (local x inside the function), then 10 (global x is unchanged).


# Q25: Create a global variable favorite_color = "blue". Create a function
#      called print_favorite() that prints "My favorite color is ___" using
#      the global variable. Call it.
favorite_color = "blue"

def print_favorite():
    print("My favorite color is", favorite_color)

print_favorite()


# Q26: Create a global variable score = 10. Create a function add_bonus(s)
#      that RETURNS s + 5. Update score using the function, then print it
#      (answer: 15).
score = 10

def add_bonus(s):
    return s + 5

score = add_bonus(score)
print(score)


# Q27: Create a global variable counter = 0. Create a function increase()
#      that adds 1 to counter using the global keyword.
#      Call it 3 times, then print counter (answer: 3).
counter = 0

def increase():
    global counter
    counter = counter + 1

increase()
increase()
increase()
print(counter)


# Q28 (Challenge): Do Q27 again WITHOUT the global keyword.
#     Create increase_value(c) that RETURNS c + 1, and use it 3 times
#     with a variable called counter2 (answer: 3).
def increase_value(c):
    return c + 1

counter2 = 0
counter2 = increase_value(counter2)
counter2 = increase_value(counter2)
counter2 = increase_value(counter2)
print(counter2)


# Q29 (Challenge): Predict the output BEFORE running. Why isn't it 2?
#     (Hint: think about local variables and what the function returns.)
total_calls = 0

def add_one():
    total_calls = 1
    return total_calls

add_one()
add_one()
print(total_calls)
# Answer: 0. Inside add_one(), total_calls is a NEW local variable.
# The global total_calls is never changed, and the returned value is ignored.
Quick Summary
- Use parameters to pass information into a function.
- Use return to send a value back from a function.
- Use print() to display information on the screen.
- Local variables belong to the function where they are created.
- Global variables are created outside functions.
- Returning a new value is often clearer than changing a global variable.
