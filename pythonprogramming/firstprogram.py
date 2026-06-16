print("Hello  World!!")

name = "Prince"
age = 19
salary = 25.00

print("my name is : ", name)
print("my age is : ", age)
print("my salary is : ", salary)

#Datatypes
print(type(name))
print(type(age))
print(type(salary))

#Arithmetic Operators
#addition 
a = 5
b = 2
print(a + b)
#Substraction
a = 5
b = 2
print(a - b)
#Multiplication
a = 5
b = 2
print(a * b)
#Division
a = 5
b = 2
print(a / b)
#Modulus(remainder)
a = 5
b = 2
print(a % b)
#Power
a = 5
b = 2
print(a ** b)

#Relational Operators
a = 40
b = 15

print(a == b)
print(a != b)
print(a >= b)
print(a > b)
print(a <= b)
print(a < b)

#Assignment Operators
x = 10
x += 3
print("x : ",x)
x -= 3
print("x: ",x)
x *= 3
print("x : ",x)
x /= 3
print("x : ",x)
x %= 3
print("x : ",x)
x **= 3
print("x : ",x)

#logical Operators
#NOT 
a = 4
b = 5
print(not(a > b))

#AND
val1 = True
val2 = False
print("AND operator : ",val1 and val2)

#OR
print("OR operator : ",val1 or val2)

#Type Casting
#Conversion(automatic)
a = 3
b = 4.20
print(a + b)

#Casting(manual)
a = int("3")
b = 4.25
print(a + b)

#taking input from the user
name = input("Enter your name : ")
age = int(input("Enter your age : "))
salary = float(input("Enter your salary: "))

print("Name : ",name)
print("Age : ",age)
print("Salary : ",salary)