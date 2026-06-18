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
    "name ": "Prince Bhagat",
    "age " : 19,
    "subjects" : {
        "maths" : 75,
        "science" : 87,
        "chemistry" : 94,
    }
}
print("student : ",student)
print("student's subjects : ",student["subjects"])
print("student's chemistry marks : ",student["subjects"]["chemistry"])