# Problem 1 - Coordinates Distance
point1 = (2,5)
point2 = (1,4)

x1 , y1 = point1
x2 , y2 = point2
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("Distance : ",round(distance, 2))

# Problem 2 - Tuple Swapper

a = input("Enter the first value : ")
b = input("Enter the second value : ")
my_tuple = a, b
swapped = b, a
print("Original : ", my_tuple)
print("Swapped : ",swapped)
