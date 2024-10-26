import asyncio

async def task(name):
    print(f"Task {name} started.")
    await asyncio.sleep(2)  # Simulate an asynchronous I/O operation
    print(f"Task {name} completed.")

async def main():
    # Create tasks
    await asyncio.gather(task("A"), task("B"))

# Running the asynchronous main function
if __name__ == "__main__":
    asyncio.run(main())
    print("All tasks completed.")


"""
Asynchronous Programming: Excellent for I/O-bound tasks where you want to manage 
a large number of operations concurrently 
without the overhead of threads or processes.
"""