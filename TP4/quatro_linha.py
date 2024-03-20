# a82952
# tp2


from jogo_abs import Jogo
from random import randint


class quatro_linha(Jogo):
    def inicializa_tabuleiro(self) -> None:
        self.numero_de_jogadas_realizadas = 0
        self.tabuleiro = [[" - " for _ in range(7)] for _ in range(7)]

    def mostra_tabuleiro(self) -> None:
        print(45 * "-")
        for linha in range(7):
            for coluna in range(7):
                print(f"| {self.tabuleiro[linha][coluna]} ", end="")
            print("|\n" + 45 * "-")

    def validar_jogada(self, msg: str):
        inputs_validos = {"1", "2", "3", "4", "5", "6", "7"}
        while True:
            pos = input(msg)

            if pos in inputs_validos:
                return int(pos) - 1
            else:
                print("Jogada inválida! Jogador, escolha outra posição: ")

    def joga_humano(self, jogador: int) -> None:
        print(f"\nJogador {jogador}, insira a sua jogada")
        while True:
            coluna = self.validar_jogada("Coluna: ")
            for i in range(6, -1, -1):
                if self.tabuleiro[i][coluna] == " - ":
                    self.tabuleiro[i][coluna] = [" O ", " X "][jogador]
                    self.numero_de_jogadas_realizadas += 1
                    return

    def joga_computador(self, jogador: int) -> None:
        print("\nÉ a vez do computador jogar...")
        while True:
            coluna = randint(0, 6)
            for i in range(6, -1, -1):
                if self.tabuleiro[i][coluna] == " - ":
                    self.tabuleiro[i][coluna] = [" O ", " X "][jogador]
                    self.numero_de_jogadas_realizadas += 1
                    return

    def terminou(self, jogador: int) -> bool:
        for linha in self.tabuleiro:
            if "".join(linha).count(([" O ", " X "][jogador]) * 4) > 0:
                return True

        else:
            for i in range(7):
                if (
                    "".join(self.tabuleiro[j][i] for j in range(7)).count(
                        ([" O ", " X "][jogador]) * 4
                    )
                    > 0
                ):
                    return True

            else:
                for i in range(4):
                    for j in range(4):
                        if (
                            "".join(
                                self.tabuleiro[i + k][j + k] for k in range(4)
                            ).count(([" O ", " X "][jogador]) * 4)
                            > 0
                        ):
                            return True
                        elif (
                            "".join(
                                self.tabuleiro[i + k][j + 3 - k] for k in range(4)
                            ).count(([" O ", " X "][jogador]) * 4)
                            > 0
                        ):
                            return True

    def ha_jogadas_possiveis(self) -> bool:
        return self.numero_de_jogadas_realizadas < 49


if __name__ == "__main__":
    jogo = quatro_linha()
    jogo.jogar()
