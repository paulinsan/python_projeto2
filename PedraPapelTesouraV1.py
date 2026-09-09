import random

# Opções disponíveis no jogo
opcoes = ["Pedra ⛰️", "Papel 📄", "Tesoura ✂️"]

# Função de validação se o jogador deseja jogar novamente
def jogar_novamente():

    # Continua perguntando até receber S ou N
    while True: 
        resposta = input("Deseja jogar novamente? [S/N]: ").lower()

        # True significa que vai continuar
        if resposta == "s":
            return True
        
        # False significa que vai encerrar
        elif resposta == "n":
            return False

        # Trata respostas diferentes de S ou N
        else:
            print("❌ Opção inválida! Por favor, Digite 'S' para sim ou 'N' para não. ")

# Pontuação inicial
pontos_jogador = 0
pontos_computador = 0

# Loop principal do jogo
while True:

    # Computador escolhe uma opção aleatória 
    computador = random.choice(opcoes)

    print('''
\n===== PEDRA, PAPEL OU TESOURA??? =====
[1] Pedra ⛰️
[2] Papel 📄
[3] Tesoura ✂️
''')

    # Loop para voltar validação da escolha do jogador
    while True:

        try:
            # Tenta converter a entrada para número inteiro    
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

        except ValueError:
            # Executa quando o jogador digita algo que não é número
            print("❌ Opção inválida! Por favor, escolha entre 1, 2 ou 3. ")

    # Mostra as escolhas de ambos
    print(f"Você escolheu: {jogador}")
    print(f"Seu adversário escolheu: {computador}")

    # Verificação das escolhas
    if jogador == computador:
        print("👀 Empate! 👀")

    elif jogador == "Pedra ⛰️" and computador == "Tesoura ✂️":
        print("🏆 Você venceu! 🏆")

        # Adiciona 1 ponto ao jogador
        pontos_jogador += 1

    elif jogador == "Papel 📄" and computador == "Pedra ⛰️":
        print("🏆 Você venceu! 🏆")

        # Adiciona 1 ponto ao jogador
        pontos_jogador += 1

    elif jogador == "Tesoura ✂️" and computador == "Papel 📄":
        print("🏆 Você venceu! 🏆")

        # Adiciona 1 ponto ao jogador
        pontos_jogador += 1

    else:
        print("😓 Você perdeu! 😓")

        # Adiciona 1 ponto ao computador
        pontos_computador += 1

    # Mostra a pontuação atual
    print(f"\nPlacar autal: Você {pontos_jogador} x {pontos_computador} Computador")

    # Pergunta se o jogador quer continuar
    if not jogar_novamente():

        # Mostra a pontuação final
        print(f"\nPlacar final: Você {pontos_jogador} x {pontos_computador} Computador")
        print("Encerrando o jogo. . . ")
        break