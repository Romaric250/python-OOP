#dictionary in python
dic = dict()

dic[0] = 23
dic[1] = 300
dic['love'] = 400
dic[3] = 30
print(type(dic))
print(dic)
for key, value in dic.items():
    print(key, value)
    

#sets

s = {3,5}
print(type(s))

s.add(35)
s.remove(3)

print(s)