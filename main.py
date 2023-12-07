'''
File Name: calculator.py
Name: Rom Yannay
ID: 326450228
Date: 07/12/2023
Description:
This program calculates the resukt of an operation on two numbers entered by the user,
 based on the operand while making sure all inputs are valid.
'''


# The AllOp is in charge of performing the calculations and error handling
def AllOp(first_num, second_num, operand):
    if operand == '+':
        return first_num + second_num
    elif operand == '-':
        return first_num - second_num
    elif operand == '*':
        return first_num * second_num
    elif operand == '/':
        if second_num != 0:
            return first_num / second_num
        else:
            return "Error: Division by zero"
    elif operand == '**':
        return first_num ** second_num
    else:
        return "Invalid operand"


# This is the calculator function. Its purpose is to read the input from the user and send them over for calculation.
# it also checks for invalid inputs
def calculator():
    try:
        first_num = float(input("Enter first number: "))
        operand = input("Enter an operand (+, -, *, /, **): ")
        second_num = float(input("Enter second number: "))
        result = AllOp(first_num, second_num, operand)
        print(f"{first_num} {operand} {second_num} = {result}")
    except ValueError:
        print("Invalid input: Please enter numbers only.")


# the main function runs as long as the user wants to keep calculating.
def main():
    while True:
        calculator()
        if input("Do another calculation? (yes/no): ").lower() != 'yes':
            break


if __name__ == "__main__":
    main()
