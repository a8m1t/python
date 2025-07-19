# 1. Create a dictionary with three key-value pairs (e.g., name, age, city)
person = {"name": "Alice", "age": 25, "city": "Kathmandu"}

# 2. Access the value of a given key in a dictionary
print(person["name"])  

# 3. Add a new key-value pair to an existing dictionary
person["country"] = "Nepal"

# 4. Update the value of an existing key in a dictionary
person["age"] = 26

# 5. Remove a key-value pair from a dictionary using del
del person["city"]

# 6. Remove a key-value pair using the .pop() method
removed_value = person.pop("country")  
# 7. Use .get() to safely access a value for a key that may not exist
value = person.get("hobby", "Not Found")  

# 8. Check if a key exists in a dictionary
if "name" in person:
    print("Key 'name' exists.")

# 9. Print all keys of a dictionary
print(person.keys())

# 10. Print all values of a dictionary
print(person.values())

# 11. Iterate over a dictionary and print keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# 12. Create a nested dictionary and access a nested value
students = {
    "student1": {"name": "John", "age": 20},
    "student2": {"name": "Sara", "age": 22}
}
print(students["student2"]["name"])  # Output: Sara

# 13. Merge two dictionaries using .update()
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)  

# 14. Create a dictionary from two lists: one for keys, one for values
keys = ["name", "age", "city"]
values = ["Bob", 30, "Lalitpur"]
combined = dict(zip(keys, values))  

# 15. Write a dictionary comprehension to create a dictionary of squares of numbers from 1 to 5
squares = {x: x**2 for x in range(1, 6)} 
