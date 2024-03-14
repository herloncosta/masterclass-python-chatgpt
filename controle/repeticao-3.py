pergunta = "Deseja continuar? (s/n) "
resposta = input(pergunta)
repeticoes = 0

while resposta.lower() != "n":
    print("Continuando...")
    resposta = input(pergunta)
    repeticoes += 1

print("Fim da execução!")
