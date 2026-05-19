#Write a program to check if a number is positive or negative.
num = float(input("enter a number: "))
if num > 0:
    print("the number is positive: ",num)
elif num < 0:
    print("the number is negative: ",num)
else:
    print("number is zero.")
    