dics = {"name":"Romaric", "age":19, "country":"Cameroon", "occupation":"Software enginer"}

print(dics)

dic2 = dics


for value, key in dics.items():
    print(value, key)
    
companies = [
    ("comapany1", 2018, 143.90),
    ("comapany2", 2020, 13.90),
    ("comapany1", 2016, 1431.90)
    
]
# sorted_companies =  dict(companies.sort(key=lambda company:company[2]))
companies.sort(key=lambda com:com[0],reverse=True)
print(companies)

li = [1,2,3,4,5]
del li[1:2]

print(li)



# print(f"Sorted companies by revenue: {sorted_companies}")
    

