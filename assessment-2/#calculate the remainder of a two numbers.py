#calculate the remainder of a two numbers.
def remainder(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    else:
        return num1 % num2
# Example usage:
number1 = 10
number2 = 3
result = remainder(number1, number2)
print(f"The remainder of {number1} divided by {number2} is: {result}")
# Example with division by zero:
number1 = 10
number2 = 0
result = remainder(number1, number2)
print(f"The remainder of {number1} divided by {number2} is: {result}")

