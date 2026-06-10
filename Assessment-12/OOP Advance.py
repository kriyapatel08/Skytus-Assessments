# Create a base class Animal and subclasses Dog and Cat.
class Animal:
    def sound(self):
        print("Animals make sound")
        
class Dog(Animal):
    def sound(self):
        print("Dog barks")
        
class Cat(Animal):
    def sound(self):
        print("Cat meows")
        
d = Dog()
c = Cat()

d.sound()
c.sound()

# Create a class hierarchy for Vehicle → Car → ElectricCar.

class vehicle:
    def show_vehicle(self):
        print("This is a vehicle")
        
class Car(vehicle):
    def show_car(self):
        print("This is a car")
        
class ElectricCar(Car):
    def show_electric(self):
        print("This is an electric car")
        
e = ElectricCar()

e.show_vehicle()
e.show_car()
e.show_electric()


# Implement method overriding in a base and derived class.
class Parent:
    def display(self):
        print("Display method of Parent class")
        
class Child(Parent):
    def display(self):
        print("Display method of Child class")

obj = Child()
obj.display()


# Demonstrate multiple inheritance with two parent classes.
class Father:
    def father_property(self):
        print("Father's property")

class Mother:
    def mother_property(self):
        print("Mother's property")

class Child(Father, Mother):
    def own_property(self):
        print("Child's property")


c = Child()

c.father_property()
c.mother_property()
c.own_property()


# Create a polymorphic function that works with different shapes.

class Circle:
    def area(self):
        return 3.14*5*5

class Rectangle:
    def area(self):
        return 10*4
    
def calculate_area(shape):
    print("Area =",shape.area())
    
c = Circle()
r = Rectangle()

calculate_area(c)
calculate_area(r)

# Create a Bank system with SavingsAccount and CurrentAccount classes.
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print("Balance =", self.balance)


class SavingsAccount(BankAccount):
    def add_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        print("Balance after interest =", self.balance)


class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Remaining Balance =", self.balance)
        else:
            print("Insufficient balance")


s = SavingsAccount(10000)
s.show_balance()
s.add_interest()

c = CurrentAccount(5000)
c.withdraw(2000)
# Create a class with private attributes and getter/setter methods.
class Students:
    def __init__(self):
        self.__marks = 0

    def set_marks(self,marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks
    
s = Students()
s.set_marks(90)

print("Marks =",s.get_marks())

# Create a Teacher and Student class to show inheritance.
class teacher:
    def teach(self):
        print("Teacher teaches students")
        
class Students(teacher):
    def studey(self):
        print("students studies subjects")

s = Students()
s.teach()
s.studey()

# Create a MusicPlayer class and subclass Spotify to override the play method.
class MusicPlayer:
    def play(self):
        print("Playing music")
        
class Spotify(MusicPlayer):
    def play(self):
        print("Playing music on Spotify")
        
s = Spotify()
s.play()


# Demonstrate the use of super() in inheritance.
class Parent:
    def __init__(self,name):
        self.name = name

class employee(Parent):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary = salary
        
    def display(self):
        print("name =", self.name)
        print("salary = ",self.salary)
        
e = employee("kriya", 50000)
e.display()