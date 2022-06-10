from teste import criando_conta, deposito, saque, extrato
from conta import ContaCorrente

conta = criando_conta(20364, "Marcus", 45105.00, 5.00000)
print(f'Esse é o numero da conta: {conta["numero"]}')

conta2 = criando_conta(89364, "Gabi", 69105.00, 5.640)
print(f'Esse é o numero da conta: {conta2["numero"]} do titular {conta2["titular"]}')

deposito(conta, 2530.00)
print('Depósito realizado')

extrato(conta)

saque(conta, 500)


extrato(conta)


