import os

import random
import time
import pandas as pd
import matplotlib.pyplot as plt

inicio = time.time()
numeroDeJogadas = 0
vez = 1
simbolo1 = "X"
simbolo2 = "O"
vitoria = False
ganhador = ""
jogoDaVelha = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
jogar = "s"
numeroV1 = 0
numeroV2 = 0
numeroV3 = 0
numeroV4 = 0
numeroV5 = 0
numeroV6 = 0
jogar = 0
numeroEmp1 = 0
numeroEmp2 = 0
numeroEmp3 = 0
dados = ""  # data frame


def tabuleiro(jogoDaVelha):
    # os.system('cls')
    print("    0   1   2")
    print("0:  " + jogoDaVelha[0][0] + " | " + jogoDaVelha[0][1] + " | " + jogoDaVelha[0][2])
    print("   -----------")
    print("1:  " + jogoDaVelha[1][0] + " | " + jogoDaVelha[1][1] + " | " + jogoDaVelha[1][2])
    print("   -----------")
    print("2:  " + jogoDaVelha[2][0] + " | " + jogoDaVelha[2][1] + " | " + jogoDaVelha[2][2])
    print(f"Numeros de jogadas: {numeroDeJogadas}")
    print("#" * 30)


def modoDificil(jog, v):
    global numeroDeJogadas
    global vez
    global vitoria
    global ganhador
    global jogoDaVelha

    jog1 = "X" if jog == "O" else "O"

    if vez == v and vitoria == False and numeroDeJogadas < 9:
        # Se Primeira jogada
        if numeroDeJogadas == 0:
            jogoDaVelha[0][0] = jog

        # Se Segunda jogada
        elif numeroDeJogadas == 1:

            # Se oponente iniciou pelo meio
            if jogoDaVelha[1][1] != " ":
                linha = random.randrange(0, 3)
                coluna = random.randrange(0, 3)
                while (linha == 0 and coluna == 1) or (linha == 1 and coluna == 0) or (linha == 1 and coluna == 2) or (
                        linha == 2 and coluna == 1) or (linha == 1 and coluna == 1):
                    linha = random.randrange(0, 3)
                    coluna = random.randrange(0, 3)
                jogoDaVelha[linha][coluna] = jog

            # Se oponente iniciou pelas pontas centrais
            elif jogoDaVelha[1][1] == " ":
                jogoDaVelha[1][1] = jog




        # Se Terceira jodada
        elif numeroDeJogadas == 2:
            if jogoDaVelha[0][1] != " " or jogoDaVelha[0][2] != " " or jogoDaVelha[1][2] != " " or jogoDaVelha[2][1] != " " or jogoDaVelha[2][
                2] != " ":
                jogoDaVelha[2][0] = jog
            elif jogoDaVelha[1][0] != " " or jogoDaVelha[2][0] != " ":
                jogoDaVelha[0][2] = jog
            else:
                jogoDaVelha[2][2] = jog

                # **Ataque**
        # Linha
        elif jogoDaVelha[0][0] == jog and jogoDaVelha[0][1] == jog and jogoDaVelha[0][2] == " ":
            jogoDaVelha[0][2] = jog
        elif jogoDaVelha[0][0] == jog and jogoDaVelha[0][1] == " " and jogoDaVelha[0][2] == jog:
            jogoDaVelha[0][1] = jog
        elif jogoDaVelha[0][0] == " " and jogoDaVelha[0][1] == jog and jogoDaVelha[0][2] == jog:
            jogoDaVelha[0][0] = jog

        elif jogoDaVelha[1][0] == jog and jogoDaVelha[1][1] == jog and jogoDaVelha[1][2] == " ":
            jogoDaVelha[1][2] = jog
        elif jogoDaVelha[1][0] == jog and jogoDaVelha[1][1] == " " and jogoDaVelha[1][2] == jog:
            jogoDaVelha[1][1] = jog
        elif jogoDaVelha[1][0] == " " and jogoDaVelha[1][1] == jog and jogoDaVelha[1][2] == jog:
            jogoDaVelha[1][0] = jog

        elif jogoDaVelha[2][0] == jog and jogoDaVelha[2][1] == jog and jogoDaVelha[2][2] == " ":
            jogoDaVelha[2][2] = jog
        elif jogoDaVelha[2][0] == jog and jogoDaVelha[2][1] == " " and jogoDaVelha[2][2] == jog:
            jogoDaVelha[2][1] = jog
        elif jogoDaVelha[2][0] == " " and jogoDaVelha[2][1] == jog and jogoDaVelha[2][2] == jog:
            jogoDaVelha[2][0] = jog

        # Coluna
        elif jogoDaVelha[0][0] == jog and jogoDaVelha[1][0] == jog and jogoDaVelha[2][0] == " ":
            jogoDaVelha[2][0] = jog
        elif jogoDaVelha[0][0] == jog and jogoDaVelha[1][0] == " " and jogoDaVelha[2][0] == jog:
            jogoDaVelha[1][0] = jog
        elif jogoDaVelha[0][0] == " " and jogoDaVelha[1][0] == jog and jogoDaVelha[2][0] == jog:
            jogoDaVelha[0][0] = jog

        elif jogoDaVelha[0][1] == jog and jogoDaVelha[1][1] == jog and jogoDaVelha[2][1] == " ":
            jogoDaVelha[2][1] = jog
        elif jogoDaVelha[0][1] == jog and jogoDaVelha[1][1] == " " and jogoDaVelha[2][1] == jog:
            jogoDaVelha[1][1] = jog
        elif jogoDaVelha[0][1] == " " and jogoDaVelha[1][1] == jog and jogoDaVelha[2][1] == jog:
            jogoDaVelha[0][1] = jog

        elif jogoDaVelha[0][2] == jog and jogoDaVelha[1][2] == jog and jogoDaVelha[2][2] == " ":
            jogoDaVelha[2][2] = jog
        elif jogoDaVelha[0][2] == jog and jogoDaVelha[1][2] == " " and jogoDaVelha[2][2] == jog:
            jogoDaVelha[1][2] = jog
        elif jogoDaVelha[0][2] == " " and jogoDaVelha[1][2] == jog and jogoDaVelha[2][2] == jog:
            jogoDaVelha[0][2] = jog

        # Diagonal
        elif jogoDaVelha[0][0] == jog and jogoDaVelha[1][1] == jog and jogoDaVelha[2][2] == " ":
            jogoDaVelha[2][2] = jog
        elif jogoDaVelha[0][0] == jog and jogoDaVelha[1][1] == " " and jogoDaVelha[2][2] == jog:
            jogoDaVelha[1][1] = jog
        elif jogoDaVelha[0][0] == " " and jogoDaVelha[1][1] == jog and jogoDaVelha[2][2] == jog:
            jogoDaVelha[0][0] = jog

        elif jogoDaVelha[0][2] == jog and jogoDaVelha[1][1] == jog and jogoDaVelha[2][0] == " ":
            jogoDaVelha[2][0] = jog
        elif jogoDaVelha[0][2] == jog and jogoDaVelha[1][1] == " " and jogoDaVelha[2][0] == jog:
            jogoDaVelha[1][1] = jog
        elif jogoDaVelha[0][2] == " " and jogoDaVelha[1][1] == jog and jogoDaVelha[2][0] == jog:
            jogoDaVelha[0][2] = jog

        # **Defesa**
        # Linha
        elif jogoDaVelha[0][0] == jog1 and jogoDaVelha[0][1] == jog1 and jogoDaVelha[0][2] == " ":
            jogoDaVelha[0][2] = jog
        elif jogoDaVelha[0][0] == jog1 and jogoDaVelha[0][1] == " " and jogoDaVelha[0][2] == jog1:
            jogoDaVelha[0][1] = jog
        elif jogoDaVelha[0][0] == " " and jogoDaVelha[0][1] == jog1 and jogoDaVelha[0][2] == jog1:
            jogoDaVelha[0][0] = jog

        elif jogoDaVelha[1][0] == jog1 and jogoDaVelha[1][1] == jog1 and jogoDaVelha[1][2] == " ":
            jogoDaVelha[1][2] = jog
        elif jogoDaVelha[1][0] == jog1 and jogoDaVelha[1][1] == " " and jogoDaVelha[1][2] == jog1:
            jogoDaVelha[1][1] = jog
        elif jogoDaVelha[1][0] == " " and jogoDaVelha[1][1] == jog1 and jogoDaVelha[1][2] == jog1:
            jogoDaVelha[1][0] = jog

        elif jogoDaVelha[2][0] == jog1 and jogoDaVelha[2][1] == jog1 and jogoDaVelha[2][2] == " ":
            jogoDaVelha[2][2] = jog
        elif jogoDaVelha[2][0] == jog1 and jogoDaVelha[2][1] == " " and jogoDaVelha[2][2] == jog1:
            jogoDaVelha[2][1] = jog
        elif jogoDaVelha[2][0] == " " and jogoDaVelha[2][1] == jog1 and jogoDaVelha[2][2] == jog1:
            jogoDaVelha[2][0] = jog

            # Coluna
        elif jogoDaVelha[0][0] == jog1 and jogoDaVelha[1][0] == jog1 and jogoDaVelha[2][0] == " ":
            jogoDaVelha[2][0] = jog
        elif jogoDaVelha[0][0] == jog1 and jogoDaVelha[1][0] == " " and jogoDaVelha[2][0] == jog1:
            jogoDaVelha[1][0] = jog
        elif jogoDaVelha[0][0] == " " and jogoDaVelha[1][0] == jog1 and jogoDaVelha[2][0] == jog1:
            jogoDaVelha[0][0] = jog

        elif jogoDaVelha[0][1] == jog1 and jogoDaVelha[1][1] == jog1 and jogoDaVelha[2][1] == " ":
            jogoDaVelha[2][1] = jog
        elif jogoDaVelha[0][1] == jog1 and jogoDaVelha[1][1] == " " and jogoDaVelha[2][1] == jog1:
            jogoDaVelha[1][1] = jog
        elif jogoDaVelha[0][1] == " " and jogoDaVelha[1][1] == jog1 and jogoDaVelha[2][1] == jog1:
            jogoDaVelha[0][1] = jog

        elif jogoDaVelha[0][2] == jog1 and jogoDaVelha[1][2] == jog1 and jogoDaVelha[2][2] == " ":
            jogoDaVelha[2][2] = jog
        elif jogoDaVelha[0][2] == jog1 and jogoDaVelha[1][2] == " " and jogoDaVelha[2][2] == jog1:
            jogoDaVelha[1][2] = jog
        elif jogoDaVelha[0][2] == " " and jogoDaVelha[1][2] == jog1 and jogoDaVelha[2][2] == jog1:
            jogoDaVelha[0][2] = jog

        # Diagonal
        elif jogoDaVelha[0][0] == jog1 and jogoDaVelha[1][1] == jog1 and jogoDaVelha[2][2] == " ":
            jogoDaVelha[2][2] = jog
        elif jogoDaVelha[0][0] == jog1 and jogoDaVelha[1][1] == " " and jogoDaVelha[2][2] == jog1:
            jogoDaVelha[1][1] = jog
        elif jogoDaVelha[0][0] == " " and jogoDaVelha[1][1] == jog1 and jogoDaVelha[2][2] == jog1:
            jogoDaVelha[0][0] = jog

        elif jogoDaVelha[0][2] == jog1 and jogoDaVelha[1][1] == jog1 and jogoDaVelha[2][0] == " ":
            jogoDaVelha[2][0] = jog
        elif jogoDaVelha[0][2] == jog1 and jogoDaVelha[1][1] == " " and jogoDaVelha[2][0] == jog1:
            jogoDaVelha[1][1] = jog
        elif jogoDaVelha[0][2] == " " and jogoDaVelha[1][1] == jog1 and jogoDaVelha[2][0] == jog1:
            jogoDaVelha[0][2] = jog

        # Se Quarta jogada
        elif numeroDeJogadas == 3:

            if ((jogoDaVelha[0][0] == jog1 and jogoDaVelha[2][2] == jog1) or (jogoDaVelha[0][2] == jog1 and jogoDaVelha[2][0] == jog1)):
                linha = random.randrange(0, 3)
                coluna = random.randrange(0, 3)
                while ((linha != 0 or coluna != 1) and (linha != 1 or coluna != 0) and (linha != 1 or coluna != 2) and (
                        linha != 2 or coluna != 1)) or (jogoDaVelha[linha][coluna] != " "):
                    linha = random.randrange(0, 3)
                    coluna = random.randrange(0, 3)
                jogoDaVelha[linha][coluna] = jog

            elif ((jogoDaVelha[0][0] != " " and jogoDaVelha[2][2] != " ") or (jogoDaVelha[0][2] != " " and jogoDaVelha[2][0] != " ")):
                linha = random.randrange(0, 3)
                coluna = random.randrange(0, 3)
                while ((linha != 0 or coluna != 0) and (linha != 0 or coluna != 2) and (linha != 2 or coluna != 0) and (
                        linha != 2 or coluna != 2)) or (jogoDaVelha[linha][coluna] != " "):
                    linha = random.randrange(0, 3)
                    coluna = random.randrange(0, 3)
                jogoDaVelha[linha][coluna] = jog

            elif jogoDaVelha[1][1] == " ":
                jogoDaVelha[1][1] = jog

            elif jogoDaVelha[1][0] == " " and jogoDaVelha[1][2] == " ":
                jogoDaVelha[1][0] = jog
            elif jogoDaVelha[0][1] == " " and jogoDaVelha[2][1] == " ":
                jogoDaVelha[0][1] = jog
            elif jogoDaVelha[0][0] == " " and jogoDaVelha[2][2] == " ":
                soma = 0
                for i in range(1, 3):
                    if jogoDaVelha[0][i] == jog1:
                        soma += 1
                    if jogoDaVelha[i][0] == jog1:
                        soma += 1
                if soma == 2:
                    jogoDaVelha[0][0] = jog
                else:
                    jogoDaVelha[2][2] = jog

            elif jogoDaVelha[0][2] == " " and jogoDaVelha[2][0] == " ":
                soma = 0
                for i in range(2):
                    if jogoDaVelha[0][i] == jog1:
                        soma += 1
                    if jogoDaVelha[i + 1][2] == jog1:
                        soma += 1
                if soma == 2:
                    jogoDaVelha[0][2] = jog
                else:
                    jogoDaVelha[2][0] = jog


        # Se quinta jogada
        elif numeroDeJogadas == 4 and jogoDaVelha[1][
            1] == " ":  # and ((jogoDaVelha[0][0]==jog1 and jogoDaVelha[1][1]!=" ") or (jogoDaVelha[2][2]!=jog1 and jogoDaVelha[1][1]!=" ") or (jogoDaVelha[0][2]==jog1 and jogoDaVelha[1][1]!=" ") or (jogoDaVelha[2][0]!=jog1 and jogoDaVelha[1][1]!=" ")):
            jogoDaVelha[1][1] = jog

        # Se sexta jogada
        elif numeroDeJogadas == 5 and (
                (jogoDaVelha[0][0] == " " and jogoDaVelha[2][2] == " ") or (jogoDaVelha[2][0] == " " and jogoDaVelha[0][2] == " ")):
            soma = 0
            vazio = 0
            if jogoDaVelha[0][0] == " " and jogoDaVelha[2][2] == " ":

                for i in range(1, 3):
                    if jogoDaVelha[0][i] == jog1:
                        soma += 1
                    elif jogoDaVelha[0][i] == " ":
                        vazio += 1
                    if jogoDaVelha[i][0] == jog1:
                        soma += 1
                    elif jogoDaVelha[i][0] == " ":
                        vazio += 1
                if soma == 2 and vazio == 2:
                    jogoDaVelha[0][0] = jog
                else:
                    jogoDaVelha[2][2] = jog
            else:
                for i in range(2):
                    if jogoDaVelha[0][i] == jog1:
                        soma += 1
                    elif jogoDaVelha[0][i] == " ":
                        vazio += 1
                    if jogoDaVelha[i + 1][2] == jog1:
                        soma += 1
                    elif jogoDaVelha[i + 1][2] == " ":
                        vazio += 1
                if soma == 2 and vazio == 2:
                    jogoDaVelha[0][2] = jog
                else:
                    jogoDaVelha[2][0] = jog

        else:
            linha = random.randrange(0, 3)
            coluna = random.randrange(0, 3)
            while jogoDaVelha[linha][coluna] != " ":
                linha = random.randrange(0, 3)
                coluna = random.randrange(0, 3)
            jogoDaVelha[linha][coluna] = jog

        numeroDeJogadas += 1
        vez = 1 if v == 2 else 2

    if numeroDeJogadas >= 4 and ganhador == "":
        vitoria = conferir_vitoria()
        if vitoria == True:
            ganhador = v


