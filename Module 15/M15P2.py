
# Base class Car
class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price
        self.discount_price = self.sticker_price * 0.90  # 10% discount
    
    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Sticker Price: ${self.sticker_price}")
        print(f"Discounted Price: ${self.discount_price}")

# Derived class Sportcar
class Sportcar(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.sport_wheels = "N"
        self.sport_engine = "N"
        self.sport_interior = "N"
    
    def sport_wheels_option(self, value):
        if value == "Y":
            self.sport_wheels = "Y"
    
    def sport_engine_option(self, value):
        if value == "Y":
            self.sport_engine = "Y"
    
    def sport_interior_option(self, value):
        if value == "Y":
            self.sport_interior = "Y"
    
    def updated_price(self):
        price = self.discount_price
        if self.sport_wheels == "Y":
            price += 1000
        if self.sport_engine == "Y":
            price += 3000
        if self.sport_interior == "Y":
            price += 2000
        return price

# Create two car objects and two sportcar objects
car1 = Car("Toyota", "Camry", 25000)
car2 = Car("Honda", "Civic", 22000)
sportcar1 = Sportcar("Porsche", "911", 100000)
sportcar2 = Sportcar("Ferrari", "488", 120000)

# Apply options to the sportcars
sportcar1.sport_wheels_option("Y")
sportcar1.sport_engine_option("Y")
sportcar1.sport_interior_option("N")

sportcar2.sport_wheels_option("N")
sportcar2.sport_engine_option("Y")
sportcar2.sport_interior_option("Y")

# Display info for cars
car1.display_info()
car2.display_info()

# Display info for sportcars and their updated prices
print(f"Updated Price for {sportcar1.make} {sportcar1.model}: ${sportcar1.updated_price()}")
print(f"Updated Price for {sportcar2.make} {sportcar2.model}: ${sportcar2.updated_price()}")
