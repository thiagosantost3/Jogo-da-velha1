class Casa:
    def __init__(self):
        self.dominado_por = 0

class Linha:
    def __init__(self):
        self.casa1 = Casa()
        self.casa2 = Casa()
        self.casa3 = Casa()

linha1 = Linha()
linha2 = Linha()
linha3 = Linha()

def domina_casa(i, j, dominador):
    global linha1, linha2, linha3
    if j == 1:
        aux = linha1
    elif j == 2:
        aux = linha2
    elif j == 3:
        aux = linha3

    if i == 1:
        aux.casa1.dominado_por = dominador
    elif i == 2:
        aux.casa2.dominado_por = dominador
    elif i == 3:
        aux.casa3.dominado_por = dominador

def checa_casa(i, j):
    global linha1, linha2, linha3
    if j == 1:
        aux = linha1
    elif j == 2:
        aux = linha2
    elif j == 3:
        aux = linha3

    if i == 1:
        return aux.casa1.dominado_por
    elif i == 2:
        return aux.casa2.dominado_por
    elif i == 3:
        return aux.casa3.dominado_por

def desenhar_jogo():
    print("+---+---+---+")
    for j in range(1, 4):
        print("|", end="")
        for i in range(1, 4):
            aux = checa_casa(i, j)
            if aux == 0:
                print("   ", end="")
            elif aux == 1:
                print(" X ", end="")
            elif aux == 2:
                print(" O ", end="")
            print("|", end="")
        print("\n+---+---+---+")

def checa_win():
    for i in range(1, 4):
        aux1 = checa_casa(1, i)
        aux2 = checa_casa(2, i)
        aux3 = checa_casa(3, i)
        if aux1 == aux2 == aux3 != 0:
            return aux1
        aux1 = checa_casa(i, 1)
        aux2 = checa_casa(i, 2)
        aux3 = checa_casa(i, 3)
        if aux1 == aux2 == aux3 != 0:
            return aux1

    aux1 = checa_casa(1, 1)
    aux2 = checa_casa(2, 2)
    aux3 = checa_casa(3, 3)
    if aux1 == aux2 == aux3 != 0:
        return aux1

    aux1 = checa_casa(1, 3)
    aux3 = checa_casa(3, 1)
    if aux1 == aux2 == aux3 != 0:
        return aux1

    return 0

def loop_jogo(jogador):
    aux = 5
    while aux != 0:
        desenhar_jogo()
        confirma = 5
        while confirma != 1:
            tmp_linha = 5
            while tmp_linha < 1 or tmp_linha > 3:
                tmp_linha = int(input(f"Jogador {jogador}. Em que linha deseja jogar? "))
            tmp_coluna = 5
            while tmp_coluna < 1 or tmp_coluna > 3:
                tmp_coluna = int(input(f"Jogador {jogador}. Em que coluna deseja jogar? "))
            confirma = 5
            while confirma < 1 or confirma > 2:
                confirma = int(input(f"Jogador {jogador}. Confirma? (1 Sim / 2 Nao) "))
        aux = checa_casa(tmp_coluna, tmp_linha)
        if aux != 0:
            print("Casa em uso. Escolha outra.")

