#importando da classse ContaCorrente

#conta é uma referência

from conta import Conta

'''conta = Conta()

#exibindo sem criar a variável na função
print("Essas exibições não contém a variável na função")
#self.numero = 548
        #self.titular = "Marcola"
        #self.saldo = 2540
        #self.limite = 2000

print(conta.numero, conta.titular, conta.saldo)

print('\n')'''

print("Essas exibições contém a variável na função e tenho que definir os paramêtros")
conta = Conta(20, "Marcus" , 500.54, 3000.00)
conta2 = Conta(1, "Marley", 1000.00, 200000.00)

#não usar mais assim, pois foi definido o metodo
#print(f'Saldo conta 2: {conta2.__saldo}')
#print(f'Esse é o saldo da conta 1: {conta.__saldo}')

print('**********************')

conta2.extrato()

#depositando na conta do Marley
conta2.depositar(200)
#conferindo valor
conta2.extrato()
#sacando na conta do Marley
conta2.sacar(520)
#conferindo valor
conta2.extrato()

print("nova consulta antes da transferência")
conta.extrato()
conta2.extrato()

print('**********************')
print("Transferindo")

conta.transferir(300, conta2)
conta2.extrato()

print("********************")
#usando get para obter valores

#conta2.get_saldo()
#conta2.get_limite()

#usando set para mudar limite
#conta2.set_limite(1200.00)
#conta2.set_titular("Gabriela")
#conta2.set_titular("Marleyzão")


conta2.limite
conta2.limite = 1300