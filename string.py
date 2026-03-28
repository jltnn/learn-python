name = input("Enter your full name:")
#result = len(name)
#result1 = name.find("e")
#result2 = name.rfind("e")
#print(result1)
#print(result2)
name.find(" ")
name.isalpha()
if len(name) >12:
    print("your name is too long")
elif not name.find(" ") == -1:
    print("your name contains space")
elif not name.isalpha():
    print("your name can not contain digit")
else:
    print(f"Welcome {name}")
