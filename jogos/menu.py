import forca
import adivinhacao
import questionario
if __name__ == '__main__':
    Jogar = True
    while Jogar:
        print('-'*100)
        print("Menu de jogos ")
        print('-'*100)
        print('1-Jogo da forca\n2- Jogo da adivinhação\n3- Questionario  ')
        escolha = int(input("O que quer jogar? [digite o numero], caso queira sair, digite qualquer outro numero "))
        if escolha == 1:
            forca.jogar()
        elif escolha == 2:
            adivinhacao.jogar()
        elif escolha == 3:
            questionario.jogar()

        else:
            quit()
