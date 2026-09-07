"""
Topic: Python Functions
File: 02_functions.py
Description: Complete review of Python functions
Course: CSC203 Data Structures
Author: Sumaiya Sadia
"""

# ============================================
# 1. BASIC FUNCTIONS
# ============================================

def greet(name):
    """Simple greeting function"""
    return f"Hello, {name}!"

def add(a, b):
    """Add two numbers"""
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

# Test
print("=" * 50)
print("1. BASIC FUNCTIONS")
print("=" * 50)
print(greet("Sadia"))
print(f"5 + 3 = {add(5, 3)}")
print(f"5 × 3 = {multiply(5, 3)}")


# ============================================
# 2. FUNCTIONS WITH DEFAULT PARAMETERS
# ============================================

def power(base, exponent=2):
    """Calculate power with default exponent 2"""
    return base ** exponent

# Test
print("\n" + "=" * 50)
print("2. DEFAULT PARAMETERS")
print("=" * 50)
print(f"3^2 = {power(3)}")      # 9 (default exponent 2)
print(f"3^4 = {power(3, 4)}")   # 81


# ============================================
# 3. FUNCTIONS WITH VARIABLE ARGUMENTS (*args)
# ============================================

def sum_all(*args):
    """Sum any number of arguments"""
    total = 0
    for num in args:
        total += num
    return total

# Test
print("\n" + "=" * 50)
print("3. VARIABLE ARGUMENTS (*args)")
print("=" * 50)
print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")


# ============================================
# 4. FUNCTIONS WITH KEYWORD ARGUMENTS (**kwargs)
# ============================================

def print_info(**kwargs):
    """Print keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Test
print("\n" + "=" * 50)
print("4. KEYWORD ARGUMENTS (**kwargs)")
print("=" * 50)
print_info(name="Sadia", age=21, course="CSC203")


# ============================================
# 5. FUNCTIONS RETURNING MULTIPLE VALUES
# ============================================

def get_min_max(numbers):
    """Return both minimum and maximum"""
    return min(numbers), max(numbers)

# Test
print("\n" + "=" * 50)
print("5. RETURNING MULTIPLE VALUES")
print("=" * 50)
min_val, max_val = get_min_max([3, 7, 2, 9, 5])
print(f"Min: {min_val}, Max: {max_val}")


# ============================================
# 6. FUNCTIONS WITH LISTS
# ============================================

def process_list(lst, operation="sum"):
    """Process a list with different operations"""
    if operation == "sum":
        return sum(lst)
    elif operation == "max":
        return max(lst)
    elif operation == "min":
        return min(lst)
    elif operation == "avg":
        return sum(lst) / len(lst)
    else:
        return "Invalid operation"

# Test
print("\n" + "=" * 50)
print("6. FUNCTIONS WITH LISTS")
print("=" * 50)
data = [1, 2, 3, 4, 5]
print(f"Sum: {process_list(data, 'sum')}")
print(f"Max: {process_list(data, 'max')}")
print(f"Avg: {process_list(data, 'avg')}")


# ============================================
# 7. PRACTICE PROBLEMS
# ============================================

print("\n" + "=" * 50)
print("7. PRACTICE PROBLEMS")
print("=" * 50)
print("Try these yourself:")
print("1. Write a function that checks if a number is prime")
print("2. Write a function that returns the factorial of a number")
print("3. Write a function that reverses a string")

# Example solutions
def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def factorial(num):
    """Calculate factorial"""
    if num == 0:
        return 1
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def reverse_string(s):
    """Reverse a string"""
    return s[::-1]

print("\n✅ Practice solutions:")
print(f"is_prime(7) = {is_prime(7)}")
print(f"factorial(5) = {factorial(5)}")
print(f"reverse_string('hello') = {reverse_string('hello')}")

# ============================================
# RUN ALL TESTS
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("✅ ALL TESTS COMPLETED")
    print("=" * 50)