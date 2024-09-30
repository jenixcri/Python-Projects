print('==='*10)
print('{:^30}'.format('BANCO FUN'))
print('==='*10)
valor = int(input('Digite o valor do saque:'))
total = valor
totced = 0
céd = 50
while True:
    if total >= céd:
        total -= céd
        totced += 1
    else:
        if total > 0:
            print(f'O total de {totced} de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totced = 0
        if total == 0:
            break