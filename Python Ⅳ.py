# Chapter 29: Object = A "bundle" of related attributes (variables) and methods (functions)
#                      Ex. phone, cup, book
#                      You need a "class" to creat many objects

# class = (blueprint) used to design the  structure and layout of an object

# Let's create some car object
class Car:
    # self means this object is creating right now (Car)
    def __init__(self, model, year, color, for_sale): # This is a constructor method in order to create object
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale # boolean
        
car1 = Car("Zenvo TSR-S", 2018, "red", False)
print(car1)
# >>> <__main__.Car object at 0x00000205B4C96F90>

# . is a attribute access operator
print(car1.model) # >>> Zenvo TSR-S
print(car1.year) # >>> 2018
print(car1.color) # >>> red
print(car1.for_sale) # >>> False

car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "black", True)

# We can write class here or import class from Python file if we love organize things
from car import Car
car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corveete", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    
    # Methods are action that object can perform
    # Such as a car can drive, stop
    def drive(self):
        print(f"You drive the {self.color} {self.model}") # self is refering to the current object we are working with
        
    def stop(self):
        print(f"You stop the {self.color} {self.model}")
        
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")
        
car1.drive() # >>> You drive the red Mustang
car2.drive() # >>> You drive the blue Corvette
car3.drive() # >>> You drive the yellow Charger

car1.stop() # >>> You stop the red Mustang
car2.stop() # >>> You stop the blue Corvette
car3.stop() # >>> You stop the yellow Charger

car1.describe() # >>> 2024 red Mustang
car2.describe() # >>> 2025 blue Corvette
car3.describe() # >>> 2026 yellow Charger

###############################################################################

# Chapter 30: Class Variables = Shared among all instances of a class
#                               Defined outside the constructor
#                               Allow you to share data among all objects created from that class

class Student:
    
    # Class Variables here
    class_year = 1998
    num_students = 0
    
    def __init__(self, name, age):
        self.name = name # These are
        self.age = age   # instance variables
        Student.num_students += 1
        
student1 = Student("Claire", 18)
student2 = Student("Jill", 24)

# Instance Variable
print(student2.name) # >>> Jill
print(student2.age) # >>> 24

# Class Variable
print(student1.class_year) # >>> 1998
print(Student.class_year) # Write it like this is better for clarity

print(Student.num_students) # >>> 2

student3 = Student("Chris", 24)
student4 = Student("Wesker", 27)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
# >>> My graduating class of 1998 has 4 students

###############################################################################

# Chapter 31: Inheritance = Allows a class to inherit attributes and methods from another class
#                           Helps with code reusability and extensibility
#                           class Child(Parent) AKA Sub(Super)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")

# Here, let's inherit class to the following class
class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(dog.name) # >>> Scooby
print(dog.is_alive) # >>> True

dog.eat() # >>> Scooby is eating
dog.sleep() # >>> Scooby is sleeping

# This inheritance can help make changes to class easier

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")
        
class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")
        
dog.speak() # WOOF!
cat.speak() # MEOW!
mouse.speak() # SQUEEK!

###############################################################################

# Chapter 32: Multiple Inheritance = inheritance from more than one parent class
#                                    C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

class Animal: # Grandparent
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        #print("This animal is eating")
        print(f"This {self.name} is eating")
        
    def sleep(self):
        #print("This animal is sleeping")
        print(f"This {self.name} is sleeping")

class Prey: # Parent
    def flee(self):
        #print("This animal is fleeing")
        print(f"This {self.name} is fleeing")

class Predator: # Parent
    def hunt(self):
        #print("This animal is hunting")
        print(f"This {self.name} is hunting")
        
class Rabbit(Prey): # Children
    pass

class Hawk(Predator): # Children
    pass

class Fish(Prey, Predator): # Children
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.hunt() # >>> 'Rabbit' object has no attribute 'hunt'
hawk.hunt() # >>> This animal is hunting
hawk.flee() # >>> 'Hawk' object has no attribute 'flee'
fish.hunt() # >>> This animal is hunting
fish.flee() # >>> This animal is fleeing

rabbit.eat() # >>> This animal is eating
fish.sleep() # >>> This animal is sleeping

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

fish.hunt() # >>> Nemo is hunting
rabbit.sleep() # >>> Bugs is sleeping

###############################################################################

# Chapter 33: super() = Function used in a child class to call methods from a parent class (superclass).
#                       Allows you to extend the functionality of the inherited methods

class Shape: # Super Class
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
        
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")    


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        #self.color = color
        #self.filled = filled
        super().__init__(color, is_filled) # OR Shape.__init__(color, is_filled)
        self.radius = radius
        
    def describe(self):
        # You'll use the describe() of a child instead of a parent
        #print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        super().describe()
        
class Square(Shape):
    def __init__(self, color, is_filled, width):
        #self.color = color
        #self.is_filled = is_filled
        super().__init__(color, is_filled)
        self.width = width
    
    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm^2")
        super().describe()
        
class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        #self.color = color
        #self.is_filled = is_filled
        super().__init__(color, is_filled)
        self.width = width
        
    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")
        super().describe()
        
circle = Circle(color="red", is_filled=True, radius=5)
print(circle.color) # red
print(circle.is_filled) # True
print(f"{circle.radius}cm") # 5cm

square = Square(color="blue", is_filled=False, width=6)
print(square.color) # blue
print(square.is_filled) # False
print(f"{square.radius}cm") # 6cm

