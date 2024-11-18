import re
class Cliente:
    def __init__(self, nome:str, endereco:str, cpf:str, idade:int)->None:
        self.__nome = nome
        self.__endereco = endereco
        self.__cpf = cpf
        self.__idade = idade



    def Getnome(self)->str:
        return self.__nome
    
    def getEndereco(self)->str:
        return self.__endereco
    
    def getCPF(self)-> str:
        return self.__cpf
    
    def getIdade(self)-> int:
        return self.__idade


    def __setNome(self, nome):
        self.__nome = nome

    def __setEndereco(self, endereco):
        self.__endereco = endereco

    def __setCPF(self, cpf):
        if self.verificaCPF(cpf):
            self.__cpf = cpf

    def __setIdade(self, idade):
        self.__idade = idade
    
    def verificaCPF(self, cpf)->bool:
        numeros = [int(digito) for digito in cpf if digito.isdigit()]
  
        formatacao = False
        quant_digitos = False
        validacao1 = False
        validacao2 = False

        #Verifica a estrutura do CPF (111.222.333-44)
        if re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            formatacao = True

        if len(numeros) == 11:
            quant_digitos = True
        
            soma_produtos = sum(a*b for a, b in zip (numeros[0:9], range (10, 1, -1)))
            digito_esperado = (soma_produtos * 10 % 11) % 10
            if numeros[9] == digito_esperado:
                validacao1 = True

            soma_produtos1 = sum(a*b for a, b in zip(numeros [0:10], range (11, 1, -1)))
            digito_esperado1 = (soma_produtos1 *10 % 11) % 10
            if numeros[10] == digito_esperado1:
                validacao2 = True

            if quant_digitos == True and formatacao == True and validacao1 == True and validacao2 == True:
                return True
            else:
                return False

        else:
            return False




