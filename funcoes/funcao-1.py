def saudacao(nome, idade):
    print(f"Olá {nome}! Você tem {idade}!")

saudacao("Maria", 20)
saudacao(nome="João", idade=21)
saudacao(idade=30, nome="José") # Quando os parâmetros são nomeados a ordem é irrelevante.