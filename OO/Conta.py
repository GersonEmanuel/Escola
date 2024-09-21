import datetime
from atualizadorconta import AtualizadordeContas
import random

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []
    def imprime(self):
        print(f'data abertura: {self.data_abertura} ')
        print('transacoes... ')
        for i in self.transacoes:
            print('-', i)

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
            


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Conta:
    _total_contas = 0
    __slots__ = ["__titular", "__numero", "__saldo", "__limite", "historico"]
    def __init__(self, cliente, numero, saldo, limite = 1000.0):
        self.__titular = cliente
        self.__numero = numero
        self._saldo = saldo
        self.__limite = limite
        self.historico = Historico()
        Conta._total_contas += 1

    @staticmethod
    def get_totalcontas():
        return Conta._total_contas
    
    def __str__(self):
        return f'Dados da conta:\nTitular: {self.__titular}\nNumero: {self.__numero}\nSaldo: {self._saldo}\nLimite: {self.__limite} '

    
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
        print(f'numero: {self.__numero}\nsaldo: {self._saldo}')
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
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa*2
        return self._saldo

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, saldo, limite = 1000):
        super().__init__(cliente, numero, saldo, limite)
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3
        return self._saldo
    
    def deposito(self, valor):
        return super().deposito(valor) -0,10


if __name__ == '__main__':
    controle = AtualizadordeContas(0,3)
    banco = Banco()
    cc = ContaCorrente('g','432',500,1000)
    banco.adicionar_conta(cc)
    cp = ContaPoupanca('h','531',1000)
    banco.adicionar_conta(cp)
    for i in Banco._todas_as_contas:
        controle.roda(i)
        