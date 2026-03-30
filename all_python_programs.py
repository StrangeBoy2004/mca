# =============================================================================
#        ALL PYTHON PROGRAMS - COMPLETE LAB MANUAL
#        14 Topics Covered with Multiple Programs Each
# =============================================================================

# ===========================================================================
# TOPIC 1: Control Structures of Python
# ===========================================================================
print("\n" + "="*60)
print("TOPIC 1: CONTROL STRUCTURES")
print("="*60)

# --- 1a: if / elif / else ---
print("\n--- 1a: if/elif/else - Grade System ---")
marks = 72
if marks >= 90:
    print("Grade: A (Distinction)")
elif marks >= 75:
    print("Grade: B (First Class)")
elif marks >= 60:
    print("Grade: C (Second Class)")
elif marks >= 40:
    print("Grade: D (Pass)")
else:
    print("Grade: F (Fail)")

# --- 1b: for loop ---
print("\n--- 1b: for loop - Sum of numbers ---")
total = 0
for i in range(1, 11):
    total += i
print(f"Sum of 1 to 10 = {total}")

# --- 1c: while loop ---
print("\n--- 1c: while loop - Factorial ---")
n = 6
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(f"Factorial of {n} = {factorial}")

# --- 1d: break and continue ---
print("\n--- 1d: break and continue ---")
print("Even numbers (skip odd, stop at 10):")
for num in range(1, 20):
    if num == 10:
        break
    if num % 2 != 0:
        continue
    print(num, end=" ")
print()

# --- 1e: Nested loops - Multiplication table ---
print("\n--- 1e: Nested loops - Multiplication Table (3x5) ---")
for i in range(1, 4):
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()


# ===========================================================================
# TOPIC 2: Data Structures - List, Dictionary, Tuples
# ===========================================================================
print("\n" + "="*60)
print("TOPIC 2: LIST, DICTIONARY, TUPLES")
print("="*60)

# --- 2a: List operations ---
print("\n--- 2a: List Operations ---")
fruits = ["apple", "banana", "cherry", "mango"]
print("Original list:", fruits)
fruits.append("orange")
print("After append:", fruits)
fruits.remove("banana")
print("After remove:", fruits)
fruits.sort()
print("After sort:", fruits)
print("Slicing [1:3]:", fruits[1:3])

# --- 2b: List comprehension ---
print("\n--- 2b: List Comprehension ---")
squares = [x**2 for x in range(1, 11)]
print("Squares:", squares)
evens = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers:", evens)

# --- 2c: Dictionary operations ---
print("\n--- 2c: Dictionary Operations ---")
student = {
    "name": "Arjun",
    "age": 20,
    "marks": 85,
    "city": "Pune"
}
print("Student:", student)
student["email"] = "arjun@mail.com"  # add key
print("After adding email:", student)
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
for key, value in student.items():
    print(f"  {key}: {value}")

# --- 2d: Tuple operations ---
print("\n--- 2d: Tuple Operations ---")
coordinates = (10.5, 20.3, 30.1)
print("Tuple:", coordinates)
print("Length:", len(coordinates))
print("Max:", max(coordinates))
x, y, z = coordinates          # unpacking
print(f"Unpacked: x={x}, y={y}, z={z}")

# Tuple of tuples
students = (("Alice", 88), ("Bob", 92), ("Carol", 75))
print("\nStudent Scores:")
for name, score in students:
    print(f"  {name}: {score}")

# --- 2e: Nested structures ---
print("\n--- 2e: Nested Dictionary ---")
college = {
    "name": "ABC College",
    "departments": {
        "CS": {"students": 120, "hod": "Dr. Sharma"},
        "EC": {"students": 95,  "hod": "Dr. Patel"},
    }
}
for dept, info in college["departments"].items():
    print(f"  {dept} - HOD: {info['hod']}, Students: {info['students']}")


# ===========================================================================
# TOPIC 3: Functions - Scoping, Recursion, List Mutability
# ===========================================================================
print("\n" + "="*60)
print("TOPIC 3: FUNCTIONS, SCOPING, RECURSION, LIST MUTABILITY")
print("="*60)

# --- 3a: Basic function and scoping ---
print("\n--- 3a: Variable Scoping (Local vs Global) ---")
x = "global"

