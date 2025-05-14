# This is a new Python file. You can start writing your code here.

# Chapter 1: Introduction to Python
# Python is a high-level programming language that is easy to learn and use.
# Comment is used as note for yourself or other people
print("I like lasagna!")
print("It's really good!")

###############################################################################

# Chapter 2: Variables
# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

# Strings
first_name = "Claire"
#print(first_name)
food = "lasagna"
email = "Claire_Redfield@cmu.ac.th"
# Try f-string so that we can use variable along with the text
print(f"Hello, {first_name}")
print(f"You like {food}?")
print(f"Your email is: {email}")

# Integers
age = 21
quantity = 3
num_of_students = 43
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

# Float
price = 10.99
gpa = 3.68
distance = 5.5
print(f"The price is ${price}")
print(f"Your GPA is: {gpa}")
print(f"You ran {distance} km")

# Boolean (True/False)
is_student = True
for_sale = False
is_online = True
print(f"Are you a student?: {is_student}")
# We usually use boolean with if statement
if is_student:
    print("You are a student")
else:
    print("You are not a student")
    
if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT available")

if is_online:
    print("You are online")
else:
    print("You are offline")
    
# Comment:
user_name = "Christopher French"
year = 2025
pi = 3.14
is_admin = True

###############################################################################

# Chapter 3: Typecasting - the process of converting a variable from one data type to another
#                          str(), int(), float(), bool()

name = "Claire Redfield"
age = 21
gpa = 3.68
is_student = True

print(type(name))  # <class 'str'>
print(type(age))   # <class 'int'>
print(type(gpa))   # <class 'float'>
print(type(is_student))  # <class 'bool'>

# Typecast float to int
gpa = int(gpa)  # 3.68 -> 3
print(gpa)
# Typecast int to float
age =float(age)
print(age)
# Strings and Numbers behave differently
age = str(age)
age += "1" # 21 -> 211

name = bool(name) # "Claire Redfield" -> True
# if user doesn't enter a name such as "", it will return False instead

###############################################################################

# Chapter 4: input() = A function that prompts the user to enter data
#                      Returns the entered data as a string

# Enter a prompt for the user
name = input("What is your name?: ")
age = input("How old are you?: ")

# Since the return value is string, we need to typecast it to int
age = int(age)
age = age + 1

print(f"Hello, {name}!") # Claire Redfield
print(f"You are {age} years old") # 18

# Or we can do it in one line
age = int(input("How old are you?: "))

###############################################################################

# Exercise 1 Rectangle Area Calculator
# We need to promt the user to enter the length and width of the rectangle

# Don't forget to typecast the input to int or float
length = float(input("Enter the length: ")) 
width = float(input("Enter the width: "))
area = length * width

# To type a super script, it will be cool to use it
# Windows: NumLock + Alt + 0178
# Mac: Control + Command + Space
print(f"The area is: {area} cm²")

###############################################################################

# Exercise 2: Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total:.2f}") # 2 decimal places

###############################################################################

# Chapter 5: Madlibs game
# word game where you create a story
# by filling in blanks with random words

adjective1 = input("Enter an adjective (description): ") # suspicious, large, dirty, etc.
noun1 = input("Enter a noun (person, place, thing):") # Mark Zuckerberg
adjective2 = input("Enter an adjective (description): ") # angry
verb1 = input("Enter a verb ending with 'ing': ") # screeching
adjective3 = input("Enter an adjective (description): ") # happy

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}")

###############################################################################

# Chapter 6: Arithmetic & Math

friends = 5

friends = friends + 1
friends = friends - 2
friends = friends * 3
friends = friends / 2
# The above code is not efficient

# Use augmented assignment operator instead
friends += 1
friends -= 2
friends *= 3
friends /= 2

friends = friends ** 2 # Exponentiation (power)

remainder = friends % 2 # Modulus (remainder)
print(remainder) # if it remains 1 then that number is odd


x = 3.14
y = -4
z = 5

result = round(x) # round to the nearest integer
print(result) # >>> 3

