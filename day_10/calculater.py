from art import logo
import os

def sum(num1, num2):
    return num1 + num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def sub(num1, num2):
    return num1 - num2

operators = {
    '+':sum,
    '*': mult,
    '/': div,
    '-': sub,
}
def calculator():
    print(logo)
    num1 = float(input('enter first no  :  '))
    shouldcontinue = True
    for i in operators:
        print(i)


    while shouldcontinue:
        
        operation_symbol = input("enter a operator :  ")
        num2 = float(input("enter next no :  "))
        calculation_function = operators[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"to contiue with  {answer}  type 'y' to start new type 'n :") == 'y':
            num1 = answer
        else:
            shouldcontinue = False
            os.system('cls')
            calculator()


calculator()



