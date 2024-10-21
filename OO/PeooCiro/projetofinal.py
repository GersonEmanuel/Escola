from tkinter import *
import pickle
import os
import random


possibilidade = random.randint(1,100)
if possibilidade <= 20:
    pagina = 'netflix'
elif possibilidade <= 40:
    pagina = 'amazon prime video'
elif possibilidade <= 60:
    pagina = 'HBO max'
elif possibilidade <= 80:
    pagina = 'paramount plus'
elif possibilidade <= 100:
    pagina = 'disney plus'


class conta:
    def __init__ (self, mestre):
        self.c1 = Frame(mestre)
        self.c1["padx"] = 100
        self.c1["pady"] = 75
        self.c1.pack()
        self.titulo = Label(self.c1, text = pagina)
        self.titulo["font"] = ("rockwell", "60", "bold")
        self.titulo.pack()


        self.c2 = Frame(mestre)
        self.c2.pack()
        self.t2 = Label(self.c2, text = "nome")
        self.t2.pack(side = LEFT)
        self.l2 = Entry(self.c2)
        self.l2.pack(side = LEFT)


        self.c3 = Frame(mestre)
        self.c3.pack()
        self.t3 = Label(self.c3, text="senha")
        self.t3.pack(side=LEFT)
        self.l3 = Entry(self.c3, show = "*")
        self.l3.pack(side=LEFT)


        self.c4 = Frame(mestre)
        self.c4.pack()
        self.botao = Button(self.c4, text="login")
        self.botao["command"] = self.login_p
        self.botao.pack()


        self.c5 = Frame(mestre)
        self.c5.pack()
        self.texto = Label(self.c5, text= 'caso esteja querendo se cadastrar, repita a sua senha abaixo:')
        self.texto.pack()
       
        self.c6 = Frame(mestre)
        self.c6.pack()
        self.l4 = Entry(self.c6, show = '*')
        self.l4.pack()


        self.c7 = Frame(mestre)
        self.c7.pack()
        self.botao = Button(self.c7, text="fazer cadastro")
        self.botao["command"] = self.cadastro_p
        self.botao.pack()
        self.mensagem = Label(self.c7, text="")
        self.mensagem.pack()


    def conta_existe(self, username):
        with open('contasusuarios.txt', 'a') as arquivo:
            for conta in arquivo.readlines():
                print(conta)
                if username == conta:
                    return True
        return False

    def login_p(self):
        verificacao = False
        with open("contasusuarios.txt") as arquivo:
            for contausuario in arquivo.readlines():
                pessoa, senha = contausuario.strip().split(",")
                print(pessoa, senha)
                if self.l2.get() == pessoa and self.l3.get() == senha:
                    verificacao = True
                    global pessoa_nome
                    pessoa_nome = self.l2.get()
                    pagina_menu()
            if verificacao == False:
                self.mensagem["text"] = "nenhuma conta encontrada"    


    def cadastro_p(self):
        if self.conta_existe(self.l2.get()):
            self.mensagem['text'] = 'conta ja existe'
            return

        arquivo.write("{},{}\n".format(self.l2.get(), self.l3.get()))
        self.mensagem["text"] = "conta salva"
        



class filme:
    def __init__(self, nome, tempo):
        self.nome = nome
        self.tempo = tempo


class curtametragem(filme):
    def __init__(self, nome, tempo):
        filme.__init__(self, nome, tempo)
        self.__duracao = "curta-metragem"
    def getduracao(self):
        return self.__duracao


class longametragem(filme):
    def __init__(self, nome, tempo):
        filme.__init__(self, nome, tempo)
        self.__duracao = "longa-metragem"
    def getduracao(self):
        return self.__duracao


