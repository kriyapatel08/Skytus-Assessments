# #Check if a person is eligible to vote (age ≥ 18).
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")  
else:
    print("You are not eligible to vote.")
    
#Grade calculator based on marks: 90+ = A, 80+ = B, else C.

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
else:
    print("Grade: C")

#Simulate a traffic light: Red = Stop, Yellow = Wait, Green = Go.

traffic_light = input("Enter your traffic light color(red,yellow,green): ")
if traffic_light == "yellow":
    print("Wait")
elif traffic_light == "red":
    print("Stop")
elif traffic_light == "green":
    print("Go")
    
#ATM withdrawal check: sufficient balance or not.
check_amount = int(input("enter your check amount: "))

if check_amount > 50000:
    print("you have sufficient balance.")
else:
    print("you have not sufficient balance.")

#Check if a number is positive, negative, or zero.

num = int(input("enter the number: "))

if num > 0:
 print("number is positive.")
elif num < 0:
    print ("number is negative.")
else:
    print("the number is zero.")

#Check if a number lies within a given range.
 
num = int(input("enter the number: "))
if 1 <= num <= 100:
    print("number is within the range.")
else:
    print("number is out of range.")

#Username & password verification.

username = str(input("enter th username: "))
password = str(input("enter the password: "))

if username == "admin" and password == "1234":
    print("login sucessful")
else:
    print("login failed")
    
# Electricity bill calculator based on units consumed.

units = int(input("enter the number of units consumed: "))
if units <= 100:
    bill = units * 0.5
elif units <= 200:
    bill = 100 * 0.5 + (units - 100) * 0.75
elif units <= 300:
    bill = 100 * 0.5 + 100 * 0.75 + (units - 200) * 1.20
else:
    bill = 100 * 0.5 + 100 * 0.75 + 100 * 1.20 + (units - 300) * 1.50
print("Electricity bill: $", bill)


# Simple calculator (add, subtract, multiply, divide)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result =", num1 + num2)

elif operator == "-":
    print("Result =", num1 - num2)

elif operator == "*":
    print("Result =", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Division by zero is not possible")

else:
    print("Invalid operator")
                
                
#Check type of triangle (equilateral, isosceles, scalene).

s1 = float(input("Enter the length of the first side: "))
s2 = float(input("Enter the length of the second side: "))
s3 = float(input("Enter the length of the third side: "))
if s1 == s2 == s3:
    print("The triangle is equilateral.")
elif s1 == s2 or s2 == s3 or s1 == s3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")
    