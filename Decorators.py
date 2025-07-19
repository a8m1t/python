# 1. Decorator that prints before executing the function

def decorator(func):
    def wrapper():
        print("Hello, I am a decorator")
        func()
    return wrapper

@decorator
def say_hi():
    print("Hi there!")

say_hi()
# 2. Decorator that logs the function name

def log_function(func):
    def wrapper():
        print(f"{func.__name__} is being called...")
        func()
    return wrapper

@log_function
def greet():
    print("Hello!")

greet()
# 3. Decorator that multiplies return value by 2

def double_result(func):
    def wrapper():
        return func() * 2
    return wrapper

@double_result
def get_number():
    return 5

print(get_number())  
#  4. Decorator that prints *args and **kwargs

def show_args(func):
    def wrapper(*args, **kwargs):
        print("Arguments:", args)
        print("Keyword Arguments:", kwargs)
        return func(*args, **kwargs)
    return wrapper

@show_args
def add(a, b):
    return a + b

print(add(3, b=4))
# 5. Decorator with login control

is_logged_in = False  

def require_login(func):
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access Denied")
    return wrapper

@require_login
def view_dashboard():
    print("Welcome to the dashboard!")

view_dashboard()
# Two stacked decorators (uppercase + exclamation)

def make_upper(func):
    def wrapper():
        return func().upper()
    return wrapper

def add_exclamation(func):
    def wrapper():
        return func() + "!"
    return wrapper

@add_exclamation
@make_upper
def message():
    return "hello"

print(message())  



