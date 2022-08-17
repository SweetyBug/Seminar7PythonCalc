import sys
import rational as op

def x():
    firstnum = float(input('Введите первое число: ').replace(',', '.'))
    return firstnum

def y():
    secondnum = float(input('Введите второе число: ').replace(',', '.'))
    return secondnum

def selectoperation():
    global operation
    operation = (input('Введите операцию: +, -, *, /: '))
    if operation == '+' or '-' or '/' or '*':
        return operation
    else:
        print('Invalid syntax')

def res(firstnum, secondnum):
    if operation == '+':
        res = firstnum + secondnum
        result = round(res, 3)
        return result
    elif operation == '-':
        res = firstnum - secondnum
        result = round(res, 3)
        return result
    elif operation == '*':
        res = firstnum * secondnum
        result = round(res, 3)
        return result
    elif operation == '/':
        res = firstnum / secondnum
        result = round(res, 3)
        return result
    else:
        print('Invalid syntax')

def mainterminal():
    global file
    x = op.x()
    while True:
        y = op.y()
        oper = op.selectoperation()
        res = op.res(x, y)
        file = 'results.txt'
        with open('results.txt', 'a') as data:
            data.write(f'{x} {oper} {y} = {res}\n')
        print(f'{x} {oper} {y} = {res}\n' )
        again = input('Вы хотите продолжить? Да/Нет: ').lower()
        if again == 'да':
            useresult = input('Вы хотите использовать результат последней операции? (Да/не): ').lower()
            if useresult == 'да':
                x = res
                continue
            elif useresult == 'нет':
                break
            else:
                sys.exit()
        else:
            sys.exit()