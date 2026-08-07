# garbage collection (GC)

Python uses a built-in garbage collection (GC) mechanism to manage memory automatically. Here’s a high-level overview of how it works:

### 1. **Reference Counting**
Python primarily uses reference counting to keep track of the number of references to each object. Each object has an associated count that increases when a reference is created and decreases when a reference is deleted or goes out of scope.

- **When an object's reference count drops to zero**, meaning there are no more references to it, Python's memory manager immediately deallocates the memory associated with that object.

### 2. **Cycle Detection**
Reference counting alone cannot handle circular references (e.g., two objects that reference each other). To address this, Python includes a cyclic garbage collector:

- **Generational Garbage Collection**: Python divides objects into three "generations":
  - **Generation 0**: Newly created objects.
  - **Generation 1**: Objects that survive one garbage collection cycle.
  - **Generation 2**: Long-lived objects that have survived multiple cycles.

- **GC Cycle**: The cyclic garbage collector periodically looks for groups of objects that reference each other but are not reachable from the program. It does this by:
  - Tracking object references.
  - Identifying unreachable objects and collecting them to free memory.

### 3. **Triggering the Garbage Collector**
The garbage collector runs automatically, but you can also control it:
- The collector is triggered when:
  - The allocation of new objects exceeds a certain threshold.
  - Explicitly invoked using `gc.collect()`.
  
### 4. **The `gc` Module**
Python provides the `gc` module to interact with the garbage collector:
- **Functions** like `gc.collect()` allow manual triggering of the GC.
- `gc.get_objects()` can be used to retrieve all objects tracked by the GC.
- You can also enable or disable the garbage collector with `gc.enable()` and `gc.disable()`.

### Summary
In summary, Python's garbage collection combines reference counting for immediate deallocation with a cyclic garbage collector for cleaning up circular references. This dual approach helps manage memory efficiently, making Python easier to use while reducing the likelihood of memory leaks.
