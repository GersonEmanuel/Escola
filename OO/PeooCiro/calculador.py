class Calculadora:
    def soma(self, a,b):
        print(f'{a}+{b} é igual a {a+b}')

    def dividir(self, a,b):
        print(f'a divisao e {a} por {b} é igual a {a/b} ')

    def multiplicar(self,a,b):
        print(f'a multiplicacao de {a} por {b} é {a*b}')

    def subtrair(self,a,b):
        print(f'a subtracao de {a} por {b} é {a-b}')

c = Calculadora()
c.multiplicar(5,5)
