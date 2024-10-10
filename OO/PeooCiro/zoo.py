class Zoo():
    catalogo = list()
    def adicionar(self, animal):
        self.catalogo.append(animal)

    def imprimir(self):
        print('Animais do Zoo: ')
        for i in self.catalogo:
            i.imprimir()