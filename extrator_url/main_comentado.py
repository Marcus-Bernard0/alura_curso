url = 'https//bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real'
print(url)


'''#fatiamento
texto = 'abcde'
print(texto[0])

print(texto[0:2])'''

#método find para exibir posição
'''texto = 'abcde'
encontrando = texto.find('b')
print(encontrando)'''




indice_interrogacao = url.find('?')
print(indice_interrogacao)

#deixando o código mais dinâmico
url_base = url[:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao + 1:]
print(url_parametros)

#encontrando posição
parametro = ('moedaOrigem')
parametro_busca =  url.find('moedaOrigem')
print(parametro_busca)

'''obtendo o tamanho do parametro
tamanho_parametro = len(parametro)
print(tamanho_parametro)'''

'''#alternativa
indice_valor = parametro_busca + tamanho_parametro + 1
print(indice_valor)'''

#formula para extrair o a modeda após o =
indice_valor = parametro_busca + len(parametro) + 1
#print(indice_valor)


valor = url[indice_valor:]
print(valor)

#

