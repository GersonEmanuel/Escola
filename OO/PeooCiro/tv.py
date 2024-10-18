class Televisao:
    def __init__(self, tamanho:float, marca:str):
        self.ligada = False
        self.channel = 0
        self.tamanho = tamanho
        self.marca = marca
    
    def turnOn(self):
        print("A televisao foi ligada")
        self.ligada = True
        
    
    def turnOff(self):
        print('A televisao foi desligada')
        self.ligada = False
        
    def change_channel(self, number_channel):
        if self.ligada:
            self.channel = number_channel
            print(f"Canal mudado para o {self.channel}")
            return self.channel
        else:
            print('Impossivel mudar o canal, a televisao esta desligada! ')
        
    def get_info(self):
        print(f"A televisao é da marca {self.marca} e tem {self.tamanho} megapixels\nagora esta desligada ")
