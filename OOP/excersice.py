class Car:
def __init__(self, make, model,):
self.make = make
self.model = model

def move(self):
print("Driving around")


class Plane:
def __init__(self, make, model,):
self.make = make
self.model = model

def move(self):
print("Flying around")


class Motobike:
def __init__(self, make, model, ):
self.make = make
self.model = model

def move(self):
print("Riding around")


# instance of out class

car = Car("Toyota","Tx")
plane = Plane("Boeing","737")
bike = Motobike("Kawasaki","ninja 650")

for vehicles in (car, plane, bike):
vehicles.move()