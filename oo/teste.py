#inicio em orientação a objetos
numero = 230    
titular = "Marcus"
saldo = 10000
limite = 500.000

conta = {"numero": 230, "titular": "Marcus", "saldo": 10000, "limite": 500.000}
print(conta["limite"])

conta2 = {"numero": 24, "titular": "Gabi", "saldo": 1400, "limite": 2.500}

#criando função para importar em outro arquivo

def criando_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposito(conta, valor):
    conta['saldo'] += valor

def saque(conta, valor):
    conta['saldo'] -=valor 
    print(f"Você fez um saque de R$ {valor:.2f} reais")

def extrato(conta):
    print(f"Seu saldo na sua conta é R${conta['saldo']:.2f}")