def joga_computador():
    aux1 = checa_casa(2, 2)
    if aux1 == 0:
        domina_casa(2, 2, 2)
        return 0

    for j in range(2, 0, -1):
        for i in range(1, 4):
            aux1 = checa_casa(1, i)
            aux2 = checa_casa(2, i)
            aux3 = checa_casa(3, i)
            if aux1 == aux3 == j and aux2 == 0:
                aux = checa_casa(2, i)
                if aux == 0:
                    domina_casa(2, i, 2)
                    return 0
            elif aux1 == aux2 == j and aux3 == 0:
                aux = checa_casa(3, i)
                if aux == 0:
                    domina_casa(3, i, 2)
                    return 0
            elif aux2 == aux3 == j and aux1 == 0:
                aux = checa_casa(1, i)
                if aux == 0:
                    domina_casa(1, i, 2)
                    return 0

            aux1 = checa_casa(i, 1)
            aux2 = checa_casa(i, 2)
            aux3 = checa_casa(i, 3)
            if aux1 == aux3 == j and aux2 == 0:
                aux = checa_casa(i, 2)
                if aux == 0:
                    domina_casa(i, 2, 2)
                    return 0
            elif aux1 == aux2 == j and aux3 == 0:
                aux = checa_casa(i, 3)
                if aux == 0:
                    domina_casa(i, 3, 2)
                    return 0
            elif aux2 == aux3 == j and aux1 == 0:
                aux = checa_casa(i, 1)
                if aux == 0:
                    domina_casa(i, 1, 2)
                    return 0

        aux1 = checa_casa(1, 1)
        aux2 = checa_casa(2, 2)
        aux3 = checa_casa(3, 3)
        if aux1 == aux3 == j and aux2 == 0:
            aux = checa_casa(2, 2)
            if aux == 0:
                domina_casa(2, 2, 2)
                return 0
        elif aux1 == aux2 == j and aux3 == 0:
            aux = checa_casa(3, 3)
            if aux == 0:
                domina_casa(3, 3, 2)
                return 0
        elif aux2 == aux3 == j and aux1 == 0:
            aux = checa_casa(1, 1)
            if aux == 0:
                domina_casa(1, 1, 2)
                return 0

        aux1 = checa_casa(3, 1)
        aux3 = checa_casa(1, 3)
        if aux1 == aux3 == j and aux2 == 0:
            aux = checa_casa(2, 2)
            if aux == 0:
                domina_casa(2, 2, 2)
                return 0
        elif aux1 == aux2 == j and aux3 == 0:
            aux = checa_casa(1, 3)
            if aux == 0:
                domina_casa(1, 3, 2)
                return 0
        elif aux2 == aux3 == j and aux1 == 0:
            aux = checa_casa(3, 1)
            if aux == 0:
                domina_casa(3, 1, 2)
                return 0

    aux1 = checa_casa(1, 1)
    aux2 = checa_casa(3, 3)
    if aux1 == 1 and aux2 == 1:
        aux = checa_casa(2, 1)
        if aux == 0:
            domina_casa(2, 1, 2)
            return 0

    aux1 = checa_casa(3, 1)
    aux2 = checa_casa(1, 3)
    if aux1 == 1 and aux2 == 1:
        aux = checa_casa(2, 1)
        if aux == 0:
            domina_casa(2, 1, 2)
            return 0

    aux1 = checa_casa(2, 1)
    aux2 = checa_casa(3, 2)
    aux3 = checa_casa(1, 2)
    if aux1 == 1 and aux2 == 1:
        aux = checa_casa(3, 1)
        if aux == 0:
            domina_casa(3, 1, 2)
            return 0


def main():
    tipo_de_jogo = 5
    jogador = 0

    while tipo_de_jogo not in range(3):
        tipo_de_jogo = int(input("[1] Jogador contra Jogador\n[2] Jogador contra Computador\n[0] Sair\n"))

    if tipo_de_jogo == 0:
        return 0

    elif tipo_de_jogo == 1:
        for _ in range(9):
            jogador += 1
            if jogador > 2:
                jogador = 1

            loop_jogo(jogador)

            aux = checa_win()
            if aux != 0:
                desenhar_jogo()
                print(f"Vencedor: Jogador {aux}!")
                return 0

    elif tipo_de_jogo == 2:
        for _ in range(9):
            jogador += 1
            if jogador > 2:
                jogador = 1

            if jogador == 1:
                loop_jogo(jogador)
            elif jogador == 2:
                joga_computador()

            aux = checa_win()
            if aux != 0:
                desenhar_jogo()
                if aux == 1:
                    print("Vencedor: Jogador!")
                elif aux == 2:
                    print("Vencedor: Computador!")
                return 0

    if tipo_de_jogo != 0:
        desenhar_jogo()
        print("Empate!")


if __name__ == "__main__":
    main()
