import datetime
from atualizadorconta import AtualizadordeContas
from random import *


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
    #terminar
    _todas_as_contas = []
    def adicionar_conta(self):
        escolha_conta = int(input('Escolha um tipo de conta\n1-Conta corrente\n2- Conta poupanca '))
        if escolha_conta == 1:
            conta = ContaCorrente(str(input("Digite seu nome")), (random.randint(100, 999)), 500)
            Banco._todas_as_contas.append(conta)
        elif escolha_conta == 2:
            conta = ContaPoupanca(str(input("Digite seu nome")),(random.randint(100, 999)), 500 )
            Banco._todas_as_contas.append(conta)
    
    def pegaConta(self, index):
        return Banco._todas_as_contas[index]
    
    def pega_total_contas(self):
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
        self.__saldo = saldo
        self.__limite = limite
        self.historico = Historico()
        Conta._total_contas += 1

    @staticmethod
    def get_totalcontas():
        return Conta._total_contas
    
    def __str__(self):
        return f'Dados da conta:\nTitular: {self.__titular}\nNumero: {self.__numero}\nSaldo: {self.__saldo}\nLimite: {self.__limite} '

    
    def atualiza(self, taxa):
        self.__saldo += self.__saldo * taxa
        return self.__saldo


    def deposito(self, valor):
        self.__saldo += valor
        self.historico.transacoes.append(f'Deposito de {valor}')
        return self.__saldo

    def get_saldo(self):
        return self.__saldo
    def sacar(self, valor):
        if self.__saldo<valor:
            return False
        else:
            self.__saldo -= valor
            self.historico.transacoes.append(f'saque de {valor} ')
            return True



    def get_extrato(self):
        print(f'numero: {self.__numero}\nsaldo: {self.__saldo}')
        self.historico.transacoes.append(f'tirou extrato - saldo de {self.__saldo} ')



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
        self.__saldo += self.__saldo * taxa*2
        return self.__saldo

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, saldo, limite = 1000):
        super().__init__(cliente, numero, saldo, limite)
    def atualiza(self, taxa):
        self.__saldo += self.__saldo * taxa * 3
        return self.__saldo
    
    def deposito(self, valor):
        return super().deposito(valor) -0,10


if __name__ == '__main__':
    banco = Banco()
    banco.adicionar_conta()