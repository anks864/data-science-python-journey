"""
File: no03_list_tuple_set_dictionary.py
Topic: Python Data Structures
Description: Covers List, Tuple, Set, and Dictionary with examples.
"""

# ==============================
# 1. LIST (Mutable, Ordered)
# ==============================
numbers_list = [1, 2, 3, 5, 4, 5, 1, 9]  # allows duplicates
print(numbers_list, type(numbers_list))

mixed_list = [4.5, 2+3j, "Paper Rings", 'A', False, 25]
print(mixed_list)  # multiple data types allowed

# Adding elements
mixed_list.append("TS")
print(mixed_list)

# Slicing and length
print(numbers_list[2:4])
print(len(numbers_list))

# Empty list
empty_list = []
print(empty_list)

# Deleting element
del numbers_list[3]
print(numbers_list)

# Joining lists
print(numbers_list + mixed_list)


# ==============================
# 2. TUPLE (Immutable, Ordered)
# ==============================
numbers_tuple = (2, 6, 4, 8)
print(numbers_tuple, type(numbers_tuple))

mixed_tuple = ("Architecture", 3.5, 8, True)
print(mixed_tuple)

# List to Tuple
sample_list = [3, 5, 7, 9]
converted_tuple = tuple(sample_list)
print(converted_tuple, type(converted_tuple))

# Tuple to List
converted_list = list(converted_tuple)
print(converted_list, type(converted_list))

# Indexing
print(numbers_tuple[3], converted_tuple[2])


# ==============================
# 3. EMPTY DATA TYPES
# ==============================
empty_list = []
empty_tuple = ()
empty_dict = {}
empty_string = ""
empty_set = set()

print(empty_list, type(empty_list))
print(empty_tuple, type(empty_tuple))
print(empty_dict, type(empty_dict))
print(empty_string, type(empty_string))
print(empty_set, type(empty_set))


# ==============================
# 4. SET (Mutable, Unordered)
# ==============================
unique_set = {1, 2, 3, 4, 5}
print(unique_set, type(unique_set))  # no indexing

# Adding element
unique_set.add(10)
print(unique_set)

# Removing duplicates from list
list_with_duplicates = [1, 2, 2, 3, 4, 4]
unique_values = set(list_with_duplicates)
print(unique_values)


# ==============================
# 5. DICTIONARY (Mutable, Key-Value)
# ==============================
student_info = {'Name': 'Ankita', 'Age': 20, 'Country': 'India'}
print(student_info, type(student_info))

# Accessing value
print(student_info['Age'])

# Duplicate keys (last value is kept)
duplicate_key_dict = {'Name': 'Archit', 'Age': 20, 'Country': 'India', 'Age': 25}
print(duplicate_key_dict)


# ==============================
# 6. Mini Practice
# ==============================
# Count unique elements in a list
sample_numbers = [1, 2, 2, 3, 4, 4, 5]
unique_count = len(set(sample_numbers))
print("Number of unique elements:", unique_count)


# ==============================
# EOF: Feel free to open an issue for bugs or suggestions
# ==============================
