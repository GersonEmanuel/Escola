import random
def mensangem_inicio():
    print("_"*50)
    print("Bem vindo")
    print("_"*50)

def gera_palavra_secreta():
    arquivo = open("C:\\Users\Master Tech LG\\school\\jogos\\palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero]
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    return ['_' for i in palavra_secreta]

def ChuteUsuario():
    chute = str(input("Digite uma letra: "))
    return chute

def ChuteCorreto(chute, palavra_secreta, letras_acertadas):
    posicao = 0
    for letra in palavra_secreta:
        if chute.upper() == letra.upper():
            letras_acertadas[posicao] = letra
        posicao+=1
    return letras_acertadas

def mensagem_vencedor():
    print('Voce ganhou!!!')

def mensagem_perdedor():
    print('Voce perdeu')



def jogar():
    mensangem_inicio()
    palavra_secreta = gera_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
    acertou = False
    enforcou = False
    erros = 0
    while not acertou and not enforcou:
        chute = ChuteUsuario()
        if chute in palavra_secreta:
            ChuteCorreto(chute, palavra_secreta, letras_acertadas)
        else:
            erros+=1
        acertou = "_" not in letras_acertadas
        enforcou = erros == 6
        print(letras_acertadas)
    if acertou:
        mensagem_vencedor()
    else:
        mensagem_perdedor()
