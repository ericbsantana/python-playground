from math import cos, sin, sqrt, tan

n1 = float(input("Digite o primeiro número: "))
operator = str(input("Digite a operação: "))

match operator:
    case '/':
        print(f'√{n1} = {sqrt(n1)}')
    case 'sen':
        print(f'cos{n1} = {cos(n1)}')
    case 'cos':
        print(f'sen{n1} = {sin(n1)}')
    case 'tan':
        print(f'tan{n1} = {tan(n1)}')

n2 = float(input("Digite o segundo número: "))

match operator:
    case ':':
        print(f'{n1} : {n2} = {n1 / n2}')
    case 'x':
        print(f'{n1} x {n2} = {n1 * n2}')
    case '+':
        print(f'{n1} + {n2} = {n1 + n2}')
    case '-':
        print(f'{n1} - {n2} = {n1 - n2}')
    case '^':
        print(f'{n1} ^ {n2} = {n1 ** n2}')
    case 'm':
        print(f'Média entre {n1} e {n2} = {(n1 + n2) / 2}')
