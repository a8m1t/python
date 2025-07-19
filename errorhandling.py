# 1. User Age Input
while True:
    try:
        age = int(input("Enter your age: "))
        if age <= 0:
            raise ValueError("Age must be greater than 0.")
        break
    except ValueError as e:
        print("Invalid input:", e)

# 2. Safe File Reader
while True:
    filename = input("Enter filename to open: ")
    try:
        with open(filename, 'r') as file:
            print("File content:\n", file.read())
        break
    except FileNotFoundError:
        print("File not found. Please try again.")

# 3. Division Calculator
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# 4. Dictionary Lookup
countries = {"Nepal": "Kathmandu", "India": "New Delhi", "China": "Beijing"}
country = input("Enter a country: ")
capital = countries.get(country)
if capital:
    print("Capital:", capital)
else:
    print("Country not found.")

# 5. List Index Access
items = ["apple", "banana", "cherry", "date", "fig"]
try:
    index = int(input("Enter an index (0-4): "))
    print("Item:", items[index])
except (ValueError, IndexError):
    print("Invalid index.")

# 6. Number List Parser
input_str = input("Enter numbers separated by commas: ")
try:
    num_list = [int(x.strip()) for x in input_str.split(',')]
    print("Parsed list:", num_list)
except ValueError:
    print("Invalid input. Make sure all values are numbers.")

# 7. Login Simulator
try:
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    if not username or not password:
        raise Exception("Username and password cannot be blank.")
    print("Login successful!")
except Exception as e:
    print("Login failed:", e)

# 8. JSON Data Parser
import json
json_string = '{"name": "Alice", "age": 30}'
try:
    data = json.loads(json_string)
    print("Parsed JSON:", data)
except json.JSONDecodeError as e:
    print("Invalid JSON:", e)

# 9. Temperature Converter
try:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")
except ValueError:
    print("Please enter a valid number.")

# 10. Simple Contact Book
contacts = {"John": "9876543210", "Alice": "1234567890", "Bob": "5555555555"}
name = input("Enter contact name: ")
if name in contacts:
    print("Phone number:", contacts[name])
else:
    print("Contact not found.")
