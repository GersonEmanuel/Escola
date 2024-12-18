from random import *
class Conta:
    def __init__(self, numero_conta: str, agencia:str, dono:str, saldo:float, senha:str):
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.dono = dono
        self.saldo = saldo
        self.senha = senha
        contas = BancoManagement()

    def depositar(self, valor):
        if valor<0:
            print('não é possivel depositar')
            return
        print(f'deposito de {valor} bem sucedido ')
        self.saldo += valor

    def sacar(self, valor):
        if valor>self.saldo:
            print('não é possivel sacar um valor que voce não possui')
            return
        print(f'saque de {valor} bem sucedido')
        self.saldo -= valor
        

    def transferir_para(self, conta, valor):
        self.sacar(valor)
        conta.depositar(self, valor)
        print(f'valor transferido')

        
    def __str__(self):
        return f'numero da conta: {self.numero_conta}\nagencia: {self.agencia}\ndono: {self.dono}\nsaldo: {self.saldo}'
    
class Usuario:
    def __init__(self, nome:str, cpf:str, nascimento:str):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        user = UsuariosManagement()

    def __str__(self):
        return f'nome: {self.nome}, cpf: {self.cpf}, ano de nascimento: {self.nascimento}'

class BancoManagement:
    banco_contas = []

    def show_contas(self):
        for i in range(len(BancoManagement.banco_contas)):
            print(BancoManagement.banco_contas[i]) 

    def create_conta(self, cpf, numero_conta, agencia, senha):
        if UsuariosManagement.user_existe(self, usercpf=cpf):
            user = UsuariosManagement.get_user(self, cpf)
            conta_user = Conta(numero_conta = numero_conta, agencia=agencia, dono = user, saldo =0, senha = senha )
            if BancoManagement.conta_existe(self, conta_user):
                print('Não é possivel adicionar essa conta, ela ja existe no banco')
                return
            BancoManagement.banco_contas.append(conta_user)
            return 
        print('cpf nao existe, impossivel criar uma conta ')
        return
        

    def conta_existe(self, numeroconta, agencia):
        for conta in BancoManagement.banco_contas:
            if conta.numero_conta == numeroconta and conta.agencia == agencia:
                return True
        return False
    

    def get_conta(self, numeroconta, agencia):
        for conta in BancoManagement.banco_contas:
            if BancoManagement.conta_existe(self, numeroconta, agencia):
                if BancoManagement.verificacao_login(self, conta, str(input('Digite sua senha'))):
                    return conta
                print('login invalido ')
        return False
    

    def verificacao_login(self, conta, senha):
        if conta.senha == senha:
            return True
        return False
            


class UsuariosManagement:
    users = []

    def show_users(self):
        for i in UsuariosManagement.users:
            print(i)


    def user_existe(self, usercpf):
        for users in UsuariosManagement.users:
            if users.cpf == usercpf:
                return True
        return False
    
    def get_user(self,usercpf):
        for user in UsuariosManagement.users:
            if user.cpf == usercpf:
                return user

    def create_user(self,nome, usercpf, nascimento):
        if UsuariosManagement.user_existe(self, usercpf):
            print('não é possivel criar esse usuario, ele ja existe')
            return
        User = Usuario(nome=nome, cpf=usercpf, nascimento=nascimento)
        UsuariosManagement.users.append(User)



    