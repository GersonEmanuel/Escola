import abc
class SistemaInterno:
    def login(self,obj):
        if(isinstance(obj, Autenticavel)):
            obj.autentica(str(input("Digite sua senha ")))
            return True
        else:
            print(f'{self.__class__.__name__} não é autenticavel ')
            return False

class Autenticavel(abc.ABC):
    @abc.abstractmethod
    def autentica(self, senha):
        if senha == self._senha:
            return True
        else:
            return False

class Funcionario(abc.ABC):
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self._cpf = cpf
        self._salario = salario
    @abc.abstractmethod
    def get_bonificacao(self):
        return self._salario * 0.10
    
class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, quantidade_funcionarios):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._quantidade_funcionarios = quantidade_funcionarios

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000


    def autentica(self, senha):
        if senha == self._senha:
            print("Acesso permitido ")
            return True
        else:
            print("Acesso negado ")
            return False
        
class Diretor(Funcionario, Autenticavel):
    def __init__(self, nome, cpf, salario,senha):
        super().__init__(nome, cpf, salario)
        self._senha = senha
    
    def autentica(self, senha):
        if senha == self._senha:
            print('Acesso permitido ')
            return True
        else:
            print('Acesso negado ')
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
    gerente = Gerente('ger', '233', 5000, '321',4)
    Autenticavel.register(Gerente)
    sistema = SistemaInterno()
    sistema.login(gerente)
