#Task 1: Perform Basic Mathematical Operations

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2


if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero)"


print("\nResults of mathematical operations:")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")





#Task 2: Create a Personalized Greeting

firstname = input("Enter first name: ")
lastname = input("Enter last name: ")
fullname = firstname + " " + lastname
print(f"Hello, {fullname}! Welcome to python programming!")