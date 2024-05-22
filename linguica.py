qtd = int(input())

heap = [0] + [int(input()) for n in range(qtd)]

tipo0 = 0
tipo1 = 1
tipo2 = 1

for i, n in enumerate(heap[1:], start=1):
    left = heap[2*i] if 2*i <= qtd else None
    right = heap[(2*i) + 1] if (2*i) + 1 <= qtd else None
    print(n, left, right)

    if left is not None:
        if tipo1 and n > left:
            tipo1 = 0

        if tipo2 and n < left:
            tipo2 = 0

    if right is not None:
        if tipo1 and n > right:
            tipo1 = 0

        if tipo2 and n < right:
            tipo2 = 0

    if not tipo1 and not tipo2:
        tipo0 = 1
        break

if tipo0:
    print(0)
elif tipo1:
    print(1)
elif tipo2:
    print(2)
