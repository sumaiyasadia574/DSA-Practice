"""
Topic: Python Sets - COMPLETE REFERENCE
File: 05_sets.py
Description: ALL Set methods and operations with examples
Course: CSC203 Data Structures
Author: Sumaiya Sadia
"""

# ============================================
# 1. SET CREATION
# ============================================

print("=" * 60)
print("1. SET CREATION - ALL WAYS")
print("=" * 60)

# Empty set (MUST use set(), not {})
empty = set()
print(f"Empty set: {empty}")
print(f"Type: {type(empty)}")

# With values
s1 = {1, 2, 3, 4, 5}
print(f"Set with values: {s1}")

# From list (removes duplicates)
s2 = set([1, 2, 2, 3, 3, 4, 4, 5])
print(f"From list with duplicates: {s2}")

# From tuple
s3 = set((1, 2, 3, 3, 4, 4))
print(f"From tuple: {s3}")

# From string
s4 = set("hello")
print(f"From string 'hello': {s4}")

# From range
s5 = set(range(1, 10, 2))
print(f"From range(1,10,2): {s5}")

# Set comprehension
s6 = {x**2 for x in range(1, 6)}
print(f"Set comprehension (squares): {s6}")


# ============================================
# 2. ADDING ELEMENTS - ALL METHODS
# ============================================

print("\n" + "=" * 60)
print("2. ADDING ELEMENTS - ALL METHODS")
print("=" * 60)

s = {1, 2, 3}
print(f"Original: {s}")

# add() - adds single element if not exists
s.add(4)
print(f"After add(4): {s}")
s.add(2)  # No change (already exists)
print(f"After add(2) (no change): {s}")

# update() - adds multiple elements (like extend for sets)
s.update([5, 6, 7])
print(f"After update([5,6,7]): {s}")

# update() with another set
s.update({8, 9})
print(f"After update({8,9}): {s}")

# update() with tuple
s.update((10, 11))
print(f"After update((10,11)): {s}")

# update() with string (adds individual characters)
s.update("AB")
print(f"After update('AB'): {s}")


# ============================================
# 3. REMOVING ELEMENTS - ALL METHODS
# ============================================

print("\n" + "=" * 60)
print("3. REMOVING ELEMENTS - ALL METHODS")
print("=" * 60)

s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(f"Original: {s}")

# remove() - removes element, ERROR if not exists
s.remove(10)
print(f"After remove(10): {s}")
# s.remove(99)  # ❌ KeyError - uncomment to test

# discard() - removes element, NO error if not exists
s.discard(9)
print(f"After discard(9): {s}")
s.discard(99)  # No error
print(f"After discard(99) (no error): {s}")

# pop() - removes and returns ARBITRARY element
popped = s.pop()
print(f"Popped: {popped}, Remaining: {s}")

# clear() - removes ALL elements
s.clear()
print(f"After clear(): {s}")


# ============================================
# 4. SET OPERATIONS - UNION
# ============================================

print("\n" + "=" * 60)
print("4. SET OPERATIONS - UNION")
print("=" * 60)

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(f"s1: {s1}")
print(f"s2: {s2}")

# Method 1: union() method
print(f"union() method: {s1.union(s2)}")

# Method 2: | operator
print(f"| operator: {s1 | s2}")

# Method 3: update() - modifies original
s1_copy = s1.copy()
s1_copy.update(s2)
print(f"update() method (modifies original): {s1_copy}")

# Union with multiple sets
s3 = {7, 8, 9}
print(f"Union of s1, s2, s3: {s1.union(s2, s3)}")


# ============================================
# 5. SET OPERATIONS - INTERSECTION
# ============================================

print("\n" + "=" * 60)
print("5. SET OPERATIONS - INTERSECTION")
print("=" * 60)

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = {4, 5, 6, 7}
print(f"s1: {s1}")
print(f"s2: {s2}")
print(f"s3: {s3}")

# Method 1: intersection() method
print(f"intersection() method: {s1.intersection(s2)}")

# Method 2: & operator
print(f"& operator: {s1 & s2}")

