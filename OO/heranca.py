class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self._cpf = cpf
        self.__salario = salario

    def get_bonificacao(self):
        return self.__salario * 0.10

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, quantidade_funcionarios):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._quantidade_funcionarios = quantidade_funcionarios

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000


    def autenticar(self, senha):
        if senha == self._senha:
            print("Acesso permitido ")
            return True
        else:
            print("Acesso negado ")
            return False

class ControleDeBonificacoes:
    def __init__(self, total_bonificacoes=0 ):
        self._total_bonificacos = total_bonificacoes
    
    def registra(self, obj):
        if(hasattr(obj, 'get_bonificacao')): #podemos usar o 'isistance' que recebe a classe em vez da instancia isistance(obj, funcionario)
            self._total_bonificacos = obj.get_bonificacao()
    
    @property
    def total_bonificacoes(self):
        return self._total_bonificacos

if __name__ == '__main__':
    pass

