class Notebook:
    def __init__(self, marca:str, memoriaHD:int, memoriaRAM:int)->None:
        self.marca = marca
        self.memoriaHD = memoriaHD
        self.memoriaRaM = memoriaRAM

    def getDados(self)->str:
        return f'{self.marca}\n {self.memoriaHD}\n {self.memoriaRaM}'
    def ligar(self)->None:
        print('Ligando')

    def desligar(self)->None:
        print('Desligando')