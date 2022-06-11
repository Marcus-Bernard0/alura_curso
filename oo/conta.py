#boa prática cololocar letras maisculas
class Conta:
#self tem o mesmo valor que rodar somente a variavel, mesma referência
    def __init__(self, numero, titular, saldo, limite):
        #print(f"Construindo objeto... {self}")
        print(f"Construindo objeto... {self}")
        self.__numero = numero #__ deixando a variavel privada
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"O saldo do titular {self.__titular} é {self.__saldo} ")
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        self.__saldo -= valor
    
    
    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
    
    def get_saldo (self):
        print(f"O saldo do titular {self.__titular} é {self.__saldo}")
        return self.__saldo
    
    def get_titular (self):
        print(f"Essa conta é titular de {self.__titular}")
        return self.__titular

    def get_limite (self):
        print(f"Seu limite é {self.__limite")
        return self.__limite