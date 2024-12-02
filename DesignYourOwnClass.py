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
    
    
# Subclass inheriting from Smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, cooling_system, refresh_rate):
        super().__init__(brand, model, price)
        self.cooling_system = cooling_system
        self.refresh_rate = refresh_rate
        
    def play_game(self, game):
        return f"Playing {game} at {self.refresh_rate}Hz with {self.cooling_system} cooling system!"
    
    
# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S21", 799)
gaming_phone = GamingSmartphone("ASUS", "ROG Phone 6", 999, "Liquid Cooling", 144)

# Testing methods
print(phone1.display_info())
print(phone1.call(123-456-7890))
print(gaming_phone.display_info())
print(gaming_phone.play_game("Call of Duty Mobile"))