import forca
import adivinhacao
import questionario 
import campoMinado

if __name__ == '__main__':
    Jogar = True
    jogosadd = {1:forca ,2:adivinhacao ,3:questionario, 4:campoMinado}
    while Jogar:
        print('-'*100)
        print("Menu de jogos ")
        print('-'*100)
        print('1- Jogo da forca\n2- Jogo da adivinhação\n3- Questionario\n4- Campo minado  ')
        escolha = int(input("O que quer jogar? [digite o numero], caso queira sair, digite 0\n"))
        if escolha == 0:
            print('fim')
            quit()
        print('comecando...')
        try:
            jogosadd[escolha].jogar()
        except KeyError:
            print('Valor invalido ')
