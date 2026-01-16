
# 🐍 **Stack & Call Stack in Python (CPython + PyFrameObject)**


## ✅ **1. How Python Executes Code Internally**

When you run a Python program:

1. Python source code is **compiled into bytecode** (`.pyc`).
2. The **Python Virtual Machine (PVM)** executes this bytecode.
3. Each function call creates a **PyFrameObject** (Python frame object).
4. These frames are stored in a **Call Stack (managed by Python)**.
5. Under the hood, Python itself runs on a **C program**, so it also uses the **C function call stack**.


## 🔍 **2. What is a PyFrameObject?**

A **PyFrameObject** is a C structure in CPython that stores everything needed to execute a function:

| Part                           | Description                                              |
| ------------------------------ | -------------------------------------------------------- |
| **f_code**                     | Bytecode of the function                                 |
| **f_locals**                   | Local variables (Python dictionary)                      |
| **f_globals**                  | Global variables                                         |
| **f_builtins**                 | Built-in functions (`len`, `print`, etc.)                |
| **f_stacktop / operand stack** | Temporary values used during execution                   |
| **f_back**                     | Pointer to the previous frame (like a linked list stack) |


## ✅ **3. Example Python Code**

```python
def multiply(a, b):
    result = a * b
    return result

def add(x, y):
    sum_ = x + y
    product = multiply(sum_, 2)
    return product

def main():
    answer = add(5, 3)
    print(answer)

main()
```


## 📟 **4. Python Call Stack (Using PyFrameObject)**

### Step-by-step visualization of frames:

```
Top of Stack (Latest Call)
+--------------------------+
| Frame: multiply()        |
| Locals: a=8, b=2        |
| Return to: add()        |
+--------------------------+
| Frame: add()             |
| Locals: x=5, y=3, sum_=8 |
| Return to: main()        |
+--------------------------+
| Frame: main()            |
| Locals: answer=?         |
| Return to: <module>      |
+--------------------------+
| Frame: <module>          |
| Python starts here       |
+--------------------------+
Bottom of Stack
```

When `multiply()` returns → that frame is removed
Then `add()` returns → its frame removed
Then `main()` returns → removed



## ⚠ **5. What is Recursion Limit in Python? (Stack Overflow)**

Python protects against infinite stack growth.

```python
import sys
print(sys.getrecursionlimit())  # Default: 1000
```

```python
def recurse():
    recurse()

recurse()       # Causes:
# RecursionError: maximum recursion depth exceeded
```

✔ This error happens **not at OS level**, but Python's own frame stack limit
✔ Prevents C stack overflow beneath Python



## 🧠 **6. Python Call Stack vs C Call Stack**

| Feature            | Python Call Stack (PyFrameObject) | C Call Stack (under CPython)   |
| ------------------ | --------------------------------- | ------------------------------ |
| Managed by         | Python Virtual Machine (PVM)      | CPU / OS                       |
| Data stored        | Locals, bytecode, f_back pointer  | Return address, CPU registers  |
| Structure          | Linked list of frames             | Contiguous block memory (LIFO) |
| Overflow error     | RecursionError                    | Segmentation fault             |
| Visible to Python? | Yes (via `inspect` module)        | No (internal to OS/CPU)        |

---

## 🛠 **7. Visual Summary Diagram**

```
                  Python Program Execution
    --------------------------------------------------
    |             CPython Interpreter (C Language)   |
    |                                                |
    |   +------------------+                        |
    |   |   C Stack        |  <-- calls eval_frame  |
    |   |  (OS-level)      |                        |
    |   +------------------+                        |
    |           ↓                                   |
    |   +------------------------+                 |
    |   | Python Call Stack      |                |
    |   | (PyFrameObject List)   |                |
    |   +------------------------+                 |
    |   | f_back → previous frame |               |
    |   | f_locals, f_globals     |               |
    |   | bytecode instructions   |               |
    |   +------------------------+                 |
    --------------------------------------------------
```


## 🎯 **Final Summary (Interview Level Explanation)**

> In Python, every function call creates a **PyFrameObject**, which stores local variables, bytecode, and a link to the previous frame. These frames form the **Python Call Stack**.
> Underneath, Python (CPython) runs within a **C program**, so there is also a **C function stack**. Python limits recursion to avoid C stack overflow.
> If too many frames are created → you get **RecursionError**, not a Segmentation Fault like in C.


# 🧠 **Memory Map of a Python Process**

