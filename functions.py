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

#Practice Question
#Average of 3 numbers

def calc_avg(a, b, c):
    sum = a + b + c
    average = sum / 3
    print("Average of the number is : ",round(average, 2))

calc_avg(18, 25, 17)

#Practice Question 2
# convert usd into inr

def converter(usd_value):
    ind_value = usd_value * 94
    print(usd_value,"USD : ",ind_value,"INR")

converter(18)

#practice Question 3
# take the user input and find whether the number is even or odd

def check_even_or_odd(value):
    if value % 2 == 0:
        print(value," is even")
    else :
        print(value," is odd")

value = int(input("Enter the number : "))
check_even_or_odd(value)

#Recursion
# Write a recursive function to calculate the sum of first n natural numbers.

def calc_sum(n):
    if (n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(10)
print("Sum of the given number is : ",sum)
