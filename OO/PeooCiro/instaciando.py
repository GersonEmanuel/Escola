from alunos import *
class Alunos:
    alunos_na_escola = []
    def adicionar_aluno(self, aluno):
        self.alunos_na_escola.append(aluno)

    def mostrar_alunos(self):
        for i in self.alunos_na_escola:
            print(i)
if __name__ == '__main__':
    gerson = Aluno('gerson', 'informatica', 2023)
    escola = Alunos()
    escola.adicionar_aluno(gerson)
    if gerson.foi_para_escola:
        gerson.lachar('bolo')
        print(f'{gerson.nome} lanchou ')

    escola.mostrar_alunos()