triangle = Triangle(color="yellow", is_filled=False, width=7, height=8)
print(triangle.color) # yellow
print(triangle.is_filled) # True
print(f"{triangle.width}cm") # 7cm
print(f"{triangle.height}cm") # 8cm


circle.describe()
# It is a circle with an area of 78.5cm^2
# It is red and filled

square.describe()
# It is a square with an area of 36cm^2
# It is blue and not filled

triangle.describe()
# It is a triangle with an area of 28.0cm^2
# It is yellow and filled

###############################################################################

# Chapter 34: Polymorphism = Greek word that means to "have many forms or faces"
#                            Poly = Many
#                            Morphe = Form

#                            TWO WAYS TO ACHIEVE POLYMORPHISM
#                            1. Inheritance = An object could be treated of the same type as a parent class
#                            2. "Duck typing" = Object must have necessary attributes/methods

from abc import ABC, abstractmethod

class Shape:
    
    @abstractmethod
    def area(self):
        pass
    

class Circle(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side ** 2
    

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height * 0.5
    

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping


circle = Circle() # Our circle will have 2 forms: a Circle and a Shape
square = Square() # Our square is not a Circle or Triangle form

shapes = [Circle(). Square(), Triangle()] # Each of these objects has 2 forms and 2 faces

shapes = [Circle(4). Square(5), Triangle(6, 7), Pizza("pepperoni", 15)] # Pizza now inherit from the Circle

for shape in shapes:
    print(f"{shape.area()}cm^2")

###############################################################################

# Chapter 35: "Duck typing" = Another way to achieve polymorphism besides Inheritance
#                             Object must have the minimum necessary attributes/methods
#                             "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True
    
class Dog(Animal):
    def speaK(self):
        print("WOOF!")
        
class Cat(Animal):
    def speak(self):
        print("MEOW!")
        
class Car:
    def horn(self):
        print("HONK!")
     
    # But if we set like these it will inherit Animal like the film Cars!
    alive = True

    def speak(self):
        print("HONK!")
        
animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)

###############################################################################

# Chapter 36: Static methods = A method that belong to a class rather than any object from that class (instance)
#                              Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

print(Employee.is_valid_position("Janitor")) # >>> True
print(Employee.is_valid_position("Rocket Scientist")) # >>> False

# You don't need to create any object from that class like this when using static method
employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

###############################################################################

# Chapter 37: Class methods = Allow operations related to the class itself
#                             Take (cls) as the first parameter, which represents the class itself.

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data
# Class methods = Best for class-level data or require access to the class itself

class Student:
    
    count = 0
    total_gpa = 0
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
        
    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"
    


student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)

print(Student.get_count())
print(Student.get_average_gpa())

###############################################################################

# Chapter 38: Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                             They are automatically called by many of Python's built-in operations.
#                             They allow developers to define or customize the behavior of objects

class Book:
    
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"
        
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

# Before function __str__
print(book1) # >>> <__main__.Book object at 0x0000017EDDBC6E40>
# After function __str__
print(book1) # >>> 'The Hobbit' by J.R.R. Tolkien
# function __eq__
print(book1 == book2) # >>> True
print(book2 < book3) # >>> Type Error

# function __lt__, __gt__, __add__
print(book2 < book3) # >>> False
print(book2 > book3) # >>> True
print(book2 + book3) # >>> 395 pages

# function __contains__
print("Rowling" in book3) # >>> False

# function __getitem__
print(book1["title"]) # >>> The Hobbit
print(book1["author"]) # >>> J.R.R. Tolkien
print(book1["num_pages"]) # >>> 310
print(book1["audio"]) # >>> Key 'audio' was not found

###############################################################################

# Chapter 39: @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#                         Benefit: Add additional logic when read, write, or delete attributes
#                         Gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        
    @property
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property
    def height(self):
        return f"{self._height:.1f}cm"
     
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero") 
            
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")     
    
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")
        
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")
        
rectangle = Rectangle(3, 4)

rectangle.width = 5
rectangle.height = 6

del rectangle.width
del rectangle.height

print(rectangle._width) # 3
print(rectangle._height) # 4

###############################################################################

# Chapter 40: Decorator = A function that extends the behavior of another function
#                         w/o modifying the base function
#                         Pass the base function as an argument to the decorator
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sprinkles 🥧")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge 🍫")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍨")
    
get_ice_cream() # >>> Here is your ice cream 🍨

get_ice_cream("vanilla") 

###############################################################################

# Chapter 41: exception = An event that interrupts the flow of a program
#                         (ZeroDivisionError, TypeError, ValueError)
#                         1.try, 2.except, 3.finally

1 / 0        # >>> ZeroDivisionError
1 + "1"      # >>> ValueError
int("pizza") # >>> ValueError


try:
    # Try some code
    pass
except Exception:
    # Handle an Exception
    pass
finally:
    # Do some clean up
    pass
    
try:
    # This code is dangerous if user input zero
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero IDIOT!")
except ValueError:
    print("Enter only numbers please!")
except Exception:
    print("Something went wrong!")
finally: # The finally block always execute no matter what
    print("Do some cleanup here")


try:
    number = int(input("Enter a number: "))
    print(1 / number)
except Exception: # Exception will count all event (not narrow but still too wide)
    print("Something went wrong") # Just like Microsoft programs lol
    
