num1 = int(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = int(input("Enter second number: "))

calculator = {
    "+": num1 + num2,
    "-": num1 - num2,
    "*": num1 * num2,
    "/": num1 / num2
}

print(calculator[operator])