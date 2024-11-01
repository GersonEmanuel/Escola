from classe_conta import *
from random import randint
banco = BancoManagement()
usuarios = UsuariosManagement()

def criar_usuario():
    global usuarios
    nome = str(input('Digite seu nome '))
    cpf = str(input('Informe seu cpf '))
    ano_nascimento = int(input('Ano de nascimento '))
    usuarios.create_user(nome, cpf, ano_nascimento)

criar_usuario()
banco.create_conta('231')
banco.show_contas()
