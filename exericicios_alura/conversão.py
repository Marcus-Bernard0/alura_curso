import re
import time


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""  

    def valida_url(self):
        if not self.url: 
            raise ValueError("A URL está vazia")
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError("A URL não é válida.")

    
    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]  
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)

#condição para extrair a moeda destino e origem e outros paramêtros
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]  
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor
    def get_instrucoes(self):
        print("1 dolár = 5,50 reais")    
    
    def get_conversao(self):
        moeda_origem = extrator_url.get_valor_parametro("Origem")
        moeda_destino = extrator_url.get_valor_parametro("Destino")
        quantidade = int(extrator_url.get_valor_parametro("quantidade"))
        
        #convertendo a quantidade em inteiro para a conta
        convesao = int(quantidade)* 5.5
        
        print(f"A moeda origem é: {moeda_origem.title()}")
        print(f"A moeda destino é: {moeda_destino.title()}")
        print(f"A quantidada a ser convertida é: {quantidade:.2f} dólares.")
        print(f"O total deu R$ {convesao:.2f} ")

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)

extrator_url.get_instrucoes()
time.sleep(2)
print(50 *'#')
extrator_url.get_conversao()









