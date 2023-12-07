# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



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

def calculator():
    try:
        first_num = float(input("Enter first number: "))
        operand = input("Enter an operand (+, -, *, /, **): ")
        second_num = float(input("Enter second number: "))
        result = AllOp(first_num, second_num, operand)
        print(f"{first_num} {operand} {second_num} = {result}")
    except ValueError:
        print("Invalid input: Please enter numbers only.")

def main():
    while True:
        calculator()
        if input("Do another calculation? (yes/no): ").lower() != 'yes':
            break

if __name__ == "__main__":
    main()
