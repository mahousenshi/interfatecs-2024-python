n = int(input())

regioes = {
    "superior": 0,
    "esquerda": 0,
    "centro": 0,
    "direita": 0,
    "inferior": 0
}

for _ in range(n):
    for i in range(6):
        linha = list(map(int, input().split()))

        if i == 0:
            regioes['superior'] += sum(linha)
        elif i == 5:
            regioes['inferior'] += sum(linha)
        else:
            regioes['esquerda'] += linha[0]
            regioes['centro'] += linha[1]
            regioes['direita'] += linha[2]

final = sorted(regioes.items(), key=lambda x: x[1], reverse=True)

print(final[0][0])