class pagina_menu:
    def __init__(self):
        self.root = Toplevel()
        self.c1 = Frame(self.root)
        self.c1["padx"] = 100
        self.c1["pady"] = 75
        self.c1.pack()
        self.titulo = Label(self.c1, text = "filmes em 'assistir mais tarde'")
        self.titulo["font"] = ("rockwell", "20", "bold")
        self.titulo.pack()


        self.c2 = Frame(self.root)
        self.c2.pack()
        self.t2 = Label(self.c2, text = "nome do filme")
        self.t2.pack(side = LEFT)
        self.l2 = Entry(self.c2)
        self.l2.pack(side = LEFT)


        self.c3 = Frame(self.root)
        self.c3.pack()
        self.t3 = Label(self.c3, text="duração em minutos")
        self.t3.pack(side=LEFT)
        self.l3 = Entry(self.c3)
        self.l3.pack(side=LEFT)


        self.c4 = Frame(self.root)
        self.c4.pack()
        self.botao = Button(self.c4, text="listar")
        self.botao["command"] = self.listarfilmes
        self.botao.pack(side = LEFT)
        self.botao = Button(self.c4, text="adicionar filme")
        self.botao["command"] = self.salvarfilme
        self.botao.pack(side = RIGHT)


        self.c5 = Frame(self.root)
        self.c5.pack()
        self.botao = Button(self.c5, text="assistir filme")
        self.botao["command"] = self.excluirfilme
        self.botao.pack(side = LEFT)
        self.botao = Button(self.c5, text="alterar tempo de filme")
        self.botao["command"] = self.mudartempo
        self.botao.pack(side = RIGHT)
       
        self.c6 = Frame(self.root)
        self.c6.pack()
        self.mensagem = Label(self.c6, text="")
        self.mensagem.pack()
    def salvarfilme(self):
        lista_obj = []
        objeto = self.l2.get()
        if float(self.l3.get()) <= 40:
            objeto = curtametragem(self.l2.get(), float(self.l3.get()))
        else:
            objeto = longametragem(self.l2.get(), float(self.l3.get()))
        problema = False
        if os.path.isfile("{}.txt".format(pessoa_nome)) == True:
            with open("{}.txt".format(pessoa_nome), "rb") as arquivo:
                for filme in pickle.load(arquivo):
                    if filme.nome == self.l2.get():
                        problema = True
                        break
                    else:
                        lista_obj.append(filme)
                if problema == False:
                    lista_obj.append(objeto)
                    with open("{}.txt".format(pessoa_nome), "wb") as arquivo:
                        pickle.dump(lista_obj, arquivo)
                    self.mensagem["text"] = "filme salvo"
        else:
            with open("{}.txt".format(pessoa_nome), "wb") as arquivo:
                lista_obj.append(objeto)
                pickle.dump(lista_obj, arquivo)
    def listarfilmes(self):
        listagem = ""
        with open("{}.txt".format(pessoa_nome), "rb") as arquivo:
            for filme in pickle.load(arquivo):
                listagem += ('{} = {}({} minutos)\n'.format(filme.nome, filme.getduracao(), filme.tempo))
        self.mensagem["text"] = listagem
    def excluirfilme(self):
        problema = False
        lista_obj = []
        with open("{}.txt".format(pessoa_nome), "rb") as arquivo:
            for filme in pickle.load(arquivo):
                if filme.nome == self.l2.get():
                    problema = True
                else:
                    lista_obj.append(filme)
        with open("{}.txt".format(pessoa_nome), "wb") as arquivo:
            pickle.dump(lista_obj, arquivo)
        if problema == True:
            self.mensagem["text"] = "você assistiu o filme"
    def mudartempo(self):
        problema = False
        lista_obj = []
        with open("{}.txt".format(pessoa_nome), "rb") as arquivo:
            for filme in pickle.load(arquivo):
                if filme.nome == self.l2.get():
                    if type(filme) == curtametragem:
                        if float(self.l3.get()) <= 40:
                            filme.tempo = float(self.l3.get())
                            problema = True
                    else:
                        if float(self.l3.get()) > 40:
                            filme.tempo = float(self.l3.get())
                            problema = True
                    lista_obj.append(filme)
                else:
                    lista_obj.append(filme)
        with open("{}.txt".format(pessoa_nome), "wb") as arquivo:
            pickle.dump(lista_obj, arquivo)
        if problema == True:
            self.mensagem["text"] = "feito"


raiz = Tk()
conta(raiz)
raiz.mainloop()