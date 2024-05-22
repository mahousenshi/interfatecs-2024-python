a, b, c = tuple(map(int, input().split()))

if b > a > c or c > a > b or a == b or a == c:
    print(a)
elif a > b > c or c > b > a or b == c:
    print(b)
elif a > c > b or b > c > a:
    print(c)
