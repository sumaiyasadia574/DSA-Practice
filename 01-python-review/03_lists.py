"""
Topic: Python Lists
File: 03_lists.py
Description: Complete Python List operations with all methods and patterns
Course: CSC203 Data Structures
Author: Sumaiya Sadia
"""

# ============================================
# 1. LIST CREATION
# ============================================

print("=" * 60)
print("1. LIST CREATION")
print("=" * 60)

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# With values
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# Using range()
range_list = list(range(1, 10))
print(f"Range list (1-9): {range_list}")

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# List repetition
zeros = [0] * 5
print(f"Zeros repeated: {zeros}")


# ============================================
# 2. ACCESSING ELEMENTS
# ============================================

print("\n" + "=" * 60)
print("2. ACCESSING ELEMENTS")
print("=" * 60)

lst = [10, 20, 30, 40, 50]
print(f"List: {lst}")

# Positive indexing
print(f"First element (index 0): {lst[0]}")
print(f"Third element (index 2): {lst[2]}")

# Negative indexing
print(f"Last element (index -1): {lst[-1]}")
print(f"Second last (index -2): {lst[-2]}")

# Slicing
print(f"Slice [1:4]: {lst[1:4]}")      # [20, 30, 40]
print(f"Slice [:3]: {lst[:3]}")         # [10, 20, 30]
print(f"Slice [2:]: {lst[2:]}")         # [30, 40, 50]
print(f"Reverse ([::-1]): {lst[::-1]}") # [50, 40, 30, 20, 10]


# ============================================
# 3. ADDING ELEMENTS
# ============================================

print("\n" + "=" * 60)
print("3. ADDING ELEMENTS")
print("=" * 60)

lst = [1, 2, 3]
print(f"Original: {lst}")

# append() - add at end
lst.append(4)
print(f"After append(4): {lst}")

# insert() - add at specific position
lst.insert(1, 10)
print(f"After insert(1, 10): {lst}")

# extend() - add multiple elements
lst.extend([5, 6, 7])
print(f"After extend([5, 6, 7]): {lst}")

# Concatenation (+)
new_lst = lst + [8, 9]
print(f"After concatenation (+ [8, 9]): {new_lst}")


# ============================================
# 4. REMOVING ELEMENTS
# ============================================

print("\n" + "=" * 60)
print("4. REMOVING ELEMENTS")
print("=" * 60)

lst = [1, 2, 3, 4, 5, 3, 6]
print(f"Original: {lst}")

# pop() - remove by index (default last)
popped = lst.pop()
print(f"After pop(): {lst}, Removed: {popped}")

popped = lst.pop(1)
print(f"After pop(1): {lst}, Removed: {popped}")

# remove() - remove by value (first occurrence)
lst.remove(3)
print(f"After remove(3): {lst}")

# clear() - remove all
lst.clear()
print(f"After clear(): {lst}")


# ============================================
# 5. SEARCHING AND COUNTING
# ============================================

print("\n" + "=" * 60)
print("5. SEARCHING AND COUNTING")
print("=" * 60)

lst = [10, 20, 30, 20, 40, 20, 50]
print(f"List: {lst}")

# index() - find position
print(f"Index of 30: {lst.index(30)}")
print(f"Index of 20 (first occurrence): {lst.index(20)}")

# count() - count occurrences
print(f"Count of 20: {lst.count(20)}")
print(f"Count of 99: {lst.count(99)}")

# Membership testing
print(f"Is 30 in list? {30 in lst}")
print(f"Is 99 in list? {99 in lst}")

# len() - get length
print(f"Length: {len(lst)}")


# ============================================
# 6. SORTING AND REVERSING
# ============================================

print("\n" + "=" * 60)
print("6. SORTING AND REVERSING")
print("=" * 60)

lst = [5, 2, 8, 1, 9, 3, 7]
print(f"Original: {lst}")

