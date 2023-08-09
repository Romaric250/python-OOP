def make_list(number):
    names = []
    for item in number:
        names.append(input("entern tr"))
        print(names)
number = int(input("enter num"))
names = make_list(number)
for name in names:
    if name [1] == "A":
        print("name", name, "start with A")