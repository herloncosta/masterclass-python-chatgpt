# Criando uma lista de 0 a 9
numeros = [x for x in range(10)]
print(numeros)


# Criando uma lista com os quadros dos números de 0 a 4
quadrados = [x**2 for x in range(5)]
print(quadrados)


# Criando uma lista com os quadrados dos números, filtrando pelos que forem pares
quadrado_numeros_pares = [x**2 for x in range(10) if x % 2 == 0]
print(quadrado_numeros_pares)


# Criando um gerador com os quadrados dos números de 0 a 9
gerador_quadrados = (x**2 for x in range(10))
print(gerador_quadrados)

# Como se trata de um gerador, podemos iterar sobre os valores
for valor in gerador_quadrados:
    print(valor)
