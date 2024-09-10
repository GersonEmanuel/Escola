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
def dificuldade():
    escolha = int(input("Digite um numero para a dificuldade:\n[1]facil\n[2]medio\n[3]dificil\n"))
    if escolha == 1:
        lista_numero = [i for i in range(5)]
        numero = random.choice(lista_numero)
        tentativas = 2
    elif escolha == 2:
        lista_numero = [i for i in range(10)]
        numero = random.choice(lista_numero)
        tentativas = 3
    elif escolha == 3:
        lista_numero = [i for i in range(20)]
        numero = random.choice(lista_numero)
        tentativas = 5
    return(lista_numero), numero, tentativas
def jogar(lista_numero,numero, tentativas):
    ganhou = False
    while tentativas>0:
        print(f'Voce tem {tentativas} para acertar um numero de 0 a {len(lista_numero)}, boa sorte!!')
        escolher_numero = int(input("Digite aqui o numero escoolhido:"))
        if escolher_numero != numero:
            print("Voce errou o numero ")
            tentativas -=1
        else:
            print(f"Voce acertou, parabens, o numero era {numero}")
            ganhou = True
            break
    if ganhou:
        print("Meus parabens, tem muita sorte ou talvez voce seja bom demais, quem sabe ")
    else:
        print(f"Voce perdeu, que pena o numero era {numero}")






