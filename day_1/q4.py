#Write a Python function to find the maximum of three numbers.

num1 = int(input("Enter the integer num1: "))
num2 = int(input("Enter the integer num2: "))
num3 = int(input("Enter the integer num3: "))

def max_of_three_numbers(num1:int, num2:int, num3:int):
    if num1 > num2:
        if num1 > num3:
            print("num1 is greater")
        else:
            print("num3 is greater")
    else:
        if num2 > num3:
            print("num2 is greater")
        else:
            print("num3 is greater")

max_of_three_numbers(num1, num2, num3)