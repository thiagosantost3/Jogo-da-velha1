import random
import time
import pandas as pd
import matplotlib.pyplot as plt

# Inicialização
inicio = time.time()
numeroDeJogadas = 0
vez = 1
simbolo1 = "X"
simbolo2 = "O"
vitoria = False
ganhador = ""
jogoDaVelha = [" "] * 9
numeroV1 = 0
numeroV2 = 0
numeroEmp1 = 0

# Definições para o aprendizado por reforço
Q = {}  # Q-Table
alpha = 0.1  # Taxa de aprendizado
gamma = 0.9  # Fator de desconto
epsilon = 0.1  # Taxa de exploração

def get_state():
    return tuple(jogoDaVelha)

def choose_action(state, symbol):
    if random.uniform(0, 1) < epsilon:
        return random.choice([i for i, x in enumerate(jogoDaVelha) if x == " "])
    else:
        q_values = [Q.get((state, a), 0) for a in range(9)]
        max_q = max(q_values)
        return random.choice([a for a in range(9) if q_values[a] == max_q])

def update_q_table(state, action, reward, next_state):
    best_next_action = max([Q.get((next_state, a), 0) for a in range(9)])
    Q[(state, action)] = Q.get((state, action), 0) + alpha * (reward + gamma * best_next_action - Q.get((state, action), 0))

def modoDificil(jog, v):
    global numeroDeJogadas, vez, vitoria, ganhador, jogoDaVelha

    jog1 = "X" if jog == "O" else "O"
    if vez == v and not vitoria and numeroDeJogadas < 9:
        pos = choose_action(get_state(), jog)
        while jogoDaVelha[pos] != " ":
            pos = random.choice([i for i, x in enumerate(jogoDaVelha) if x == " "])
        jogoDaVelha[pos] = jog
        numeroDeJogadas += 1
        vez = 1 if vez == 2 else 2
        return pos  # Retornar a posição escolhida

def modoAleatorio(jog, v):
    global numeroDeJogadas, vez, vitoria, ganhador, jogoDaVelha
    if vez == v and not vitoria and numeroDeJogadas < 9:
        pos = random.choice([i for i, x in enumerate(jogoDaVelha) if x == " "])
        jogoDaVelha[pos] = jog
        numeroDeJogadas += 1
        vez = 1 if vez == 2 else 2
        return pos  # Retornar a posição escolhida

def checarVencedor():
    global vitoria, ganhador
    for i in range(0, 9, 3):
        if jogoDaVelha[i] == jogoDaVelha[i + 1] == jogoDaVelha[i + 2] != " ":
            vitoria = True
            ganhador = jogoDaVelha[i]
            return
    for i in range(3):
        if jogoDaVelha[i] == jogoDaVelha[i + 3] == jogoDaVelha[i + 6] != " ":
            vitoria = True
            ganhador = jogoDaVelha[i]
            return
    if jogoDaVelha[0] == jogoDaVelha[4] == jogoDaVelha[8] != " ":
        vitoria = True
        ganhador = jogoDaVelha[0]
        return
    if jogoDaVelha[2] == jogoDaVelha[4] == jogoDaVelha[6] != " ":
        vitoria = True
        ganhador = jogoDaVelha[2]
        return

def reiniciar_jogo():
    global numeroDeJogadas, vez, vitoria, ganhador, jogoDaVelha
    numeroDeJogadas = 0
    vez = 1
    vitoria = False
    ganhador = ""
    jogoDaVelha = [" "] * 9

def jogar_jogo():
    global numeroV1, numeroV2, numeroEmp1

    jogar = 0
    while jogar < 100:
        reiniciar_jogo()
        estado_anterior = get_state()

        while True:
            pos = modoAleatorio(simbolo1, 1)
            checarVencedor()
            estado_atual = get_state()
            if vitoria or numeroDeJogadas >= 9:
                recompensa = 1 if ganhador == simbolo1 else 0
                update_q_table(estado_anterior, pos, recompensa, estado_atual)
                break

            pos = modoDificil(simbolo2, 2)
            checarVencedor()
            estado_anterior = estado_atual
            estado_atual = get_state()
            if vitoria or numeroDeJogadas >= 9:
                recompensa = 1 if ganhador == simbolo2 else 0
                update_q_table(estado_anterior, pos, recompensa, estado_atual)
                break

        if vitoria:
            if ganhador == simbolo1:
                numeroV1 += 1
            elif ganhador == simbolo2:
                numeroV2 += 1
        else:
            numeroEmp1 += 1

        jogar += 1

    print("Vitorias aleatorio 1: " + str(numeroV1))
    print("Vitorias Dificil 1: " + str(numeroV2))
    print("Empates: " + str(numeroEmp1))
    fim = time.time()
    print(f"Tempo total: {((fim - inicio)):.3f}")

    df_resultado = pd.DataFrame({
        'Soma Aleatorio 1': [numeroV1],
        'Soma Dificil 1': [numeroV2],
        'Empates jogo 1': [numeroEmp1],
    })

    df_resultado.to_excel('planilhaTeste.xlsx', index=False)
    print(df_resultado)
    df_resultado.plot(kind='bar', width=0.2)
    plt.show()

jogar_jogo()
