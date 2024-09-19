# MAIOR_IDADE = 18
# IDADE_ESPECIAL = 12

# idade = int(input("informe sua idade: "))

# if idade >= MAIOR_IDADE:
#     print("maior de idade, pode tirar a CNH!")

# if idade < MAIOR_IDADE:
#     print("ainda não pode tirar a CNH")

# ##############################

# if idade >= MAIOR_IDADE:
#     print("maior de idade, pode tirar a CNH!")

# else:
#     print("ainda não pode tirar a CNH")

# ##############################

# if idade >= MAIOR_IDADE:
#     print("maior de idade, pode tirar a CNH!")

# elif idade >= IDADE_ESPECIAL and idade < MAIOR_IDADE:
#     print("pode fazer aula teorica")
# else:
#     print("ainda não pode tirar a CNH")


#IF aninhado >> If dentro de outro if

# conta_normal = False
# conta_universitaria = True
# saldo = 2000
# saque = 1900
# cheque_especial = 450

# if conta_normal:
#     if saldo >= saque:
#         print("saque realizado")
#     elif saque <= (saldo + cheque_especial):
#         print("saque realizado com limite")
#     else:
#         print("saque nao realizado. saldo insuficiente")
# elif conta_universitaria:
#     if saldo >= saque:
#         print("saque realizado")
#     else:
#         print("saque nao realizado. saldo insuficiente")
# else:
#     print("conta nao reconhecida")

# if ternario

saldo = 2000
saque = 2500

status = "sucesso" if saldo >= saque else "falha"
print(f"{status} ao realizar o saque!")