# Method 3: intersection_update() - modifies original
s1_copy = s1.copy()
s1_copy.intersection_update(s2)
print(f"intersection_update() (modifies original): {s1_copy}")

# Intersection of multiple sets
print(f"Intersection of s1, s2, s3: {s1.intersection(s2, s3)}")


# ============================================
# 6. SET OPERATIONS - DIFFERENCE
# ============================================

print("\n" + "=" * 60)
print("6. SET OPERATIONS - DIFFERENCE")
print("=" * 60)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(f"s1: {s1}")
print(f"s2: {s2}")

# Method 1: difference() method
print(f"difference() method (s1 - s2): {s1.difference(s2)}")
print(f"difference() method (s2 - s1): {s2.difference(s1)}")

# Method 2: - operator
print(f"- operator (s1 - s2): {s1 - s2}")
print(f"- operator (s2 - s1): {s2 - s1}")

# Method 3: difference_update() - modifies original
s1_copy = s1.copy()
s1_copy.difference_update(s2)
print(f"difference_update() (modifies original): {s1_copy}")


# ============================================
# 7. SET OPERATIONS - SYMMETRIC DIFFERENCE
# ============================================

print("\n" + "=" * 60)
print("7. SET OPERATIONS - SYMMETRIC DIFFERENCE")
print("=" * 60)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(f"s1: {s1}")
print(f"s2: {s2}")

# Method 1: symmetric_difference() method
print(f"symmetric_difference() method: {s1.symmetric_difference(s2)}")

# Method 2: ^ operator
print(f"^ operator: {s1 ^ s2}")

# Method 3: symmetric_difference_update() - modifies original
s1_copy = s1.copy()
s1_copy.symmetric_difference_update(s2)
print(f"symmetric_difference_update() (modifies original): {s1_copy}")


# ============================================
# 8. SET COMPARISONS - ALL METHODS
# ============================================

print("\n" + "=" * 60)
print("8. SET COMPARISONS - ALL METHODS")
print("=" * 60)

s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
s3 = {1, 2, 3}
s4 = {6, 7, 8}

print(f"s1: {s1}, s2: {s2}, s3: {s3}, s4: {s4}")

# issubset() - all elements of s1 are in s2
print(f"Is s1 subset of s2? {s1.issubset(s2)}")
print(f"Is s1 subset of s3? {s1.issubset(s3)}")
print(f"Is s4 subset of s1? {s4.issubset(s1)}")

# issuperset() - all elements of s2 are in s1
print(f"Is s2 superset of s1? {s2.issuperset(s1)}")
print(f"Is s3 superset of s1? {s3.issuperset(s1)}")

# isdisjoint() - no common elements
print(f"Are s1 and s4 disjoint? {s1.isdisjoint(s4)}")
print(f"Are s1 and s2 disjoint? {s1.isdisjoint(s2)}")

# Equality
print(f"Are s1 and s3 equal? {s1 == s3}")
print(f"Are s1 and s2 equal? {s1 == s2}")


# ============================================
# 9. FROZENSET - IMMUTABLE SET
# ============================================

print("\n" + "=" * 60)
print("9. FROZENSET - IMMUTABLE SET")
print("=" * 60)

# frozenset() - creates immutable set
fs = frozenset([1, 2, 3, 4, 5])
print(f"frozenset: {fs}")
print(f"Type: {type(fs)}")

# Can use frozenset as dictionary key
d = {}
d[fs] = "Value"
print(f"Dictionary with frozenset key: {d}")

# Cannot modify frozenset
# fs.add(6)  # ❌ AttributeError
# fs.remove(1)  # ❌ AttributeError


# ============================================
# 10. SET COMPREHENSION
# ============================================

print("\n" + "=" * 60)
print("10. SET COMPREHENSION")
print("=" * 60)

# Basic set comprehension
s = {x for x in range(10)}
print(f"Range 0-9: {s}")

