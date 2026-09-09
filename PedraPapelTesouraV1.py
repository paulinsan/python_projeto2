import random

opcoes = ["Pedra ⛰️", "Papel 📄", "Tesoura ✂️"]

while True:

    computador = random.choice(opcoes)

    print('''
===== PEDRA, PAPEL OU TESOURA??? =====
[1] Pedra ⛰️
[2] Papel 📄
[3] Tesoura ✂️
''')
    
    while True:
        jogador = int(input("Você escolhe pedra, papel ou tesoura??? "))

        if jogador == 1:
            jogador = "Pedra ⛰️"
            break

        elif jogador == 2:
            jogador = "Papel 📄"
            break

        elif jogador == 3:
            jogador = "Tesoura ✂️"
            break

        else:
            print("❌ Opção inválida! Por favor, escolha entre 1, 2 ou 3. ")

    print(f"Você escolheu: {jogador}")
    print(f"Seu adversário escolheu: {computador}")

    if jogador == computador:
        print("👀 Empate! 👀")

    elif jogador == "Pedra ⛰️" and computador == "Tesoura ✂️":
        print("🏆 Você venceu! 🏆")

    elif jogador == "Papel 📄" and computador == "Pedra ⛰️":
        print("🏆 Você venceu! 🏆")

    elif jogador == "Tesoura ✂️" and computador == "Papel 📄":
        print("🏆 Você venceu! 🏆")

    else:
        print("😓 Você perdeu! 😓")

    jogar_novamente = input("Deseja jogar novamente? [S/N]: ").lower()
    if jogar_novamente == "n":
        print("Encerrando o jogo. . . ")
        break