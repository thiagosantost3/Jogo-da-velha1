from random import randint

from random import randint

def limpar_tela():
    print('\n' * 3)

def cabecalho():
    print('{:^50}'.format('=' * 50))
    print('{:^50}'.format('JOGO DA VELHA'))
    print('{:^50}'.format('=' * 50))

def desenhar_tabuleiro(c1, c2, c3, c4, c5, c6, c7, c8, c9):
    print('{:^19}'.format('MAPA DO JOGO'), '          ', '{:^19}'.format('JOGO EM ANDAMENTO'))
    print(f'+-----+-----+-----+', '          ', f'+-----+-----+-----+')
    print(f'│  1  │  2  │  3  │', '          ', f'│  {c1}  │  {c2}  │  {c3}  │')
    print(f'+-----+-----+-----+', '          ', f'+-----+-----+-----+')
    print(f'│  4  │  5  │  6  │', '          ', f'│  {c4}  │  {c5}  │  {c6}  │')
    print(f'+-----+-----+-----+', '          ', f'+-----+-----+-----+')
    print(f'│  7  │  8  │  9  │', '          ', f'│  {c7}  │  {c8}  │  {c9}  │')
    print(f'+-----+-----+-----+', '          ', f'+-----+-----+-----+')
    print()

def verificar_vencedor(tabuleiro):
    # Combinacões de vitória
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]              # Diagonais
    ]
    for combination in win_combinations:
        if tabuleiro[combination[0]] == tabuleiro[combination[1]] == tabuleiro[combination[2]] and tabuleiro[combination[0]] != ' ':
            return True
    return False

def verificar_empate(tabuleiro):
    return ' ' not in tabuleiro

def modo_aleatorio(tabuleiro):
    return randint(0, 8)

