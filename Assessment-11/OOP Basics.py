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

car = Car("Scorpio","S12", 50)
car.accelerate(20)
car.brake(10)

# Create a BankAccount class with deposit and withdraw methods.
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print("Balance after deposit:", self.balance)
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Balance after withdrawal:", self.balance)
        else:
            print("Insufficient balance.")
            
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)               
                 
# Create a Student class with a method to calculate average marks.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def calculate_average(self):
        average = sum(self.marks) / len(self.marks)
        print("Average marks for", self.name, "is:", average)
student = Student("Alice", [85, 90, 78])
student.calculate_average()

# Create a Rectangle class with methods to find area and perimeter.
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def area(self):
        print("Area=", self.length * self.width)
        
    def perimeter(self):
        print("Perimeter = ", 2 * (self.length + self.width))
        
rect = Rectangle(10, 5)
rect.area()
rect.perimeter()
    
# Create an Employee class that displays salary details.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)

emp = Employee("Amit", 50000)
emp.display()
# Create a Book class to store title, author, and price, and display details.
class book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
        
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)
        
book = book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
book.display()
        
# Create a Circle class to find area and circumference.
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        print("Area = ",3.14 * self.radius ** 2)
            
    def circumference(self):
        print("Circumference =", 2 * 3.14 * self.radius)

c = Circle(5)
c.area()
c.circumference()

# Create a Laptop class with a method to apply discounts on price.
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    
    def apply_discount(self, percent):
        discount = self.price * percent / 100
        final_price = self.price - discount
        print("Price after discount: ", final_price)
        
laptop = Laptop("Victus", 70000)
laptop.apply_discount(10)
    
# Create a Flight class with seat booking functionality.
class Flight:
    def __init__(self,seats):
        self.seats = seats
        
    def book_seat(self, num_seats):
     if self.seats >= num_seats:
        self.seats -= num_seats
        print("Seat booked successfully")
        print("Available Seats:",self.seats)
     else:
         print("No seats available")
         
f = Flight(120)
f.book_seat(220)
        
# Create a Shop class with a method to add and list products.
class Shop:
    def __init__(self):
        self.products = []
        
    def add_product(self, product):
        self.products.append(product)
        print("Product added:", product)
    def list_products(self):
        print("Products in the shop:")
        for product in self.products:
            print(product)
            
shop = Shop()
shop.add_product("Laptop")
shop.add_product("Smartphone")
shop.list_products()

