class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    
    def sanitiza_url(self, url):
        return url.strip()
    
    def valida_url(self):
        if self.url == "":
            raise ValueError("A url está vazia")


#extrator_url = ExtratorURL('https//bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real')
extrator_url = ExtratorURL(" ")