def jogHumano(jog, v):
    global numeroDeJogadas
    global vez
    global vitoria
    global ganhador

    if vez == v and vitoria == False and numeroDeJogadas < 9 and ganhador == "":
        linha = int(input("Informe a linha da jogada: "))
        coluna = int(input("Informe a coluna da jogada: "))
        while jogoDaVelha[linha][coluna] != " ":
            print("Essa posição já está selecionada!")
            linha = int(input("Informe a linha da jogada: "))
            coluna = int(input("Informe a coluna da jogada: "))

        jogoDaVelha[linha][coluna] = jog
        numeroDeJogadas += 1

        if numeroDeJogadas >= 4 and ganhador == "":
            vitoria = conferir_vitoria()
            if vitoria == True:
                ganhador = v

    vez = 1 if v == 2 else 2


def modoAleatorio(jog, v):
    global numeroDeJogadas
    global vez
    global vitoria
    global ganhador
    global jogoDaVelha

    if vez == v and vitoria == False and numeroDeJogadas < 9:
        linha = random.randrange(0, 3)
        coluna = random.randrange(0, 3)
        while jogoDaVelha[linha][coluna] != " ":
            linha = random.randrange(0, 3)
            coluna = random.randrange(0, 3)
        jogoDaVelha[linha][coluna] = jog
        numeroDeJogadas += 1

    if numeroDeJogadas >= 4 and ganhador == "":
        vitoria = conferir_vitoria()
        if vitoria == True:
            ganhador = v

    vez = 1 if v == 2 else 2


