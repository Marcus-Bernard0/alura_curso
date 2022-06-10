import forca
import adivinhacao

#nesse arquivo poderia criar um def para executá-lo.
nome = input("Olá, qual o seu nome? ")

print("Bem vindo ao game, escolha qual deseja")
print((" Digite 1 para jogar a forca ou 2 para advinhação: "))

escolha = int(input("Qual o jogo? "))


if escolha == 1:
    print("Jogando a forca")
    forca.jogar()
elif escolha == 2:
    print("Tente adivinhar :D")
    adivinhacao.jogar()