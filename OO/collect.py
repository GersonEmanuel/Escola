
from collections.abc import *
from Conta import *
        
class Contas(MutableSequence):
    _dados = []
    def __len__(self) -> int:
        return len(self._dados)
    
    def __getitem__(self, posicao):
        return self._dados[posicao]
    
    def __setitem__(self, posicao, valor):
        if(isinstance(valor, Conta)):
            self._dados[posicao] = valor
        else:
            raise TypeError('Valor informado não é uma conta ')
        
    def __delitem__(self, posicao):
        del self._dados[posicao]
    
    def insert(self, valor, posicao):
        if(isinstance(valor, Conta)):
            return self._dados.insert(posicao, valor)
        else:
            raise TypeError('Valor inserido não é uma conta ')
    
if __name__ == '__main__':
    pass