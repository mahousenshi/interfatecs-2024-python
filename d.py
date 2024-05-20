from math import cos, sin

n, angle = list(map(int, input().split()))

angle = angle * 3.1415/180

result = []

for _ in range(n):
    x, y = list(map(int, input().split()))
    result.append(f'{x * cos(angle) - y * sin(angle):.2f} {x * sin(angle) + y * cos(angle):.2f}')

print('\n'.join(result))
