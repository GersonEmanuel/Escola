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


def criar_conta():
    global banco
    cpf = str(input('para criar a conta deve primeiro informar seu cpf'))
    agencia = str(input('Em qual agencia deseja criar? '))
    senha = criar_senha()
    banco.create_conta(cpf,randint(1000,10000), agencia, senha)


def criar_senha():
    senha = str(input('Crie uma senha'))
    confirmando_senha = str(input('digite novamente a senha '))
    if senha != confirmando_senha:
        print('as senhas nao se condizem, tente novamente')
        criar_senha()
    return senha
    


