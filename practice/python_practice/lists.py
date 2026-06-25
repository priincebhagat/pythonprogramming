# Problem 1 - Student Marks Tracker
student_marks=[81, 87, 65, 86, 75, 68]
print("Highest : ",max(student_marks))
print("Lowest : ",min(student_marks))
print("Average : ",sum(student_marks) / len(student_marks))

# Problem 2 - Even Number Filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for number in numbers :
    if number % 2 == 0 :

        even_numbers.append(number)
        
print("Even Numbers : ", even_numbers)
        