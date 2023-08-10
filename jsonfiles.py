import json
numbers = [1,3,5,6,45]
objects = [
    
    {'id':4,
            'name':"Romaric",
            "age":19,
            "town":"Yaounde"
            
            },
           {'id':4,
            'name':"Romaric",
            "age":19,
            "town":"Yaounde"
            
            
            
            },
           {'id':4,
            'name':"Romaric",
            "age":19,
            "town":"Yaounde"
           
            },
           {'id':4,
            'name':"Romaric",
            "age":19,
            "town":"Yaounde"
           
            },
           {'id':4,
            'name':"Romaric",
            "age":19,
            "town":"Yaounde"
            
            },
           {'id':4,
            'name':"Romaric",
            "age":19,
            "town":"Yaounde"
          
            
            },
           {'id':4,
            'name':"Romaric",
            "age":19,
            "town":"Yaounde"
            
            }
           ]

filename = 'numbers.json'
try:
    with open(filename, 'w') as f:
        json.dump(objects,f)
except FileNotFoundError:
    print("file not found")


with open('numbers.json') as c:
    num = json.loads(c)
print(num)
