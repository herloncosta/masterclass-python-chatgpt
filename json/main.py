import json


exemplo = """
  {
      "pergunta": "Qual o resultado da soma de 2 + 2?",
      "opcoes": ["2", "31", "4", "17"],
      "resposta_certa": "4"
  }
"""

questao = json.loads(exemplo)

pergunta = questao.get('pergunta')
opcoes = questao.get('opcoes')
resposta_certa = questao.get('resposta_certa')

print(pergunta)

for indice, opcao in enumerate(opcoes, start=1):
    print(f"{indice}) {opcao}")

resposta_usuario = int(input("Qual a resposta certa [1-4]: "))
valor_resposta_usuario = opcoes[resposta_usuario-1]

if (valor_resposta_usuario == resposta_certa):
    print("Você acertou!!!")
else:
    print(f"Você errou. A resposta certa é {resposta_certa}.")
