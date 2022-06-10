


palavra_jogo =open("palavras.txt", "w") #a para adicionar #r leitura
palavra_jogo.write ("banana \n" "carro \n" "navio \n" "alura \n" ) #usado para escrever
palavra_jogo = open("palavras.txt" , "a")
palavra_jogo.write("macbook \n")
palavra_jogo.close()

palavra_jogo = open("palavras.txt", "r")
linha = palavra_jogo.readline()

print(linha)