def conferir_vitoria():
    global jogoDaVelha
    global vitoria
    simbolos = [simbolo1, simbolo2]

    for s in simbolos:
        # Linha
        il = ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if (jogoDaVelha[il][ic] == s):
                    soma += 1
                ic += 1

            if (soma == 3):
                vitoria = True
                break
            il += 1

            # Colunas
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if (jogoDaVelha[il][ic] == s):
                    soma += 1
                il += 1

            if (soma == 3):
                vitoria = True
                break
            ic += 1

            # Diagonal
        soma = 0
        diag = 0

        while diag < 3:
            if (jogoDaVelha[diag][diag] == s):
                soma += 1
            diag += 1
        if (soma == 3):
            vitoria = True
            break

        soma = 0
        diagL = 0
        diagC = 2

        while diagC >= 0:
            if (jogoDaVelha[diagL][diagC] == s):
                soma += 1
            diagL += 1
            diagC -= 1
        if (soma == 3):
            vitoria = True
            break
    return vitoria


def reset():
    global numeroDeJogadas
    global vez
    global vitoria
    global ganhador
    global jogoDaVelha
    # os.system("cls")

    numeroDeJogadas = 0
    vez = 1
    vitoria = False
    ganhador = ""
    jogoDaVelha = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


# Gerar arquivo exel
def arquivoExel(jogar):
    global dados
    if jogar == 0:
        d = {'Partida' : [1,2,3], 'Resultado': [1,2,3], 'Ganhador 1' : [1,2,3], 'Ganhador 2' : [1,2,3], 'Empates': [1,2,3]}
        dados = pd.DataFrame(data=d)
        dados.to_excel('planilha.xlsx', index=False, engine='openpyxl')
        dados.loc[jogar] = [jogar, ganhador, numeroV1, numeroV2, numeroEmp1]
        # print(dados)
        dados.to_excel('planilha.xlsx', index=False, engine='openpyxl')
    else:
        dados.loc[jogar] = [jogar, ganhador, numeroV1, numeroV2, numeroEmp1]
        # print(dados)
        dados.to_excel('planilha.xlsx', index=False, engine='openpyxl')


