num = quest = 0
tabu = int(input('Você quer tabuada de qual valor?'))
while True:
    if num >= 10:
        num = 0
        tabu = int(input('Você quer tabuada de qual valor?'))
        if tabu < 0:
            break
    num += 1
    print(f'{tabu} x {num} = {tabu*num}')
print('Fim do programa ;)')