result = abs(y) # absolute value
print(result) # >>> 4

result = pow(4, 3) # power function 4x4x4 or 4^3
print(result) # >>> 64

result = max(x, y, z) # max value among x, y, z
result = min(x, y, z) # min value among x, y, z

# import math module to use math functions
import math 

x = 9

print(math.pi) # 3.141592653589793
print(math.e) # an exponential constant ≈ 2.718281828459045 
result = math.sqrt(x) # square root of x
result = math.ceil(x) # round up to the nearest integer such as 9.1 -> 10
result = math.floor(x) # round down to the nearest integer such as 9.9 -> 9

# Circumference of a circle = 2 * pi * r
import math
radius = float(input("Enter the radius of a circle: ")) # 10.5
circumference = 2 * math.pi * radius
print(f"The circumference is: {round(circumference, 2)} cm") # round to 2 digits


# Area of a circle = pi * r^2
import math
radius = float(input("Enter the radius of a circle: ")) # 10.5
area = math.pi * pow(radius, 2) # or radius ** 2
print(f"The area of the circle is: {round(area, 2)} cm²") # round to 2 digits

# Hypotenuse of a right triangle = sqrt(a^2 + b^2)
import math
a = float(input("Enter side A: ")) # 3
b = float(input("Enter side B: ")) # 4
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C = {c}")

###############################################################################

# Chapter 7: if = Do some code only IF some condition is True
#                 Else do something else
# 1st Example
age = int(input("Enter your age: ")) # 21 or 17

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet")
#elif age > 100: should be above age >= 18
   #print("You are too old to sign up")
else:
    print("You must be 18+ to sign up")

# 2nd Example
response = input("Would you like food? (yes or no): ")
if response == "yes":
    print("Have some food!")
else:
    print("No food for you!")
    
# 3rd Example
name = input("Enter your name: ") # Claire Redfield
if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello, {name}")
    
# 4th Example
for_sale = True
if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")

online = True
if online:
    print("The user is online")
else:
    print("The user is offline")

###############################################################################

# Exercise 2 : Python Calculator Program (Simple)

operator = input("Enter an operator (+, -, *, /): ") # +, -, *, /
num1 = input("Enter the 1st number: ")
num2 = input("Enter the 2nd number: ")

print(num1 + num2) # We would end up with two strings concatenated together
# We need to typecast the input to int or float
num1 = input("Enter the 1st number: ")
num2 = input("Enter the 2nd number: ")

if operator == "+":
    result = num1 + num2
    print(result, 3)
elif operator == "-":
    result = num1 - num2
    print(result, 3)
elif operator == "*":
    result = num1 * num2
    print(result, 3)
elif operator == "/":
    result = num1 / num2
    print(result, 3)
else:
    print(f"{operator} is not a valid operator")

###############################################################################

# Exercise 3: Python Weight Converter Program
# Convert weight from kg to lb and vice versa

weight = float(input("Enter your weight: ")) # 62.8 kg or 138.8 lb
unit = input("Kilograms or Pounds? (kg or lb): ") # kg or lb

if unit == "kg":
    weight =weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "lb":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not valid")

###############################################################################

