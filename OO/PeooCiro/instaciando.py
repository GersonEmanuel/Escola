from alunos import *
from classes import *
class Alunos3:
    alunos_na_escola = []
    def adicionar_aluno(self, aluno):
        self.alunos_na_escola.append(aluno)

    def mostrar_alunos(self):
        for i in self.alunos_na_escola:
            print(i)

if __name__ == '__main__':
    pessoa1 = Pessoa('Gerson', 10)
    pessoa2 = Pessoa('Emanuel', 20)
    pessoa1.DizerONome()
    pessoa1.DizerAidade()
    pessoa2.DizerONome()
    pessoa2.DizerAidade()
    pessoa2.FazerAniversario()
    pessoa1.FazerAniversario()
    pessoa1.DizerAidade()
    pessoa2.DizerAidade()