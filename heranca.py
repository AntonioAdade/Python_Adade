class veiculo: #cria uma classe chamada veiculo com atributos cor placa e numero de rodas
    def __init__(self, cor, placa, num_rodas): #metodo para inicializar a classe veiculo
        self.cor = cor #atribui valor ao metodo
        self.placa = placa
        self.num_rodas = num_rodas
    
    def ligar_motor(self): #criar uma função dentro da classe que vai rodar uma rotina, nesse caso um print
        print("ligando o motor")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}"
        

class motocicleta(veiculo): #cria uma classe motocicleta e herda os atributos da classe veiculo
    pass

class carro(veiculo):
    pass

class caminhao(veiculo):
    def __init__(self, cor, placa, num_rodas, carregado): #sobreescrevendo o metodo pai
        super().__init__(cor, placa, num_rodas) #atributo super evoca os atribuitos originais do metodo pai
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f"{"Sim" if self.carregado else "Não"} estou carregado")


moto = motocicleta("preto", "abc-1234", 2)
moto.ligar_motor()

carro = carro("azul", "abc-1234", 4)
carro.ligar_motor()

caminhao = caminhao("amarelo", "abc-1234", 6, False)
caminhao.ligar_motor()
caminhao.esta_carregado()

print(moto)
print(carro)
print(caminhao)
