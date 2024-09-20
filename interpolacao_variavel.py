nome = "Antonio"
idade = 28
profissao = "Engenheiro"
linguagem = "Python"
dados = {"nome": "Antonio", "idade": 28}
saldo = 43.764372384


#old format
print("nome: %s idade: %d" % (nome, idade))

#format
print("nome: {} idade: {}".format(nome, idade))
print("nome: {0} idade: {1}".format(nome, idade))
print("nome: {nome} idade: {idade}".format(nome = nome, idade = idade))
print("nome: {name} idade: {age}".format(name = nome, age = idade))
print("nome: {nome} idade: {idade}".format(**dados))

#F-string

print(f"nome: {nome} idade: {idade}")
print(f"nome: {nome} idade: {idade} saldo: {saldo:.3f}")    #retorna os 3 primeiros valores depois da virgula
print(f"nome: {nome} idade: {idade} saldo: {saldo:10.3f}")    #acrescenta 10 espaços antes de retorna os 3 primeiros valores depois da virgula

#fatiamento de string

alias = "Antonio Adade de Castro Batista"

print(alias[0])
print(alias[:9])
print(alias[-2])
print(alias[10:])
print(alias[10:16])
print(alias[10:16:2])
print(alias[:])
print(alias[::-1])

#string multiplas linhas

mensagem = f"""
    olá meu nome é {nome}
estou aprendendo python
        esse exercicio tem diferentes recuos.
    teste de linhas
            inclusive pode haver diversas linhas
        com tipos diferentes de recuos.
"""

print(mensagem)

print(
    """
        ======================== MENU ===========================

    Opções:

    1 - sacar
    2 - depositar
    0 - sair

        ============================================================
    
                   Obrigado por usar nosso sistema!!!    
"""    
)