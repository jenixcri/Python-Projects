from time import sleep
n1 = int(input('digite o primeiro valor:'))
n2 = int(input('digite o segundo valor:'))
op = 0
cor = {'roxo':'\033[1;35m',
         'lim':'\033[m'}
while op != 5:
    print(f'{cor['roxo']}','---'*15,f'{cor['lim']}')
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair''')
    op = int(input('escolha uma das opções: '))
    print(f'{cor['roxo']}', '---' * 15, f'{cor['lim']}')
    if op == 1:
        print(f'>>>O resultado da soma é {n1 + n2}')
    elif op == 2:
        print(f'>>>O valor da multiplicação entre {n1} e {n2} é {n1 * n2}')
    elif op == 3:
        if n1 > n2:
            print(f'>>>{n1} é maior que {n2}')
        elif n1 == n2:
            print('>>>Os dois números são iguais')
        else:
            print(f'>>>{n2} é maior que {n1}')
    elif op == 4:
        print('informe os números novamente')
        n1 = int(input('digite o primeiro valor:'))
        n2 = int(input('digite o segundo valor:'))
    elif op == 5:
        print('finalizando...')
    else:
        print('opção inválida, tente novamente!')
sleep(1)
print('você saiu do programa')
