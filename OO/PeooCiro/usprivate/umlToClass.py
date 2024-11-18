class Animal:
    def __init__(self, name:str, cor:str, idade:int)->None:
        self.name = name
        self._cor = cor
        self._idade = idade

    def _latir(self)->str:
        return f'{self.name} latiu'

    def comer(self, quantidade:int, nomeRacao:str)->None:
        print(f'{self.name} comeu {quantidade} gramas da racao {nomeRacao}')

