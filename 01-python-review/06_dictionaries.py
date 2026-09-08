"""
Topic: Python Dictionaries - COMPLETE REFERENCE
File: 06_dictionaries.py
Description: ALL Dictionary methods and operations with examples
Course: CSC203 Data Structures
Author: Sumaiya Sadia
"""

# ============================================
# 1. DICTIONARY CREATION
# ============================================

print("=" * 60)
print("1. DICTIONARY CREATION - ALL WAYS")
print("=" * 60)

# Empty dictionary (MUST use {}, not set()!)
empty = {}
print(f"Empty dict: {empty}")
print(f"Type: {type(empty)}")

# With values
d1 = {"name": "Alice", "age": 25, "city": "NYC"}
print(f"With values: {d1}")

# Using dict() constructor
d2 = dict(name="Alice", age=25, city="NYC")
print(f"Using dict(): {d2}")

# From list of tuples
d3 = dict([("name", "Alice"), ("age", 25), ("city", "NYC")])
print(f"From list of tuples: {d3}")

# From two lists using zip()
keys = ["name", "age", "city"]
values = ["Alice", 25, "NYC"]
d4 = dict(zip(keys, values))
print(f"From zip(): {d4}")

# Dictionary comprehension
d5 = {x: x**2 for x in range(1, 6)}
print(f"Dict comprehension: {d5}")

# Fromkeys() - create dict with default values
d6 = dict.fromkeys(["a", "b", "c"], 0)
print(f"fromkeys(): {d6}")


# ============================================
# 2. ACCESSING VALUES
# ============================================

print("\n" + "=" * 60)
print("2. ACCESSING VALUES")
print("=" * 60)

d = {"name": "Alice", "age": 25, "city": "NYC", "country": "USA"}
print(f"Dictionary: {d}")

# Direct access (raises KeyError if missing)
print(f"d['name']: {d['name']}")
# print(d['gender'])  # ❌ KeyError

# get() - safe access (returns None if missing)
print(f"d.get('age'): {d.get('age')}")
print(f"d.get('gender'): {d.get('gender')}")
print(f"d.get('gender', 'Unknown'): {d.get('gender', 'Unknown')}")

# setdefault() - get or set default
print(f"d.setdefault('phone', 'N/A'): {d.setdefault('phone', 'N/A')}")
print(f"After setdefault(): {d}")

# keys() - get all keys
print(f"Keys: {list(d.keys())}")

# values() - get all values
print(f"Values: {list(d.values())}")

# items() - get all key-value pairs
print(f"Items: {list(d.items())}")


# ============================================
# 3. ADDING AND UPDATING
# ============================================

print("\n" + "=" * 60)
print("3. ADDING AND UPDATING")
print("=" * 60)

d = {"name": "Alice", "age": 25}
print(f"Original: {d}")

# Direct assignment - add new key
d["city"] = "NYC"
print(f"Add 'city': {d}")

# Direct assignment - update existing
d["age"] = 26
print(f"Update 'age': {d}")

# update() - add multiple key-value pairs
d.update({"country": "USA", "age": 27})
print(f"After update(): {d}")

# update() with keyword arguments
d.update(city="LA", age=28)
print(f"After update(kwargs): {d}")


# ============================================
# 4. REMOVING ELEMENTS
# ============================================

print("\n" + "=" * 60)
print("4. REMOVING ELEMENTS")
print("=" * 60)

d = {"name": "Alice", "age": 25, "city": "NYC", "country": "USA", "phone": "123"}
print(f"Original: {d}")

# pop() - remove key and return value
removed = d.pop("phone")
print(f"After pop('phone'): {d}, Removed: {removed}")

# pop() with default (no error if missing)
removed = d.pop("gender", "Not found")
print(f"pop('gender', default): {removed}")

# popitem() - remove and return last item
key, value = d.popitem()
print(f"After popitem(): {d}, Removed: {key}:{value}")

# del - delete key
del d["country"]
print(f"After del 'country': {d}")

# clear() - remove all
d.clear()
print(f"After clear(): {d}")


# ============================================
# 5. LOOPING THROUGH DICTIONARIES
# ============================================

print("\n" + "=" * 60)
print("5. LOOPING THROUGH DICTIONARIES")
print("=" * 60)

d = {"name": "Alice", "age": 25, "city": "NYC"}

# Loop through keys
print("Keys:")
for key in d:
    print(f"  {key}")

# Loop through values
print("Values:")
for value in d.values():
    print(f"  {value}")

# Loop through key-value pairs
print("Key-Value pairs:")
for key, value in d.items():
    print(f"  {key}: {value}")

# Loop with enumerate
for i, (key, value) in enumerate(d.items()):
    print(f"  {i+1}. {key}: {value}")


# ============================================
# 6. DICTIONARY COMPREHENSION
# ============================================

print("\n" + "=" * 60)
print("6. DICTIONARY COMPREHENSION")
print("=" * 60)

# Square values
d1 = {"a": 1, "b": 2, "c": 3, "d": 4}
squared = {k: v**2 for k, v in d1.items()}
print(f"Original: {d1}")
print(f"Squared: {squared}")

# Filter by value
filtered = {k: v for k, v in d1.items() if v > 2}
print(f"Filtered (value > 2): {filtered}")

# Swap keys and values
inverted = {v: k for k, v in d1.items()}
print(f"Inverted: {inverted}")

# From two lists
keys = ["a", "b", "c", "d"]
values = [10, 20, 30, 40]
d2 = {k: v for k, v in zip(keys, values)}
print(f"From zip(): {d2}")

# Nested comprehension
d3 = {x: {y: x*y for y in range(1, 4)} for x in range(1, 4)}
print(f"Multiplication table dict: {d3}")


