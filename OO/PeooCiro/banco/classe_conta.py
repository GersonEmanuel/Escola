from random import *
class Conta:
    def __init__(self, numero_conta: str, agencia:str, dono:str, saldo:float):
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.dono = dono
        self.saldo = saldo
    
class Usuario:
    def __init__(self, nome:str, cpf:str, nascimento:str):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento

    def __str__(self):
        return f'nome: {self.nome}, cpf: {self.cpf}, ano de nascimento: {self.nascimento}'

class BancoManagement:
    banco_contas = []

    def show_contas(self):
        for i in range(len(BancoManagement.banco_contas)):
            print(BancoManagement.banco_contas[i]) 

    def create_conta(self, cpf):
        if UsuariosManagement.user_existe(self, usercpf=cpf):
            conta_user = Conta(numero_conta=random.randint(1000,10000), agencia=str(input('Em qual agencia deseja criar? ')), dono= user, saldo=0)
            if BancoManagement.conta_existe(conta_user):
                print('Não é possivel adicionar essa conta, ela ja existe no banco')
                return
            BancoManagement.banco_contas.append(conta_user)
            return conta_user
        print('cpf nao existe, impossivel criar uma conta ')
        return
        

    def conta_existe(self, conta):
        for contas in BancoManagement.banco_contas:
            if contas.numero_conta == conta.numero_conta and contas.agencia == conta.agencia:
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



    