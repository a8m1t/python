# 1. What is the main difference between a list and a tuple in Python?
# Lists are mutable, while tuples are immutable.

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

# 2. How do you create an empty list and an empty tuple?
empty_list = []
empty_tuple = ()

# 3. Given the list `my_list = [1, 2, 3, 4, 5]`, how would you:
my_list = [1, 2, 3, 4, 5]
# a) Access the first element?
first_element = my_list[0]
# b) Access the last element?
last_element = my_list[-1]
# c) Access the elements from index 1 to 3 (inclusive of 1 and exclusive of 3)?
slice_1_to_3 = my_list[1:3]

# 4. Given the tuple `my_tuple = (10, 20, 30, 40, 50)`, how would you:
my_tuple = (10, 20, 30, 40, 50)
# a) Access the third element?
third_element = my_tuple[2]
# b) Try to change the first element to 100. What happens?
# my_tuple[0] = 100  # This will raise a TypeError because tuples are immutable.

# 5. List Methods:
sample_list = [1, 2, 3]
# a) How do you add an element to the end of a list?
sample_list.append(4)
# b) How do you insert an element at a specific position?
sample_list.insert(1, 10)
# c) How do you remove an element by value? And by index?
sample_list.remove(10)     # by value
del sample_list[0]         # by index
# d) How do you sort a list in ascending and descending order?
sample_list.sort()         # ascending
sample_list.sort(reverse=True)  # descending

# 6. Since tuples are immutable, what methods are available for tuples? (Name at least 3)
# Tuples support methods like:
# count(), index(), and conversion using tuple()
t = (1, 2, 2, 3)
count_2 = t.count(2)
index_3 = t.index(3)

# 7. Convert the list `[1, 2, 3]` into a tuple.
converted_tuple = tuple([1, 2, 3])

# 8. Convert the tuple `(4, 5, 6)` into a list.
converted_list = list((4, 5, 6))

# 9. What is the purpose of the `len()` function? Show with an example for both list and tuple.
# It returns the number of items.
len_list = len([1, 2, 3])     # 3
len_tuple = len((4, 5, 6))    # 3

# 10. What is the output of the following code?
a = [1, 2, 3]
b = a
b[0] = 100
print(a)  # Output: [100, 2, 3]
# Explanation: `b` is a reference to the same list as `a`, so changing `b` also affects `a`.

# 11. How would you create a tuple with a single element?
single_tuple = (1,)  # Note the comma!

# 12. What is the result of `[1, 2] + [3, 4]`? And what about `(1, 2) + (3, 4)`?
list_concat = [1, 2] + [3, 4]     # [1, 2, 3, 4]
tuple_concat = (1, 2) + (3, 4)    # (1, 2, 3, 4)

# 13. How do you check if an element exists in a list or tuple?
3 in [1, 2, 3]       # True
5 in (1, 2, 3)       # False

# 14. How do you count the number of occurrences of an element in a list? And in a tuple?
[1, 2, 2, 3].count(2)      # 2
(1, 2, 2, 3).count(2)      # 2

# 15. How do you find the index of the first occurrence of an element in a list? And in a tuple?
[1, 2, 3, 2].index(2)      # 1
(1, 2, 3, 2).index(2)      # 1

# 16. Given a list `[5, 2, 8, 2, 1]`, use slicing to get:
my_list = [5, 2, 8, 2, 1]
from_index_1 = my_list[1:]         # [2, 8, 2, 1]
to_index_2 = my_list[:2]           # [5, 2]
every_second = my_list[::2]        # [5, 8, 1]

# 17. How do you reverse a list? (two methods: using slicing and using a method)
reversed_by_slicing = my_list[::-1]
my_list.reverse()  # This reverses in place

# 18. How do you reverse a tuple? (remember tuples are immutable)
reversed_tuple = (1, 2, 3)[::-1]  # (3, 2, 1)

# 19. What is a nested list? How would you access an element in a nested list?
nested = [[1, 2], [3, 4], [5, 6]]
element = nested[1][0]  # 3

# 20. Create a tuple containing three lists. Can you change the contents of these lists within the tuple? Why or why not?
tup_with_lists = ([1], [2], [3])
tup_with_lists[0].append(100)  # Allowed: because the tuple is immutable, but the lists inside are mutable.
# Output: ([1, 100], [2], [3])
