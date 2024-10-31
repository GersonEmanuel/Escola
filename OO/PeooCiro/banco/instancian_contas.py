from classe_conta import *
banco = BancoManagement()
usuarios = UsuariosManagement()

def criar_usuario():
    global usuarios
    nome = str(input('Digite seu nome '))
    cpf = str(input('Informe seu cpf '))
    ano_nascimento = int(input('Ano de nascimento '))
    usuarios.create_user(nome, cpf, ano_nascimento)


