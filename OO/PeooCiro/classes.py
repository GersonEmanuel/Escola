class Animal:
    nome = ''
    peso=0

    def imprimir(self):
        print(f'meu nome: {self.nome}')
        print(f'meu peso: {self.peso}')

    def alimentar(self, comida):
        self.peso += comida


class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def DizerONome(self):
        print(f'Ola, meu nome é {self.nome}')

    def DizerAidade(self):
        print(f'Ola, eu tenho {self.idade} anos ')

    def FazerAniversario(self):
        print(f'{self.nome} fez aniversario ')
        self.idade +=1
        return self.idade