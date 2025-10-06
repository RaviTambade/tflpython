# Simple File I/O operation using Python

# Reusable functions for writing and reading text file
def write(filename, content):
    """Write content to a text file."""
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Content written to {filename}.")

def read(filename):
    """Read content from a text file."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"Content read from {filename}:\n{content}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

# Test(Entry Point)
if __name__ == "__main__":
    filename = 'tfl.txt'
    
    # Content to write to the file
    content = """Welcome to Transflower!Tansflower Acceleration Program.Mentor as a Service!"""
    # Write to the file
    write(filename, content)

    # Read from the file
    read(filename)