def show_scope():
    x = "local"
    print("Inside function:", x)

show_scope()
print("Outside function:", x)

# Global keyword
counter = 0
def increment():
    global counter
    counter += 1

increment()
increment()
print("Counter after 2 increments:", counter)

# --- 3b: Default and keyword arguments ---
print("\n--- 3b: Default and Keyword Arguments ---")
def greet(name, msg="Hello", punctuation="!"):
    print(f"{msg}, {name}{punctuation}")

greet("Priya")
greet("Rahul", msg="Good Morning")
greet("Sneha", msg="Hi", punctuation=".")

# --- 3c: *args and **kwargs ---
print("\n--- 3c: *args and **kwargs ---")
def total_marks(*args):
    return sum(args)

def student_info(**kwargs):
    for k, v in kwargs.items():
        print(f"  {k}: {v}")

print("Total marks:", total_marks(85, 90, 78, 92))
student_info(name="Vikram", roll=101, cgpa=8.5)

# --- 3d: Recursion ---
print("\n--- 3d: Recursion ---")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(f"Factorial(7) = {factorial(7)}")
fib_seq = [fibonacci(i) for i in range(10)]
print(f"Fibonacci(0-9) = {fib_seq}")
print(f"GCD(48, 18) = {gcd(48, 18)}")

# --- 3e: List mutability ---
print("\n--- 3e: List Mutability ---")
original = [1, 2, 3, 4, 5]

# Mutable - changes inside function affect original
def modify_list(lst):
    lst.append(99)
    lst[0] = 100

modify_list(original)
print("After modifying inside function:", original)

# Shallow copy vs deep copy
import copy
a = [[1, 2], [3, 4]]
b = copy.copy(a)       # shallow
c = copy.deepcopy(a)   # deep

a[0][0] = 999
print(f"Original: {a}")
print(f"Shallow copy: {b}")   # affected!
print(f"Deep copy: {c}")      # not affected


# ===========================================================================
# TOPIC 4: Object Oriented Programming (OOP)
# ===========================================================================
print("\n" + "="*60)
print("TOPIC 4: OBJECT ORIENTED PROGRAMMING")
print("="*60)

# --- 4a: Class and Object ---
print("\n--- 4a: Class and Object ---")
class BankAccount:
    bank_name = "Python Bank"   # class variable

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Balance: ₹{self.balance}")

    def __str__(self):
        return f"Account[{self.owner}] - ₹{self.balance}"

acc = BankAccount("Arjun", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc)

# --- 4b: Inheritance ---
print("\n--- 4b: Inheritance ---")
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

animals = [Dog("Bruno"), Cat("Whiskers"), Duck("Donald")]
for animal in animals:
    print(f"{animal} says: {animal.speak()}")

# --- 4c: Encapsulation ---
print("\n--- 4c: Encapsulation (Private attributes) ---")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary   # private

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary!")

emp = Employee("Meera", 50000)
print(f"{emp.name}'s salary: ₹{emp.get_salary()}")
emp.set_salary(60000)
print(f"Updated salary: ₹{emp.get_salary()}")

# --- 4d: Polymorphism ---
print("\n--- 4d: Polymorphism ---")
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        import math
        return round(math.pi * self.r**2, 2)

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h

class Triangle(Shape):
    def __init__(self, b, h):
        self.b, self.h = b, h
    def area(self):
        return 0.5 * self.b * self.h

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]
for s in shapes:
    print(f"{s.__class__.__name__}: area = {s.area()}")


# ===========================================================================
# TOPIC 5: Data Structure Algorithms - Searching, Sorting, Hash Tables
# ===========================================================================
print("\n" + "="*60)
print("TOPIC 5: DATA STRUCTURE ALGORITHMS")
print("="*60)

# --- 5a: Linear Search ---
print("\n--- 5a: Linear Search ---")
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

data = [64, 25, 12, 22, 11, 90, 45]
print("Array:", data)
idx = linear_search(data, 22)
print(f"Linear search for 22: found at index {idx}")

# --- 5b: Binary Search ---
print("\n--- 5b: Binary Search ---")
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

sorted_data = sorted(data)
print("Sorted:", sorted_data)
idx = binary_search(sorted_data, 45)
print(f"Binary search for 45: found at index {idx}")

