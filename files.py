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

try:
    file = 'object.txt'
    with open(file, encoding="utf-8") as f:
       fcontent = f.read()
except FileNotFoundError:
    print("file {} does not exist".format(file))
else:
    words = fcontent.split()
    print("number of words in {} is {}" .format(file,len(words)))


print("the programs still continuous")


