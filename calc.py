op1 = 0.0
op2 = 0.0
op = ''
while (op1 != 'q'):
    print('enter your first number:')
    op1 = input()
    if op1 == 'q':
        break
    op1 = float(op1)
    print('enter your second number:')
    op2 = input()
    print('Enter the operation (+, -, *, /):')
    op = input()
    if op2 == 'q':
        break
    op2 = float(op2)
    if op == '+':
        print(op1 + op2)
    elif op == '-':
        print(op1 - op2)
    elif op == '*':
        print(op1 * op2)
    elif op == '/':
        print(op1 / op2)
    else:
        print('Didn\'t recognize you request.')
