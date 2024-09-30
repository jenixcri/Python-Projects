import random
count = 1
num = random.randint(0, 10)
print('-->'*15)
print('            JOGO DA ADVINHAÇÃO')
print('-->'*15)
ask = int(input('Digite um número de 0 à 10:'))
while ask != num:
    ask = int(input('Você não acertou! tente novamente:'))
    count += 1
print(f'Você adivinhou, escolhi o número {num} e você o mesmo! com {count} tentativas!!')