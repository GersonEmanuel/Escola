import datetime
from atualizadorconta import AtualizadordeContas
import abc

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []
    def imprime(self):
        print(f'data abertura: {self.data_abertura} ')
        print('transacoes... ')
        for i in self.transacoes:
            print('-', i)
class Tributavel(abc.ABC):
    @abc.abstractmethod
    def get_valor_imposto(self):
        pass
class Banco:
    _todas_as_contas = []
        
    def adicionar_conta(self,conta):
        Banco._todas_as_contas.append(conta)


    def lista_conta(self):
        for i in range(len(Banco._todas_as_contas)):
            print(f'Conta {i+1} {Banco._todas_as_contas[i]}\n')

    def pegaConta(self, index):
        return Banco._todas_as_contas[index]
    
    @staticmethod
    def pega_total_contas():
        return f'Tem o total de {len(Banco._todas_as_contas)} contas nesse banco'
            


class Conta(abc.ABC):
    _total_contas = 0
    __slots__ = ["_titular", "_numero", "_saldo", "_limite", "historico", "tipo_conta"]
    def __init__(self, cliente, numero, saldo, limite = 1000.0 ):
        self._titular = cliente
        self._numero = numero
        self._saldo = saldo
        self._limite = limite
        self.historico = Historico()
        Conta._total_contas += 1

    @staticmethod
    def get_totalcontas():
        return Conta._total_contas
    
    def __str__(self):
        return f'Dados da conta:\nTitular: {self._titular}\nNumero: {self._numero}\nSaldo: {self._saldo}\nLimite: {self._limite} '

    @abc.abstractmethod
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa
        return self._saldo


    def deposito(self, valor):
        self._saldo += valor
        self.historico.transacoes.append(f'Deposito de {valor}')
        return self._saldo

    def get_saldo(self):
        return self._saldo
    def sacar(self, valor):
        if self._saldo<valor:
            return False
        else:
            self._saldo -= valor
            self.historico.transacoes.append(f'saque de {valor} ')
            return True



    def get_extrato(self):
        print(f'numero: {self._numero}\nsaldo: {self._saldo}')
        self.historico.transacoes.append(f'tirou extrato - saldo de {self._saldo} ')



    def transfere_para(self,destino, valor):
        if self.sacar(valor):
            destino.deposito(valor)
            self.historico.transacoes.append(f'transferencia de {valor} para {destino} ')
            return True
        else:
            return False
        
class ContaPoupanca(Conta):
    def __init__(self, cliente, numero, saldo, limite=1000):
        super().__init__(cliente, numero, saldo, limite)
        self.conta_tipo = 'poupanca'

    def __str__(self):
        return f'Dados da conta:\nTitular: {self._titular}\nNumero: {self._numero}\nSaldo: {self._saldo}\nLimite: {self._limite}\nTipo da conta: {self.conta_tipo} '
        
    def atualiza(self, taxa):
        return super().atualiza(taxa) * 2

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, saldo, limite = 1000):
        super().__init__(cliente, numero, saldo, limite)
        self.conta_tipo = 'Corrente'

    def __str__(self):
        return f'Dados da conta:\nTitular: {self._titular}\nNumero: {self._numero}\nSaldo: {self._saldo}\nLimite: {self._limite}\nTipo da conta: {self.conta_tipo} '

    def get_valor_imposto(self):
        return self._saldo * 0.01

    def atualiza(self, taxa):
        return super().atualiza(taxa) *3
    
    def deposito(self, valor):
        return super().deposito(valor) -0,10
    
class ContaInvestimento(Conta):
    def __init__(self, cliente, numero, saldo, limite=1000):
        super().__init__(cliente, numero, saldo, limite)
        self.conta_tipo = 'Investimento' 
    
    def __str__(self):
        return f'Dados da conta:\nTitular: {self._titular}\nNumero: {self._numero}\nSaldo: {self._saldo}\nLimite: {self._limite}\nTipo da conta: {self.conta_tipo} '


    def atualiza(self, taxa):
        return super().atualiza(taxa) * 5
    
    def get_valor_imposto(self):
        return self._saldo * 0.03
    
class SegurodeVIda:
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor *0.05

        

if __name__ == '__main__':
    pass