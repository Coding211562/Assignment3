#Task 1
def factorial():
    num = int(input("Enter a number: "))
    if num < 2:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial())


