class Banco:
    def __init__(self, numero_conta: str, agencia:str, dono:str, saldo:float):
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.dono = dono
        self.saldo = saldo
        listaContas = BancoManagement()
    
class Usuario:
    def __init__(self, nome:str, cpf:str, nascimento:str):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        Usuarios = UsuariosManagement()

class BancoManagement:
    banco_contas = []

    def show_contas(self):
        for i in range(len(self.banco_contas)):
            print(self.banco_contas[i])

    def add_conta(self, conta):
        if self.conta_existe(conta):
            print('Não é possivel adicionar essa conta, ela ja existe no banco')
            return
        self.banco_contas.append(conta)
        

    def conta_existe(self, conta):
        for contas in self.banco_contas:
            if contas.numero_conta == conta.numero_conta and contas.agencia == conta.agencia:
                return True
        return False

class UsuariosManagement:
    users = []

    def show_users(self):
        for i in range(len(self.users)):
            print(self.users[i])

    def user_existe(self, user):
        for users in self.users:
            if users.cpf == user.cpf:
                return True
        return False

    def add_user(self, user):
        if self.user_existe(user):
            print('não é possivel criar esse usuario, ele ja existe')
            return
        self.users.append(user)

    