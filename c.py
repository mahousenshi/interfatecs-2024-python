carrinho, n = list(map(int, input().split()))

alvo = 200 - carrinho

precos = [int(input()) for _ in range(n)]
precos.sort()

for i in range(n):
    alvo1 = alvo - precos[i]
    esq = i + 1
    dire = n - 1

    while esq < dire:
        if precos[esq] + precos[dire] == alvo1:
            print('fretegratis')
            quit()
        elif precos[esq] + precos[dire] < alvo1:
            esq += 1
        else:
            dire -= 1

print('fretepago')
