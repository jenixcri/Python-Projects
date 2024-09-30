num = (int(input('Digite um número:')),
        int(input('Digite outro número:')),
        int(input('Digite o penúltimo número:')),
        int(input('Digite o último número:')))
print('-_-'*15)
print(f'Você digitou: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
print(f'O primeiro valor 3 foi digitado na posição {num.index(3)+1}')
print(f'Os números pares foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n} ',end='')