# Exercise 4: Python Temperature Conversion Program
unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: ")) # 30.5 C or 86.9 F

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1) # Convert to Fahrenheit
    print(f"The temperature in Fahrenheit is: {temp} °F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1) # Convert to Celsius
    print(f"The temperature in Celsius is: {temp} °C")
else:
    print(f"{unit} is an invalid unit of measurement") # Such as Kevin Unit

###############################################################################

# Chapter 8: Logical Operators = evaluate multiple conditions (or, and, not)
#                           or = at least one condition must be True
#                          and = both conditions must be True
#                          not = inverts the condition (not False, not True)

temp = 25 # Try change to 36, -5, 20
is_raining = False

if temp > 35 or temp < 0 or is_raining: # If any of these conditions are True
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")
    
temp = 0 # Try change to 30, 0, -5, 20
is_sunny = True
if temp >= 28 and is_sunny:
    print("It is HOT outside 🥵")
    print("It is SUNNY ☀️")
elif temp <= 0 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY ☀️")
elif temp < 28 and temp > 0 and is_sunny: # 28 > temp > 0 and is_sunny
    print("It is WARM outside 🙂")
    print("It is SUNNY ☀️")
# NOT is_sunny
elif temp >= 28 and not is_sunny:
    print("It is HOT outside 🥵")
    print("It is CLOUDY ⛅")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside 🥶")
    print("It is CLOUDY ⛅")
elif temp < 28 and temp > 0 and not is_sunny: # 28 > temp > 0 and not is_sunny
    print("It is WARM outside 🙂")
    print("It is CLOUDY ⛅")
    
###############################################################################

# Chapter 9: Conditional Expression - A one-line shortcut for the if-else statement (ternary operator)
#                                     Print or assign one of two values based on a condition
#                                     X if condition else Y

num = 5
a = 6
b = 7
age = 13
temperature = 30
user_role = "admin" # admin, user, guest

print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Minor"
wether = "HOT" if temperature > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)
# Basically, we can use the conditional expression to replace the if-else statement

###############################################################################

# Chapter 10: String Methods

name = input("Enter your full name: ") # Claire Redfield

result = len(name) # Length of the string
print(result)

result = name.find(" ")
print(result) # Find the first space in the string >>> 5
result = name.find("Redfield") # Find the first occurrence of "Redfield"
print(result) # index >>> 6

result = name.rfind("e") # Find the last occurrence of "e"
print(result) # index >>> 12
result = name.rfind("q") # Find the last occurrence of "q"
print(result) # not found >>> -1

name = name.upper() # Convert to uppercase
name = name.lower() # Convert to lowercase
name = name.title() # Convert to title case (first letter of each word is capitalized)

result = name.isdigit() # Only return True if the string is only a number like "123" not "Claire123"
result = name.isalpha() # Only return True if the string is only letters like "Claire" not "Claire123"

phone_number = input("Enter your phone number #: ") # They typically contain numbers and dashes
# 1-234-567-8901
result = phone_number.count("-") # Count the number of dashes in the string
print(result)

phone_number.replace("-", " ") # Replace all dashes with spaces >>> 1 234 567 8901
phone_number.replace("-", "") # Replace all dashes with nothing >>> 12345678901

# Finally you can use a bunch of method from this command
print(help(str)) # To see all the methods available for string

###############################################################################

# Validate User Input Exercise
# 1. username is no more than 12 characters long
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ") # Claire Redfield
username.find(" ") # if no space a found this statement will return -1

if len(username) > 12:
    print("Your user name can't be more than 12 characters long")
elif not username.find(" ") == -1: # username.find(" ") != -1
    print("Your user name can't contain spaces")
elif not username.isalpha():
    print("Your user name can't contain numbers")
else:
    print(f"Welcome {username}")

###############################################################################

# Chapter 11: Indexing = accessing elements of a sequence using [] (indexing operator)
#                        [start : end : step]

# Computer always start with operator so 0 is the first index
credit_number = "1234-5678-9012-3456" # 16 digits

print(credit_number[0]) # 1
print(credit_number[0:4]) # 1234 or just use credit_number[:4]
print(credit_number[5:9]) # 5678
print(credit_number[5:]) # 5678-9012-3456
print(credit_number[-1]) # 6 (last character)
print(credit_number[::2]) # 13579-2468 (every 2nd character)

# To hide the first 12 digits of the credit card number
last_digits = credit_number[-4:] # 3456 (last 4 digits)
print(f"XXXX-XXXX-XXXX-{last_digits}") # XXXX-XXXX-XXXX-3456

# To reverse the whole credit card number
credit_number = credit_number[::-1]
print(credit_number) # 6543-2109-8765-4321

###############################################################################

# Chapter 12: Format Specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is {price1:.2f}") # 3.14
print(f"Price 2 is {price2:.2f}") # -987.65
print(f"Price 3 is {price3:.2f}") # 12.34

