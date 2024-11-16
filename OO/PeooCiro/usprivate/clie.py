class Cliente:
    __nome = ''
    __endereco = ''
    __cpf = ''
    __idade = 0

    def mudaCPF(self, cpf):
        self.__cpf = cpf

    def Getnome(self):
        return self.__nome
    
    def getEndereco(self):
        return self.__endereco
    
    def getCPF(self):
        return self.__cpf
    
    def getIdade(self):
        return self.__idade
    
