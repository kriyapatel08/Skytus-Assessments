#Write a program to handle division by zero error.
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))

    result = num1 / num2
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    
#Write a program to handle invalid integer input.
try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
    
except ValueError:
    print("Error: Please enter a valid integer.")

#Write a program to open a file and handle the "file not found" error.
try:
    file = open("nonexistent.txt", "r")
    content = file.read()
    print(content)
    file.close()
    
except FileNotFoundError:
    print("Error: File not found.")

#Write a program to demonstrate multiple exception blocks.
try:
    num = int(input("Enter a number: "))
    result = 10 / num

except ValueError:
    print("Invalid input. Enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except Exception as e:
    print("Some other error occurred:", e)
    
#Write a program to use finally for resource cleanup
try:
    file = open("sample.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    print("Program execution completed.")

#Write a program to create a custom exception for invalid age (<18).
class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")

    print("Eligible.")

except InvalidAgeError as e:
    print("Error:", e)

#Write a program to handle IndexError when accessing a list.
try:
    list = [20,40,60,80]
    index = int(input("Enter index :"))
    print("value= ",list[index])
    
except IndexError:
    print("Error: Index out of range.")

# Write a program that takes two numbers and handles all possible errors.
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    result = num1 / num2
    print("Result = ",result)
    
except ValueError:
    print("Error: Enter valid integers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except Exception as e:
    print("unexpected Error: ",e)

#Write a program to log errors to a file instead of printing them.
try:
    num = int(input("enter a number: "))
    result = 10 / num
    print("Result = ",result)
    
except Exception as e:
    file = open("backu.txt", "a")
    file.write(str(e)  + "\n")
    file.close()
    
    print("Error logged to file.")
    
#Write a program that validates an email format and raises an exception for invalid ones.

class InvalidEmailError(Exception):
    pass

try:
    email = input("Enter email: ")

    if "@" not in email or "." not in email:
        raise InvalidEmailError("Invalid Email Format")

    print("Valid Email")

except InvalidEmailError as e:
    print("Error:", e)

    
    
    