print(f"Price 1 is {price1:.1f}") # 3.1
print(f"Price 2 is {price2:.3f}") # -987.650
print(f"Price 3 is {price3:.3f}") # 12.340

print(f"Price 1 is {price1:10}") #    3.14159
print(f"Price 2 is {price2:10}") #    -987.65
print(f"Price 3 is {price3:10}") #      12.34

print(f"Price 1 is ${price1:010}") # $0003.14159
print(f"Price 2 is ${price2:010}") # $-000987.65
print(f"Price 3 is ${price3:010}") # $0000012.34

print(f"Price 1 is ${price1:>10}") # $ 3.14159
print(f"Price 2 is ${price2:>10}") # $ -987.65
print(f"Price 3 is ${price3:>10}") # $   12.34

print(f"Price 1 is ${price1:<10}") # $3.14159
print(f"Price 2 is ${price2:<10}") # $-987.65
print(f"Price 3 is ${price3:<10}") # $12.34

print(f"Price 1 is ${price1:^10}") # $ 3.14159
print(f"Price 2 is ${price2:^10}") # $ -987.65
print(f"Price 3 is ${price3:^10}") # $  12.34

print(f"Price 1 is ${price1:+}") # $+3.14159
print(f"Price 2 is ${price2:+}") # $-987.65
print(f"Price 3 is ${price3:+}") # $+12.34

print(f"Price 1 is ${price1: }") # $ 3.14159
print(f"Price 2 is ${price2: }") # $-987.65
print(f"Price 3 is ${price3: }") # $ 12.34

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

# Each thousand is seperate with a comma
print(f"Price 1 is ${price1:,}") # $3,000.14159
print(f"Price 2 is ${price2:,}") # $-9,870.65
print(f"Price 3 is ${price3:,}") # $1,200.34

print(f"Price 1 is ${price1:+,.2f}") # $+3,000.14
print(f"Price 2 is ${price2:+,.2f}") # $-9,870.65
print(f"Price 3 is ${price3:+,.2f}") # $+1,200.34

###############################################################################

# Chapter 13: While Loop = execute some code WHILE some condition remains True

name = input("Enter your name: ")

# We can use while loop to check if the user has entered a name or not
if name == "": 
    print("You did not enter your name")
else:
    print(f"Hello, {name}")
    
while name == "": # while this condition is True
    print("You did not enter your name")
    name = input("Enter your name:") # We add this line to prevent infinite loop
    
print(f"Hello, {name}")

# Another Example
age = int(input("Enter your age: "))
          
while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")

# Exit while loop example
food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")
    
print("bye")

# While wit OR logical operator
num = int(input("Enter a # between 1 - 10: "))
while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10:"))
    
print(f"Your number is {num}")

###############################################################################

# Exercise 5: Python Compound Interest Calculator Program

principe = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if principle <= 0:
        print("Interest rate can't be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the time in years: "))
    if principle <= 0:
        print("Time can't be less than or equal to zero")
        
print(principle)
print(rate)
print(time)

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")

# How to allow user to enter 0 values
# while True will always be an infinite loop unless we put break statement
while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than to zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if principle < 0:
        print("Interest rate can't be less than to zero")
    else:
        break

while True:
    rate = float(input("Enter the time in years: "))
    if principle < 0:
        print("Time can't be less than to zero")
    else:
        break

###############################################################################

# Chapter 14: For Loop = execute a block of code a fixed number of times.
#                        You can iterate over a range, string, sequence, etc.

for x in range(1, 11): # Counter x will count from 1 to 10
    print(x) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    
for x in reversed(range(1, 11)):
    print(x) # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
print("HAPPY NEW YEAR!")

for x in range(1, 11, 3):
    print(x) # 1, 4, 7, 10

# We can iterate a string with a for loop as well
credit_card = "1234-5678-9012-3456" # 16 digits
for x in credit_card:
    print(x)

# Let's skip over number 13
for x in range(1, 21):
    if x == 13:
        continue # Skip this number
    else:
        print(x) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20
        
