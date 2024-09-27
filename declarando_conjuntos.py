num = set([1, 2, 3, 3, 2, 1, 4]) # comando set utilizado para remover valores duplicados de um interavel (string é um interavel)
print(num)

carros = set(["gol", "palio", "uno", "gol", "celta"])
print(carros)

numero = {1, 2, 3, 3, 2, 1, 4} #chaves indicam que a variavel é um conjunto e ja remove valores duplicados
print(numero)
#print(numero[0]) #valores em conjunto ou set não podem ser subescritos ou interaveis

numero = list(numero)
print(numero[0])

car = {"gol", "palio", "uno", "gol", "celta"}

for indice, i in enumerate(car):
    print(f"{indice}: {car}")

print()
print("#################################################")

#dicionarios

contatos = {
    "guilerme@gmail.com": {"nome": "guilherme", "telefone": "783497839"},
    "giovana@gmail.com": {"nome": "giovana", "telefone": "8734983"},
    "adade@gmail.com": {"nome": "adade", "telefone": "92384908", "extra": {"a": 1}},
     
}

telefone = contatos["giovana@gmail.com"]
print(telefone)

extra = contatos["adade@gmail.com"]["extra"]["a"]
print(extra)