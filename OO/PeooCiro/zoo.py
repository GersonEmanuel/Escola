class Zoo():
    catalogo = list()
    def adicionar(self, animal):
        self.catalogo.append(animal)

    def imprimir(self):
        print('Animais do Zoo: ')
        for i in self.catalogo:
            i.imprimir()

    def remover(self, animal):
        for i in self.catalogo:
            if i.nome == animal:
                self.catalogo.remove(animal)

    def animalisinCatalogo(self, animal):
        for i in self.catalogo:
            if i.nome == animal:
                return True
        return False
