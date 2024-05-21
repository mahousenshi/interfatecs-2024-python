from math import cos, sin

n, angle = list(map(int, input().split()))

angle = angle * 3.1415/180

saida = []

for _ in range(n):
    x, y = list(map(int, input().split()))
    saida.append(f'{x * cos(angle) - y * sin(angle):.2f} {x * sin(angle) + y * cos(angle):.2f}')

print('\n'.join(saida))
