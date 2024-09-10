import forca
import adivinhacao
if __name__ == '__main__':
    Jogar = True
    while Jogar:
        print('-'*100)
        print("Menu de jogos ")
        print('-'*100)
        print('1-Jogo da forca\n2- Jogo da adivinhação ')
        escolha = int(input("O que quer jogar? [digite o numero], caso queira sair, digite qualquer outro numero "))
        if escolha == 1:
            forca.jogar()
            Jogar = True
        elif escolha == 2:
            adivinhacao.inicio()
            adivinhacao.regras()
            adivinhacao.jogar(*adivinhacao.dificuldade())
            Jogar = True

        else:
            quit()
