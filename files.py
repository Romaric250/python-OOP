with open("serialisation.txt", 'a') as file_serialisation:
    file_serialisation.write("take not of the json serialisation technics\n")
    

    print("Hello")



name = str(input("enter your name: "))

with open("guest.txt","w") as guest_object:
    guest_object.write("hello my name is {}".format(name))

try:
    with open("text.txt") as f:
        f.read()
except FileNotFoundError:
    print("the file you are trying to read does not exist")


print("the programs still continuous")


