import math

while True:
    # inputs:
    num1 = float(input('Enter the first number: '))
    act = input('Enter the action: ')

    num2 = True

    # extra for sqrt
    result6 = math.sqrt(num1)

    if act == 'sqrt':
        print(result6)
        num2 = False
    else:
        num2 = float(input('Enter the second number: '))

    # result variables:
    result1 = num1 + num2
    result2 = num1 - num2
    result3 = num1 * num2
    result5 = pow(int(num1), int(num2))

    #Acts for comparisons
    act4 = num1 == num2
    act5 = num1 != num2



    if act == '=' and act4 is True:
        print('True')
    elif act5 is True:
        print('False')

    act2 = num1 > num2

    if act == '>' and act2 is True:
        print('True')
    elif act2 is False and act == '>':
        print('False')

    act3 = num1 < num2

    if act == '<' and act3 is True:
        print('True')
    elif act3 is False and act == '<':
        print('False')



    # acts:
    if act == '+':
        print(result1)
    elif act == '-':
        result2 = num1 - num2
        print(result2)
    elif act == '*':
        print(result3)
    elif act == '^':
        print(result5)

    if num2 is True and act == '/':
        result4 = num1 / num2
        print(result4)








