def factorial(number):
    fac = 1
    while number > 1:
        fac *= number
        number -= 1
    return fac

num = int(input("Insert 1 number: "))
print("Factorial of", num, "is", factorial(num))