# Let's stop counting when we reach number 13
for x in range(1, 21):
    if x == 13:
        break # Stop counting
    else:
        print(x) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

###############################################################################

# Exercise 6: Python Count Down Timer Program
import time
# We can use the sleep function to pause the program for a few seconds
time.sleep(3) # Sleep for 3 seconds
print("TIME'S UP!")

import time
my_time = int(input("Enter the time in seconds: ")) # 3
for x in range(my_time, 0, -1): # Count down from 3 to 1
    print(x)
    time.sleep(1)
print("TIME'S UP!")

import time
my_time = 11 # 11 seconds
my_time = 60 # 1 minute
my_time = 3600 # 1 hour
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"00:{minutes:02}:{seconds:02}")
    time.sleep(1)

###############################################################################

# Chapter 15: Nested Loop = A loop within another loop (outer, inner)
#                           outer loop:
#                               inner loop
for x in range(1, 10):
    print(x, end="") # 123456789
    
# Let's do this loop 3 times
for x in range(3):
    for y in range(1, 10): # don't for get to rename the variable to be different
        print(y, end="") # 123456789
    print() # New line after each loop
    
# Let's do some square from text
rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print() # New line after each loop

###############################################################################

# Chapter 16: Collection = single "variable" used to store multiple values
#   List   = [] ordered and changeable. Duplicates OK
#   Set    = {} unordered and immutable, but Add/Remove OK. NO Duplicates
#   Tuple  = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut"]

print(fruits)
print(fruits[0]) # apple
print(fruits[1]) # orange
print(fruits[2]) # banana
print(fruits[3]) # coconut
print(fruits[4]) # IndexError: list index out of range
print(fruits[0:3]) # ['apple', 'orange', 'banana']
print(fruits[::2]) # ['apple', 'banana']
print(fruits[::-1]) # ['coconut', 'banana', 'orange', 'apple']

# replace x with fruit is more readable
for fruit in fruits:
    print(fruit)

# To see all the methods available for list
print(dir(fruits))
print(help(fruits)) 

# There is a length function
print(len(fruits)) # 4

# Boolean checker
print("apple" in fruits) # True
print("grape" in fruits) # False
print("pineapple" not in fruits) # True

# replace one of the value in the list
fruits[0] = "pineapple"
# append to add a new element to a list
fruits.append("grape")
# remove to remove an element from a list
fruits.remove("apple")
# insert to insert an element at a specific index
fruits.insert(0, "kiwi") # Insert at index 0
# sort the list in ascending order
fruits.sort()
# reverse the list
fruits.reverse()
# remove all elements from the list
fruits.clear()

print(fruits.index("apple")) # Find the index of "apple"
print(fruits.count("banana")) # Count the number of "banana" in the list

# A Set {} unordered and immutable, but Add/Remove OK. NO Duplicates
fruits = {"apple", "orange", "banana", "coconut"}
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits)) # 4
# print("pineapple" in fruits) # False

# We can't alter/change the value but we can add/remove
fruits.add("pineapple")
fruits.remove("apple")
fruits.pop() # Remove a random element from the set
fruits.clear() # Remove all elements from the set

# Set works well with constant or colours

# A Tuple () ordered and unchangeable. Duplicates OK. FASTER
fruits = ("apple", "orange", "banana", "coconut", "coconut")
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

print(fruits.count("coconut")) # Count the number of "coconut" in the tuple

# print(fruits)
for fruit in fruits:
    print(fruit)

###############################################################################

# Exercise 7: Python Shopping Cart Program

# Declare an empty list to store the items
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q": # Just incase they type "Q"
        break # Stop the loop
    else:
        foods.append(food)
        price = float(input("Enter the price of {food}: $"))
        prices.append(price)

print("----- YOUR CART -----")

for food in foods:
    print(food, end=" ") # Print all the food in the list (Horizontal List)
    
for price in prices:
    total += price

print()    
print(f"Your total is: $(total)")