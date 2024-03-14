geracoes = {
    "silenciosa": 1945,
    "baby_boomers": 1964,
    "x": 1980,
    "millennials": 1996,
    "centennials": 2012,
    "alpha": 2024
}

ano_nascimento = int(input("Qual o seu ano de nascimento: "))

if (ano_nascimento <= geracoes["silenciosa"]):
    print(f"Sua geração é: Silenciosa")
elif (ano_nascimento <= geracoes["baby_boomers"]):
    print(f"Sua geração é: Baby Boomer")
elif (ano_nascimento <= geracoes["x"]):
    print(f"Sua geração é: X")
elif (ano_nascimento <= geracoes["millennials"]):
    print(f"Sua geração é: Millennials")
elif (ano_nascimento <= geracoes["centennials"]):
    print(f"Sua geração é: Centennials")
elif (ano_nascimento <= geracoes["alpha"]):
    print(f"Sua geração é: Alpha")