# ============================================
# 7. CHECKING AND SEARCHING
# ============================================

print("\n" + "=" * 60)
print("7. CHECKING AND SEARCHING")
print("=" * 60)

d = {"name": "Alice", "age": 25, "city": "NYC"}
print(f"Dictionary: {d}")

# Check if key exists
print(f"Has 'name'? {'name' in d}")
print(f"Has 'gender'? {'gender' in d}")

# Check if value exists
print(f"Has value 'Alice'? {'Alice' in d.values()}")
print(f"Has value 'Bob'? {'Bob' in d.values()}")

# Get length
print(f"Length: {len(d)}")


# ============================================
# 8. NESTED DICTIONARIES
# ============================================

print("\n" + "=" * 60)
print("8. NESTED DICTIONARIES")
print("=" * 60)

# Creating nested dictionary
students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "grades": [85, 90, 78],
        "address": {
            "city": "NYC",
            "zip": "10001"
        }
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "grades": [75, 80, 85],
        "address": {
            "city": "LA",
            "zip": "90001"
        }
    }
}

print("Nested Dictionary:")
for student_id, data in students.items():
    print(f"\n{student_id}:")
    print(f"  Name: {data['name']}")
    print(f"  Age: {data['age']}")
    print(f"  Grades: {data['grades']}")
    print(f"  City: {data['address']['city']}")

# Access nested data
print(f"\nStudent1's city: {students['student1']['address']['city']}")
print(f"Student2's first grade: {students['student2']['grades'][0]}")


# ============================================
# 9. DICTIONARY METHODS - COMPLETE LIST
# ============================================

print("\n" + "=" * 60)
print("9. COMPLETE DICTIONARY METHODS REFERENCE")
print("=" * 60)

print("""
📚 ALL DICTIONARY METHODS:

ACCESSING:
├── d[key]           - Direct access (KeyError if missing)
├── get(key, default) - Safe access (returns default if missing)
├── setdefault(key, default) - Get or set default
├── keys()           - Get all keys
├── values()         - Get all values
└── items()          - Get all key-value pairs

ADDING/UPDATING:
├── d[key] = value   - Add or update
└── update(dict)     - Add/update multiple

REMOVING:
├── pop(key, default) - Remove and return (default if missing)
├── popitem()        - Remove and return last item
├── del d[key]       - Delete key
└── clear()          - Remove all

CHECKING:
├── key in d         - Check if key exists
├── value in d.values() - Check if value exists
└── len(d)           - Get length

CREATING:
├── dict()           - Create empty dict
├── dict(key=value)  - Create with kwargs
├── dict(zip(keys, values)) - From two lists
├── fromkeys(keys, default) - Create with default values
└── {} comprehension - Dict comprehension

ITERATION:
├── for key in d            - Iterate keys
├── for value in d.values() - Iterate values
└── for key, val in d.items() - Iterate pairs
""")

# ============================================
# 10. COMMON USE CASES FOR DSA
# ============================================

print("\n" + "=" * 60)
print("10. COMMON USE CASES IN DSA")
print("=" * 60)

# 1. Frequency Counter (MOST IMPORTANT!)
def count_frequency(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(f"Frequency counter: {count_frequency(data)}")

# 2. Graph as Adjacency List
graph = {}
def add_edge(graph, u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

add_edge(graph, 1, 2)
add_edge(graph, 1, 3)
add_edge(graph, 2, 4)
print(f"Graph adjacency list: {graph}")

# 3. Memoization (Caching)
memo = {}
def fibonacci_with_memo(n):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_with_memo(n-1) + fibonacci_with_memo(n-2)
    return memo[n]

print(f"Fibonacci(10) with memo: {fibonacci_with_memo(10)}")
print(f"Memo cache: {memo}")

# 4. Two Sum Problem (O(n))
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

nums = [2, 7, 11, 15]
print(f"Two sum (9): {two_sum(nums, 9)}")


# ============================================
# 11. PRACTICE PROBLEMS
# ============================================

print("\n" + "=" * 60)
print("11. PRACTICE PROBLEMS")
print("=" * 60)

print("Try these yourself:")
print("1. Write a function to merge two dictionaries")
print("2. Write a function to find the most frequent element in a list")
print("3. Write a function to invert a dictionary (keys ↔ values)")
print("4. Write a function to find keys with a specific value")

# Solutions

def merge_dicts(d1, d2):
    """Merge two dictionaries (d2 overrides d1)"""
    result = d1.copy()
    result.update(d2)
    return result

def most_frequent(lst):
    """Find most frequent element"""
    freq = count_frequency(lst)
    return max(freq, key=freq.get)

def invert_dict(d):
    """Invert dictionary (keys become values)"""
    inverted = {}
    for key, value in d.items():
        # Handle duplicate values
        if value not in inverted:
            inverted[value] = [key]
        else:
            inverted[value].append(key)
    return inverted

def find_keys_with_value(d, target):
    """Find all keys with a specific value"""
    return [key for key, value in d.items() if value == target]

print("\n✅ Practice Solutions:")

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print(f"Merge {d1} and {d2}: {merge_dicts(d1, d2)}")

lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(f"Most frequent in {lst}: {most_frequent(lst)}")

d = {"a": 1, "b": 2, "c": 1, "d": 3}
print(f"Invert {d}: {invert_dict(d)}")
print(f"Keys with value 1 in {d}: {find_keys_with_value(d, 1)}")


# ============================================
# RUN ALL TESTS
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ ALL TESTS COMPLETED")
    print("=" * 60)
    print("\n📚 COMPLETE DICTIONARIES REFERENCE ADDED TO REPO!")