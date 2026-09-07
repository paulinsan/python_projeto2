import random

opcoes = ["pedra", "papel", "tesoura"]

jogador = input("Você escolhe pedra, papel ou tesoura? ").lower().strip()

computador = random.choice(opcoes)

print(f"Você escolheu: {jogador}")
print(f"Seu adversário escolheu: {computador}")

if jogador == computador:
    print("Empate! ")

elif jogador == "pedra" and computador == "tesoura":
    print("Você venceu! ")

elif jogador == "papel" and computador == "pedra":
    print("Você venceu! ")

elif jogador == "tesoura" and computador == "papel":
    print("Você venceu! ")
 
else:
    print("Você perdeu! ")
    