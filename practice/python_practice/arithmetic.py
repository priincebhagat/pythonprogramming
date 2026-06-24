# Problem 1 - Bill Splitter

total_bill = float(input("Enter the total bill amount : "))
number_of_people = int(input("Enter the number of people : "))
share_per_person = total_bill / number_of_people
with_tip = (total_bill * 1.10) / number_of_people
print("Each person's share is : ", round(share_per_person, 2))
print("Each person's share with tip is : ", round(with_tip, 2))

# Problem 2 - Temperature Converter
#Ask the user for a temperature in Celsius and convert it to Fahrenheit and Kelvin. Print all three values.
celsius = float(input("Enter temperature in Celsius : "))
Fahrenheit = (celsius * 9/5) + 32
kelvin =  celsius + 273.15

print("Celsius : ",celsius)
print("Fahrenheit : ",Fahrenheit)
print("Kelvin : ",kelvin)