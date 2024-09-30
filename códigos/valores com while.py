acu = 1
soma = 0
perg = int(input('Digite um número [999 para parar]:'))
while perg != 999:
     if perg != 999:
          acu += 1
          soma += perg
          perg = int(input('Digite um número [999 para parar]:'))
     else:
          perg = 0

print(f'A soma de todos os {acu - 1} valores é {soma}')