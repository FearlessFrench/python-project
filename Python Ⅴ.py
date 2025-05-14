# Chapter 42: Python file detection

import os

file_path = "C:\\Users\\ThinkPad\\Desktop\\test.txt" # Absolute file path
#file_path = "C:/Users/ThinkPad/Desktop/test.txt" 

file_path = "Python/test.txt" # Relative file path

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location doesn't exist")

###############################################################################

# Chapter 43: Python writing files (.txt, .json, .csv)

txt_data = "I like pizza!"

file_path = "output.txt"

# 'with' is a statement that open and close file automatically

# the 2nd parameter of open is the mode
# "w" is to write
# "x" is to write if file doesn't exist yet
# "a" is to append
# "r" is for read

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}' was created")
    
txt_data = "I just need to run away, run far far away! Before you comes back to destroy me!"

file_path = "C:/Users/ThinkPad/Desktop/output.txt"

try:
    with open(file_path, "x") as file:
        file.write(txt_data)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")

# Let's appending our next sentence will added in the new line
try:
    with open(file_path, "x") as file:
        file.write("\n", txt_data)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")


employees = ["Leon", "Claire", "Chris", "Jill"]
file_path = "C:/Users/ThinkPad/Desktop/output.txt"

try:
    with open(file_path, "w") as file:
        for employee in employees:
            file.write(employee + " ")
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")
    
# Let's implement a .json file
import json

employee = {
    "name": "Wesker",
    "age": 45,
    "Job": "Terrorist"
}

file_path = "C:/Users/ThinkPad/Desktop/output.txt"

try:
    with open(file_path, "w", indent=4) as file:
        for employee in employees:
            file.write(employee + " ")
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")


# Let's write a .csv file
import csv

employees = [["Name", "Age", "Job"],
             ["Lara Croft", 21, "Archaeologist"],
             ["Max Rockatansky", 35, "Police officer"],
             ["Leon S. Kennedy", 42, "Special agent"]]

file_path = "C:/Users/ThinkPad/Desktop/output.txt"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")

###############################################################################

# Chapter 44: Python reading files (.txt, .json, .csv)

file_path = "C:\\Users\\ThinkPad\\Desktop\\input.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError: # Prevention program interruption
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")
    
# Reading .json file
import json

file_path = "C:\\Users\\ThinkPad\\Desktop\\input.txt"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content["name"]) # content["age"] or content["job"]
except FileNotFoundError: # Prevention program interruption
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")
    
# Reading .csv file
import csv

file_path = "C:\\Users\\ThinkPad\\Desktop\\input.txt"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line) # To read a specific column line[0], line[1], and line[2]
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")

###############################################################################

# Chapter 45: Datetime Module

import datetime

date = datetime.date(1998, 9, 20) # YYYY, MM, DD

today = datetime.date.today()
print(today) # >>> 2025-05-07

time = datetime.time(12, 30, 0) # >>> 12:30:00

now = datetime.datetime.now()
print(now)

now = now.strftime("%H %M %S") # >>> 17 14 14
now = now.strftime("%H:%M:%S") # >>> 17:14:14
now = now.strftime("%H:%M:%S %m-%d-%Y") # >>> 17:14:14 05-07-2025

target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")

###############################################################################

# Exercise 18: Python Alarm Clock
import time
import datetime
import pygame # pip install pygame

def set_alarm(alarm_time): # ex. "23:00:00"
    print(f"Alarm set for {alarm_time}")
    sound_file = "my_music.mp3"
    is_running = True
    
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        if current_time == alarm_time:
            print("WAKE UP! 🥱")
            
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            
            is_running = False
            
        time.sleep(1)
        
        
        
        

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)

###############################################################################

# Chapter 46: Multithreading = Used to perform multiple tasks concurrently (multitasking)
#                              Good for I/O bound tasks like reading files or fetching data from APIs
#                              threading.Thread(target=my_function)

import threading

def walk_dog(first):
    time.sleep(8)
    print("You finish walking the dog")
    
def walk_dog(first, last):
    time.sleep(8)
    print(f"You finish walking {first} {last}")
    
def take_out_trash():
    time.sleep(2)
    print("You take out the trash")
    
def get_mail():
    time.sleep(4)
    print("You get the mail")

#walk_dog()
#take_out_trash()
#get_mail()

chore1 = threading.Thread(target=walk_dog, args=("Scooby",)) # interpreted as a string enclosed in parentheses
chore1.start()

chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore1.start()


chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")

###############################################################################

# Chapter 47: How to connect to an API using Python

import requests # pip install requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    print(response) # >>> <Response [200]>
    
    if response.status_code == 200: # OK response
        #print("Data retrieved!")
        pokemon_data = response.json()
        print(pokemon_data)
    else:
        print(f"Failed to retrieve data {response.status_code}")
    
pokemon_name = "pikachu"
pokemon_name = "typhlosion"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info: # If it exists, this will be True
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"ID: {pokemon_info["id"]}") # The ordered number of pokemon that appear in the franchise
    print(f"Height: {pokemon_info["height"]} ft")
    print(f"Weight: {pokemon_info["height"]} lbs")

###############################################################################

# Chapter 48: PyQt5 introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon # To change window icon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI") # Graphical User Interface
        self.setGeometry(700, 300, 500, 500) # Set window opening position and size
        self.setWindowIcon(QIcon("profile_pic.jpg"))
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # .exec() is used for older code bases
    sys.exit(app.exec_()) # ensure a clean exit of our program and stay in place for us
    

