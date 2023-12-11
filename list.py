first_list = list()
first_list = ["first", "second", "third"]

# first_list.pop(1)
# first_list.remove("first")

f1, *f2 = first_list

print(f2)
first_list.append("fourth")
first_list.insert(1, "before")
print(type(first_list))
print(first_list)