from datetime import datetime
import uuid
from random import *
from exceptions import enterAge

class Restaurant(object):
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)
    def open_restaurant(self, open = False):
        if open:
            print("restaurant is open")
        else:
            print("restaurant close")

restaurant = Restaurant("chez Raymon", "Italian")

restaurant.describe_restaurant()
restaurant.open_restaurant(True)


class User(object):
    def __init__(self, first_name, second_name, password):
        self.first_name = first_name
        self.second_name = second_name
        self.password = password

    def describe_user(self):
        print(self.second_name, self.first_name, self.password)


class Users(User):
    def __init__(self, first_name, second_name, password):
        super().__init__(first_name, second_name, password)




user = User("Romaric", "Lofonyuy","12345")

users = Users("Ronald", "James","15682681")
user.describe_user()
num = randint(3,100)

counter = 100
i = 1
for i in range(100):
    print(num)

