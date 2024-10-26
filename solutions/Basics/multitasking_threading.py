import threading
import time

def task(name):
    print(f"Task {name} started.")
    time.sleep(2)  # Simulate a blocking I/O operation
    print(f"Task {name} completed.")

# Creating threads
thread1 = threading.Thread(target=task, args=("A",))
thread2 = threading.Thread(target=task, args=("B",))

# Starting threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("All tasks completed.")

"""
Threading: Good for I/O-bound tasks. 
Threads share the same memory space, 
which can lead to issues if not handled properly 
(e.g., race conditions).

"""