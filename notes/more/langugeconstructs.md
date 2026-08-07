## **1. Python Basics**

* Python is **interpreted, high-level, dynamically typed**.
* File extension: `.py`
* Run: `python filename.py`

```python
print("Hello, World!")  # Print to console
```


## **2. Variables & Data Types**

* **Numbers**: `int`, `float`, `complex`
* **Boolean**: `True` / `False`
* **String**: `"text"` or `'text'`
* **List**: `[1, 2, 3]`
* **Tuple**: `(1, 2, 3)`
* **Set**: `{1, 2, 3}`
* **Dictionary**: `{"key": "value"}`

```python
x = 10          # int
y = 3.14        # float
name = "Ravi"   # string
flag = True     # boolean
```


## **3. Type Conversion**

```python
int("10")     # str → int
float(5)      # int → float
str(123)      # int → str
```


## **4. Operators**

* **Arithmetic:** `+ - * / % ** //`
* **Comparison:** `== != > < >= <=`
* **Logical:** `and or not`
* **Assignment:** `= += -= *= /=`
* **Membership:** `in`, `not in`

```python
a, b = 5, 2
print(a + b, a ** b)  # 7, 25
print(a > b and b < 10)  # True
```

## **5. Control Flow**

### **If-Else**

```python
age = 20
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### **For Loop**

```python
for i in range(5):  # 0,1,2,3,4
    print(i)
```

### **While Loop**

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### **Break & Continue**

```python
for i in range(5):
    if i == 3:
        break   # exit loop
    print(i)
```


## **6. Functions**

```python
def greet(name):
    return f"Hello, {name}"

print(greet("Ravi"))
```

* **Default Arguments:**

```python
def add(a, b=5):
    return a + b
```

* **Keyword Arguments:** `add(b=10, a=3)`

* **Variable-length arguments:**

```python
def total(*nums):  # tuple
    return sum(nums)
```


## **7. Lists, Tuples, Sets, Dictionaries**

### **List**

```python
lst = [1,2,3]
lst.append(4)
lst.remove(2)
lst[0]  # access first element
```

### **Tuple**

```python
t = (1,2,3)
t[1]  # 2, immutable
```

### **Set**

```python
s = {1,2,3,3}
s.add(4)
s.remove(2)
```

### **Dictionary**

```python
d = {"name":"Ravi", "age":30}
d["name"]  # 'Ravi'
d["age"] = 31
```


## **8. String Operations**

```python
s = "Hello Python"
s.lower()       # 'hello python'
s.upper()       # 'HELLO PYTHON'
s.replace("Python","World")
s.split()       # ['Hello', 'Python']
```

* **f-strings:**

```python
name = "Ravi"
print(f"My name is {name}")
```


## **9. File Handling**

```python
# Write
with open("file.txt","w") as f:
    f.write("Hello World")

# Read
with open("file.txt","r") as f:
    print(f.read())
```

---

## **10. Exception Handling**

```python
try:
    a = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Always executes")
```

---

## **11. Modules & Libraries**

```python
import math
print(math.sqrt(16))  # 4.0

from random import randint
print(randint(1, 10))
```

---

## **12. Quick Tips**

* Indentation = **Python syntax**
* `#` for single-line comment
* `""" """` for multi-line comment / docstring
* Lists and dictionaries are **mutable**, tuples and sets have **immutability rules**


# **1. Python Loops Overview**

Python has **two main types of loops**:

1. **`for` loop** – used for iterating over sequences (lists, tuples, strings, etc.)
2. **`while` loop** – repeats as long as a condition is `True`

You can control loops using:

* `break` → exit the loop completely
* `continue` → skip the current iteration
* `else` (with loop) → executes if loop completes normally (no `break`)


## **2. For Loop**

Iterates over a **sequence** (list, tuple, string, range).

### Syntax:

```python
for variable in sequence:
    # code block
```

### Examples:

```python
# Loop over list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop over range of numbers
for i in range(5):  # 0 to 4
    print(i)

# Loop with step
for i in range(1, 11, 2):  # 1,3,5,7,9
    print(i)

# Loop with string
for ch in "Python":
    print(ch)
```


### **For loop with else**

```python
for i in range(3):
    print(i)
else:
    print("Loop completed without break")
```

## **3. While Loop**