while jogar < 100:
    while True:

        # tabuleiro(jogoDaVelha)
        #modoDificil(simbolo1, 1)
        modoAleatorio(simbolo1, 1)
        # tabuleiro(jogoDaVelha)
        #jogadorBrabo(simb2, 1)
        modoAleatorio(simbolo2, 2)

        if (vitoria == True):
            # tabuleiro(jogoDaVelha)
            # print("*"*30)
            # print(f"Parabens '{vencedor}' foi o vencedor!")
            # print("*"*30)
            if ganhador == 1:
                numeroV1 += 1
            elif ganhador == 2:
                numeroV2 += 1
            arquivoExel(jogar)
            jogar += 1
            break
        if numeroDeJogadas == 9:
            # tabuleiro(jogoDaVelha)
            # print("*"*30)
            # print("Empatou!")
            # print("*"*30)
            ganhador = 0
            numeroEmp1 += 1
            arquivoExel(jogar)
            jogar += 1
            break
    #print(jogar)
    # jogar = input("Deseja jogar novamente?(s/n): ")
    reset()
jogar = 0
while jogar < 100:
    while True:

        # tabuleiro(jogoDaVelha)
        #modoDificil(simbolo1, 1)
        modoAleatorio(simbolo1, 1)
        # tabuleiro(jogoDaVelha)
        modoDificil(simbolo2, 2)
        #modoAleatorio(simbolo2, 2)

        if (vitoria == True):
            # tabuleiro(jogoDaVelha)
            # print("*"*30)
            # print(f"Parabens '{vencedor}' foi o vencedor!")
            # print("*"*30)
            if ganhador == 1:
                numeroV3 += 1
            elif ganhador == 2:
                numeroV4 += 1
           # arquivoExel(jogar)
            jogar += 1
            break
        if numeroDeJogadas == 9:
            # tabuleiro(jogoDaVelha)
            # print("*"*30)
            # print("Empatou!")
            # print("*"*30)
            ganhador = 0
            numeroEmp2 += 1
            #arquivoExel(jogar)
            jogar += 1
            break
    #print(jogar)
    # jogar = input("Deseja jogar novamente?(s/n): ")
    reset()
