#boa prática cololocar letras maisculas
class Conta:
#self tem o mesmo valor que rodar somente a variavel, mesma referência
    def __init__(self, numero, titular, saldo, limite):
        #print(f"Construindo objeto... {self}")
        print(f"Construindo objeto... {self}")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"O saldo do titular {self.titular} é {self.saldo} ")
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.saldo -= valor
