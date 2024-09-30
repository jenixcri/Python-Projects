azul = '\033[34m'
limpa = '\033[m'
verde = '\033[32m'
vermelho = '\033[31m'
print(f'{azul}','=-'*30, f'{limpa}')
salario = int(input('Qual o seu salário?'))
casa = int(input('Qual o valor da casa?'))
anos = int(input('Em quantos anos deseja pagar?'))
ano = anos*12
p = casa/ano
po = (30*salario)/100
if p<=po:
    print('{}SEU FINANCIAMENTO FOI APROVADO{}, suas parcelas serão de R${:.2f} durante {} anos!!!'.format(verde, limpa, p, anos))
else:
    print('{}SEU FINANCIAMENTO FOI NEGADO{}, suas parcelas seriam de R${:.2f} durante {} anos. Portanto, seria inviável.'.format (vermelho, limpa, p, anos))
print(f'{azul}','=-'*30, f'{limpa}')