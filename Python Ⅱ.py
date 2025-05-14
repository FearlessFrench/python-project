# Chapter 17: 2D Collections

# Each of these list is a 1-Dimensional List
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

# We can create a 2-Dimensional List
groceries = [fruits, vegetables, meats]
print(groceries)
# >>> orange', 'banana', 'coconut'], ['celery', 'carrots', 'potatoes'], ['chicken', 'fish', 'turkey']]

print(groceries[2])
# >>> ['chicken', 'fish', 'turkey']

print(groceries[0][0])
# >>> orange

#print(groceries[2][3])
# >>> list index out of range

# We can also declare a 2D List like this
groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]

# Using nested loop to iterate all element found in the 2D List
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
    
# We can also use a tuple-tuple or tuple-set
groceries = ({"apple", "orange", "banana", "coconut"},
             {"celery", "carrots", "potatoes"},
             {"chicken", "fish", "turkey"})

# But remember tuple is always FASTER
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
    
# And those are 2D Collections in Python

###############################################################################

# Exercise 8: Python Quiz Game

questions = ("How many elements are in the periodic table?: ",
             "which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?",)

# A 2D tupleo of options, you can add more than 5
options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")) 

answers = ("C", "D", "A", "A", "B")
guesses = [] # Use list to be able to append guess to answer
score = 0
question_num = 0 # Keep track of the question we are on

for question in questions:
    print("-----------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

###############################################################################

# Chapter 18: Dictionary = a collection of {key:value} pairs
#                          ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("India")) >>> New Delhi
# print(capitals.get("Japan") >>> None

if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital doesn't exist")
    
capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.popitem()
capitals.clear()

keys = capitals.keys()
print(keys) # Will show all dict_keys(["USA", "India", "China", "Russia"])

for key in capitals.keys():
    print(key)

values = capitals.values() # Will show all dict_values(["Washington D.C.", "New Delhi", "Beijing", "Moscow"])

for value in capitals.values():
    print(value)
    
items = capitals.items()

for key, value in capitals.items():
    print(f"{key}: {value}")

###############################################################################

# Exercise 9: Python Concession Stand Program

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}
cart = []
total = 0

print("---------- MENU ----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
for food in cart:
    total = total + menu.get(food)
    # total += menu.get(food)
    print(food, end=" ")
    
print()
print(f"Total is: ${total:.2f}")

###############################################################################

# Exercise 10: Random Numbers

import random

number = random.randint(1, 6) # Roll a Dice

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

number = random.randint(low, high)
number = random.random()
option = random.choice(options)
random.shuffle(cards)

print(option)
print(cards)

###############################################################################

# Exercise 11: Python Number Guessing Game

import random
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    
    guess = input("Enter your guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
        
    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")

###############################################################################

# Exercise 12: Rock, Paper, Scissors Game

import random

options = ("rock", "paper", "scissors")
playing = True

while playing:
    
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")
        
    play_again = input("Play again? (y/n): ").lower()
    if not play_again == "y":
        running = False
        
    # if not input("Play again? (y/n): ").lower( == 'y":
    #   running = False)

print("Thanks for playing!")

###############################################################################

# Exercise 13: Dice Roller Program

import random
# • ┌ ─ ┐ | └ ┘

# To Enter a Unicode Characters
print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

# random.randint(1, 6)

for die in range(num_of_dice):
    dice.append(random.randint(1, 6)) 
# print(dice)

# Show each dice by vertical
#for die in range(num_of_dice):
#    for line in dice_art.get(dice[die]):
#        print(line)

# Show each dice by horizontal
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

for die in dice:
    total += die
print(f"total: {total}")

###############################################################################

# Chapter 19: Function = A block of reusable code
#                        place () after the function name to invoke it

# Try repeat this code 3 times
print("Happy birthday to you!")
print("You are old!")
print("Happy birthday to you!")
print()

print("Happy birthday to you!")
print("You are old!")
print("Happy birthday to you!")
print()

print("Happy birthday to you!")
print("You are old!")
print("Happy birthday to you!")
print()

# Do this instead
def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()

# Any data we're sending in is a parameter (a temporary variable)
happy_birthday("Bro", 20)
happy_birthday("Steve", 30)
happy_birthday("Joe", 40)


def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Yourbill of ${amount:.2f} is due: {due_date}")
    
display_invoice("French", 42.50, "01/01")


# return = statement used to end a function
#          and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))

# A value is return
#print(3)
#print(-1)
#print(2)
#print(0.5)


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

# We can call a function this way too
full_name = create_name("Claire", "Redfield")

print(full_name)

###############################################################################

# Chapter 20: Default Arguments = A default value for certain parameters
#                                 default is used when that argument is omitted
#                                 make your functions more flexible, reduces # of arguments
#                                 1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

# positional default arguments
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500, 0.1)) # Let's pass in a 2nd argument
print(net_price(500, 0.1, 0)) # Finally we can pass all the argument


import time

def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")
    
# To invoke this function
count(0, 10)

# Let's assume that most of the time user will likely begin with 0        
def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")
    
count(30, 15) # Begin at 15, End at 30

###############################################################################

# Chapter 21: Keyword Arguments = an argument preceded by an identifier
#                                 helps with readability
#                                 order of arguments doesn't matter
#                                 1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")
    
hello("Hello", "Mr.", "Chris", "Redfield") # These can be switch order if we give keyword argument
hello("Hello", title="Mr.", last="Redfield", first="Claire") # Remember the first argument must not be a default one

for x in range(1, 11):
    print(x, end=" ")

# with end=" " >>> 1 2 3 4 5 6 7 8 9 10
# without end=" " >>> 1 to 10 (in vertical)

