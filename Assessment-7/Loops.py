#Print numbers from 1 to 10.
for i in range(1, 11):
    print(i)


#Display multiplication table for a given number.
number = 5
print("Multiplication table for", number, ":")
for i in range(1, 11):
    print(number, "x", i, "=", number * i)


#Find factorial of a number.
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is :", factorial)


#Generate the first N Fibonacci numbers.
N = 10
fib_sequence = []
a, b = 0, 1
for _ in range(N):
    fib_sequence.append(a)
    a, b = b, a + b
print("First", N, "Fibonacci numbers:", fib_sequence)


#Check if a number is prime.
num = int(input("enter the number: "))
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")


#Reverse a number (e.g., 123 → 321).
num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print("Reversed number:", reversed_num)


#Count digits in a number.
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print("Number of digits:", count)


# Find sum of even numbers between 1–100.
total = int(input("Enter the number: "))    
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print("Sum of even numbers between 1 and 100:", total)


#Print a pyramid pattern.
rows = int(input("Enter the number of rows: "))
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))
    
    
#Find all divisors of a number.
num = int(input("Enter a number: "))
divisors = []
for i in range(1, num + 1):
    if num % i == 0:
        divisors.append(i)
print("Divisors of", num, "are:", divisors)

