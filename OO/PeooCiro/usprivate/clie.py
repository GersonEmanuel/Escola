class Cliente:
    __nome = ''
    __endereco = ''
    __cpf = ''
    __idade = 0

    def mudaCPF(self, cpf):
        self.__cpf = cpf

cliente = Cliente()
cliente.cpf