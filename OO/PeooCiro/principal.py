from pproduto import *
from carro import *
from alluno import *

aluno = Aluno("Gerson", 20231094010008, 'Informatica', 21, 'gersonemanuel432@gmail.com')
#aluno se matriculou
aluno.matricula("apicultura")
#aluno desmatriculou
aluno.cancelarMatricula("apicultura")


carro = Carro("Fiat", "Uno", 1996, 'branco', 12000)
carro.acelerar()
carro.frear()
carro.ligar()


produto = Produto('macarro', 421, 8, 3, "macarrao gostoso")
produto.calcularDesconto(3)
produto.estoque()
produto.descricao()
