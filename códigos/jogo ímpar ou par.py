import random
print('=-='*15)
title = 'VAMOS JOGAR PAR OU ÍMPAR'
print(f'{title:^43}')
print('=-='*15)

val = ip = soma = acu = 0
rand = random.randint(0, 10)
while True:
    val = int(input('Diga um valor: '))
    ip = str(input('Ímpar ou Par [I/P]?'))
    soma = val + rand
    print('=-=' * 15)
    print(f'Você jogou {val} e o computador {rand}, O total deu {soma} que é ',end='')
    if soma % 2 == 0:
        print('par')
    else:
        print('ímpar')
    print('=-=' * 15)
    if ip in 'Pp' and soma % 2 == 0:
        print('Você ganhou! O resultado foi PAR.')
        acu += 1
    if ip in 'Ii' and soma % 2 != 0:
        print('Você Ganhou! O resultado foi ÍMPAR.')
        acu += 1
    if ip in 'Pp' and soma % 2 != 0:
       break
    if ip in 'Ii' and soma % 2 == 0:
        break
    rand = random.randint(0, 10)
print(f'Você perdeu com {acu} vitórias!')