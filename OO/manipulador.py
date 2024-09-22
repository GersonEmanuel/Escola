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
    cc = ContaCorrente('ger', '342', 5000)
    sg = SegurodeVIda(1000, 'ger', '431')
    Tributavel.register(ContaCorrente)
    Tributavel.register(SegurodeVIda)
    Tributavel.register(ContaInvestimento) 
    ci = ContaInvestimento('ger', '2345', 3000, 1000)
    lista_ = [cc, sg, ci]
    mp = ManipuladordeTributaveis()
    total =mp.calcula_impostos(lista_)
    print(total)