When you run a Python program (e.g., `python script.py`), the **Operating System loads a process in memory**.
Although Python is interpreted, internally it still follows the same basic structure as C/Java processes with `.text`, `.data`, heap, stack, etc.

But the difference is:
**Your Python code runs inside an interpreter (`python.exe` or `python3`)**, which itself is a **C program**.
So:

> **Python process memory = OS memory layout + Python Virtual Machine + Objects on heap**


## 🗺 **High-Level Memory Map of a Python Process**

```
+--------------------------------------------------------+
|                Kernel Space (Protected)               |
+--------------------------------------------------------+
|            User Space (Python Process)                |
|  +-----------------------------------------------+     |
|  |      Python Interpreter Executable (.text)    |     |
|  |      - Bytecode interpreter loop              |     |
|  |      - Built-in functions (print, len, etc.)  |     |
+  +-----------------------------------------------+     |
|  |      .data section                            |     |
|  |      - Global/static C variables of interpreter|    |
+  +-----------------------------------------------+     |
|  |      .bss section                             |     |
|  |      - Uninitialized global/static variables   |    |
+  +-----------------------------------------------+     |
|  |      Heap (Dynamic Memory)                    |     |
|  |      - Python objects (int, list, dict, str)  |     |
|  |      - User-defined class objects             |     |
|  |      - Garbage-collected memory               |     |
+  +-----------------------------------------------+     |
|  |      Stack (per thread)                       |     |
|  |      - C stack frames (function calls in C)   |     |
|  |      - Each C frame holds a PyFrameObject     |     |
+  +-----------------------------------------------+     |
|  |      Memory-mapped shared libs (.so / .dll)   |     |
|  |      - Python Standard Library                |     |
|  |      - NumPy, pandas loaded binaries          |     |
+-----------------------------------------------+--------+
```


## ⚙ **Call Stack in Python (Dual Stack Concept)**

When a Python function is called:

### 🧩 1. C Stack Frame (Low-level)

* Python interpreter is written in C.
* Each function call pushes a **C stack frame**.
* C function like `PyEval_EvalFrameEx()` handles execution.

### 🧩 2. PyFrameObject (High-level)

Python also maintains its **own stack**, implemented in heap memory:

```
struct PyFrameObject {
    PyCodeObject *f_code;     // Bytecode of function
    PyObject *f_locals;       // Local variables
    PyObject *f_globals;      // Global variables
    PyObject *f_builtins;     // Built-in objects
    PyFrameObject *f_back;    // Previous frame (call stack link)
}
```

### ✅ Visualization:

```
C Stack:
+---------------------+
| PyEval_EvalFrame() |
|  → Points to PyFrameObject
+---------------------+
| main()             |
+---------------------+

Python Stack (PyFrameObject on Heap):
+--------------------------+
| f_code: add()           |
| f_locals: a=2, b=3      |
| f_back → caller frame   |
+--------------------------+
| f_code: main()          |
| f_locals: x=10          |
+--------------------------+
```


## 🧹 **Heap & Garbage Collection**

All Python objects live in **heap memory**, managed by:
✔ Reference Counting
✔ Generational Garbage Collector
✔ Memory allocated by Python’s **private heap allocator (PyMalloc)**

Example:

```python
x = [1, 2, 3]
y = x
del x
# Object still exists because y references it
```



## 📊 **Comparison: C vs Java vs Python Memory**

| Feature        | C Program           | Java Program (JVM)       | Python Program (CPython)  |
| -------------- | ------------------- | ------------------------ | ------------------------- |
| Code Execution | Native machine code | Bytecode → JVM → JIT     | Bytecode → CPython VM     |
| Stack          | C stack only        | JVM Stack (Stack Frames) | C stack + PyFrameObject   |
| Heap           | malloc/free         | Java Heap (GC managed)   | Python Heap (with GC)     |
| GC             | Manual (free)       | Automatic (JVM GC)       | Ref Counting + Cyclic GC  |
| Interpreter?   | No                  | Yes (JVM)                | Yes (CPython interpreter) |


## 🎓 **Mentor-Style Story Summary**

Imagine Python as a **theatre play inside another theatre**:

- 🎭 The outer theatre = **OS Process**
- 🎭 The inner play = **Python Interpreter (written in C)**
- 📜 Every Python function call writes a diary page = **PyFrameObject on heap**
- 📚 But every diary is managed by a stage manager = **C call stack**
- 🧹 Old diaries are removed by **garbage collection & reference counting**