from Conta import *
class ManipuladordeTributaveis:
    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            if(isinstance(t,Tributavel)):
                total += t.get_valor_imposto()
            else:
                print(f'{t.__repr__} não é tributavel ')
        return total
    
if __name__ == '__main__':
    pass
