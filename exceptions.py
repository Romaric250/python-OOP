def enterAge(age):
    if age<0:
        raise ValueError("only positive numbers ohh")
    
    if age % 2 == 0:
        print('Entered age is even')
    else:
        print("Entered age is odd")


num = int(input('enter your age'))
enterAge(num)


