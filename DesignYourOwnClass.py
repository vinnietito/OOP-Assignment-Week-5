# Base Class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model  
        self.price = price
        
    def call(self, number):
        return f"{self.brand} {self.model} is calling {number}."
    
    def display_info(self):
        return f"Smartphone: {self.brand} {self.model}, Price: {self.price}"