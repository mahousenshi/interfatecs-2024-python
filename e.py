n = int(input())

perfil = list(map(int, input().split()))

m = int(input())

result = []

for _ in range(m):
    regiao = input().split()
    disp = list(map(int, regiao[1:]))

    equipes = min([d // p for p, d in zip(perfil, disp)])

    result.append(f'{regiao[0]} {equipes}')

print('\n'.join(result))
