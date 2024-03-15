def media_simples(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def media_ponderada(n1, n2, n3):
    return (n1 * 5 + n2 * 3 + n3 * 2) / 10


def melhor_media(n1, n2, n3):
    m1 = media_simples(n1, n2, n3)
    m2 = media_ponderada(n1, n2, n3)

    return m1 if m1 > m2 else m2


resultado1 = melhor_media(9, 6, 4)
resultado2 = melhor_media(4, 6, 9)

print(f"{resultado1:.2f}")
print(round(resultado2, 2))
