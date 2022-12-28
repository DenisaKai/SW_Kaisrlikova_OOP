import random
# each object has 4 initial conditions: position, weight, speed, type of object
class Object:

    def __init__(self, position, weight, speed, object):
        self.position = position
        self.weight = weight
        self.speed = speed
        self.object = object

    def __repr__(self):
        return f"{self.object}: {self.position}m,  {self.weight}kg,  {self.speed}km/h"

    def generate_speed(self, l_limit, h_limit):
        speed = random.randint(l_limit, h_limit)
        return speed

    def generate_weight(self, l_limit, h_limit):
        weight = random.randint(l_limit, h_limit)
        return weight


class Pedestrian(Object):
    pass


class Vehicle(Object):
    pass


class Rider(Object):
    pass