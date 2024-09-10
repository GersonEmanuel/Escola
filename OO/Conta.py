import datetime


class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []
    def imprime(self):
        print(f'data abertura: {self.data_abertura} ')
        print('transacoes... ')
        for i in self.transacoes:
            print('-', i)


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


if __name__ == '__main__':
    conta = Conta('Gerson', '2345', 56000)
    conta.get_extrato()
    conta.historico.imprime()

