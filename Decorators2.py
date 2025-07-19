#  Write a decorator that logs the arguments passed to a function and also logs its return value.

def log_args_and_return(func):
    def wrapper(*args, **kwargs):
        print("Function name:", func.__name__)
        print("Arguments passed:", args)
        print("Keyword arguments passed:", kwargs)
        
        result = func(*args, **kwargs)  
        print("Return value:", result)
        
        return result
    return wrapper


@log_args_and_return
def add(a, b):
    return a + b


add(5, 3)

## 
#  Create a decorator that calculates and prints the time a function takes to execute.

import time  

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  
        result = func(*args, **kwargs)  
        end_time = time.time()  

        duration = end_time - start_time  
        print(f"Function took {duration:.4f} seconds to run")
        return result  
    return wrapper


@measure_time
def example_task():
    print("Task is running.")
    time.sleep(2) 
    print("Task completed.")


example_task()


# #
#  Write a decorator that converts a function’s return value to a specified type (like int, str, or float).


def convert_return(return_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return return_type(result)  
        return wrapper
    return decorator

@convert_return(int)
def get_string_number():
    return "10"

print(get_string_number()) 

@convert_return(str)
def get_number():
    return 100

print(get_number())


##
# Implement a decorator that caches (remembers) the result of a function for given inputs to avoid re-computation.
def cache(func):
    saved_results = {}  # Dictionary to store results

    def wrapper(*args):
        if args in saved_results:
            return saved_results[args]  # Return cached result
        result = func(*args)  # Compute result
        saved_results[args] = result  # Save result in cache
        return result

    return wrapper

@cache
def slow_add(a, b):
    print("Calculating...")
    return a + b

print(slow_add(2, 3))  
print(slow_add(2, 3))  
print(slow_add(4, 5))  

##

#  Create a decorator that checks if function arguments satisfy a certain condition before the function runs.

def validate_positive(func):
    def wrapper(*args):
        for arg in args:
            if arg <= 0:
                raise ValueError("All arguments must be greater than 0")
        return func(*args)
    return wrapper

@validate_positive
def multiply(a, b):
    return a * b

print(multiply(3, 4))    
print(multiply(-2, 5)) 

##
# Write a decorator that retries a function if it raises an error, for a set number of times.

def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed")
            print("All attempts failed.")
        return wrapper
    return decorator


@retry(3)
def risky_function():
    number = int(input("Enter a number: "))
    return 10 / number

print(risky_function())

##
# Implement a decorator to restrict how often a function can be called (e.g., once every few seconds).

import time

def rate_limit(seconds):
    last_called = 0

    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal last_called
            now = time.time()
            if now - last_called < seconds:
                print(f"Wait {seconds - (now - last_called):.2f} seconds before calling again.")
                return
            last_called = now
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(3)
def my_function():
    print("Function is called!")


my_function()  
my_function()  
time.sleep(3)
my_function()  


