class Animal:
    nome = ''
    peso=0

    def imprimir(self):
        print(f'meu nome: {self.nome}')
        print(f'meu peso: {self.peso}')

    def alimentar(self, comida):
        self.peso += comida