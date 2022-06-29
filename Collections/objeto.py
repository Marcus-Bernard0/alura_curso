class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor
    
    def __str__(self):
        return f"Código {self.codigo} saldo R$ {self.saldo}"
    
    def deposita_em_todas(contas):
        for conta in contas:
            conta.deposita(100)
            contas = [conta_marcus, conta_gabi, conta_marcus]


conta_marcus = ContaCorrente(25)


conta_marcus.deposita(600)


conta_gabi = ContaCorrente(56)
conta_gabi.deposita(1500)


contas = [conta_marcus, conta_gabi]
for conta in contas:
    print(f'{conta}\n')

contas = [conta_marcus, conta_gabi, conta_marcus]
print(contas[0])
conta_marcus.deposita(200)
print(contas[0])
print(contas[2])

contas[0].deposita(300), print(contas[0])

contas = [conta_marcus, conta_gabi, conta_marcus]

#tupla
marcus = ('Marcus', 22, 2000)
gabi = ('Gabi', 20, 2002)

#lista com tupla
usuarios = [marcus, gabi]
print(usuarios)
#inserindo uma tupla dentro de uma lista
usuarios.append(('Pedro', 2, 2020))
print(usuarios)

print(usuarios[0])
print(usuarios[0][0])

#criando tupla com lista

contas = (conta_marcus, conta_gabi)
print(conta)

for conta in contas:
    print(conta)

#tupla imutável mas a lista conta_marcus e conta_gabi não
contas[0].deposita(5200)
print(conta)