from abc import abstractmethod

class ControleRemoto():
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
class ControleTV(ControleRemoto):
    def ligar(self):
        print("ligando tv...")
        print("tv ligada")
    
    def desligar(self):
        print("desligando tv...")
        print("tv deligada")

class ControleAR(ControleRemoto):
    def ligar(self):
        print("ligando AR...")
        print("AR ligado")
    
    def desligar(self):
        print("desligando AR...")
        print("AR deligado")
        
controle = ControleTV()
controle.ligar()
controle.desligar()


controle = ControleAR()
controle.ligar()
controle.desligar()