jogar = 0
while jogar < 100:
    while True:

        # tabuleiro(jogoDaVelha)
        modoDificil(simbolo1, 1)
        #modoAleatorio(simbolo1, 1)
        # tabuleiro(jogoDaVelha)
        modoDificil(simbolo2, 2)
        #modoAleatorio(simbolo2, 2)

        if (vitoria == True):
            # tabuleiro(jogoDaVelha)
            # print("*"*30)
            # print(f"Parabens '{vencedor}' foi o vencedor!")
            # print("*"*30)
            if ganhador == 1:
                numeroV5 += 1
            elif ganhador == 2:
                numeroV6 += 1
           # arquivoExel(jogar)
            jogar += 1
            break
        if numeroDeJogadas == 9:
            # tabuleiro(jogoDaVelha)
            # print("*"*30)
            # print("Empatou!")
            # print("*"*30)
            ganhador = 0
            numeroEmp3 += 1
            arquivoExel(jogar)
            jogar += 1
            break
    #print(jogar)
    # jogar = input("Deseja jogar novamente?(s/n): ")
    reset()

print("Vitorias aleatorio 1: " + str(numeroV1))
print("Vitorias aleatorio 2: " + str(numeroV2))
print("Empates: " + str(numeroEmp1))
fim = time.time()
print(f"Tempo total: {((fim - inicio)):.3f}")

