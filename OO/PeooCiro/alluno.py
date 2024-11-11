class Aluno:
    def __init__(self, nome:str, matricula:int, curso:str, idade:int, email:str) -> None:
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.idade = idade
        self.email = email

    def matricularEmDisciplina(self, disciplina:str) -> None:
        print(f"O aluno {self.nome} matricula {self.matricula} se matriculou em {disciplina}")

    def cancelarMatricula(self, disciplina:str) -> None:
        print(f"O aluno {self.nome} matricula {self.matricula} cancelou a matricula em {disciplina}")

    def consultarNota(self) -> float:
        #self.curso.disciplina.notas()
        #return not
        return 2929.2