# --- 5c: Bubble Sort ---
print("\n--- 5c: Bubble Sort ---")
def bubble_sort(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("Before:", arr)
print("After Bubble Sort:", bubble_sort(arr))

# --- 5d: Selection Sort ---
print("\n--- 5d: Selection Sort ---")
def selection_sort(arr):
    arr = arr[:]
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print("After Selection Sort:", selection_sort(arr))

# --- 5e: Insertion Sort ---
print("\n--- 5e: Insertion Sort ---")
def insertion_sort(arr):
    arr = arr[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print("After Insertion Sort:", insertion_sort(arr))

# --- 5f: Hash Table using dictionary ---
print("\n--- 5f: Hash Table (Dictionary-based) ---")
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        for item in self.table[idx]:
            if item[0] == key:
                item[1] = value
                return
        self.table[idx].append([key, value])

    def get(self, key):
        idx = self._hash(key)
        for item in self.table[idx]:
            if item[0] == key:
                return item[1]
        return None

ht = HashTable()
ht.insert("name", "Alice")
ht.insert("age", 25)
ht.insert("city", "Mumbai")
print("name ->", ht.get("name"))
print("age  ->", ht.get("age"))
print("city ->", ht.get("city"))


# ===========================================================================
# TOPIC 6: Regular Expressions
# ===========================================================================
print("\n" + "="*60)
print("TOPIC 6: REGULAR EXPRESSIONS")
print("="*60)

import re

# --- 6a: Basic matching ---
print("\n--- 6a: Basic Matching ---")
text = "The price is ₹250 and ₹1500 for two items."
numbers = re.findall(r'\d+', text)
print("Numbers found:", numbers)

# --- 6b: Email validation ---
print("\n--- 6b: Email Validation ---")
emails = ["user@example.com", "bad-email@", "hello.world@domain.org", "test@.com"]
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
for email in emails:
    status = "Valid" if re.match(pattern, email) else "Invalid"
    print(f"  {email:30} -> {status}")

# --- 6c: Phone number extraction ---
print("\n--- 6c: Phone Number Extraction ---")
text2 = "Call us at 9876543210 or +91-9123456789 for support."
phones = re.findall(r'[\+\d][\d\-]{9,}', text2)
print("Phone numbers:", phones)

# --- 6d: search, sub, split ---
print("\n--- 6d: re.search, re.sub, re.split ---")
sentence = "Python is awesome. Python is powerful. Python is fun."
match = re.search(r'Python is (\w+)', sentence)
print("First match:", match.group(1))

cleaned = re.sub(r'Python', 'Java', sentence, count=2)
print("After sub:", cleaned)

parts = re.split(r'[.!?]\s*', "Hello! How are you? I am fine.")
print("Split:", [p for p in parts if p])

# --- 6e: Groups and flags ---
print("\n--- 6e: Groups and Flags ---")
date_text = "Today is 2024-07-15 and tomorrow is 2024-07-16"
dates = re.findall(r'(\d{4})-(\d{2})-(\d{2})', date_text)
for y, m, d in dates:
    print(f"  Year: {y}, Month: {m}, Day: {d}")


# ===========================================================================
# TOPIC 7: Exception Handling
# ===========================================================================
print("\n" + "="*60)
print("TOPIC 7: EXCEPTION HANDLING")
print("="*60)

# --- 7a: try/except/else ---
print("\n--- 7a: try/except/else ---")
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("  Error: Cannot divide by zero!")
        return None
    else:
        print(f"  {a} / {b} = {result}")
        return result

safe_divide(10, 2)
safe_divide(5, 0)

# --- 7b: try/except/finally ---
print("\n--- 7b: try/except/finally ---")
def read_file_demo(filename):
    try:
        f = open(filename, 'r')
        content = f.read()
        print("  File read successfully")
    except FileNotFoundError:
        print(f"  Error: '{filename}' not found!")
    finally:
        print("  Finally block always runs (cleanup here)")

read_file_demo("nonexistent.txt")

# --- 7c: raise Statement ---
print("\n--- 7c: raise Statement ---")
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0 or age > 150:
        raise ValueError(f"Age {age} is out of valid range (0-150)")
    return age

for test_age in [25, -5, 200, "old"]:
    try:
        result = set_age(test_age)
        print(f"  Age set to: {result}")
    except (ValueError, TypeError) as e:
        print(f"  Error for {test_age!r}: {e}")

# --- 7d: assert Statement ---
print("\n--- 7d: assert Statement ---")
def calculate_sqrt(n):
    assert n >= 0, f"Cannot compute sqrt of negative number: {n}"
    return n ** 0.5

try:
    print(f"  sqrt(16) = {calculate_sqrt(16)}")
    print(f"  sqrt(-1) = {calculate_sqrt(-1)}")
except AssertionError as e:
    print(f"  AssertionError: {e}")

# --- 7e: Catch multiple specific exceptions ---
print("\n--- 7e: Multiple Specific Exceptions ---")
def risky_operation(data, idx):
    try:
        value = int(data[idx])
        result = 100 / value
        print(f"  Result: {result:.2f}")
    except IndexError:
        print("  Error: Index out of range!")
    except ValueError:
        print("  Error: Cannot convert to integer!")
    except ZeroDivisionError:
        print("  Error: Division by zero!")
    except Exception as e:
        print(f"  Unexpected error: {e}")

test_data = ["5", "0", "abc", "10"]
for i in [0, 1, 2, 3, 9]:
    print(f"  Testing index {i}:", end=" ")
    risky_operation(test_data, i)


# ===========================================================================
# TOPIC 8: String-Based, Class-Based Exceptions & Nesting
# ===========================================================================
print("\n" + "="*60)
print("TOPIC 8: STRING, CLASS-BASED EXCEPTIONS & NESTING")
print("="*60)

# --- 8a: Class-Based Custom Exceptions ---
print("\n--- 8a: Class-Based Custom Exceptions ---")
class AppError(Exception):
    """Base exception for application"""
    pass

class InsufficientFundsError(AppError):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Need ₹{amount}, but only ₹{balance} available")

class InvalidAgeError(AppError):
    def __init__(self, age):
        super().__init__(f"Age {age} is invalid (must be 1-120)")
        self.age = age

class NetworkError(AppError):
    pass

def withdraw_funds(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_bal = withdraw_funds(500, 1000)
except InsufficientFundsError as e:
    print(f"  Custom Error: {e}")
    print(f"  Short by: ₹{e.amount - e.balance}")

# --- 8b: Exception hierarchy with class-based ---
print("\n--- 8b: Exception Hierarchy ---")
def validate_user(name, age):
    if not name:
        raise AppError("Name cannot be empty")
    if not isinstance(age, int) or age < 1 or age > 120:
        raise InvalidAgeError(age)

for name, age in [("Alice", 25), ("", 20), ("Bob", -5)]:
    try:
        validate_user(name, age)
        print(f"  Valid: {name}, {age}")
    except InvalidAgeError as e:
        print(f"  InvalidAgeError: {e}")
    except AppError as e:
        print(f"  AppError: {e}")

# --- 8c: Nested Exception Handlers ---
print("\n--- 8c: Nested Exception Handlers ---")
def complex_operation(data):
    try:
        print("  Outer try: Processing data...")
        try:
            value = int(data)
            if value < 0:
                raise ValueError("Negative not allowed")
            print(f"  Inner try: Processed value = {value}")
        except ValueError as e:
            print(f"  Inner except: {e}")
            raise AppError("Inner error escalated to outer") from e
    except AppError as e:
        print(f"  Outer except: {e}")
    finally:
        print("  Outer finally: Cleanup done")

complex_operation("42")
print()
complex_operation("-5")


# ===========================================================================
# TOPIC 9: Anonymous Functions (Lambda)
# ===========================================================================
print("\n" + "="*60)
print("TOPIC 9: ANONYMOUS FUNCTIONS (LAMBDA)")
print("="*60)

# --- 9a: Basic lambda ---
print("\n--- 9a: Basic Lambda ---")
square = lambda x: x ** 2
add = lambda a, b: a + b
greet = lambda name: f"Hello, {name}!"

print("square(7):", square(7))
print("add(3, 4):", add(3, 4))
print(greet("Python"))

# --- 9b: Lambda with sorted ---
print("\n--- 9b: Lambda with sorted() ---")
students = [
    {"name": "Arjun",  "marks": 85},
    {"name": "Priya",  "marks": 92},
    {"name": "Rahul",  "marks": 78},
    {"name": "Sneha",  "marks": 95},
]
by_marks = sorted(students, key=lambda s: s["marks"], reverse=True)
print("Sorted by marks:")
for s in by_marks:
    print(f"  {s['name']:10} {s['marks']}")

# --- 9c: Lambda with map, filter ---
print("\n--- 9c: Lambda with map() and filter() ---")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cubes = list(map(lambda x: x**3, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Cubes:", cubes)
print("Evens:", evens)

# --- 9d: Immediately Invoked Lambda ---
print("\n--- 9d: Immediately Invoked Lambda ---")
result = (lambda x, y: x * y)(6, 7)
print("6 × 7 =", result)

# Conditional lambda
classify = lambda n: "even" if n % 2 == 0 else "odd"
for n in [3, 8, 15, 22]:
    print(f"  {n} is {classify(n)}")


# ===========================================================================
# TOPIC 10: Functional Programming - filter and reduce
# ===========================================================================
print("\n" + "="*60)
print("TOPIC 10: FUNCTIONAL PROGRAMMING - filter & reduce")
print("="*60)

from functools import reduce

# --- 10a: filter() ---
print("\n--- 10a: filter() ---")
numbers = list(range(1, 21))
primes = list(filter(lambda n: all(n % i != 0 for i in range(2, n)) and n > 1, numbers))
print("Prime numbers (1-20):", primes)

words = ["apple", "Banana", "cherry", "Date", "elderberry"]
capitalized = list(filter(lambda w: w[0].isupper(), words))
print("Capitalized words:", capitalized)

# --- 10b: reduce() ---
print("\n--- 10b: reduce() ---")
nums = [1, 2, 3, 4, 5]
product = reduce(lambda a, b: a * b, nums)
maximum = reduce(lambda a, b: a if a > b else b, [3, 7, 2, 9, 1])
total = reduce(lambda a, b: a + b, nums)
print(f"Product of {nums} = {product}")
print(f"Maximum of [3,7,2,9,1] = {maximum}")
print(f"Sum of {nums} = {total}")

# --- 10c: map() ---
print("\n--- 10c: map() ---")
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("Celsius:    ", celsius)
print("Fahrenheit: ", fahrenheit)

# --- 10d: Combining map, filter, reduce ---
print("\n--- 10d: Combining map + filter + reduce ---")
data = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
positive_squares_sum = reduce(
    lambda a, b: a + b,
    map(lambda x: x**2, filter(lambda x: x > 0, data))
)
print("Sum of squares of positive numbers:", positive_squares_sum)


# ===========================================================================
# TOPIC 11: Module Creation and Usage
# ===========================================================================
print("\n" + "="*60)
print("TOPIC 11: MODULE CREATION AND USAGE")
print("="*60)

# --- 11a: Creating a module inline (simulated) ---
print("\n--- 11a: Module simulation (functions as module) ---")

# Simulated mymath module
class mymath:
    PI = 3.14159265358979

    @staticmethod
    def circle_area(r):
        return mymath.PI * r * r

    @staticmethod
    def circle_perimeter(r):
        return 2 * mymath.PI * r

    @staticmethod
    def power(base, exp):
        return base ** exp

    @staticmethod
    def is_perfect(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n

print(f"Circle area (r=5): {mymath.circle_area(5):.2f}")
print(f"Circle perimeter (r=5): {mymath.circle_perimeter(5):.2f}")
print(f"2^10 = {mymath.power(2, 10)}")
perfect_nums = [n for n in range(1, 500) if mymath.is_perfect(n)]
print(f"Perfect numbers (1-500): {perfect_nums}")

# --- 11b: Using standard library modules ---
print("\n--- 11b: Standard Library Modules ---")
import math
import random
import datetime
import os

print(f"math.sqrt(144) = {math.sqrt(144)}")
print(f"math.log(100, 10) = {math.log(100, 10)}")
print(f"math.gcd(48, 18) = {math.gcd(48, 18)}")

random.seed(42)
print(f"random.randint(1,100) = {random.randint(1, 100)}")
sample = random.sample(range(50), 5)
print(f"random.sample(0-50, 5) = {sample}")

now = datetime.datetime.now()
print(f"Current datetime: {now.strftime('%Y-%m-%d %H:%M:%S')}")

print(f"Current directory: {os.getcwd()}")
print(f"Platform: {os.name}")

# --- 11c: collections module ---
print("\n--- 11c: collections module ---")
from collections import Counter, defaultdict, OrderedDict, deque

text = "hello world hello python world hello"
word_count = Counter(text.split())
print("Word count:", dict(word_count))
print("Most common:", word_count.most_common(2))

# defaultdict
scores = defaultdict(list)
for student, subj, score in [("Alice","Maths",85),("Bob","Maths",90),
                               ("Alice","Science",78),("Bob","Science",88)]:
    scores[student].append((subj, score))

for student, subj_scores in scores.items():
    avg = sum(s for _, s in subj_scores) / len(subj_scores)
    print(f"  {student}: avg = {avg:.1f}")

# deque
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print("Deque:", list(dq))


# ===========================================================================
# TOPIC 12: Image Insertion in Python
# ===========================================================================
print("\n" + "="*60)
print("TOPIC 12: IMAGE INSERTION IN PYTHON")
print("="*60)

# --- 12a: Using PIL/Pillow ---
print("\n--- 12a: PIL/Pillow Image Operations ---")
try:
    from PIL import Image, ImageDraw, ImageFont
    import io

    # Create a sample image programmatically
    img = Image.new('RGB', (300, 200), color=(70, 130, 180))  # steel blue
    draw = ImageDraw.Draw(img)

    # Draw shapes
    draw.rectangle([20, 20, 280, 180], outline=(255, 255, 255), width=3)
    draw.ellipse([100, 60, 200, 140], fill=(255, 215, 0))  # gold circle
    draw.text((90, 10), "Hello Python!", fill=(255, 255, 255))

    # Save the image
    img.save("sample_output.png")
    print("  Image created and saved as 'sample_output.png'")

    # Open and get info
    img2 = Image.open("sample_output.png")
    print(f"  Image size: {img2.size}")
    print(f"  Image mode: {img2.mode}")
    print(f"  Image format: {img2.format}")

    # Convert to grayscale
    gray = img2.convert('L')
    gray.save("sample_gray.png")
    print("  Grayscale image saved as 'sample_gray.png'")

    # Resize
    resized = img2.resize((150, 100))
    resized.save("sample_resized.png")
    print("  Resized image saved as 'sample_resized.png'")

    # Rotate
    rotated = img2.rotate(45)
    rotated.save("sample_rotated.png")
    print("  Rotated image saved as 'sample_rotated.png'")

    # Cleanup
    import os
    for f in ["sample_output.png","sample_gray.png","sample_resized.png","sample_rotated.png"]:
        if os.path.exists(f):
            os.remove(f)
    print("  (Demo files cleaned up)")

except ImportError:
    print("  Pillow not installed. Install with: pip install Pillow")
    print("  Demo code structure:")
    print("""
    from PIL import Image, ImageDraw

    # Create image
    img = Image.new('RGB', (300, 200), color=(70, 130, 180))
    draw = ImageDraw.Draw(img)
    draw.text((90, 10), "Hello!", fill=(255,255,255))
    img.save("output.png")

    # Open & process
    img = Image.open("photo.jpg")
    gray = img.convert('L')       # Grayscale
    resized = img.resize((100,100))
    rotated = img.rotate(90)
    img.show()                    # Display
    """)

# --- 12b: Using matplotlib for image display ---
print("\n--- 12b: Matplotlib Image Display ---")
try:
    import matplotlib
    matplotlib.use('Agg')  # non-interactive backend
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import numpy as np

    fig, axes = plt.subplots(1, 3, figsize=(12, 4))

    # Random noise image
    noise = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    axes[0].imshow(noise)
    axes[0].set_title("Random Noise")
    axes[0].axis('off')

    # Gradient image
    gradient = np.linspace(0, 1, 100).reshape(1, -1)
    gradient = np.repeat(gradient, 100, axis=0)
    axes[1].imshow(gradient, cmap='viridis')
    axes[1].set_title("Gradient")
    axes[1].axis('off')

    # Concentric circles
    y, x = np.ogrid[-50:50, -50:50]
    circle_img = np.sqrt(x**2 + y**2)
    axes[2].imshow(circle_img, cmap='plasma')
    axes[2].set_title("Concentric Circles")
    axes[2].axis('off')

    plt.savefig("image_demo.png", bbox_inches='tight', dpi=80)
    plt.close()
    print("  Matplotlib image demo saved as 'image_demo.png'")
    if os.path.exists("image_demo.png"):
        os.remove("image_demo.png")

except ImportError:
    print("  matplotlib/numpy not installed. Install with: pip install matplotlib numpy")


# ===========================================================================
# TOPIC 13: DataFrame and CSV Files
# ===========================================================================
print("\n" + "="*60)
print("TOPIC 13: DATAFRAME AND CSV FILES")
print("="*60)

import csv
import os

# --- 13a: Writing and reading CSV with csv module ---
print("\n--- 13a: CSV with csv module ---")
csv_file = "students.csv"

# Write CSV
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "Marks", "City"])
    writer.writerows([
        ["Arjun",   20, 85, "Mumbai"],
        ["Priya",   21, 92, "Delhi"],
        ["Rahul",   20, 78, "Pune"],
        ["Sneha",   22, 95, "Chennai"],
        ["Vikram",  21, 67, "Bangalore"],
    ])

print(f"  CSV written: {csv_file}")

# Read CSV
with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    print("  Reading CSV:")
    for row in reader:
        print(f"    {row['Name']:10} | Age: {row['Age']} | Marks: {row['Marks']} | {row['City']}")

# --- 13b: Using pandas ---
print("\n--- 13b: Pandas DataFrame ---")
try:
    import pandas as pd

    # Create DataFrame
    df = pd.read_csv(csv_file)
    print("\n  DataFrame:")
    print(df.to_string(index=False))

    print("\n  Basic Info:")
    print(f"  Shape: {df.shape}")
    print(f"  Columns: {list(df.columns)}")
    print(f"\n  Descriptive Statistics:")
    print(df[['Age','Marks']].describe().to_string())

    print("\n  Filtering (Marks > 80):")
    print(df[df['Marks'] > 80][['Name', 'Marks']].to_string(index=False))

    print("\n  Grouping by City:")
    print(df.groupby('City')['Marks'].mean().to_string())

    # Add a new column
    df['Grade'] = df['Marks'].apply(
        lambda m: 'A' if m >= 90 else ('B' if m >= 75 else 'C'))
    print("\n  With Grade column:")
    print(df.to_string(index=False))

    # Save modified CSV
    df.to_csv("students_with_grades.csv", index=False)
    print("\n  Saved 'students_with_grades.csv'")

    # Cleanup
    for f in ["students_with_grades.csv"]:
        if os.path.exists(f):
            os.remove(f)

except ImportError:
    print("  pandas not installed. Install with: pip install pandas")
    print("  Basic csv operations above still work without pandas.")

# Cleanup csv
if os.path.exists(csv_file):
    os.remove(csv_file)

# --- 13c: csv.DictWriter ---
print("\n--- 13c: csv.DictWriter ---")
products_file = "products.csv"
products = [
    {"id": 1, "product": "Laptop",  "price": 55000, "qty": 10},
    {"id": 2, "product": "Mouse",   "price":   500, "qty": 50},
    {"id": 3, "product": "Keyboard","price":   800, "qty": 30},
]
with open(products_file, 'w', newline='') as f:
    fieldnames = ["id", "product", "price", "qty"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products)

print(f"  Products CSV written.")
with open(products_file) as f:
    print(f.read())

if os.path.exists(products_file):
    os.remove(products_file)


# ===========================================================================
# TOPIC 14: GUI Programming using Tkinter
# ===========================================================================
print("\n" + "="*60)
print("TOPIC 14: GUI PROGRAMMING USING TKINTER")
print("="*60)

print("""
NOTE: Tkinter requires a display (screen). The code below is ready to run
in any environment with a GUI. Run it directly on your machine.

--- 14a: Basic Window ---

    import tkinter as tk

    root = tk.Tk()
    root.title("My First GUI")
    root.geometry("300x200")
    label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
    label.pack(pady=20)
    button = tk.Button(root, text="Click Me",
                       command=lambda: label.config(text="Button Clicked!"))
    button.pack()
    root.mainloop()

--- 14b: Calculator App ---
""")

# Full Tkinter Calculator (runnable code)
TKINTER_CALCULATOR = '''
import tkinter as tk

class Calculator:
    def __init__(self, root):
        root.title("Python Calculator")
        root.geometry("320x420")
        root.configure(bg="#1e1e2e")
        root.resizable(False, False)

        self.expression = ""
        self.display_var = tk.StringVar(value="0")

        # Display
        display = tk.Entry(root, textvariable=self.display_var,
                           font=("Consolas", 24), justify="right",
                           bg="#313244", fg="#cdd6f4",
                           insertbackground="#cdd6f4",
                           relief="flat", bd=10)
        display.pack(fill="x", padx=10, pady=(15, 5))

        # Buttons layout
        buttons = [
            ["C", "±", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "−"],
            ["1", "2", "3", "+"],
            ["0", ".", "⌫", "="],
        ]

        btn_frame = tk.Frame(root, bg="#1e1e2e")
        btn_frame.pack(fill="both", expand=True, padx=10, pady=10)

        for r, row in enumerate(buttons):
            for c, btn_text in enumerate(row):
                if btn_text in "=":
                    bg, fg = "#89b4fa", "#1e1e2e"
                elif btn_text in "÷×−+":
                    bg, fg = "#fab387", "#1e1e2e"
                elif btn_text in "C±%":
                    bg, fg = "#45475a", "#cdd6f4"
                else:
                    bg, fg = "#313244", "#cdd6f4"

                btn = tk.Button(btn_frame, text=btn_text,
                                font=("Consolas", 16, "bold"),
                                bg=bg, fg=fg, relief="flat",
                                activebackground="#585b70",
                                cursor="hand2", bd=0,
                                command=lambda t=btn_text: self.on_click(t))
                btn.grid(row=r, column=c, padx=3, pady=3,
                         sticky="nsew", ipadx=5, ipady=10)
                btn_frame.rowconfigure(r, weight=1)
                btn_frame.columnconfigure(c, weight=1)

    def on_click(self, text):
        if text == "C":
            self.expression = ""
            self.display_var.set("0")
        elif text == "⌫":
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression or "0")
        elif text == "=":
            try:
                expr = (self.expression.replace("÷", "/")
                        .replace("×", "*").replace("−", "-"))
                result = eval(expr)
                self.display_var.set(result)
                self.expression = str(result)
            except:
                self.display_var.set("Error")
                self.expression = ""
        elif text == "±":
            try:
                val = float(self.expression)
                self.expression = str(-val)
                self.display_var.set(self.expression)
            except:
                pass
        elif text == "%":
            try:
                val = float(self.expression)
                self.expression = str(val / 100)
                self.display_var.set(self.expression)
            except:
                pass
        else:
            self.expression += text
            self.display_var.set(self.expression)

root = tk.Tk()
Calculator(root)
root.mainloop()
'''

print("Calculator source code (copy and run separately):")
print(TKINTER_CALCULATOR)

print("""
--- 14c: Student Registration Form ---

    import tkinter as tk
    from tkinter import ttk, messagebox

    def submit():
        name = name_var.get()
        age  = age_var.get()
        city = city_var.get()
        if not name:
            messagebox.showwarning("Warning", "Name is required!")
            return
        messagebox.showinfo("Submitted",
            f"Name: {name}\\nAge: {age}\\nCity: {city}")

    root = tk.Tk()
    root.title("Student Registration")
    root.geometry("350x250")

    name_var = tk.StringVar()
    age_var  = tk.IntVar()
    city_var = tk.StringVar()

    tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=8)
    tk.Entry(root, textvariable=name_var).grid(row=0, column=1)

    tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=8)
    tk.Spinbox(root, from_=1, to=100, textvariable=age_var).grid(row=1, column=1)

    tk.Label(root, text="City:").grid(row=2, column=0, padx=10, pady=8)
    ttk.Combobox(root, textvariable=city_var,
        values=["Mumbai","Delhi","Pune","Chennai"]).grid(row=2, column=1)

    tk.Button(root, text="Submit", command=submit,
              bg="green", fg="white").grid(row=3, columnspan=2, pady=15)

    root.mainloop()
""")

# ===========================================================================
print("\n" + "="*60)
print("  ALL 14 TOPICS COMPLETED SUCCESSFULLY")
print("="*60 + "\n")