# Square each element
squares = {x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Filter even numbers
evens = {x for x in range(20) if x % 2 == 0}
print(f"Even numbers: {evens}")

# Nested set comprehension
nested = {x*y for x in range(1, 4) for y in range(1, 4)}
print(f"Nested comprehension (multiplication table): {nested}")


# ============================================
# 11. SET METHODS - COMPLETE LIST
# ============================================

print("\n" + "=" * 60)
print("11. COMPLETE SET METHODS REFERENCE")
print("=" * 60)

print("""
📚 ALL SET METHODS:

ADDING:
├── add(x)          - Add single element
├── update(iterable) - Add multiple elements

REMOVING:
├── remove(x)       - Remove element (ERROR if missing)
├── discard(x)      - Remove element (NO error if missing)
├── pop()           - Remove and return arbitrary element
├── clear()         - Remove all elements

OPERATIONS:
├── union(...)      - Combine sets (|)
├── intersection(...) - Common elements (&)
├── difference(...) - Elements in first but not others (-)
├── symmetric_difference(...) - Elements in either but not both (^)

MODIFICATION:
├── intersection_update(...) - Intersection (modifies original)
├── difference_update(...)   - Difference (modifies original)
├── symmetric_difference_update(...) - Symmetric difference (modifies original)

COMPARISONS:
├── issubset(other)  - Check if subset (<=)
├── issuperset(other) - Check if superset (>=)
├── isdisjoint(other) - Check if no common elements

COPYING:
├── copy()          - Return shallow copy

IMMUTABLE:
├── frozenset()     - Create immutable set
""")

# ============================================
# 12. COMMON USE CASES
# ============================================

print("\n" + "=" * 60)
print("12. COMMON USE CASES")
print("=" * 60)

# Remove duplicates from list
lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(lst))
print(f"Remove duplicates: {lst} → {unique}")

# Find common elements between lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(f"Common elements: {common}")

# Find elements in one list but not another
only_in_list1 = list(set(list1) - set(list2))
print(f"Only in list1: {only_in_list1}")

# Find elements in either list but not both
symmetric = list(set(list1) ^ set(list2))
print(f"Elements in either but not both: {symmetric}")

# Count unique elements in a list
print(f"Number of unique elements: {len(set(lst))}")

# Check if two lists have any common element
have_common = len(set(list1) & set(list2)) > 0
print(f"Have common elements? {have_common}")


# ============================================
# 13. PRACTICE PROBLEMS
# ============================================

print("\n" + "=" * 60)
print("13. PRACTICE PROBLEMS")
print("=" * 60)

print("Try these yourself:")
print("1. Write a function to find the intersection of three sets")
print("2. Write a function to remove all elements of one set from another")
print("3. Write a function to check if two sets are identical")
print("4. Write a function to find the symmetric difference of three sets")

# Solutions

def intersection_of_three(s1, s2, s3):
    """Find intersection of three sets"""
    return s1.intersection(s2, s3)

def remove_elements_from_set(s1, s2):
    """Remove all elements of s2 from s1"""
    result = s1.copy()
    result.difference_update(s2)
    return result

def sets_are_identical(s1, s2):
    """Check if two sets are identical"""
    return s1 == s2

def symmetric_diff_of_three(s1, s2, s3):
    """Find symmetric difference of three sets"""
    # First get symmetric diff of s1 and s2, then with s3
    return s1 ^ s2 ^ s3

print("\n✅ Practice Solutions:")

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = {5, 6, 7, 8, 9}

print(f"s1: {s1}")
print(f"s2: {s2}")
print(f"s3: {s3}")

print(f"Intersection of all three: {intersection_of_three(s1, s2, s3)}")
print(f"Remove s2 from s1: {remove_elements_from_set(s1, s2)}")
print(f"Are s1 and s2 identical? {sets_are_identical(s1, s2)}")
print(f"Symmetric diff of all three: {symmetric_diff_of_three(s1, s2, s3)}")


# ============================================
# RUN ALL TESTS
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ ALL TESTS COMPLETED")
    print("=" * 60)
    print("\n📚 COMPLETE SETS REFERENCE ADDED TO REPO!")