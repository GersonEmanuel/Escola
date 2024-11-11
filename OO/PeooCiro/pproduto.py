class Produto:
    def __init__(self, nome:str, codigo:int, preco:float, estoque:int, descricao:str) -> None:
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.estoque = estoque
        self.descricao = descricao

    def calcularDesconto(self, percentual:float) -> float:
        self.preco *= (percentual/100)
        return self.preco

    def atualizarEstoque(self, quantidade:int)->None:
        self.estoque += quantidade

    def exibirDetalhes(self)->None:
        print(f"nome do produto: {self.nome}\nCodigo do produto {self.codigo}\npreco do produto: {self.preco}\n quantidades restantes: {self.estoque}\ndescricao do produto: {self.descricao}")

