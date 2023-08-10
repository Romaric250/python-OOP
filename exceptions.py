def enterAge(age):
    age = int(input("enter your age: "))
    if age<0:
        raise ValueError("only positive numbers ohh")
    
    if age % 2 == 0:
        print('Entered age is even')
    else:
        print("Entered age is odd")




