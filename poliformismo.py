class passaro:
    def voar(self):
        print("voando")

class pardal(passaro):
    def voar(self):
        print("pardal pode voar")
        
class avestruz(passaro):
    def voar(self):
        print("Avestruz não voa")

def plano_voo(obj):
    obj.voar()


p1 = pardal()
p2 = avestruz()

plano_voo(p1)
plano_voo(p2)






    