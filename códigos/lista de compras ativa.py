produto = valor = caro = soma = barato = acu = barato2 = 0
title = ' LISTA DE COMPRAS '
print(f'{title:=^40}')
while True:
    produto = str(input('Qual o nome do produto? '))
    valor = int(input('Qual o valor do produto? '))
    quest = str(input('-> Deseja continuar [S/N]?'))
    print('---'*10)
    soma += valor
    acu += 1
    if acu == 1 or valor < barato:
        barato = valor
        barato2 = produto
    if valor > 1000:
        caro += 1
    if quest not in 'SsNn':
        quest = str(input('-> Deseja continuar [S/N]?'))
    else:
        if quest in 'Nn':
            break
print(f'''A compra ficou no valor de: R${soma}
{caro} itens foram mais que 1000R$
O item mais barato foi: {barato2} no valor de R${barato}''')
