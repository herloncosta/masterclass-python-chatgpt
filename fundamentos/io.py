# ENTRADA DE DADOS
nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

# INTERPOLAÇÃO DE STRING
print(f"\n\nDados do Usuário \nNome: {nome}\nIdade: {idade}")

# CONVERSÃO DE TIPO
# print(idade + 1) -> TypeError: can only concatenate str (not "int") to str

print(type(idade))  # <class 'str'>

idadeNumero = int(idade)
print(type(idadeNumero))  # <class 'int'>

# INFERÊNCIA DIRETA A PARTIR DO INPUT
valor = int(input("O valor digitado será convertido para o tipo int: "))
print(type(valor))  # <class 'int'>
