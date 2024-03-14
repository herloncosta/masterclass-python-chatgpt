produto = {
    "nome": "Notebook",
    "preco": 2.500,
    "quantidade": 100
}

# Acessando todas as chaves do objeto
for chave in produto:
    print(chave)

# Acessando chaves e valores
for chave in produto:
    print(f"{chave} => {produto[chave]}")

# Utilizando métodos built-in
for chave in produto.keys():
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(f"{chave} => {valor}")
