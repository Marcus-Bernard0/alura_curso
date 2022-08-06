import array as arr
import numpy as np
from functools import total_ordering

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return self._codigo == outro._codigo and self.saldo == outro._saldo

    def __lt__(self,outro):
        return self._saldo < outro._saldo

    def deposita(self, valor):
        self._saldo += valor

    
    def __str__(self):
        return f"Código {self._codigo} saldo R$ {self._saldo}"



class contaCorrente(ContaSalario):
    def passa_o_mes(self):
        self._saldo -=2

class contaPoupanca(ContaSalario):
    def passa_o_mes(self):
        self._saldo *=1.01
        self._saldo -=3


conta16 = contaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = contaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)


contas = [conta16, conta17]
for conta in contas:
    conta.passa_o_mes() 
    print(conta)

arrayTrue = arr.array('d', [1,3.5])
print(arrayTrue)



arraynp = np.array([1,3.5])
print(arraynp)

print(isinstance(contaPoupanca(17), ContaSalario))
