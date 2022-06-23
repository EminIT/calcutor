first_num = int(input('first number:'))
second_num = int(input('second number:'))
math_operation = input('math operation:')


def division():
    try:
        return first_num / second_num
    except ZeroDivisionError:
        print("you cant divide by zero")


def addition():
    return first_num + second_num


def subtraction():
    return first_num - second_num


def multiplication():
    return first_num * second_num


if math_operation == '+':
    print(addition())


if math_operation == '-':
    print(subtraction())


if math_operation == '*':
    print(multiplication())


if math_operation == '/':
    print(division())


input('type random key to close')