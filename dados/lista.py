numeros = [1, 2, 3, 4, 5]

# OPERAÇÃO MATEMÁTICA ACESSANDO ELEMENTOS POR ÍNDICE
print(numeros[1] + numeros[2])

# SUBSTITUIÇÃO DE ELEMENTO ATRAVÉS DO ÍNDICE
numeros[1] = 20
print(numeros)  # [1, 20, 3, 4, 5]

# INSERÇÃO DE NOVO ELEMENTO
numeros.append(6)
print(numeros)  # [1, 20, 3, 4, 5, 6]

# REMOÇÃO DE ELEMENTO
numeros.remove(1)
print(numeros)  # [20, 3, 4, 5, 6]

# ORDENAR OS VALORES
numeros.sort()  # Ordem crescente
numeros.sort(reverse=True)  # Ordem crescente
print(numeros)

# VERIFICANDO TAMANHO DA LISTA (quantidade de elementos)
print(len(numeros))

# VERIFICANDO SE EXISTE UM DETERMINADO ELEMENTO NA LISTA
print(10 in numeros)
print(5 in numeros)
