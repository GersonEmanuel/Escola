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


        