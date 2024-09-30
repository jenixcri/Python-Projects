valor = float(input('digite o valor da sua compra:'))
print('[ 1 ] à vista/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
esc = float(input('Qual opção deseja?'))
if esc == 1:
    print('A sua compra no valor de {}R$ ficará à vista por {:.2f}R$ com desconto de 10%'.format(valor, valor-(10/100)*valor))
elif esc == 2:
    print('A sua compra no valor de {}R$ ficará à vista no cartão por {:.2f}R$ com desconto de 5%'.format(valor, valor-(5/100)*valor))
if esc == 3:
    a = input('1x no crédito ou 2x?')
    if a == 1:
        print(f'A sua compra ficará 1x no cartão de {valor}R$')
    else:
        print('A sua compra ficará no valor de 2 parcelas de {:.2f}R$'.format(valor/2))
if esc == 4:
    b = float(input('Quantas parcelas deseja?'))
    c = valor + (20/100)*valor
    print('A sua compra no valor de {}R$ ficará em {}x de {:.2f} pois o valor completo com juros de 20% é {}R$'.format(valor, b, c/b, c))