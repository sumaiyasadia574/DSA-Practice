#Python Conditionals Review
"""
Topic: Python Conditionals (if, elif, else)
File: 01_conditionals.py
Description: Complete review of conditional statements for CSC203
Author: Sumaiya Sadia
"""

# ============================================
# 1. BASIC IF-ELSE
# ============================================

def check_number(num):
    """Check if number is positive, negative, or zero"""
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print("=" * 50)
print("1. BASIC IF-ELSE")
print("=" * 50)
print(f"5 is {check_number(5)}")
print(f"-3 is {check_number(-3)}")
print(f"0 is {check_number(0)}")


# ============================================
# 2. GRADE CALCULATOR (IF-ELIF-ELSE)
# ============================================

def get_grade(marks):
    """Calculate grade based on marks"""
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "A-"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

print("\n" + "=" * 50)
print("2. GRADE CALCULATOR")
print("=" * 50)
print(f"85 marks → Grade: {get_grade(85)}")
print(f"65 marks → Grade: {get_grade(65)}")
print(f"45 marks → Grade: {get_grade(45)}")
print(f"35 marks → Grade: {get_grade(35)}")


# ============================================
# 3. NESTED CONDITIONALS
# ============================================

def analyze_number(num):
    """Check if number is even/odd AND positive/negative"""
    if num > 0:
        if num % 2 == 0:
            return "Positive Even"
        else:
            return "Positive Odd"
    elif num < 0:
        if num % 2 == 0:
            return "Negative Even"
        else:
            return "Negative Odd"
    else:
        return "Zero"

print("\n" + "=" * 50)
print("3. NESTED CONDITIONALS")
print("=" * 50)
print(f"4 is {analyze_number(4)}")
print(f"7 is {analyze_number(7)}")
print(f"-6 is {analyze_number(-6)}")
print(f"-9 is {analyze_number(-9)}")


# ============================================
# 4. MULTIPLE CONDITIONS (AND / OR)
# ============================================

def is_eligible_for_scholarship(gpa, attendance, has_backlog):
    """Check scholarship eligibility using multiple conditions"""
    # Must have GPA >= 3.5 AND attendance >= 80% AND no backlogs
    if gpa >= 3.5 and attendance >= 80 and not has_backlog:
        return "Eligible for Scholarship"
    elif gpa >= 3.0 and attendance >= 75:
        return "Eligible for Partial Scholarship"
    else:
        return "Not Eligible"

print("\n" + "=" * 50)
print("4. MULTIPLE CONDITIONS (AND / OR)")
print("=" * 50)
print(f"GPA: 3.7, Att: 85%, No Backlog → {is_eligible_for_scholarship(3.7, 85, False)}")
print(f"GPA: 3.2, Att: 80%, No Backlog → {is_eligible_for_scholarship(3.2, 80, False)}")
print(f"GPA: 3.8, Att: 70%, No Backlog → {is_eligible_for_scholarship(3.8, 70, False)}")


# ============================================
# 5. LEAP YEAR CHECKER (Complex Conditions)
# ============================================

def is_leap_year(year):
    """Check if a year is a leap year"""
    # Divisible by 4, but if divisible by 100, must also be divisible by 400
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

print("\n" + "=" * 50)
print("5. LEAP YEAR CHECKER")
print("=" * 50)
print(f"2024 is leap year? {is_leap_year(2024)}")
print(f"2025 is leap year? {is_leap_year(2025)}")
print(f"2000 is leap year? {is_leap_year(2000)}")
print(f"1900 is leap year? {is_leap_year(1900)}")


# ============================================
# 6. MENU-DRIVEN SYSTEM (MULTIPLE ELIF)
# ============================================

def calculator_menu():
    """Simple menu-driven calculator"""
    print("\n" + "=" * 50)
    print("CALCULATOR MENU")
    print("=" * 50)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(f"Result: {a + b}")
    elif choice == '2':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(f"Result: {a - b}")
    elif choice == '3':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(f"Result: {a * b}")
    elif choice == '4':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b == 0:
            print("❌ Error: Cannot divide by zero!")
        else:
            print(f"Result: {a / b}")
    elif choice == '5':
        print("👋 Goodbye!")
    else:
        print("❌ Invalid choice!")

# Uncomment to test the menu
# calculator_menu()


# ============================================
# 7. CONDITIONAL EXPRESSIONS (TERNARY)
# ============================================

def max_of_two(a, b):
    """Return maximum using ternary operator"""
    return a if a > b else b

print("\n" + "=" * 50)
print("6. TERNARY OPERATOR")
print("=" * 50)
print(f"Max of 10 and 20: {max_of_two(10, 20)}")
print(f"Max of 30 and 25: {max_of_two(30, 25)}")


# ============================================
# 8. PRACTICE PROBLEMS
# ============================================

print("\n" + "=" * 50)
print("8. PRACTICE PROBLEMS")
print("=" * 50)
print("Try these yourself:")
print("1. Write a function that checks if a number is divisible by 3 and 5")
print("2. Write a function that returns the largest of three numbers")
print("3. Write a function that checks if a character is a vowel")

# Solutions
def divisible_by_3_and_5(num):
    if num % 3 == 0 and num % 5 == 0:
        return True
    else:
        return False

def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def is_vowel(char):
    vowels = "aeiouAEIOU"
    if char in vowels:
        return True
    else:
        return False

print("\n✅ Practice Solutions:")
print(f"15 divisible by 3 and 5? {divisible_by_3_and_5(15)}")
print(f"7 divisible by 3 and 5? {divisible_by_3_and_5(7)}")
print(f"Largest of 5, 10, 7: {largest_of_three(5, 10, 7)}")
print(f"'a' is vowel? {is_vowel('a')}")
print(f"'b' is vowel? {is_vowel('b')}")


# ============================================
# RUN ALL TESTS
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("✅ ALL TESTS COMPLETED")
    print("=" * 50)