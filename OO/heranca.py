class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.__cpf = cpf
        self.__salario = salario

    def get_bonificacao(self):
        return self.__salario * 0.10

class Gerente(Funcionario):
    def __int__(self, nome, cpf, salario, senha, quantidade_funcionarios):
        super().__init__(nome, cpf, salario)
        self.__senha = senha
        self.__quantidade_funcionarios = quantidade_funcionarios

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000


    def autenticar(self, senha):
        if senha == self.__senha:
            print("Acesso permitido ")
            return True
        else:
            print("Acesso negado ")
            return False