print("Vitorias aleatorio: " + str(numeroV3))
print("Vitorias Brabo: " + str(numeroV4))
print("Empates: " + str(numeroEmp2))
fim = time.time()
print(f"Tempo total: {((fim - inicio)):.3f}")

print("Vitorias Brabo 1: " + str(numeroV5))
print("Vitorias Brabo 2: " + str(numeroV6))
print("Empates: " + str(numeroEmp3))
fim = time.time()
print(f"Tempo total: {((fim - inicio)):.3f}")

tabela = pd.read_excel('planilha.xlsx')


soma_brabo1 = numeroV1
soma_brabo2 = numeroV2
soma_brabo = numeroV3
soma_aleatorio = numeroV4
soma_aleatorio1 = numeroV5
soma_aleatorio2 = numeroV6
empates_brabos = numeroEmp1
empates_brabo_aleatorio = numeroEmp2
empates_aleatorios = numeroEmp3


df_resultado = pd.DataFrame({
    'Soma Brabo 1': [soma_brabo1],
    'Soma Brabo 2': [soma_brabo2],
    'Empates jogo 1': [numeroEmp1],
    'Soma Brabo': [soma_brabo],
    'Soma aleatorio': [soma_aleatorio],
    'Empates jogo 2': [numeroEmp2],
    'Soma aleatorio 1': [soma_aleatorio1],
    'Soma aleatorio 2': [soma_aleatorio2],
    'Empates jogo 3': [numeroEmp3],
})

df_resultado.to_excel('planilhaTeste.xlsx', index=False)
print(tabela)
print(df_resultado)
print(tabela.iloc[99, 2])
df_resultado.plot(kind='bar', width=0.2)

plt.show()

