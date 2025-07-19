# 1. Write a function add_numbers that takes any number of positional arguments and returns their sum.
def add_numbers(*args):
    return sum(args)

# 2. Create a function print_info that accepts keyword arguments and prints each key and value.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 3. Write a function greet with a default parameter name="Guest" that prints Hello, <name>!.
def greet(name="Guest"):
    print(f"Hello, {name}!")

# 4. Define a function multiply that takes two parameters, a and b, where b has a default value of 2, and returns their product.
def multiply(a, b=2):
    return a * b

# 5. Write a function concat_strings that accepts any number of strings as arguments and concatenates them with spaces in between.
def concat_strings(*args):
    return " ".join(args)

# 6. Implement a function describe_pet with parameters name, animal_type='dog', and age=None. It should print details about the pet.
def describe_pet(name, animal_type='dog', age=None):
    print(f"Pet name: {name}")
    print(f"Animal type: {animal_type}")
    if age is not None:
        print(f"Age: {age}")

# 7. Create a function calculate that accepts any number of positional arguments and keyword argument operation.
def calculate(*args, operation):
    if not args:
        return "No numbers provided"
    result = args[0]
    for num in args[1:]:
        if operation == "add":
            result += num
        elif operation == "subtract":
            result -= num
        elif operation == "multiply":
            result *= num
        else:
            return "Unsupported operation"
    return result

# 8. Write a function build_profile that takes first and last name and arbitrary keyword arguments to build a user profile dictionary.
def build_profile(first, last, **kwargs):
    profile = {'first': first, 'last': last}
    profile.update(kwargs)
    return profile

# 9. Define a function count_vowels that takes a string and returns the number of vowels in it. Add a default parameter to ignore case or not.
def count_vowels(text, ignore_case=True):
    vowels = "aeiouAEIOU" if not ignore_case else "aeiou"
    text = text.lower() if ignore_case else text
    return sum(1 for char in text if char in vowels)

# 10. Write a function print_scores that accepts named scores for any number of students using **kwargs and prints them.
def print_scores(**kwargs):
    for student, score in kwargs.items():
        print(f"{student}: {score}")

# 11. Create a function safe_divide with parameters a and b=1. It should return a/b but handle division by zero.
def safe_divide(a, b=1):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

# 12. Write a function sum_even_numbers that takes any number of arguments and returns the sum of only the even numbers.
def sum_even_numbers(*args):
    return sum(num for num in args if num % 2 == 0)

# 13. Define a function describe_city that takes parameters city and country='Nepal'. It should print a message.
def describe_city(city, country='Nepal'):
    print(f"{city} is in {country}.")

# 14. Write a function custom_greeting that takes *args for names and a keyword argument greeting="Hello".
def custom_greeting(*args, greeting="Hello"):
    for name in args:
        print(f"{greeting}, {name}!")

# 15. Create a function filter_kwargs that accepts **kwargs and returns a dictionary of keys starting with a specific letter.
def filter_kwargs(letter='a', **kwargs):
    return {k: v for k, v in kwargs.items() if k.startswith(letter)}
