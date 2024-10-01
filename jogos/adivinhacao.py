import random
def inicio():
    print("Bem vindo ao jogo da adivinhaçao ")
    print("-"*100)


def regras():
    regra = int(input("Deseja ver as regras? Se sim digite 1, caso nao, qualquer outra coisa"))
    if regra == 1:
        print("Dada a dificuldade escolhida, escolha um numero entre determinado range, se acertar, dentro das determinadas chances, voce ganha, caso nao, perde! ")
        print("Dificuldade: facil, range: 0 a 5, tentativas: 2 ")
        print("Dificuldade: media, range: 0 a 10, tentativas: 3")
        print("Dificuldade: dificil, range: 0 a 20, tentativas: 5")
    else:
        pass
def dificuldade(escolha):
    chaves = {1:{'dificuldade':'facil', 'tentativas':2, 'numero': random.randint(0,5), 'range': 5},
              2:{'dificuldade':'medio', 'tentativas':3, 'numero': random.randint(0,10), 'range': 10},
              3:{'dificuldade':'dificil', 'tentativas':5, 'numero': random.randint(0,20), 'range': 20}}
    for k,v in chaves.items():
        if k ==escolha:
            return v
    
def jogar():
    inicio()
    regras()
    norma = dificuldade(int(input("Digite um numero para a dificuldade:\n[1]facil\n[2]medio\n[3]dificil\n")))
    ganhou = False
    while norma['tentativas']>0:
        print(f'Voce tem {norma['tentativas']} para acertar um numero de 0 a {norma['range']}, boa sorte!!')
        escolher_numero = int(input("Digite aqui o numero escoolhido:"))
        if escolher_numero != norma['numero']:
            print("Voce errou o numero ")
            norma['tentativas'] -=1
        else:
            print(f"Voce acertou, parabens, o numero era {norma['numero']}")
            ganhou = True
            break
    if ganhou:
        print("Meus parabens, tem muita sorte ou talvez voce seja bom demais, quem sabe ")
    else:
        print(f"Voce perdeu, que pena o numero era {norma['numero']}")






