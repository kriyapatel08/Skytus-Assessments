# Create a Car class with attributes like brand, model, and speed, and methods to accelerate/brake.
class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self, value):
        self.speed += value
        print("Speed after acceleration:", self.speed)

    def brake(self, value):
        self.speed -= value
        print("Speed after braking:", self.speed)

car = Car("Toyota", "Fortuner", 50)
car.accelerate(20)
car.brake(10)

# Create a BankAccount class with deposit and withdraw methods.
# Create a Student class with a method to calculate average marks.
# Create a Rectangle class with methods to find area and perimeter.
# Create an Employee class that displays salary details.
# Create a Book class to store title, author, and price, and display details.
# Create a Circle class to find area and circumference.
# Create a Laptop class with a method to apply discounts on price.
# Create a Flight class with seat booking functionality.
# Create a Shop class with a method to add and list products.