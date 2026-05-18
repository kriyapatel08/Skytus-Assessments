#Write a program that uses and (&) or or operators to check multiple conditions.
# Get user input for two numbers
num1 = int(input("Enter the first number: "))   
num2 = int(input("Enter the second number: "))
# Check if both numbers are positive using the and operator
if num1 > 0 and num2 > 0:
    print("Both numbers are positive.")
# Check if at least one number is positive using the or operator
elif num1 > 0 or num2 < 0:
    print("At least one number is positive.")
else:
    print("Neither number is positive.")
        