# A lot of built-in function such as the print function, they have a keyword arguments
print("1", "2", "3", "4", "5", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=213, first=373, last=4235)

print(phone_num)

# *args      = allows you to pass multiple non-key arguments
# **kwargs   = allows you to pass multiple keyword-arguments
#              * unpacking operator
#            1. positional, 2. default, 3. keyword, 4. ARBITRARY

def add(a, b):
    return a + b

print(add(1, 2, 3)) # We couldn't insert 3 arguments

# Let's modify a function to fix that
def add(*args):
    print(type(args))
# >>> <class 'tuple'>
add(1, 2, 3)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1))

# We could use other parameter name
def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

def display_name(*args):
    for arg in args:
        print(arg, end=" ")
        
display_name("Chris", "Redfield")
display_name("Corporal", "Leon", "S.", "Kennedy")

# Multiple Keyword Arguments
def print_address(**kwargs):
    pass

print_address(street="123 Fake St.",
              city="Detroit",
              state="MI", 
              zip="54321")
# >>> <class 'dict'>

# We can treat it as a dictionary
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print_address(street="123 Fake St.",
              city="Detroit",
              state="MI", 
              zip="54321")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    
    #for value in kwargs.values():
     #   print(value, end=" ")
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
        
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get(zip)}")

shipping_label("Dr.", "Albert", "Wesker", "III",
               steet="123 Fake St.",
               pobox="PO box #1001",
               apt="100",
               city="Detroit",
               state="MI",
               zip="54321")

###############################################################################

# Chapter 22: Iterables = An object/collection that can return its elements one at a time, 
#                         allowing it to be iterated over in a loop

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number) # this will give us 1 to 5 (vertical)
    
for item in numbers:
    print(item) # This one is understandable
    
for blablabla in numbers:
    print(blablabla) # This will cause confusion to other user
    
# tuples are also iterable
numbers = (1, 2, 3, 4, 5)

for number in reversed(numbers):
    print(number, end=" - ")

# a sets of fruit
fruits = {"apple", "orange", "banana", "coconut"}

for fruit in reversed(fruits):
    print(fruit) # ERROR: Set object is not reversable

name = {"French"}

for character in name:
    print(character, end=" ")

# if we iterate over dictionary it will return keys not the values
my_dictionary = {"A": 1,
                 "B": 2,
                 "C": 3}

for key in my_dictionary:
    print(key)
    
for value in my_dictionary.values():
    print(value) # This will return values
    
for key, value in my_dictionary.items():
    print(f"{key} = {value}")

###############################################################################

# Chapter 23: Membership Operators = used to test wether a value or variable is found in a sequence
#                                    (sting, list, tuple, set, or dictionary)
#                                    1. in
#                                    2. not in

# String
word = "APPLE"
letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")    
else:
    print(f"{letter} was not found")

# Set
students = {"Chris", "Leon", "Jill"}
student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")

# if "not in" just swap it around
if student not in students:
    print(f"{student} was not found")
else:
    print(f"{student} is a student")
    
# Dictionary
grades = {"Claire": "A", 
          "Leon": "B", 
          "Jill": "C", 
          "Chris": "D"}
student = input("Enter the name of a student: ")
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")

# Checking 2 conditions using "and"
email = "doctorchristopherfrench@gmail.com"

if "@" in email and "." in email: 
    print("Valid email")
else:
    print("Invalid email")

###############################################################################

# Chapter 24: List Comprehension = A concise way to create lists in Python
#                                  Compact and easier to read than traditional loops
#                                  [expression for value in iterable if condition]

# This is a lot to write
doubles = []
for x in range(1, 11):
    doubles.append(x * 2)
print(doubles)

# Write this way instead
#doubles = [expression for value in iterable]
doubles = [x * 2 for x in range(1, 11)]
print(doubles)
# >>> [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

fruits = ["apple", "orange", "banana", "coconut"]

#uppercase_fruits = []
fruits = [fruit.upper() for fruit in fruits]
print(fruits)
# >>> ["APPLE", "ORANGE", "BANANA", "COCONUT"]

fruit_chars = [fruit[0] for fruits in fruits]
print(fruit_chars)
# >>> ["A", "O", "B", "C"]

# if condition
numbers = [1, -2, -3, -4, 5, -6, 8, -7]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print(positive_nums)
print(negative_nums)
print(even_nums)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)
# >>> [85, 79, 90, 61]

###############################################################################

# Chapter 25: Match-Case Statement (switch): An alternative to using many 'elif' statements
#                                            Execute some code if a value matches a 'case'
#                                            Benefits: cleaner and syntax is more readable

def day_of_week(day):
    if day == 1:
        return "It is Sunday"
    elif day == 2:
        return "It is Monday"
    elif day == 3:
        return "It it Tuesday"
    elif day == 4:
        return "It is Wednesday"
    elif day == 5:
        return "It is Thursday"
    elif day == 6:
        return "It is Friday"
    elif day == 7:
        return "It is Saturday"
    else:
        return "Not a valid day"
    
print(day_of_week(1)) # >>> It is Sunday

# Do this instead
def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It it Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _: # _ = wild card (will perform this case if there are no match case)
            return "Not a valid day"


print(day_of_week(7)) # >>> It is Saturday
print(day_of_week("pizza")) # >>> Not a valid day


def is_weekend(day):
    match day:
        case "Sunday":
            return True
        case "Monday":
            return False
        case "Tuesday":
            return False
        case "Wednesday":
            return False
        case "Thursday":
            return False
        case "Friday":
            return False
        case "Saturday":
            return True
        case _: # _ = wild card (will perform this case if there are no match case)
            return False

print(is_weekend("Pizza")) # >>> False

# | = or
def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _: # _ = wild card (will perform this case if there are no match case)
            return False

print(is_weekend("Sunday")) # >>> True