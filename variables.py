# ==========================================
# variables.py
# Topic: Variables
# ==========================================

# Example 1: Storing values
name = "Ali"
age = 15
print(name)
print(age)

# Example 2: Printing with text
print("My name is", name, "and I am", age, "years old")

# Example 3: Changing a variable
score = 10
print("Score:", score)
score = score + 5
print("Score after bonus:", score)

# Example 4: Calculations with variables
a = 8
b = 3
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Remainder:", a % b)

# Example 5: A counter (used later inside loops)
count = 0
count = count + 1
count = count + 1
print("Count:", count)

# Example 6: A total (accumulator)
total = 0
total = total + 4
total = total + 6
print("Total:", total)


# ---------- PRACTICE PROBLEMS (task comment, then solution) ----------

# Q1: Create a variable called city and store your city name. Print it.
city = "Karachi"
print(city)


# Q2: Store your age in a variable. Print: "I am ___ years old"
age = 15
print("I am", age, "years old")


# Q3: Create two variables x = 12 and y = 5.
#     Print their sum, difference and product.
x = 12
y = 5
print("Sum:", x + y)
print("Difference:", x - y)
print("Product:", x * y)


# Q4: Create a variable lives = 3. Reduce it by 1 and print it.
lives = 3
lives = lives - 1
print(lives)


# Q5: Create a variable price = 50 and quantity = 4.
#     Calculate and print the total cost.
price = 50
quantity = 4
total_cost = price * quantity
print("Total cost:", total_cost)


# Q6: Create count = 0. Add 1 to it five times (five separate lines).
#     Print count at the end.
count = 0
count = count + 1
count = count + 1
count = count + 1
count = count + 1
count = count + 1
print(count)


# Q7 (Challenge): Swap the values of a and b WITHOUT typing numbers again.
#     a = 10, b = 20  ->  after swapping: a = 20, b = 10
a = 10
b = 20
temp = a
a = b
b = temp
print(a, b)
