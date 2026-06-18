#List's 
student_info = ["Prince" , 19 , "Palghar"]
print("Student-Info : ",student_info)
# A list in Python is an ordered, mutable collection that can store elements of different datatypes, 
# defined using square brackets `[ ]`.
# It allows duplicate values and supports indexing and slicing to access, modify, add, or remove elements.

#Practice Question
#wap to ask the user to enter names of their 3 fav movies and store them in a list
movies =[]
mov1 = input("Enter your 1st fav movie : ")
mov2 = input("Enter your 2nd fav movie : ")
mov3 = input("Enter your 3rd fav movie : ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print("Your favourite movies : ",movies)

# wap to check if a list contains a palindrome of elements(use copy method) 
list1 = ['r','a','c','e','c','a','r']
copylist1 = list.copy(list1)
if(copylist1 == list1):
    print("List is palindrome.")
else:
    print("List is not palindrome.")
    
