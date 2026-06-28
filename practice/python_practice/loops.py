# Problem 1 - Multiplication Table
#Ask the user for a number and print its multiplication table from 1 to 10.
n = int(input("Enter the number : "))

for i in range(1, 11):
    table = n * i

print(n, "x", i, "=",table)
