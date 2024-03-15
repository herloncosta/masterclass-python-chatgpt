from functools import reduce


def quadrado(x: int):
    return x * x


# Atribuindo uma função a uma variável
funcao = quadrado
print(funcao(5))


# Passando uma função como argumento
def aplicar_funcao(f, valor):
    return f(valor)


print(aplicar_funcao(quadrado, 10))


# Retorando uma função a partir de outra função
def cria_funcao():
    print("Execução externa")

    def nova_funcao():
        print("Execução interna")

    return nova_funcao


funcao = cria_funcao()  # Externa
funcao()  # Interna


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map: aplicando uma função para todos os elementos de uma lista
quadrado_numeros = list(map(quadrado, numeros))
print(quadrado_numeros)


# Filter: filtrar os elementos de uma lista, com base em uma função
def ehPar(x: int):
    return x % 2 == 0


numeros_pares = list(filter(ehPar, numeros))
print(numeros_pares)


# Reduce: reduzir uma lista a um único valor, aplicando uma função acumuladora
def somar(x: int, y: int):
    return x + y


total_soma_numeros_pares = reduce(somar, numeros_pares)
print(total_soma_numeros_pares)
