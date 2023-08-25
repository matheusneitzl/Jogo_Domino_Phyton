import random

def criar_deck():
    pecas = []
    for i in range(7):
        for j in range(i, 7):
            pecas.append((i, j))
    return pecas

def distribuir_pecas_jogadores(numero_de_jogadores):
    deck = criar_deck()
    random.shuffle(deck)
    jogadores = [deck[i::numero_de_jogadores] for i in range(numero_de_jogadores)]
    return jogadores

def verificar_jogada_valida(pecas_na_mao, mesa):
    for peca in pecas_na_mao:
        if peca[0] in mesa[-1] or peca[1] in mesa[-1]:
            return True
    return False

def jogada_auto(pecas_na_mao, mesa):
    jogada_valida = None
    for peca in pecas_na_mao:
        if peca[0] in mesa[-1] or peca[1] in mesa[-1]:
            jogada_valida = peca
            break
    return jogada_valida

def jogar():
    jogadores = distribuir_pecas_jogadores(2)
    mesa = [(6, 6)]
    jogador_atual = 0
    
    while True:
        peca_escolhida = jogada_auto(jogadores[jogador_atual], mesa)
        
        if peca_escolhida:
            if peca_escolhida[0] == mesa[-1][-1]:
                mesa.append(peca_escolhida)
            else:
                mesa.append((peca_escolhida[1], peca_escolhida[0]))
            jogadores[jogador_atual].remove(peca_escolhida)
            
            print(f"\nMesa:\n{mesa}")
            print(f"Jogador {jogador_atual + 1} jogou: {peca_escolhida}")
            print(f"Pedras do Jogador {jogador_atual + 1}:", jogadores[jogador_atual])
            
            if len(jogadores[jogador_atual]) == 0:
                print(f"Jogador {jogador_atual + 1} venceu!")
                break
        else:
            print(f"Jogador {jogador_atual + 1} não tem jogada válida. Passando a vez.")
        
        jogador_atual = (jogador_atual + 1) % 2

if __name__ == "__main__":
    jogar()
