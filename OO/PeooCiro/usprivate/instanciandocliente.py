from clie import  *

cliente1 = Cliente('gerson', 'luis gomes', '124.333.444-54', 21)
if cliente1.verificaCPF(cliente1.getCPF()):
    print('cliente valido')
else:
    print('cliente invalido')
