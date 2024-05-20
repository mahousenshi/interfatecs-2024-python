import timeit
from itertools import combinations


def frete_gratis_combinacoes(V, N, precos):
    target = 200 - V
    for combo in combinations(precos, 3):
        if sum(combo) == target:
            return "fretegratis"
    return "fretepago"


def frete_gratis_dicionario(V, N, precos):
    target = 200 - V
    freq_precos = {}
    for p in precos:
        if p in freq_precos:
            freq_precos[p] += 1
        else:
            freq_precos[p] = 1

    for p1 in freq_precos:
        for p2 in freq_precos:
            if p1 == p2 and freq_precos[p1] < 2:
                continue
            p3 = target - p1 - p2
            if p3 in freq_precos:
                if p3 != p1 and p3 != p2:
                    return "fretegratis"
                elif (p3 == p1 and freq_precos[p1] >= 2) or (p3 == p2 and freq_precos[p2] >= 2):
                    return "fretegratis"
    return "fretepago"


def frete_gratis_dicionario_2(V, N, precos):
    target = 200 - V
    freq_precos = {}
    for p in precos:
        if p in freq_precos:
            freq_precos[p] += 1
        else:
            freq_precos[p] = 1

    for p1 in freq_precos:
        remaining = target - p1
        for p2 in freq_precos:
            if p2 <= remaining:
                p3 = remaining - p2
                if p3 in freq_precos:
                    if p1 != p2 and p1 != p3 and p2 != p3:
                        return "fretegratis"
                    elif (p1 == p2 and freq_precos[p1] >= 2) or (p1 == p3 and freq_precos[p1] >= 2) or (
                            p2 == p3 and freq_precos[p2] >= 2):
                        return "fretegratis"
    return "fretepago"


def frete_gratis_twosum(V, N, precos):
    alvo = 200 - V

    precos.sort()

    for i in range(N):
        alvo2 = alvo - precos[i]
        esq = i + 1
        dire = N - 1

        while esq < dire:
            if precos[esq] + precos[dire] == alvo2:
                return 'fretegratis'
            elif precos[esq] + precos[dire] < alvo2:
                esq += 1
            else:
                dire -= 1

    return 'fretepago'


def test():
    V = 52
    N = 10
    precos = [50, 30, 33, 91, 68, 40, 30, 32, 41, 39]

    start1 = timeit.default_timer()
    resultado1 = frete_gratis_combinacoes(V, N, precos)
    end1 = timeit.default_timer()
    runtime1 = (end1 - start1) * 1e9

    start2 = timeit.default_timer()
    resultado2 = frete_gratis_dicionario(V, N, precos)
    end2 = timeit.default_timer()
    runtime2 = (end2 - start2) * 1e9

    start3 = timeit.default_timer()
    resultado3 = frete_gratis_dicionario_2(V, N, precos)
    end3 = timeit.default_timer()
    runtime3 = (end3 - start3) * 1e9

    start7 = timeit.default_timer()
    resultado7 = frete_gratis_twosum(V, N, precos)
    end7 = timeit.default_timer()
    runtime7 = (end7 - start7) * 1e9

    print(f"frete_gratis_dicionario Teste 1:            {runtime1:.5f} nanosegundos - Resultado: {resultado1}")
    print(f"frete_gratis_combinacoes Teste 1:           {runtime2:.5f} nanosegundos - Resultado: {resultado2}")
    print(f"frete_gratis_dicionario_otimizado Teste 1:  {runtime3:.5f} nanosegundos - Resultado: {resultado3}")
    print(f"frete_gratis_twosum Teste 1:                {runtime7:.5f} nanosegundos - Resultado: {resultado7}")

    V2 = 34
    N2 = 10
    precos2 = [50, 30, 33, 91, 68, 40, 30, 32, 41, 38]

    start4 = timeit.default_timer()
    resultado4 = frete_gratis_combinacoes(V2, N2, precos2)
    end4 = timeit.default_timer()
    runtime4 = (end4 - start4) * 1e9

    start5 = timeit.default_timer()
    resultado5 = frete_gratis_dicionario(V2, N2, precos2)
    end5 = timeit.default_timer()
    runtime5 = (end5 - start5) * 1e9

    start6 = timeit.default_timer()
    resultado6 = frete_gratis_dicionario_2(V2, N2, precos2)
    end6 = timeit.default_timer()
    runtime6 = (end6 - start6) * 1e9

    start8 = timeit.default_timer()
    resultado8 = frete_gratis_twosum(V2, N2, precos2)
    end8 = timeit.default_timer()
    runtime8 = (end8 - start8) * 1e9

    print()
    print(f"frete_gratis_dicionario Teste 2:            {runtime4:.5f} nanosegundos - Resultado: {resultado4}")
    print(f"frete_gratis_combinacoes Teste 2:           {runtime5:.5f} nanosegundos - Resultado: {resultado5}")
    print(f"frete_gratis_dicionario_otimizado Teste 2:  {runtime6:.5f} nanosegundos - Resultado: {resultado6}")
    print(f"frete_gratis_twosum Teste 2:                {runtime8:.5f} nanosegundos - Resultado: {resultado8}")



def main():
    test()


if __name__ == "__main__":
    main()
