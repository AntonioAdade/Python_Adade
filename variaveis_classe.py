class estudante:
    escola = "DIO"
    
    def __init__(self, nome, matricula, ano_nascimento):
        self.nome = nome
        self.matricula = matricula
        self.ano_nescimento = ano_nascimento
    
    @property
    def idade(self):
        ano_atual = 2024
        return ano_atual - self.ano_nescimento
        
    
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola} - {self.idade}"

def mostrar_valores(*obj):
    for i in obj:
        print(i)
        
aluno1 = estudante("guilherme", 1, 1989)
aluno2 = estudante("adade", 2, 2010)
mostrar_valores(aluno1, aluno2)