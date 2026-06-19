# Dictionary
info = {
    "name" : "Prince Bhagat",
    "age" : 19,
    }
print("Student-Info : ",info)
# A dictionary in Python is an unordered, mutable collection of key-value pairs,
# defined using curly braces `{ }`. Each key is unique and maps to a value,
# allowing for efficient data retrieval based on keys.

# Nested Dictionary
student = {
    "name": "Prince Bhagat",
    "age" : 19,
    "subjects" : {
        "maths" : 75,
        "science" : 87,
        "chemistry" : 94,
    }
}
print("student : ",student)
print("student's subjects : ",student["subjects"])
print("student's chemistry marks : ",student["subjects"]["chemistry"])

print(student.get("age"))
new_dict = {"city" : "Palghar"}
student.update(new_dict)
print(student)

#Set
# A set is an unordered collection of unique elements, 
# defined using curly braces `{ }` or the `set()` constructor. 
# Sets are mutable, allowing for the addition and removal of elements, 
# but they do not support indexing or slicing. 

collection = {1,2,3,3,4,5}
print("collection : ",collection)

my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(3)
print("my_set : ",my_set)

my_set.remove(3)
print("my_set after removing 3 : ",my_set)

popping = { "Prince" , "Bishal" , "Rohit" , "Hriday"}
print(popping.pop())