def modo_dificil(c1, c2, c3, c4, c5, c6, c7, c8, c9, pc):
    if pc == 'o':
        adv = 'x'
    elif pc == 'x':
        adv = 'o'
    sugestao = 0
    listaOpcoes1 = []
    listaOpcoes2 = []
    listaOpcoes3 = []
    listaOpcoes4 = []
    listaOpcoes5 = []
    listaOpcoes6 = []
    #lista sugestões 1
    #vai sugerir casa 1
    if c1 == ' ':
        if c2 == pc and c3 == pc or c4 == pc and c7 == pc or c5 == pc and c9 == pc:
            listaOpcoes1.append(1)
    #vai sugerir casa 2
    if c2 == ' ':
        if c1 == pc and c3 == pc or c5 == pc and c8 == pc:
            listaOpcoes1.append(2)
    #vai sugerir casa 3
    if c3 == ' ':
        if c1 == pc and c2 == pc or c6 == pc and c9 == pc or c5 == pc and c7 == pc:
            listaOpcoes1.append(3)
    #vai sugerir casa 4
    if c4 == ' ':
        if c5 == pc and c6 == pc or c1 == pc and c7 == pc:
            listaOpcoes1.append(4)
    #vai sugerir casa 5
    if c5 == ' ':
        if c4 == pc and c6 == pc or c2 == pc and c8 == pc or c1 == pc and c9 == pc:
            listaOpcoes1.append(5)
    #vai sugerir casa 6
    if c6 == ' ':
        if c4 == pc and c5 == pc or c3 == pc and c9 == pc:
            listaOpcoes1.append(6)
    #vai sugerir casa 7
    if c7 == ' ':
        if c8 == pc and c9 == pc or c1 == pc and c4 == pc or c3 == pc and c5 == pc:
            listaOpcoes1.append(7)
    #vai sugerir casa 8
    if c8 == ' ':
        if c7 == pc and c9 == pc or c2 == pc and c5 == pc:
            listaOpcoes1.append(8)
    #vai sugerir casa 9
    if c9 == ' ':
        if c7 == pc and c8 == pc or c3 == pc and c6 == pc or c1 == pc and c5 == pc:
            listaOpcoes1.append(9)
    #lista sugestões 2
    #vai sugerir casa 1
    if c1 == ' ':
        if c2 == adv and c3 == adv or c4 == adv and c7 == adv or c5 == adv and c9 == adv:
            listaOpcoes2.append(1)
    if c2 == ' ':
        if c1 == adv and c3 == adv or c5 == adv and c8 == adv:
            listaOpcoes2.append(2)
    if c3 == ' ':
        if c1 == adv and c2 == adv or c6 == adv and c9 == adv or c5 == adv and c7 == adv:
            listaOpcoes2.append(3)
    if c4 == ' ':
        if c5 == adv and c6 == adv or c1 == adv and c7 == adv:
            listaOpcoes2.append(4)
    if c5 == ' ':
        if c4 == adv and c6 == adv or c2 == adv and c8 == adv or c1 == adv and c9 == adv:
            listaOpcoes2.append(5)
    if c6 == ' ':
        if c4 == adv and c5 == adv or c3 == adv and c9 == adv:
            listaOpcoes2.append(6)
    if c7 == ' ':
        if c8 == adv and c9 == adv or c1 == adv and c4 == adv or c3 == adv and c5 == adv:
            listaOpcoes2.append(7)
    if c8 == ' ':
        if c7 == adv and c9 == adv or c2 == adv and c5 == adv:
            listaOpcoes2.append(8)
    if c9 == ' ':
        if c7 == adv and c8 == adv or c3 == adv and c6 == adv or c1 == adv and c5 == adv:
            listaOpcoes2.append(9)
    #lista sugestões 3
    #vai sugerir casa 1
    if c1 == ' ':
        if c2 == pc and c3 == ' ' or c3 == pc and c2 == ' ':
            listaOpcoes3.append(1)
        if c4 == pc and c7 == ' ' or c7 == pc and c4 == ' ':
            listaOpcoes3.append(1)
        if c5 == pc and c9 == ' ' or c9 == pc and c5 == ' ':
            listaOpcoes3.append(1)
    #vai sugerir casa 2
    if c2 == ' ':
        if c1 == pc and c3 == ' ' or c3 == pc and c1 == ' ':
            listaOpcoes3.append(2)
        if c5 == pc and c8 == ' ' or c8 == pc and c5 == ' ':
            listaOpcoes3.append(2)
    #vai sugerir casa 3
    if c3 == ' ':
        if c1 == pc and c2 == ' ' or c2 == pc and c1 == ' ':
            listaOpcoes3.append(3)
        if c6 == pc and c9 == ' ' or c9 == pc and c6 == ' ':
            listaOpcoes3.append(3)
        if c5 == pc and c7 == ' ' or c7 == pc and c5 == ' ':
            listaOpcoes3.append(3)
    #vai sugerir casa 4
    if c4 == ' ':
        if c5 == pc and c6 == ' ' or c6 == pc and c5 == ' ':
            listaOpcoes3.append(4)
        if c1 == pc and c7 == ' ' or c7 == pc and c1 == ' ':
            listaOpcoes3.append(4)
    #vai sugerir casa 5
    if c5 == ' ':
        if c4 == pc and c6 == ' ' or c6 == pc and c4 == ' ':
            listaOpcoes3.append(5)
        if c2 == pc and c8 == ' ' or c8 == pc and c2 == ' ':
            listaOpcoes3.append(5)
        if c3 == pc and c7 == ' ' or c7 == pc and c3 == ' ':
            listaOpcoes3.append(5)
    #vai sugerir casa 6
    if c6 == ' ':
        if c4 == pc and c5 == ' ' or c5 == pc and c4 == ' ':
            listaOpcoes3.append(6)
        if c3 == pc and c9 == ' ' or c9 == pc and c3 == ' ':
            listaOpcoes3.append(6)
    #vai sugerir casa 7
    if c7 == ' ':
        if c8 == pc and c9 == ' ' or c9 == pc and c8 == ' ':
            listaOpcoes3.append(7)
        if c1 == pc and c4 == ' ' or c4 == pc and c1 == ' ':
            listaOpcoes3.append(7)
        if c3 == pc and c5 == ' ' or c5 == pc and c3 == ' ':
            listaOpcoes3.append(7)
    #vai sugerir casa 8
    if c8 == ' ':
        if c7 == pc and c9 == ' ' or c9 == pc and c7 == ' ':
            listaOpcoes3.append(8)
        if c2 == pc and c5 == ' ' or c5 == pc and c2 == ' ':
            listaOpcoes3.append(8)
    #vai sugerir casa 9
    if c9 == ' ':
        if c7 == pc and c8 == ' ' or c8 == pc and c7 == ' ':
            listaOpcoes3.append(9)
        if c3 == pc and c6 == ' ' or c6 == pc and c3 == ' ':
            listaOpcoes3.append(9)
        if c1 == pc and c5 == ' ' or c5 == pc and c1 == ' ':
            listaOpcoes3.append(9)
    #lista sugestões 4
    #vai sugerir casa 5
    if c5 == ' ':
        if c1 == adv or c3 == adv or c7 == adv or c9 == adv:
            listaOpcoes4.append(5)
    #lista sugestões 5
    #vai sugerir casas 1, 3, 7 ou 9
    if c1 == ' ':
        listaOpcoes5.append(1)
    if c3 == ' ':
        listaOpcoes5.append(3)
    if c7 == ' ':
        listaOpcoes5.append(7)
    if c9 == ' ':
        listaOpcoes5.append(9)
    #lista sugestões 6
    if c1 == ' ':
        listaOpcoes6.append(1)
    if c2 == ' ':
        listaOpcoes6.append(2)
    if c3 == ' ':
        listaOpcoes6.append(3)
    if c4 == ' ':
        listaOpcoes6.append(4)
    if c5 == ' ':
        listaOpcoes6.append(5)
    if c6 == ' ':
        listaOpcoes6.append(6)
    if c7 == ' ':
        listaOpcoes6.append(7)
    if c8 == ' ':
        listaOpcoes6.append(8)
    if c9 == ' ':
        listaOpcoes6.append(9)

    #vai sugerir um número com base na situação do jogo
    if len(listaOpcoes1) > 0:
        sugestao = listaOpcoes1[randint(0, len(listaOpcoes1)-1)]
    elif len(listaOpcoes2) > 0:
        sugestao = listaOpcoes2[randint(0, len(listaOpcoes2)-1)]
    elif len(listaOpcoes3) > 0:
        sugestao = listaOpcoes3[randint(0, len(listaOpcoes3)-1)]
    elif len(listaOpcoes4) > 0:
        sugestao = listaOpcoes4[randint(0, len(listaOpcoes4)-1)]
    elif len(listaOpcoes5) > 0:
        sugestao = listaOpcoes5[randint(0, len(listaOpcoes5)-1)]
    else:
        sugestao = listaOpcoes6[randint(0, len(listaOpcoes6)-1)]

    return sugestao
def jogar_100_vezes():
    for _ in range(3):
        tab = [' ' for _ in range(9)]
        jogador1 = 'o'
        jogador2 = 'x'
        vencedor = None
        for _ in range(9):  # Máximo de 9 movimentos
            limpar_tela()
            cabecalho()
            desenhar_tabuleiro(tab[0], tab[1], tab[2], tab[3], tab[4], tab[5], tab[6], tab[7], tab[8])
            # Jogador 1 (modo aleatório)
            posicao = modo_aleatorio(tab)
            tab[posicao] = jogador1
            if verificar_vencedor(tab):
                vencedor = jogador1
                break
            if verificar_empate(tab):
                break
            # Jogador 2 (modo difícil)
            posicao = modo_dificil(tab, jogador2)
            tab[posicao] = jogador2
            if verificar_vencedor(tab):
                vencedor = jogador2
                break
            if verificar_empate(tab):
                break
        if vencedor == jogador1:
            print("Jogador 1 (modo aleatório) venceu!")
        elif vencedor == jogador2:
            print("Jogador 2 (modo difícil) venceu!")
        else:
            print("Empate!")
        input("Pressione Enter para continuar...")
        limpar_tela()

jogar_100_vezes()
