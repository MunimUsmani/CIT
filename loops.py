# ==========================================
# loops.py
# Topic: for loops (mixed with variables and conditions)
# ==========================================
# Loop = Repeat a set of instructions multiple times.
# Tip: To run one example at a time, put # in front of the others.

# ---------- EXAMPLES (already covered in class) ----------

print("--- Print numbers 1 to 10 ---")
for i in range(1, 11):
    print(i)

print("--- Table of 2 ---")
for i in range(1, 11):
    print("2 x", i, "=", 2 * i)


# ---------- NEW EXAMPLES: builds up step by step ----------

print("--- Step 1: Just print numbers ---")
for i in range(1, 11):
    print(i)

print("--- Step 2: Use i in a calculation ---")
for i in range(1, 11):
    print(i * 2)

print("--- Step 3: Message with the number ---")
for i in range(1, 6):
    print("Current number is", i)

print("--- Step 4: A simple condition ---")
for i in range(1, 11):
    if i > 5:
        print(i)

print("--- Step 5: Even numbers ---")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

print("--- Step 6: Odd numbers ---")
for i in range(1, 21):
    if i % 2 != 0:
        print(i)

print("--- Step 7: if-else inside a loop ---")
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")

print("--- Step 8: Multiple conditions ---")
for i in range(1, 21):
    if i > 10 and i % 2 == 0:
        print(i)

print("--- Step 9: Counting things ---")
count = 0
for i in range(1, 21):
    if i % 2 == 0:
        count = count + 1
print("Even numbers:", count)

print("--- Step 10: Sum of even numbers ---")
total = 0
for i in range(1, 11):
    if i % 2 == 0:
        total = total + i
print("Total:", total)


# ---------- MORE LOOP EXAMPLES ----------

print("--- Countdown ---")
for i in range(10, 0, -1):
    print(i)

print("--- Squares ---")
for i in range(1, 6):
    print(i, "->", i * i)

print("--- Stars on one line ---")
for i in range(5):
    print("*", end="")
print()

print("--- Triangle ---")
for i in range(1, 6):
    print("*" * i)


# ---------- PRACTICE PROBLEMS (task comment, then solution) ----------

# Q1: Print numbers from 5 to 15.
for i in range(5, 16):
    print(i)


# Q2: Print your favorite fruit 7 times.
for i in range(7):
    print("Mango")


# Q3: Print the table of 7.
for i in range(1, 11):
    print("7 x", i, "=", 7 * i)


# Q4: Print numbers from 20 down to 1.
for i in range(20, 0, -1):
    print(i)


# Q5: Print only the numbers from 1 to 30 that are greater than 15.
for i in range(1, 31):
    if i > 15:
        print(i)


# Q6: Print even numbers from 10 to 30 using if and %.
for i in range(10, 31):
    if i % 2 == 0:
        print(i)


# Q7: Print each number from 1 to 10 with "Even" or "Odd" next to it.
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "Even")
    else:
        print(i, "Odd")


# Q8: Print numbers from 1 to 50 that are divisible by 5.
for i in range(1, 51):
    if i % 5 == 0:
        print(i)


# Q9: Print numbers between 1 and 30 that are odd AND greater than 10.
for i in range(1, 31):
    if i % 2 != 0 and i > 10:
        print(i)


# Q10: Count how many numbers between 1 and 50 are divisible by 3.
#      Print the count at the end.
count = 0
for i in range(1, 51):
    if i % 3 == 0:
        count = count + 1
print("Count:", count)


# Q11: Find the sum of all numbers from 1 to 100.
#      Print the total at the end.
total = 0
for i in range(1, 101):
    total = total + i
print("Total:", total)


# Q12: Find the sum of only the odd numbers from 1 to 20.
total = 0
for i in range(1, 21):
    if i % 2 != 0:
        total = total + i
print("Total:", total)


# Q13: Print squares of numbers from 1 to 10.
for i in range(1, 11):
    print(i * i)


# Q14: Print a triangle with 4 rows of stars.
for i in range(1, 5):
    print("*" * i)


# Q15 (Challenge): Loop from 1 to 30. Print "Fizz" if divisible by 3,
#      "Buzz" if divisible by 5, "FizzBuzz" if divisible by both,
#      otherwise print the number.
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
