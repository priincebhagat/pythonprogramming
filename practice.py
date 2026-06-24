#Ask the user for a total bill amount and the number of people. Calculate and print each person's share, and also show the amount with a 10% tip included.

total_bill = float(input("Enter the total bill amount : "))
number_of_people = int(input("Enter the number of people : "))
share_per_person = total_bill / number_of_people
with_tip = total_bill * 1.10 / number_of_people
print("Each person's share is : ",share_per_person)
print("Each person's share with tip is : ",with_tip)