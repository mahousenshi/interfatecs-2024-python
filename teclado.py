n = int(input())

saida = []

for _ in range(n):
    palavras = input()

    telefone = ''
    for ch in palavras:
        if ch in 'ABC':
            telefone += '2'
        if ch in 'DEF':
            telefone += '3'
        if ch in 'GHI':
            telefone += '4'
        if ch in 'JKL':
            telefone += '5'
        if ch in 'MNO':
            telefone += '6'
        if ch in 'PQRS':
            telefone += '7'
        if ch in 'TUV':
            telefone += '8'
        if ch in 'WXYZ':
            telefone += '9'

    saida.append(telefone)

print('\n'.join(saida))
