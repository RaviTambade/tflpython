# 🧹 Garbage Collection (GC) in Python 

> **"A good programmer writes code. A great programmer understands what happens after the code runs."**

When students begin learning Python, they enjoy creating variables, objects, lists, dictionaries, and classes. But very few ask an important question:

> **"After I stop using an object, who cleans it up?"**

Imagine if Python never removed unused objects.

* Every string would remain in memory.
* Every list would stay forever.
* Every object would occupy RAM permanently.

Soon your computer would run out of memory.

That's why Python has a **Garbage Collector (GC)**—a silent housekeeping system that automatically cleans unused objects from memory.


# Story Time: The Classroom Whiteboard

Imagine you are conducting a programming class.Every student receives a notebook. Whenever a notebook is no longer needed, students leave it on their desk. If nobody collects those notebooks:

* desks become crowded
* students cannot work
* classroom becomes messy

So every evening, the classroom assistant walks around and collects unused notebooks. Python's Garbage Collector behaves exactly like that classroom assistant.

```
Objects Created
        │
        ▼
   Used by Program
        │
        ▼
No Longer Needed
        │
        ▼
Garbage Collector
        │
        ▼
Memory Released
```


# Why Garbage Collection?

Memory is limited.Suppose your computer has:

```
RAM = 8 GB
```

Your application continuously creates objects.

```
Customer
Order
Invoice
Products
Images
JSON Objects
Lists
Dictionaries
```

If unused objects remain forever,

```
Memory Usage

100 MB
300 MB
700 MB
1.5 GB
4 GB
8 GB
Crash!
```

Garbage Collection prevents this.


# Python Memory Manager

Python internally contains a Memory Manager.

```
                Python Program
                      │
                      ▼
             Python Memory Manager
                      │
      ┌───────────────┴───────────────┐
      ▼                               ▼
Reference Counting           Garbage Collector
```

It performs two important jobs:

* Allocate memory
* Free unused memory


# Method 1: Reference Counting

Python primarily manages memory using **Reference Counting**. Every object stores a number called its **Reference Count**.

Example:

```python
x = [10,20,30]
```

Memory

```
Variable x
     │
     ▼
+------------------+
| [10,20,30]       |
| Ref Count = 1    |
+------------------+
```

Now create another reference.

```python
y = x
```

```
x ─────┐
       ▼
     +------------------+
     | [10,20,30]       |
     | Ref Count = 2    |
     +------------------+
       ▲
y ─────┘
```

Two variables point to the same object. Reference Count becomes **2**.

# Removing References

```python
del x
```

```
y
│
▼
+------------------+
| [10,20,30]       |
| Ref Count = 1    |
+------------------+
```

Still alive because **y** references it. Now,

```python
del y
```

Reference Count becomes:

```
0
```

Python immediately removes the object.

```
Memory Released
```

This makes Python extremely efficient.


# Demonstration

```python
import sys

x = [1,2,3]

print(sys.getrefcount(x))
```

Output might be

```
2
```

(The extra reference is created temporarily by `getrefcount()`.)


# Problem with Reference Counting

Reference Counting cannot solve **Circular References**. Consider two friends.

```
Alice → Bob
Bob → Alice
```

Even if nobody else knows them, they still point to each other. Reference Count never becomes zero.


# Circular Reference Example

```python
class Student:
    pass

a = Student()
b = Student()

a.friend = b
b.friend = a
```

Memory

```
a -----> Student A
          │
          ▼
       Student B
          ▲
          │
b --------┘
```

Delete variables.

```python
del a
del b
```

Problem:

```
Student A → Student B
Student B → Student A
```

Reference Counts remain greater than zero. Memory cannot be released using reference counting alone.


# Python's Solution: Cyclic Garbage Collector

Python has an additional system called the **Cyclic Garbage Collector**. Its job is to detect unreachable groups of objects that reference each other.

```
Reference Counting
        +
Cycle Detector
        =
Automatic Memory Cleanup
```

# Generational Garbage Collection

Python assumes:

> **Most newly created objects die quickly.**

Therefore, it divides objects into generations.

```
+----------------+
| Generation 0   |
| New Objects    |
+----------------+

        │ survives
        ▼

+----------------+
| Generation 1   |
| Older Objects  |
+----------------+

        │ survives
        ▼

+----------------+
| Generation 2   |
| Long-lived     |
+----------------+
```

# Why Generations?

Suppose a web application creates

```
Request Object
Response Object
Temporary JSON
Temporary Lists
```

These objects live only a few milliseconds. Checking old objects every time would waste CPU.

Instead:

```
Generation 0
checked frequently

Generation 1
checked less often

Generation 2
checked rarely
```

This improves performance.


# Garbage Collection Process

```
Create Objects
      │
      ▼
Reference Counting
      │
      ▼
Reference Count = 0 ?
      │
 ┌────┴────┐
 │         │
Yes        No
 │         │
Delete     Keep Object
           │
           ▼
Periodic GC Scan
           │
           ▼
Circular References?
           │
      ┌────┴─────┐
      │          │
     Yes         No
      │
Delete Objects
```


# When Does GC Run?

Python automatically runs the cyclic garbage collector when:

* many new objects have been allocated
* configurable collection thresholds are exceeded
* enough allocations occur relative to deallocations

You can also trigger it manually.

```python
import gc

gc.collect()
```

# The `gc` Module

```python
import gc
```

Useful functions:

```python
gc.collect()
```

Runs garbage collection immediately.

```python
gc.enable()
```

Enables automatic garbage collection.


```python
gc.disable()
```

Disables automatic garbage collection.

```python
gc.get_objects()
```

Returns objects currently tracked by the cyclic garbage collector.


```python
gc.get_count()
```

Returns allocation counters for each generation.


```python
gc.get_threshold()
```

Shows the collection thresholds for each generation.


# Real-Life Analogy

Imagine a city.

```
People
│
▼
Homes

Unused Homes
│
▼
Municipality Inspection

Abandoned Houses
│
▼
Demolished

Land Becomes Available
```

Python's Garbage Collector is like the municipality that periodically removes abandoned structures so resources can be reused.


# Interview Questions

### Q1. Why does Python use Reference Counting?

**Answer:** To immediately free memory when an object's reference count becomes zero.

### Q2. What problem cannot be solved using Reference Counting?

**Answer:** Circular (cyclic) references.


### Q3. Why is Generational GC faster?

**Answer:** Because most objects have a short lifetime, so Python checks newer generations more frequently and older generations less often.

### Q4. Which module is used to control Garbage Collection?

**Answer:**

```python
gc
```

### Q5. How do you manually invoke Garbage Collection?

```python
import gc

gc.collect()
```

# Key Takeaways

* Python automatically manages memory through a built-in Memory Manager.
* **Reference Counting** frees objects immediately when their reference count drops to zero.
* **Circular references** require the **Cyclic Garbage Collector**.
* Objects are organized into **Generation 0, Generation 1, and Generation 2** to make collection efficient.
* The **`gc` module** allows developers to inspect and manually control garbage collection when needed.
* Understanding garbage collection helps developers write memory-efficient, high-performance Python applications and troubleshoot memory-related issues.
