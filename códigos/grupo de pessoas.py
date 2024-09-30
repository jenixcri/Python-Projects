title = 'Análise de Pessoas'
cores = {'ama':'\033[1;33m',
         'lim':'\033[m',
         'azul':'\033[1;32m'}

print(f'{cores['ama']}', '=-='*15, f'{cores['lim']}')
print(f'{title:^47}')
print(f'{cores['ama']}', '=-='*15, f'{cores['lim']}')

idade = sexo = cont = acu = maior = fem = masc = 0
while True:
    acu += 1
    sexo = input(f'{cores['azul']} --> {cores['lim']}Digite o sexo da {acu}° pessoa [M/F]:').strip()
    idade = int(input(f'Digite a idade da {acu}° pessoa: '))
    cont = input('Deseja continuar [S/N]?').strip()
    print(' ')
    if idade > 18:
        maior += 1
    if sexo in 'Mm':
        masc += 1
    elif sexo in 'Ff' and idade < 20:
        fem += 1
    if cont in 'nN':
        break
print(f'''No grupo de {acu} pessoas existem:
{maior} pessoas maiores que 18 anos
{masc} homens e {fem} mulheres menores que 20 anos''')