if __name__ == "__main__": # if we're running this file directly
    main() # we'll call main function

###############################################################################

# Chapter 49: PyQt5 QLabels

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont # Use for text format
from PyQt5.QtCore import Qt # Use for alignment

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(self)
        self.setGeometry(700, 300, 500, 500)
        
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #292929;"
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: italics;"
                            "text-decoration: underline") # Color Picke
        
        # label.setAlignment(Qt.AlignTop) # VERTICALLY TOP
        # label.setAlignment(Qt.AlignBottom) # VERTICALLY BOTTOM
        # label.setAlignment(Qt.AlignVCenter) # VERTICALLY CENTER (DEFAULT)
        
        # label.setAlignment(Qt.AlignRight) # HORIZONTALLY RIGHT
        # label.setAlignment(Qt.AlignHCenter) # HORIZONTALLY CENTER
        # label.setAlignment(Qt.AlignLeft) # HORIZONTALLY LEFT
        
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # CENTER & TOP
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # CENTER & BOTTOM
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # CENTER & CENTER
        # label.setAlignment(Qt.AlignCenter) VERTICALLY & HORIZONTALLY CENTER
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
###############################################################################

# Chapter 50: PyQt5 images

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        
        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)
        
        pixmap = QPixmap("profile_pic.jpg")
        label.setPixmap(pixmap)
        
        label.setScaledContents(True)
        
        label.setGeometry(self.width() - label.width() // 2,
                          self.height() - label.height() // 2,
                          label.width(),
                          label.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

###############################################################################

# Chapter 51: PyQt5 layouts

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        label1 = QLabel("#1", self) # You do not need to add self
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)
        
        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: purple;")
        
        # vbox = QVBoxlayout()
        # hbox = QVBoxlayout()
        gridbox = QVBoxlayout()
        
        gridbox.addWidget(label1, 0, 0)
        gridbox.addWidget(label2, 0, 1)
        gridbox.addWidget(label3, 1, 0)
        gridbox.addWidget(label4, 1, 1)
        gridbox.addWidget(label5, 2, 2)
        
        central_widget.setLayout(hbox)

        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
    
###############################################################################

# Chapter 52: PyQt5 buttons

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.button = QPushButton("Click me!", self)
        self.label = QLabel("Hello", self)
        self.initUI()
        
    def initUI(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)
        
        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px;")
        
    def on_click(self):
        #print("Button clicked!")
        #self.button.setText("Clicked!")
        #self.button.setDisabled(True) # After clicked you can no longer click on it
        self.label.setText("Goodbye")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


###############################################################################

# Chapter 53: PyQt5 checkboxes

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.checkbox = QCheckBox("Do you like food?", self)
        self.initUI()
        
    def initUI(self):
        self.checkbox.setGeometry(0, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial;")
        # checkbox.*signal*.connect(*slot*)
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect()
    
    def checkbox_changed(self, state): # When we check state = 2, if uncheck state = 0
        if state == Qt.Checked: # Qt.Checked is more readable than number 2
            print("You like food")
        else:
            print("You DO NOT like food")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
        
###############################################################################

# Chapter 54: PyQt5 radio buttons

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(self)
        self.setGeometry(700, 300, 500, 500)
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("Gift Card", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        self.initUI()
        
    def initUI(self):
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)
        
        # The font is too small! Let's apply a StyleSheet
        self.setStyleSheet("QRadioButton{"
                           "font-size: 40px;"
                           "font-family: Arial"
                           "padding: 10px;"
                           "}")
        
        self.button_group1.addButton(self.radio1)
        self.button_group2.addButton(self.radio2)
        self.button_group3.addButton(self.radio3)
        self.button_group4.addButton(self.radio4)
        self.button_group5.addButton(self.radio5)
        
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)
        
    def radio_button_changed(self):
        radio_button = self.sender() # it will return a text of selected radio signal we select
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

###############################################################################

# Chapter 55: PyQt5 LineEdit (Text boxes)
        
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(self)
        self.setGeometry(700, 300, 500, 500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.initUI()
        
    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.button.setGeometry(210, 10, 100, 40)
        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial")
        self.button.setStyleSheet("font-size: 25px;"
                                  "font-family: Arial")
        self.line_edit.setPlaceholderText("Enter your name")
        
        
        self.button.clicked.connect(self.submit)
        
    def submit(self):
        text = self.line_edit.text()
        print(f"Hello {text}")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


###############################################################################

# Chapter 56: PyQt5 CSS (Cascading Style Sheets)

# PyQt5 setStyleSheet()

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(self)
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        hbox = QHBoxLayout()
        
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        
        central_widget.setLayout(hbox)
        
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")
        
        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
                font_family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 15px;
            }
            QPushButton#button1{
                background-color: rgb(255, 71, 71);
            }
            QPushButton3#button2{
                background-color: hsl(122, 100%, 64%);
            }
            QPushButton#button3{
                background-color: blue
            }
            QPushButton#button1:hover{
                background-color: rgb(255, 111, 111;
            }
            QPushButton3#button2:hover{
                background-color: hsl(122, 100%, 84%);
            }
            QPushButton#button3{
                background-color: cyan
            }
        """)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
        