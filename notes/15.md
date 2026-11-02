# Interoperability

**Interoperability** means:  **The ability of two different technologies, programming languages, systems, or applications to work together and exchange data successfully.**

In your **C → Python** case, interoperability means **Python can use existing C code without rewriting that C code completely**.

### Simple example

Suppose you already have 20 years of legacy C code:

```text
Legacy C Application
       │
       │ C functions
       ▼
┌──────────────────┐
│ calculateSalary()│
│ processOrder()   │
│ validateCustomer()│
└──────────────────┘
```

You now build a Python application:

```text
Python Application
       │
       ▼
Python Wrapper
       │
       ▼
Legacy C Library
```

Python might call:

```python
result = legacy.calculate_salary(101)
```

while the actual calculation is still performed by:

```c
double calculate_salary(int employee_id)
{
    // existing legacy logic
}
```

That's **interoperability**.

### Think of it like two people speaking different languages

Imagine:

```text
C Developer                    Python Developer
     │                              │
     │       C ↔ Python Bridge      │
     └───────────┬──────────────────┘
                 │
          Interoperability
```

The bridge allows them to communicate even though they use different languages. Technically, that bridge could be:

* **ctypes**
* **CFFI**
* **Cython**
* **CPython extension**
* **REST API**
* **gRPC**
* **shared libraries (`.dll`, `.so`)**

### Why pointers matter

C works directly with memory:

```c
int x = 10;
int *p = &x;
```

Python normally doesn't expose memory addresses in the same way. So interoperability requires a mechanism to translate:

```text
C                         Python
────────────────────────────────────
int                       c_int
int *                     POINTER(c_int)
char *                    c_char_p / buffer
struct                    ctypes.Structure
struct *                  POINTER(Structure)
array                     ctypes array
void *                    c_void_p
```

For example:

```python
value = ctypes.c_int(10)
legacy.increment(ctypes.byref(value))
print(value.value)
```

Python has successfully communicated with C **at the memory/API boundary**.


### Interoperability vs rewriting

This distinction is important for legacy modernization.

**Rewriting:**

```text
Old C code
     ↓
Rewrite everything
     ↓
Python
```

Potentially huge risk and effort.

**Interoperability:**

```text
Old C code
     ↓
C/Python interface
     ↓
Python
```

You **reuse what already works** and gradually modernize around it. That is why interoperability is particularly valuable when dealing with **large legacy C/C++ systems**. Yes. You **can reuse legacy C code from Python**, including C code that uses pointers. In most cases, you should **not translate the pointer logic into Python**. Instead, keep the C code as a native library and create a Python wrapper around it.

The main approaches are:

1. **`ctypes`** — easiest for existing C libraries
2. **CFFI** — good for larger C APIs
3. **CPython C extension / pybind11** — more advanced, when you need tight integration
4. **Cython** — useful when gradually migrating C/Cython code to Python

For legacy code, I would start with **`ctypes`**.

### Example: Legacy C code with pointers

Suppose you have this existing C code:

```c
// legacy.c

#include <stdio.h>

void increment(int *value)
{
    (*value)++;
}

void process(int *input, int *output, int size)
{
    for (int i = 0; i < size; i++)
    {
        output[i] = input[i] * 2;
    }
}
```

Compile it as a shared library.

### Windows

Using GCC/MinGW:

```bash
gcc -shared -o legacy.dll legacy.c
```

### Linux

```bash
gcc -shared -fPIC -o liblegacy.so legacy.c
```

Now Python can call the C functions.


## 1. Calling `int *` from Python

```python
import ctypes

lib = ctypes.CDLL("./legacy.dll")

lib.increment.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.increment.restype = None

value = ctypes.c_int(10)

lib.increment(ctypes.byref(value))

print(value.value)
```

Output:

```text
11
```

The important mapping is:

| C          | Python `ctypes`                 |
| ---------- | ------------------------------- |
| `int`      | `ctypes.c_int`                  |
| `char`     | `ctypes.c_char`                 |
| `float`    | `ctypes.c_float`                |
| `double`   | `ctypes.c_double`               |
| `int *`    | `ctypes.POINTER(ctypes.c_int)`  |
| `char *`   | `ctypes.POINTER(ctypes.c_char)` |
| `void *`   | `ctypes.c_void_p`               |
| `struct *` | `ctypes.POINTER(MyStruct)`      |

`ctypes.byref(value)` essentially gives C a pointer to the Python-managed C-compatible value.


# 2. Passing arrays through pointers

This is where legacy C becomes particularly interesting.

C:

```c
void process(int *input, int *output, int size)
{
    for (int i = 0; i < size; i++)
    {
        output[i] = input[i] * 2;
    }
}
```

Python:

```python
import ctypes

lib = ctypes.CDLL("./legacy.dll")

lib.process.argtypes = [
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    ctypes.c_int
]

lib.process.restype = None
size = 5
input_data = (ctypes.c_int * size)(1, 2, 3, 4, 5)
output_data = (ctypes.c_int * size)()
lib.process(
    input_data,
    output_data,
    size
)

print(list(output_data))
```

Output:

```text
[2, 4, 6, 8, 10]
```

Notice that we didn't convert the C pointer algorithm into Python. We simply created a C-compatible memory block and passed its address to C.


