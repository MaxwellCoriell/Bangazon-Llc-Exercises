from departments import *
import random


class Employees(Department):
    '''
    Parent class for all employees at the company

    Properties: first_name,
                                last_name,

        Methods:	__init__,
                                eat
    '''

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + " " + self.last_name

    def eat(self, food, companions):
        randomRestaurant = ["Five Guys Burger's and Fries",
                            "Melrose Billiards Parlor", "Bobbie's Dairy Dip"]
        self.restaurant = random.choice(randomRestaurant)
        print(self.restaurant)
        self.food = food
        self.companions = companions
        print("{} ate a {} at {} with {}, {}, and {}".format(self.full_name,
                                                             self.restaurant,
                                                             self.companions[
                                                                 0],
                                                             self.companions[
                                                                 1],
                                                             self.companions[2]
                                                             ))
        return self.restaurant


max_is_me = Employees("Max", "Baldridge")
max_is_me.eat(food="fries", companions=["Angela", "Adam", "Kayla"])
