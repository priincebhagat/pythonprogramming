# A function is a reusable block of code that does a specific job. Instead of writing the same code over and over, you define it once and call it whenever you need it.

def greet():
    print("Hey, how are you doing?")

greet()

# Without return statement, the function performs its task but does not send any value back to the caller. It simply executes the code within its block and then exits.
def add(a, b):
    print(a + b)

result = add(3, 5) 
print(result)   

# With return statement, the function performs its task and sends a value back to the caller. The caller can then use this returned value for further processing or display.
def add(a, b):
    return a + b

result = add(3, 5)   
print(result) 