# 3. C `struct *` is also possible

Suppose legacy C contains:

```c
typedef struct
{
    int id;
    float salary;
} Employee;

void increase_salary(Employee *employee)
{
    employee->salary += 5000;
}
```

Python representation:

```python
import ctypes

class Employee(ctypes.Structure):
    _fields_ = [
        ("id", ctypes.c_int),
        ("salary", ctypes.c_float)
    ]
```

Configure the function:

```python
lib.increase_salary.argtypes = [
    ctypes.POINTER(Employee)
]

lib.increase_salary.restype = None
```

Create the object:

```python
employee = Employee(
    id=101,
    salary=50000
)
```

Call C:

```python
lib.increase_salary(ctypes.byref(employee))
```

Read the result:

```python
print(employee.id)
print(employee.salary)
```

C modifies the memory, and Python sees the modified structure.

# 4. What about `char *`?

Legacy C code often looks like:

```c
void uppercase(char *text)
{
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (text[i] >= 'a' && text[i] <= 'z')
        {
            text[i] = text[i] - 32;
        }
    }
}
```

Python:

```python
lib.uppercase.argtypes = [
    ctypes.POINTER(ctypes.c_char)
]

lib.uppercase.restype = None
```

Create a mutable buffer:

```python
text = ctypes.create_string_buffer(b"hello world")
```

Call C:

```python
lib.uppercase(text)
```

Read it:

```python
print(text.value)
```

Output:

```text
b'HELLO WORLD'
```

This is important:

```python
ctypes.create_string_buffer()
```

creates **mutable memory**, which is appropriate when C expects to modify a `char *`.


# 5. Pointer-to-pointer

Legacy code can become more complicated:

```c
void create_number(int **value)
{
    *value = malloc(sizeof(int));

    **value = 100;
}
```

Here:

```text
int **value
    │
    └── pointer to an int pointer
```

Python can technically handle this:

```python
lib.create_number.argtypes = [
    ctypes.POINTER(ctypes.POINTER(ctypes.c_int))
]
```

But this is where you need to be careful. Because C is allocating memory:

```c
malloc(...)
```

Python must know **who owns that memory and who frees it**. A better legacy API is often:

```c
void create_number(int *value)
{
    *value = 100;
}
```

Then Python becomes much safer:

```python
value = ctypes.c_int()

lib.create_number(ctypes.byref(value))

print(value.value)
```


# 6. The most important issue: memory ownership

When integrating C with Python, pointers aren't the hardest problem. **Memory ownership is.**

For example:

```c
char* get_name()
{
    char *name = malloc(100);
    strcpy(name, "Ravi");
    return name;
}
```

Python:

```python
ptr = lib.get_name()
```

Who calls:

```c
free(ptr);
```

If nobody does → **memory leak**. If Python tries to free memory incorrectly → **crash / heap corruption**. For production systems, expose a matching C function:

```c
char* get_name()
{
    char *name = malloc(100);
    strcpy(name, "Ravi");
    return name;
}

void free_memory(char *ptr)
{
    free(ptr);
}
```

Then Python can explicitly release it.



# 7. A practical architecture

For a large legacy C application, I would **not expose hundreds of C functions directly to Python**. Instead:

```text
                 Python Application
                        │
                        ▼
                Python Wrapper
                   ctypes/CFFI
                        │
                        ▼
                C API Boundary
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
        Legacy C Modules      Legacy C Modules
              │                   │
              └─────────┬─────────┘
                        ▼
                    C Memory
```

Create a small **C facade/API layer**.

For example:

```c
// legacy_api.h

int calculate_salary(
    int employee_id,
    double *result
);

int process_orders(
    const Order *orders,
    int count,
    OrderResult *results
);

void free_result(
    OrderResult *result
);
```

Python interacts with this stable API rather than directly touching the entire legacy codebase.

# 8. Think of pointers as memory addresses

A useful mental model when teaching this to developers:

### C

```c
int x = 10;

int *p = &x;
```

Think:

```text
x
┌──────────┐
│    10    │
└──────────┘
     ▲
     │
     │ address
     │
┌──────────┐
│    p     │
└──────────┘
```

Python/ctypes:

```python
x = ctypes.c_int(10)

p = ctypes.pointer(x)
```

Now:

```python
p.contents.value
```

gives:

```text
10
```

And:

```python
p.contents.value = 50
```

changes the underlying C-compatible memory.

# 9. What should you use?

For a **legacy C modernization project**, I'd recommend:

```text
Existing C
   │
   │ Don't rewrite immediately
   ▼
C API / Facade
   │
   ▼
ctypes / CFFI
   │
   ▼
Python
   │
   ▼
FastAPI / Flask / CLI / AI application
```

This allows you to modernize incrementally:

```text
Phase 1
Python → C

Phase 2
Python → C API + new Python logic

Phase 3
Python → new Python modules
              ↓
          selected C modules

Phase 4
Legacy C gradually retired
```

**Don't start by converting pointers to Python objects.** First identify the C API boundary, data structures, pointer ownership, memory allocation/freeing, callbacks, and thread-safety. Then wrap it.  If your legacy C code is something like **`*.h + *.c` files**, you can share a small representative example, and I can show you exactly how to expose its **pointers, structures, arrays, callbacks, and memory management to Python**, step by step.
