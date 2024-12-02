# Base Class
class Vehicle:
    def move(self):
        raise NotImplementedError("SUbclasses must implement this method!")
    
# Subclass for Car
class Car(Vehicle):
    def move(self):
        return "Driving on the road"
    
# Subclass for Plane
class Plane(Vehicle):
    def move(self):
        return "Flying in the sky"

# Subclass for Boat
class Boat(Vehicle):
    def move(self):
        return "Sailling on water"