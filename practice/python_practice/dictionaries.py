# Problem 1 - Contact Book
#Create a dictionary of 3 contacts with names as keys and phone numbers as values. Print each contact
contacts = {
    "Prince": 9730239470,
    "Riya": 8765432987
}

for name, phone in contacts.items():
    print("Name : ",name, ",  Phone : ",phone)


# Problem 2 - Student grade Checker

class_info = {
    "prince": 94,
    "riya":74,
    "deepak":35
}
for name, marks in class_info.items():
    if marks >= 40 :
        print(name," Passed")
    else :
        print(name," failed")
