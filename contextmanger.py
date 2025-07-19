# Task 1: Use with to Read a File Safely
with open("file.txt", "r") as f:
    content = f.read()
    print(content)



# Task 2: Use with to Write to a File
with open("file.txt", "w") as f:
    f.write("This is written using the with statement.")

# Task 3: Handle FileNotFoundError with Context Manager
try:
    with open("missing_file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found.")


# Task 4: Custom Context Manager Using Class
class MyContext:
    def __enter__(self):
        print("Entering context.")
        return "Resource"
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context.")

with MyContext() as resource:
    print("Using:", resource)


# Task 5: Time a Code Block
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print(f"Elapsed time: {end - self.start:.4f} seconds")

with Timer():
    for i in range(1000000):
        pass


# Task 6: Context Manager with contextlib
from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, "r")
    try:
        yield f
    finally:
        f.close()

with open_file("file.txt") as f:
    print(f.read())


# Task 7: Open Two Files at Once
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    print("File 1:", f1.readline())
    print("File 2:", f2.readline())


# Task 8: Catch Exception in __exit__
class CatchError:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("Error caught:", exc_type, exc_val)

with CatchError():
    print("Inside context.")
    x = 1 / 0  # This will raise ZeroDivisionError


# Task 9: Change and Restore Working Directory
import os

class ChangeDir:
    def __init__(self, new_dir):
        self.new_dir = new_dir
        self.original_dir = os.getcwd()

    def __enter__(self):
        os.chdir(self.new_dir)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.original_dir)

print("Before:", os.getcwd())
with ChangeDir("/tmp" if os.name != "nt" else os.environ.get("TEMP", "C:\\Windows\\Temp")):
    print("Inside:", os.getcwd())
print("After:", os.getcwd())


# Task 10: Temp File Auto-Delete
import tempfile
import os

class TempFile:
    def __enter__(self):
        self.file = tempfile.NamedTemporaryFile(delete=False)
        self.name = self.file.name
        self.file.write(b"Temporary data")
        self.file.close()
        return self.name

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.remove(self.name)
        print(f"Deleted temp file: {self.name}")

with TempFile() as temp_name:
    print(f"Temp file created: {temp_name}")
    with open(temp_name, 'r') as f:
        print(f.read())


