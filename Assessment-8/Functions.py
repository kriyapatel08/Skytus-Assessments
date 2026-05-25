#Function to check if a number is prime.
def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num + 1):
        if num % i == 0:
            return False

    return True
number = 13

if is_prime(number):
    print("Prime Number")
else:
    print("Not Prime Number")


#Function to reverse  a string.
def reverse_string(s):
    return s[::-1]

string = "Python"
print("Reversed String:", reverse_string(string))


# #Function to calculate the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number: "))
print("Factorial of", num, "is:", factorial(num))


#Function to calculate simple interest.

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
print("Simple Interest:", simple_interest(principal, rate, time))


#Function to check if a word is palindrome.

def is_palindrome(word):
    return word == word[::-1]
word = input("Enter a word: ")
if is_palindrome(word):
    print(word, "is a palindrome.")
else:
    print(word, "is not a palindrome.")
    
    
#Function to count vowels in a string.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
string = input("Enter a string: ")
print("Number of vowels in the string:", count_vowels(string))


#Function to merge two lists.

def merge_lists(list1, list2):
    return list1 + list2
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = merge_lists(list1, list2)
print("Merged List:", merged_list)


#Function to find GCD of two numbers.

def gcd(a,b) :
    while b != 0:
        a, b = b, a % b
        return a
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("GCD of", num1, "and", num2, "is : ", gcd(num1, num2))


# function to find area of a ractangle.

def area_of_rectangle(Length, Breath):
    return Length * Breath
Length = float(input("Enetr the length of the rectangle: "))
Breath = float(input("Enter the Breath of the rectangle: "))

print("Area of rectangle is: ", area_of_rectangle(Length,Breath))


# #Function to check Armstrong number

def is_armstrong(num):
    digits = len(str(num))
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == num
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")

    
