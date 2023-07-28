class student():
    def __init__(self, first, last, age):
        self.firstname = first
        self.secondname = last
        self.age = age
        
    def __str__(self):
        return self.firstname

    def set_attributes(self, age):
        if (age % 10 == 0):

            self.age = age/2

    def get_attributes(self):
        return self.age
   


student1 = student("romaric", "lonfonyuy", 30)
print(student1.firstname, student1.secondname, student1.age)
student1.set_attributes(30)

print(student1.age)


