#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

num = int(input("Enter the number: "))

def factorial_of_num(num:int):
    i = 1
    fac = 1
    while i <= num:
        fac = fac * i
        i = i + 1
    return fac

Factorial = factorial_of_num(num)
print(f"Factorial of {num}: {Factorial}")

