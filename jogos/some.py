
from lib import *

menu = [["BIBLIOTECA"],
        ["MENU DE OPCOES:"],
        ["1. Adicionar livro."],
        ["2. Listar todos os livros."],
        ["3. Buscar livro."],
        ["4. Contar livros por autor."],
        ["5. Listar livros por ano."],
        ["6. Remover livro."],
        ["7. Sair."]]

def imprimir_menu(menu):
    for linha in menu:
        print(" ".join(linha))
while True:
    imprimir_menu(menu)
    opcao = int(input(" escolha uma opcao: "))
    if opcao == 1:
        if adicionar_livro(str(input("Digite o titulo ")),str(input("Digite o nome do autor ")), int(input("Digite o ano em que o livro foi lançado "))):
            print("Livro adicionado!")
            listar_livros()
        else:
            print("Erro em adicionar o livro ")

    elif opcao == 2:
        listar_livros()
    elif opcao == 3:
        buscar_livro(str(input("deseja buscar por titulo, autor ou ano?: ").strip().lower()))
    elif opcao == 4:
        contar_livros_por_autor()
    elif opcao == 5:
        listar_livros_por_ano()
    elif opcao == 6:
        listar_livros()
        remover_livro(str(input("qual livro deseja remover da biblioteca?: ").lower()))
    elif opcao == 7:
        sair()
        break