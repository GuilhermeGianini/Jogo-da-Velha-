def exibir_tabuleiro(tabuleiro):
    print("\n")
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)


def verificar_vencedor(tabuleiro, jogador):
    for i in range(3):
        if (tabuleiro[i][0] == jogador and
            tabuleiro[i][1] == jogador and
            tabuleiro[i][2] == jogador):
            return True

        if (tabuleiro[0][i] == jogador and
            tabuleiro[1][i] == jogador and
            tabuleiro[2][i] == jogador):
            return True

    if (tabuleiro[0][0] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][2] == jogador):
        return True

    if (tabuleiro[0][2] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][0] == jogador):
        return True

    return False


def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        for casa in linha:
            if casa == " ":
                return False
    return True


def jogada_valida(tabuleiro, linha, coluna):
    if linha < 1 or linha > 3 or coluna < 1 or coluna > 3:
        return False

    if tabuleiro[linha - 1][coluna - 1] != " ":
        return False

    return True


def jogar():
    tabuleiro = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    jogador1 = input("Jogador 1, escolha X ou O: ").upper()

    while jogador1 != "X" and jogador1 != "O":
        print("Escolha inválida!")
        jogador1 = input("Escolha X ou O: ").upper()

    if jogador1 == "X":
        jogador2 = "O"
    else:
        jogador2 = "X"

    jogador_atual = jogador1

    print("\nJogador 1:", jogador1)
    print("Jogador 2:", jogador2)

    while True:
        exibir_tabuleiro(tabuleiro)

        print("Vez do jogador", jogador_atual)

        try:
            linha = int(input("Digite a linha (1 a 3): "))
            coluna = int(input("Digite a coluna (1 a 3): "))
        except ValueError:
            print("Digite apenas números!")
            continue

        if not jogada_valida(tabuleiro, linha, coluna):
            print("Jogada inválida! Tente novamente.")
            continue

        tabuleiro[linha - 1][coluna - 1] = jogador_atual

        if verificar_vencedor(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print("Jogador", jogador_atual, "venceu!")
            break

        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("O jogo terminou empatado!")
            break

        if jogador_atual == jogador1:
            jogador_atual = jogador2
        else:
            jogador_atual = jogador1


jogar()