Repeats **until a condition is False**.

### Syntax:

```python
while condition:
    # code block
```

### Examples:

```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# While loop with else
num = 0
while num < 3:
    print(num)
    num += 1
else:
    print("While loop completed")
```


## **4. Break & Continue**

### **Break** – exit loop immediately

```python
for i in range(5):
    if i == 3:
        break
    print(i)  # prints 0,1,2
```

### **Continue** – skip current iteration

```python
for i in range(5):
    if i == 3:
        continue
    print(i)  # prints 0,1,2,4
```


## **5. Nested Loops**

Loops inside loops:

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```


## **6. Looping through data structures**

### **List**

```python
numbers = [1, 2, 3]
for n in numbers:
    print(n)
```

### **Tuple**

```python
t = (10, 20, 30)
for val in t:
    print(val)
```

### **Dictionary**

```python
d = {"name":"Ravi", "age":30}
for key in d:
    print(key, d[key])
# OR
for key, value in d.items():
    print(key, value)
```

### **String**

```python
s = "Hello"
for ch in s:
    print(ch)
```


## **7. Quick Tips**

* `for` loop is **best for sequences**
* `while` loop is **best for conditions**
* Avoid infinite loops! (`while True:` needs break or exit)
* `else` in loops executes **only if no break occurs**


# **1. Traditional Switch in Other Languages**

In C/C++/Java:

```c
switch(day){
    case 1: printf("Monday"); break;
    case 2: printf("Tuesday"); break;
    default: printf("Other day");
}
```

Python **does not have a traditional switch-case**. Instead, you can use:

1. **`if-elif-else` statements**
2. **`match-case` statement** (Python 3.10+)


## **2. Using if-elif-else**

```python
day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
else:
    print("Other day")
```

✅ Works in **all Python versions**.


## **3. Using match-case (Python 3.10+)**

Python 3.10 introduced **structural pattern matching**, which behaves like a switch.

```python
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Other day")  # default case
```

### Notes:

* `case _:` → acts like the default in C/Java switch.
* Can match **values, types, sequences, and even complex patterns**.


## **4. Advanced Example: Matching Strings**

```python
command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "pause":
        print("Pausing...")
    case _:
        print("Unknown command")
```


## **5. Quick Comparison Table**

| Feature                         | if-elif-else | match-case (Python 3.10+) |
| ------------------------------- | ------------ | ------------------------- |
| Python version                  | All          | 3.10+                     |
| Default case                    | else         | case _                    |
| Can match complex patterns      | No           | Yes                       |
| Recommended for simple          | Yes          | Optional                  |
| Recommended for multiple values | Optional     | Yes                       |


💡 **Mentor Tip:**

* Use **if-elif-else** for simple conditions.
* Use **match-case** if you have **many discrete cases** or **pattern matching**.


# **1. What is Recursion?**

**Recursion** is a programming technique where a **function calls itself** to solve a smaller instance of the same problem.

* **Think of it like Russian dolls:** you keep opening one doll (function call) until you reach the smallest one (base case).
* **Key components:**

  1. **Base case** – the condition where recursion stops.
  2. **Recursive case** – the part where the function calls itself with a smaller/simpler input.


## **2. Why use Recursion?**

* When a problem can be **broken into smaller identical sub-problems**.
* Simplifies code for problems like:

  * Factorial
  * Fibonacci series
  * Tree traversal
  * Searching in recursive structures
  * Backtracking problems (mazes, puzzles)


## **3. Factorial Example**

```python
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

**Explanation:**

* factorial(5) = 5 * factorial(4)
* factorial(4) = 4 * factorial(3) … until factorial(1) = 1 (base case)


## **4. Fibonacci Example**

```python
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))  # Output: 13
```


## **5. Key Points / Mentor Tips**

1. **Always define a base case**, otherwise you’ll get a **RecursionError: maximum recursion depth exceeded**.
2. **Recursion can be memory-intensive**: each call is stored in the call stack.
3. For **large problems**, consider **iterative solution or memoization** to optimize.
4. Recursion works best for problems that have **natural hierarchical structure**.


## **6. Quick Visualization**

```text
factorial(3)
  -> 3 * factorial(2)
           -> 2 * factorial(1)
                     -> 1 (base case)
Result: 3*2*1 = 6
```
 