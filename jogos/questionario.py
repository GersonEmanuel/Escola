import random
def separador_terminal():
    print("_"*80)

def mensagem_inicio():
    print("Bem vindo ao quiz de animações")
    print("Nesse quiz teremos 10 perguntas, cada uma valendo 1 ponto e no final será mostrado seu resultado, mas caso o numero de jogadores seja maior que 1, entao é ativado o modo multiplayer, cada jogador respondera as questoes e no final sera mostrado um ranking.")

def mensagem_final():
    separador_terminal()
    print("fim de jogo")
    separador_terminal()


def mensagem_acerto():
    print('Parabens! voce acertou ')
def mensagem_erro():
    return 'vixe, resposta errada misera'

def mensagem_conquista(acertos, erros):
    if acertos == 10:
        print('Uma pontuacao perfeita, muito bem ')
    elif acertos>6:
        print('Voce foi muito bem! parabens!!')
    else:
        print('Obrigado pela participacao, na proxima voce vai melhor ')
    print(f'Voce acabou com {acertos} acertos e {erros} erros')

def jogar(NumeroJogadores=None):
    AcertoseErros = []
    numeros = [i for i in range(10)]
    random.shuffle(numeros)
    if not NumeroJogadores:
        mensagem_inicio()
        Comecar()
        separador_terminal()
        NumeroJogadores = int(input("Informe quantos jogadores irão jogar: "))
        if NumeroJogadores >1:
            Multiplayer(NumeroJogadores)
        else:
            mensagem_conquista(*ExibirMatriz(questoes, numeros))
            mensagem_final()
    else:
        AcertoseErros = ExibirMatriz(questoes, numeros)
        return AcertoseErros
        
def ExibirMatriz(questoes, numeros, acertos=0, erros=0):
    for i in range(len(questoes)):
        print(f'--> Questão {i+1} - {"".join(questoes[numeros[i]][0])}')
        separador_terminal()
        for j in range(len(questoes[numeros[i]][1])-1):
            print(questoes[numeros[i]][1][j])
        if VerificarResposta(str(input("Digite a alternativa correta: a, b ou c ")).lower()) == questoes[numeros[i]][1][-1].lower():
            acertos += 1
            mensagem_acerto()
            separador_terminal()
        else:
            erros+= 1
            print(f'{mensagem_erro()}, a resposta correta era a alternativa {questoes[numeros[i]][1][-1]}')
            separador_terminal()
    return [acertos, erros]

def Multiplayer(NumeroJogadores):
    Jogadores = []
    for i in range(NumeroJogadores):
        jogador = []
        jogador.append(str(input(f"Digite o nome do jogador {i+1} ")))
        print()
        print("Questionario modo Multiplayer ")
        separador_terminal()
        jogador.append(jogar(NumeroJogadores))
        Jogadores.append(jogador)
    Ranking(Jogadores)
    print(f'O vencedor foi o jogador \'{Jogadores[0][0]}\' com {Jogadores[0][1][0]} acertos\nPressione Enter para ver o ranking final ')
    input()
    separador_terminal()
    for i in range(len(Jogadores)):
        print(f'O jogador \'{Jogadores[i][0]}\' acertou {Jogadores[i][1][0]} perguntas, ficando na posicao de numero {i+1} no ranking ')
    mensagem_final()



def Ranking(Jogadores):
    for i in range(len(Jogadores)):
        PosicaoMinima = i
        for j in range(i+1, len(Jogadores)):
            if Jogadores[j][1][0]>Jogadores[PosicaoMinima][1][0]:
                PosicaoMinima = j
        if PosicaoMinima != i:
            Jogadores[i], Jogadores[PosicaoMinima] = Jogadores[PosicaoMinima], Jogadores[i]
    return Jogadores

       
def Comecar():
    Resposta_inicio = str(input("Deseja iniciar? [S/N] "))
    if Resposta_inicio == "n" or Resposta_inicio == 'N':
        print("Não?? Que pena então. ")
        quit()
            
def VerificarResposta(RespostaUsuario):
    alternativas = ['a', 'b', 'c']
    if RespostaUsuario in alternativas:
        return RespostaUsuario
    else:
        return VerificarResposta(str(input("Escolha invalida! Tente novamente\nDigite a alternativa correta: a, b ou c ")).lower())



questoes = [[["Em qual esporte se baseia a Obra \"Ping Pong\" do autor Taiyo Matsumoto? "],["a) Tenis de mesa ", "b) Basquete ", "c) Futebol ", 'a']],
            [['Qual a primeira animação criada? '],['a) Mickey Mouse ' ,'b) Fantasmagorie ','c) Belladonna of Sadness ','b']],
            [['Qual o ano de lançamento do primeiro filme da branca de neve '],['a) 1937 ',"b) 1837 ",'c) 1987 ','a']],
            [['Na obra \"Naruto\" quem é o protagonista? '],["a) Goku ","b) Luffy ","c) Naruto ",'c']],
            [['Na animação \"O conto da princesa Kaguya\" é contada a lenda de qual princesa? '],["a) Isabel ","b) Kaguya ","c) Ariel ",'b']],
            [['Na obra \"Akagi\" o protagonista é conhecido principalmente por: '],["a) Sonegar impostos ","b) Ser um genio das apostas ","c) Ser um fracassado ",'b']],
            [['Em \"Hadashi no Gen\" é mostrado um evento traumatizante da humanidade, que evento é esse? '],["a) Holocausto ","b) Caçadas dos ciganos ","c) Bomba de Hiroshima ",'c']],
            [['A direção do filme \"Ongaku\" tem um fato interessante, Qual é ele? '],["a) Foi a animação que foi feita mais rápida ","b) Foi feito apenas por uma pessoa ","c) O diretor morreu no meio da criação e o filho dele assumiu ",'b']],
            [['Em \"Slam Dunk\" Por que o protagonista começa a jogar basquete? '],["a) Impressionar uma garota ","b) Amor pelo esporte ","c) Um sonho do seu pai",'a']],
            [['\"Houseki no Kuni\" é uma animação em que os personagens são: '],["a) Animais ",'b) Maquinas ',"c) Minerios ",'c']]]
