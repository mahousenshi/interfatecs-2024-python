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

regioes_f = [(value, i) for i, value in enumerate(regioes.values())]
regioes_f.sort(reverse=True)

maxr = regioes_f[0][0]

regioes_f = [regiao for regiao in regioes_f if regiao[0] == maxr]
regioes_f.sort(key=lambda x: x[1])

print(list(regioes)[regioes_f[0][1]])
