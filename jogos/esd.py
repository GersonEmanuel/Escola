def MaiorElemento(lista):
    maior = lista[0]
    for numero in lista:
        if maior<numero:
            maior = numero
    return maior
lista = [4,56,57,4,2,2,6,5,8,6,4535,231]
def MenorElemento(lista):
    menor = lista[0]
    for numero in lista:
        if menor>numero:
            menor = numero
    return menor
def Pares(lista):
    for numero in lista:
        if numero % 2 == 0:
            print(numero, end=' ')
def Ocorrencias(lista, numero):
    ocorrencia = 0
    for number in lista:
        if numero == number:
            ocorrencia +=1
    return ocorrencia
def Media(lista):
    media = 0
    for numero in lista:
        media += numero
    return (media/len(lista))

