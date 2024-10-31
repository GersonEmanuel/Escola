class Banco:
    def __init__(self, numero_conta: str, agencia:str, dono:str, saldo:float):
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.dono = dono
        self.saldo = saldo
        listaContas = Contas()
    
class Usuario:
    def __init__(self, nome:str, cpf:str, nascimento:str):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        listaUsuarios = ()

class Contas:
    contas = []

    def show_contas(self):
        for i in range(len(self.contas)):
            print(self.contas[i])

    def add_conta(self, conta):
        self.contas.append(conta)

class Usuarios:
    users = []

    def show_users(self):
        for i in range(len(self.users)):
            print(self.users[i])

    def add_user(self, user):
        self.users.append(user)

    