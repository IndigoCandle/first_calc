# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def AllOp(first_num,second_num, operand):
    if operand == '+':
        return first_num + second_num
    elif operand == '-':
        return first_num - second_num
    elif operand == '*':
        return first_num * second_num
    elif operand == '/' and second_num != 0:
        return first_num / second_num
    elif operand == '**':
        return first_num ** second_num
    else:
        print("invalid input")

def calculator():
    first_num = input()
    operand = input()
    second_num = input()
    first_num = float(first_num)
    second_num = float(second_num)
    result = AllOp(first_num,second_num,operand)
    print(first_num + " " + operand + " " + second_num + " = " + result)

def main():
    calculator()