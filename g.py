n = int(input())

assuntos = {
    'ALGORITMOS': [],
    'BOAS PRATICAS': [],
    'DESEMPENHO': [],
    'FLUXOGRAMAS': [],
    'INTERPRETACAO DE ENUNCIADOS': [],
    'SINTAXE DA LINGUAGEM': [],
    'FICA PARA A PROXIMA!': []
}

while True:
    try:
        alunos = input().split()
        categorias = list(map(int, alunos[1:]))

        if n > 0:
            for categoria in categorias:
                key = list(assuntos)[categoria-1]
                assuntos[key].append(alunos[0])
        else:
            assuntos["FICA PARA A PROXIMA!"].append(alunos[0])

        n -= 1
    except EOFError:
        break

for i, key in enumerate(assuntos):
    if key != "FICA PARA A PROXIMA!":
        if i:
            print()

        print('-' * 30)
        print(key)
        print('-' * 30)

        if assuntos[key]:
            print('\n'.join(sorted(assuntos[key])))

    elif assuntos[key]:
        print()
        print('-' * 30)
        print(key)
        print('-' * 30)
        print('\n'.join(assuntos[key]))
