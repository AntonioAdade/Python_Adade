class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    @classmethod        
    def data_nascimento(cls, ano, dia, mes, nome):
        idade = 2022 - ano
        return cls(nome, idade)

    @staticmethod
    def maior_idade(idade):
        return idade >= 18


p = pessoa.data_nascimento(1989, 3, 21, "adade")
print(p.nome, p.idade)

print("maior de idade" if pessoa.maior_idade(17) else "menor de idade")
print("maior de idade" if pessoa.maior_idade(30) else "menor de idade")
