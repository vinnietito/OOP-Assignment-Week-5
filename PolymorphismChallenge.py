# Base Class
class Vehicle:
    def move(self):
        raise NotImplementedError("SUbclasses must implement this method!")
    
# Subclass for Car
class Car(Vehicle):
    def move(self):
        return "Driving on the road"
    
    