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