# sort() - modifies original (ascending)
lst.sort()
print(f"After sort(): {lst}")

# sort(reverse=True) - descending
lst.sort(reverse=True)
print(f"After sort(reverse=True): {lst}")

# sorted() - returns new sorted list (original unchanged)
new_lst = sorted([5, 2, 8, 1, 9])
print(f"sorted([5, 2, 8, 1, 9]): {new_lst}")

# reverse() - modifies original
lst.reverse()
print(f"After reverse(): {lst}")


# ============================================
# 7. LIST COMPREHENSION (IMPORTANT!)
# ============================================

print("\n" + "=" * 60)
print("7. LIST COMPREHENSION")
print("=" * 60)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original: {numbers}")

# Square all elements
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")

# Filter even numbers
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")

# Square only even numbers
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Square of evens: {even_squares}")

# Nested list comprehension
matrix = [[j for j in range(3)] for i in range(3)]
print(f"3x3 matrix: {matrix}")


# ============================================
# 8. COPYING LISTS (IMPORTANT!)
# ============================================

print("\n" + "=" * 60)
print("8. COPYING LISTS")
print("=" * 60)

original = [1, 2, 3]
print(f"Original: {original}")

# Method 1: copy() - SHALLOW copy
copy1 = original.copy()
copy1.append(4)
print(f"Original after copy1 modification: {original}")
print(f"Copy1: {copy1}")

# Method 2: slicing
copy2 = original[:]

# Method 3: list() constructor
copy3 = list(original)

# ⚠️ WRONG way (this is a reference, not a copy!)
copy_wrong = original
copy_wrong.append(5)
print(f"Original after wrong copy modification: {original}")  # Original changed!


# ============================================
# 9. 2D LISTS (MATRICES)
# ============================================

print("\n" + "=" * 60)
print("9. 2D LISTS (MATRICES)")
print("=" * 60)

# Create a 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

# Access elements
print(f"\nElement at [0][0]: {matrix[0][0]}")
print(f"Element at [1][2]: {matrix[1][2]}")

# Sum of all elements
total = 0
for row in matrix:
    for element in row:
        total += element
print(f"Sum of all elements: {total}")

# Row sums
row_sums = []
for row in matrix:
    row_sums.append(sum(row))
print(f"Row sums: {row_sums}")

# Column sums
col_sums = [0] * len(matrix[0])
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        col_sums[j] += matrix[i][j]
print(f"Column sums: {col_sums}")

# Diagonal sum (main diagonal)
diag_sum = 0
for i in range(len(matrix)):
    diag_sum += matrix[i][i]
print(f"Diagonal sum: {diag_sum}")


# ============================================
# 10. PRACTICE PROBLEMS
# ============================================

print("\n" + "=" * 60)
print("10. PRACTICE PROBLEMS")
print("=" * 60)

print("Try these yourself:")
print("1. Write a function to remove duplicates from a list")
print("2. Write a function to find the second largest element")
print("3. Write a function to rotate a list by k positions")

# Solutions

def remove_duplicates(lst):
    """Remove duplicates while preserving order"""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def second_largest(lst):
    """Find second largest element"""
    if len(lst) < 2:
        return None
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None

def rotate_list(lst, k):
    """Rotate list to the right by k positions"""
    if not lst:
        return []
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

print("\n✅ Practice Solutions:")
test_list = [1, 2, 2, 3, 4, 4, 5]
print(f"Original: {test_list}")
print(f"Remove duplicates: {remove_duplicates(test_list)}")

test_list2 = [3, 7, 1, 9, 5]
print(f"Second largest in {test_list2}: {second_largest(test_list2)}")

test_list3 = [1, 2, 3, 4, 5]
print(f"Rotate {test_list3} by 2: {rotate_list(test_list3, 2)}")


# ============================================
# RUN ALL TESTS
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ ALL TESTS COMPLETED")
    print("=" * 60)