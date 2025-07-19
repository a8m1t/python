# Temperature Check
temp = float(input("Enter temperature in °C: "))
if temp > 37.5:
    print("Fever detected")
else:
    print("Normal")

# Shopping Basket (List)
items = ["rice", "oil", "salt"]
for item in items:
    print(f"Added {item} to your basket.")

# Skip Expired Items
items = ["milk", "", "bread", "", "eggs"]
for item in items:
    if item == "":
        continue
    print(item)

# Find First Long Word
words = ["cat", "elephant", "dog", "tiger"]
for word in words:
    if len(word) > 5:
        print(word)
        break

# Student Grades Dictionary
grades = {"Alice": 80, "Bob": 45, "Eve": 30}
for student, mark in grades.items():
    if mark >= 40:
        print(f"{student} passed")
    else:
        print(f"{student} failed")

# Odd Numbers Between 1–20
for i in range(1, 21):
    if i % 2 != 0:
        print(i)

# Water Level Alarm
level = 0
while level <= 100:
    print(f"Water level: {level}")
    level += 10

# Name Search in Tuple
names = ("Sita", "Gita", "Hari", "Nita")
search_name = input("Enter name to search: ")
if search_name in names:
    print("Found")
else:
    print("Not Found")

# Count Words in a Sentence
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print(f"Total words: {word_count}")

# Number Classification
numbers = [3, -1, 0, 5, -7]
for num in numbers:
    if num > 0:
        print(f"{num} is Positive")
    elif num < 0:
        print(f"{num} is Negative")
    else:
        print(f"{num} is Zero")

# Room Booking Availability
rooms = {"101": "yes", "102": "no", "103": "yes"}
for room, available in rooms.items():
    if available == "yes":
        print(f"Room {room} is available")

# Login Attempt Tracker
attempts = 0
while attempts < 3:
    password = input("Enter password: ")
    if password == "admin123":
        print("Access Granted")
        break
    else:
        print("Wrong password")
        attempts += 1

# Create Price List (Dict)
price_list = {}
for _ in range(3):
    item = input("Enter item name: ")
    price = float(input(f"Enter price for {item}: "))
    price_list[item] = price
print("Final price list:", price_list)

# Find Maximum from List
nums = [2, 10, 5, 3]
max_num = nums[0]
for num in nums:
    if num > max_num:
        max_num = num
print(f"Maximum number is: {max_num}")

# Attendance Percentage
total_classes = int(input("Enter total classes held: "))
attended_classes = int(input("Enter classes attended: "))
percentage = (attended_classes / total_classes) * 100
print(f"Attendance: {percentage:.2f}%")
if percentage >= 75:
    print("Eligible for exam")
else:
    print("Not eligible")
