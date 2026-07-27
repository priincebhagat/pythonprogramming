with open("practice/python_practice/sample.txt", "r+") as f:
   data = f.read()
   print(data)
   data = f.write("this")
