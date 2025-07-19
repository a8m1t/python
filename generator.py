# 1. Generator that yields numbers from 1 to 5
def gen_one_to_five():
    for i in range(1, 6):
        yield i

# 2. Generator that yields characters of a string one by one
def gen_chars(text):
    for char in text:
        yield char

# 3. Generator that yields even numbers between 2 and 10
def gen_even():
    for i in range(2, 11, 2):
        yield i

# 4. Generator expression to generate squares of numbers from 1 to 10
squares_gen = (x**2 for x in range(1, 11))

# 5. Generator that yields first 5 multiples of 3
def gen_multiples_of_3():
    for i in range(1, 6):
        yield i * 3

# 6. Loop over a generator and print all values
for val in gen_one_to_five():
    print(val)

# 7. What happens if you call next() on a generator after it's exhausted?
def simple_gen():
    yield 1
g = simple_gen()
print(next(g))     
try:
    print(next(g)) 
except StopIteration:
    print("Generator exhausted")

# 8. Generator that yields elements from a given list
def gen_from_list(lst):
    for item in lst:
        yield item

# 9. Generator to yield numbers from 10 down to 1
def gen_descending():
    for i in range(10, 0, -1):
        yield i

# 10. Convert [x*2 for x in range(5)] into generator expression
double_gen = (x * 2 for x in range(5))

# 11. Generator that yields first 5 letters of the alphabet
def gen_letters():
    for c in "abcde":
        yield c

# 12. Generator that yields only odd numbers from 1 to 15
def gen_odds():
    for i in range(1, 16, 2):
        yield i

# 13. Loop over a generator twice
g = gen_one_to_five()
for x in g:
    print(x) 
for x in g:
    print(x)  

# 14. Generator that yields numbers from 1 to n (parameter)
def gen_up_to_n(n):
    for i in range(1, n + 1):
        yield i

# 15. Generator that yields words of a sentence one by one
def gen_words(sentence):
    for word in sentence.split():
        yield word

# 16. Generator expression to produce cubes of numbers 1 to 7
cubes = (x**3 for x in range(1, 8))

# 17. Generator that yields True or False alternately, 6 times
def gen_alternate_bools():
    for i in range(6):
        yield i % 2 == 0

# 18. Generator that yields Fibonacci numbers up to 10
def gen_fibonacci_upto_10():
    a, b = 0, 1
    while a <= 10:
        yield a
        a, b = b, a + b

# 19. Generator that yields characters of a string in uppercase
def gen_upper(text):
    for char in text:
        yield char.upper()

# 20. Generator expression to yield numbers divisible by 3 between 1 and 20
div3_gen = (x for x in range(1, 21) if x % 3 == 0)
