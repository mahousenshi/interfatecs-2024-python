j = int(input())

jogadores = {input().strip(): 0 for jogador in range(j)}

r = int(input())

for _ in range(r):
    mao = sum(map(int, input().split()))

    for jogador, aposta in zip(jogadores, list(map(int, input().split()))):
        if aposta == mao:
            jogadores[jogador] += 1
            break

final = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)

if final[0][1] == final[1][1]:
    print('EMPATE')
else:
    print(f'{final[0][0]} GANHOU')
