class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self. valor = valor
        
    def buzinar(self):
        print ("plim plim")
    
    def parar(self):
        print ("parando bicicleta...")
        print("bicicleta parada")
        
    def correr(self):
        print("taca-le pau nesse carrinho")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}"
    

bl = Bicicleta("vermelha", "caloi", 2022, 600)
print(bl)
bl.buzinar()
bl.correr()
bl.parar()

bl2 = Bicicleta("verde", "monark", 2000, 189)
print(bl2)
bl2.correr()
bl2.buzinar()
bl2.parar()

         