n = int(input())

mentira = 0

for i in range(2, n):
    if n % i == 0:
        if mentira:
            mentira += 1
            break

        mentira += 1

if mentira == 1:
    print('sim')
else:
    print('nao')
