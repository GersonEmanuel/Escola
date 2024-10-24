from classes import *
from zoo import *
if __name__  == '__main__':

    a = Animal()
    a.nome = 'Cavalo de fogo'
    a.peso = 300

    z = Zoo()
    z.adicionar(a)
    z.imprimir


