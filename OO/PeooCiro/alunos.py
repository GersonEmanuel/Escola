import random
class Aluno:
    def __init__(self, nome:str, curso:str, matricula:int):
        self.nome = nome
        self.curso = curso
        self.matricula = matricula
        self.curso_trancado = False

    def __str__(self):
        return f'aluno {self.nome}, matriculado no curso {self.curso} com a matricula {self.matricula}'

    def foi_para_escola(self):
        if random.randint(1,6) <5:
            return False
        return True

    def assistir_aula(self):
        if random.randint(1,6) <5:
            return False
        return True
    
    def lachar(self, lanche:str):
        if lanche!= 'bolacha':
            return True
        return False
    
    def trancar_curso(self, anosreprovados):
        if anosreprovados>2:
            return True
        return False
    

class Pessoa:
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade

    def DizerONome(self):
        print(f'Ola meu nome é {self.nome}')
    
    def DizerAIdade(self):
        print(f'Ola eu tenho {self.idade}')

    def fazerAniversario(self):
        print('Voce fez aniversario ')
        self.idade +=1 
        

class Lampada:
    def __init__(self, acesa:bool, volts:float) -> None:
        self.acesa = False
        self.volts = volts

    def acender(self):
        self.acesa = True
        
    def apagar(self):
        self.acesa = False

    def informarSituacao(self):
        if self.acesa:
            print('A luz esta acesa')
            return
        print('A luz esta apagada ')

    def informarPotencia(self):
        print(f'A potencia da lampada é {self.volts} volts')

        
        

        


        