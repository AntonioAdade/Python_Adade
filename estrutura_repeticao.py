
# texto = input("digite uma palavra: ")
# texto = ""     #atalho ctrl k + ctrl u comenta toda a seleção
# VOGAIS = "AEIOU"

# exemplo usando iteravel
# for letras in texto:
#     if letras.upper() in VOGAIS:
#         print(letras, end=" ")
#     else:
#         print()
# print()
# print("exiba esta mensagem no final")

# exemplo usando range

# for numero in range(0, 51, 5):
#     print(numero, end=" ")  #end no final do comando print força o resultado em apenas uma linha


#exemplo usando while

# opcao = -1

# while opcao != 0:
#     print("escolha uma opção abaixo: ")
#     opcao = int(input("[1]sacar \n[2]saldo \n[0]sair \n:"))

#     if opcao == 1:
#         print("sacando...")
#     if opcao == 2:
#         print("seu saldo é: ")
    
# else:
#     print()
#     print("obrigado")


#exemplo usando break e continue

while True:
    numero = int(input("adivinhe o numero correto: "))

    if numero == 10:
        break   #break é usado para interromper um laço quando uma condição for alcançada 

print("parabens, o numero correto é: ", numero)

for numero in range(100):
    if numero % 2 == 0: #notação para retornar numeros pares
        continue

    print(numero, end=" ")