def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite':limite}
    return conta

def deposita(conta, valor):
    conta['saldo'] += valor
    return conta['saldo']

def saca(conta, valor):
    conta['saldo'] -= valor
    return conta['saldo']

def extrato(conta):
    print(f'numero: {conta['numero']}\nsaldo: {conta['saldo']} ')

conta = cria_conta('123-43', 'gerson', 500, 1000)
deposita(conta, 100)
saca(conta, 200)
extrato(conta)