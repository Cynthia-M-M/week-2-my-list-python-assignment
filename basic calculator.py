#basic calculator

def basic_calculator():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Enter operator (-, +, *, /): ")

    if operator == "-":
       result = num1 - num2
    elif operator == "+":
       result = num1 + num2
    elif operator == "*":
       result = num1 * num2   
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result ="Error! Cant divide by zero"
    else:
        result = "invalid operator!"    
    print(f"Result of {num1} {operator} {num2} is: {result}" )    
basic_calculator()

