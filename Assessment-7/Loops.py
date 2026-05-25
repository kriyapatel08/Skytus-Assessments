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