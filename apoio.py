n = int(input())

perfil = list(map(int, input().split()))

m = int(input())

saida = []

for _ in range(m):
    regiao = input().split()
    disp = list(map(int, regiao[1:]))

    equipes = min([d // p for p, d in zip(perfil, disp)])

    saida.append(f'{regiao[0]} {equipes}')

print('\n'.join(saida))
