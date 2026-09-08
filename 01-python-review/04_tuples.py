"""
Topic: Python Tuples
File: 04_tuples.py
Description: Complete Python Tuple operations with all methods and patterns
Course: CSC203 Data Structures
Author: Sumaiya Sadia
"""

# ============================================
# 1. TUPLE CREATION
# ============================================

print("=" * 60)
print("1. TUPLE CREATION")
print("=" * 60)

# Empty tuple
empty = ()
print(f"Empty tuple: {empty}")

# With values
t = (1, 2, 3, 4, 5)
print(f"Tuple: {t}")

# Without parentheses (tuple packing)
t2 = 1, 2, 3
print(f"Without parentheses: {t2}")

# Single element (MUST have comma!)
single = (5,)
print(f"Single element tuple: {single}")
print(f"Type: {type(single)}")

# From list
t3 = tuple([1, 2, 3])
print(f"From list: {t3}")

# From string
t4 = tuple("hello")
print(f"From string: {t4}")


# ============================================
# 2. ACCESSING ELEMENTS
# ============================================

print("\n" + "=" * 60)
print("2. ACCESSING ELEMENTS")
print("=" * 60)

t = (10, 20, 30, 40, 50)
print(f"Tuple: {t}")

# Indexing (same as lists)
print(f"First element (index 0): {t[0]}")
print(f"Third element (index 2): {t[2]}")
print(f"Last element (index -1): {t[-1]}")
print(f"Second last (index -2): {t[-2]}")

# Slicing
print(f"Slice [1:4]: {t[1:4]}")      # (20, 30, 40)
print(f"Slice [:3]: {t[:3]}")         # (10, 20, 30)
print(f"Slice [2:]: {t[2:]}")         # (30, 40, 50)
print(f"Reverse: {t[::-1]}")          # (50, 40, 30, 20, 10)


# ============================================
# 3. TUPLE UNPACKING (IMPORTANT!)
# ============================================

print("\n" + "=" * 60)
print("3. TUPLE UNPACKING")
print("=" * 60)

# Basic unpacking
a, b, c = (1, 2, 3)
print(f"Unpacking: a={a}, b={b}, c={c}")

# Swap values using tuple unpacking
x, y = 5, 10
print(f"Before swap: x={x}, y={y}")
x, y = y, x
print(f"After swap: x={x}, y={y}")

# Extended unpacking with *
first, *rest = (1, 2, 3, 4, 5)
print(f"First: {first}, Rest: {rest}")

# Unpacking in loops
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
print("Loop unpacking:")
for num, letter in pairs:
    print(f"  Number: {num}, Letter: {letter}")


# ============================================
# 4. TUPLE OPERATIONS
# ============================================

print("\n" + "=" * 60)
print("4. TUPLE OPERATIONS")
print("=" * 60)

t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenation (+)
t3 = t1 + t2
print(f"Concatenation (t1 + t2): {t3}")

# Repetition (*)
t4 = t1 * 3
print(f"Repetition (t1 * 3): {t4}")

# Membership testing
print(f"Is 3 in t1? {3 in t1}")
print(f"Is 7 in t1? {7 in t1}")

# Length
print(f"Length of t1: {len(t1)}")


# ============================================
# 5. TUPLE METHODS
# ============================================

print("\n" + "=" * 60)
print("5. TUPLE METHODS")
print("=" * 60)

t = (1, 2, 3, 2, 4, 2, 5)
print(f"Tuple: {t}")

# count() - count occurrences
print(f"Count of 2: {t.count(2)}")
print(f"Count of 7: {t.count(7)}")

# index() - find position (first occurrence)
print(f"Index of 4: {t.index(4)}")
print(f"Index of 2 (first occurrence): {t.index(2)}")

# min() and max()
print(f"Minimum: {min(t)}")
print(f"Maximum: {max(t)}")
print(f"Sum: {sum(t)}")


# ============================================
# 6. TUPLES VS LISTS (IMMUTABILITY)
# ============================================

print("\n" + "=" * 60)
print("6. TUPLES VS LISTS (IMMUTABILITY)")
print("=" * 60)

# ✅ Lists are MUTABLE (can change)
lst = [1, 2, 3]
print(f"List before: {lst}")
lst[0] = 10
lst.append(4)
print(f"List after modification: {lst}")

# ❌ Tuples are IMMUTABLE (cannot change)
t = (1, 2, 3)
print(f"Tuple: {t}")
# t[0] = 10  # ❌ ERROR! TypeError: 'tuple' object does not support item assignment

# ✅ Convert tuple to list, modify, convert back
temp = list(t)
temp[0] = 10
t = tuple(temp)
print(f"Tuple converted to list and back: {t}")


# ============================================
# 7. TUPLES AS DICTIONARY KEYS
# ============================================

print("\n" + "=" * 60)
print("7. TUPLES AS DICTIONARY KEYS")
print("=" * 60)

# ✅ Tuples can be dictionary keys (immutable)
coordinates = {}
coordinates[(1, 2)] = "Point A"
coordinates[(3, 4)] = "Point B"
print(f"Dictionary with tuple keys: {coordinates}")
print(f"Value at (1,2): {coordinates[(1, 2)]}")

# ❌ Lists CANNOT be dictionary keys (mutable)
# coordinates[[5, 6]] = "Point C"  # ❌ ERROR! TypeError


# ============================================
# 8. COMMON USE CASES
# ============================================

print("\n" + "=" * 60)
print("8. COMMON USE CASES")
print("=" * 60)

# Returning multiple values from a function
def get_min_max(data):
    return min(data), max(data)

numbers = [3, 7, 1, 9, 5]
min_val, max_val = get_min_max(numbers)
print(f"Function returning tuple: min={min_val}, max={max_val}")

# Using tuples for fixed data
months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
print(f"Months (tuple): {months[0:3]}")  # ('Jan', 'Feb', 'Mar')


# ============================================
# 9. PRACTICE PROBLEMS
# ============================================

print("\n" + "=" * 60)
print("9. PRACTICE PROBLEMS")
print("=" * 60)

print("Try these yourself:")
print("1. Write a function that returns the second largest element in a tuple")
print("2. Write a function that checks if two tuples are equal")
print("3. Write a function that merges two tuples")

# Solutions

def second_largest_tuple(t):
    """Find second largest in tuple"""
    if len(t) < 2:
        return None
    unique = sorted(set(t), reverse=True)
    return unique[1] if len(unique) > 1 else None

def tuples_equal(t1, t2):
    """Check if two tuples are equal"""
    return t1 == t2

def merge_tuples(t1, t2):
    """Merge two tuples"""
    return t1 + t2

print("\n✅ Practice Solutions:")
test_t = (1, 3, 5, 2, 4)
print(f"Second largest in {test_t}: {second_largest_tuple(test_t)}")

t1 = (1, 2, 3)
t2 = (1, 2, 3)
t3 = (1, 2, 4)
print(f"Are {t1} and {t2} equal? {tuples_equal(t1, t2)}")
print(f"Are {t1} and {t3} equal? {tuples_equal(t1, t3)}")

print(f"Merge {t1} and {t3}: {merge_tuples(t1, t3)}")


# ============================================
# RUN ALL TESTS
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ ALL TESTS COMPLETED")
    print("=" * 60)