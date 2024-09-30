from time import sleep
cor = {'azul':'\033[1;34m',
       'lim':'\033[m'}
print(f'{cor['azul']}','_-_'*15, f'{cor['lim']}')
num = int(input('Digite um número para saber o seu fatorial:'))
n = num
f = 1
print(f'Calculando {num}!: ', end='')
while n > 0:
    print(f'{n}',end='')
    print(' x ' if n > 1  else ' = ', end='')
    f *= n
    n -= 1
print(f'{f}')
print(f'{cor['azul']}' , '_-_'*15, f'{cor['lim']}')
sleep(1)
print('fim do programa')
