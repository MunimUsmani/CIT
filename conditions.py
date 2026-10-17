# ==========================================
# conditions.py
# Topic: Conditions (if / elif / else)
# ==========================================

# ---------- EXAMPLES (run these first) ----------

# Example 1: Simple if
number = 8
if number > 5:
    print(number, "is greater than 5")

# Example 2: if - else
number = 3
if number > 5:
    print("Big number")
else:
    print("Small number")

# Example 3: Even or odd (% means remainder)
# 4 % 2 = 0, 5 % 2 = 1
number = 7
if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")

# Example 4: Not equal (!=)
number = 7
if number % 2 != 0:
    print(number, "is Odd")

# Example 5: Multiple conditions with AND
number = 14
if number > 10 and number % 2 == 0:
    print(number, "is greater than 10 AND even")

# Example 6: OR
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Weekend!")
else:
    print("School day")

# Example 7: elif (more than two choices)
marks = 72
if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")


# ---------- PRACTICE PROBLEMS (task comment, then solution) ----------

# Q1: Store a number. Print "Positive" if it is greater than 0.
number = 8
if number > 0:
    print("Positive")


# Q2: Store a number. Print "Even" or "Odd".
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Q3: Store your age. Print "Adult" if 18 or more, otherwise "Minor".
age = 20
if age >= 18:
    print("Adult")
else:
    print("Minor")


# Q4: Store a number. Print "Divisible by 5" if the remainder
#     after dividing by 5 is 0.
number = 25
if number % 5 == 0:
    print("Divisible by 5")


# Q5: Store a number. Print it only if it is between 10 and 50
#     (use "and").
number = 30
if number > 10 and number < 50:
    print(number)


# Q6: Store marks out of 100. Print:
#     90+ -> "Excellent", 50-89 -> "Pass", below 50 -> "Fail"
marks = 72
if marks >= 90:
    print("Excellent")
elif marks >= 50:
    print("Pass")
else:
    print("Fail")


# Q7: Store a number. Print "Positive", "Negative" or "Zero".
number = -4
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# Q8 (Challenge): Store a number. Print "Even and greater than 20",
#     "Odd and greater than 20", or "20 or less".
number = 27
if number > 20 and number % 2 == 0:
    print("Even and greater than 20")
elif number > 20:
    print("Odd and greater than 20")
else:
    print("20 or less")
