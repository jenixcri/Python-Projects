from time import sleep
import random
verde = '\033[32m'
red = '\033[31m'
ama = '\033[33m'
roxo = '\033[35m'
lim = '\033[m'
print(f'{roxo}=-={lim}'*15)
p = int(input('''[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura
Qual a sua escolha?'''))
print(f'{roxo}=-={lim}'*15)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print(f'{roxo}=-={lim}'*15)
item = ('pedra', 'papel', 'tesoura')
esc = random.randint(0,2)
if esc == p:
    print(f'''Nós {ama}empatamos{lim}...
escolhi {item[esc]} e você também escolheu {item[p]}''')
if esc != p:
    if esc == 2 and p == 1 or esc == 1 and p == 0 or esc == 0 and p == 2:
        print(f'''Você {red}PERDEU!{lim}
ganhei de você hahaha, escolhi {item[esc]}
você escolheu {item[p]}.''')
    else:
        print(f'''Você {verde}GANHOU!{lim}
escolhi {item[esc]} e você escolheu {item[p]} :(''')
