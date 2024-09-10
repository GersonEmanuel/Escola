
biblioteca = [["a cinco passos de voce", "Rachel Lippincott", "2019"],
              ["como eu era antes de voce", "Jojo Moyes", "2012"],
              ["depois de voce", "Jojo Moyes", "2015"],
              ["ainda sou eu", "Jojo Moyes", "2018"],
              ["o pequeno principe", "Antoine de Saint-Exupéry", "1943"],
              ["1984", "George Orwell", "1949"],
              ["a mao e a luva", "Machado de Assis", "1879"],
              ["dom casmurro", "Machado de Assis", "1899"]]


def adicionar_livro(titulo, autor, ano):
    biblioteca.append([titulo, autor, ano])
    return True


# adicionar_livro() print(biblioteca)

def listar_livros():
    for i in range(len(biblioteca)):
        print(f'{i + 1} - TITULO: {biblioteca[i][0]}, . AUTOR: {biblioteca[i][1]}, . ANO: {biblioteca[i][2]}')


# listar_livros()

def buscar_livro(opcao):
    if opcao == "titulo":
        titulo = input("titulo que deseja buscar: ").strip().lower()
        for i in range(len(biblioteca)):
            if biblioteca[i][0] == titulo.lower().strip():
                print(f'TITULO: {biblioteca[i][0]}, . AUTOR: {biblioteca[i][1]}, . ANO:  {biblioteca[i][2]}')
                break
        else:
            print("livro não encontrado!")

    elif opcao == "autor":
        autor = input("autor que deseja buscar: ").strip().lower()
        for i in range(len(biblioteca)):
            if biblioteca[i][1].lower() == autor.lower():
                print(f'TITULO: {biblioteca[i][0]}, . AUTOR: {biblioteca[i][1]}, . ANO:  {biblioteca[i][2]}')
                break
        else:
            print("livro não encontrado!")

    elif opcao == "ano":
        ano = input("ano que deseja buscar: ").strip()
        for i in range(len(biblioteca)):
            if biblioteca[i][2] == ano:
                print(f'TITULO: {biblioteca[i][0]}, . AUTOR: {biblioteca[i][1]}, . ANO:  {biblioteca[i][2]}')
                break
        else:
            print("livro não encontrado!")
    else:
        print("opcao invalida! opcoes validas: 'titulo', 'autor' ou 'ano.'")


# buscar_livro()

def contar_livros_por_autor():
    autores = {}
    for livro in biblioteca:
        autor = livro[1]
        if autor in autores:  # verifica se o autor ja ta presente na contagem
            autores[autor] += 1  # se ta presente, adiciona mais 1 a contagem
        else:
            autores[autor] = 1  # se n ta presente, comeca sua contagem com 1

    return autores


# resultado = contar_livros_por_autor() print(resultado)

def listar_livros_por_ano():
    anos = {}
    for livro in biblioteca:
        ano = livro[2]
        if ano in anos:
            anos[ano] += 1
        else:
            anos[ano] = 1
    return anos


# resultado = listar_livros_por_ano() print(resultado)

def remover_livro(titulo):
    for i in range(len(biblioteca)):
        if str(titulo.lower()) == biblioteca[i][0].lower():
            biblioteca.remove(biblioteca[i])
            print("livro removido!")
            return True
    return False




def sair():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

