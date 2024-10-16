#def analise_vendas(vendas):
#    #TODO: Calcule o total de vendas e realize a média mensal:
#    total_vendas = sum(vendas)
#    media_vendas = total_vendas / len(vendas)
#    
#    return f"{total_vendas}, {media_vendas:.2f}"
#
#def obter_entrada_vendas():
#    #Solicita a entrada do usuário em uma única linha
#    entrada = input("Digite os valores de vendas mensais separados por virgula: ")
#    
#    #TODO: Converta a entrada em uma lista de inteiros:
#    vendas = list(map(int, entrada.split(',')))
#    
#    return vendas
#
#vendas = obter_entrada_vendas()
#print(analise_vendas(vendas))
#print()
#print("###########################################")

#desafio@2
# def produto_mais_vendido(produtos):
#     contagem = {}
    
#     for produto in produtos:
#         if produto in contagem:
#             contagem[produto] += 1
#         else:
#             contagem[produto] = 1
    
#     max_produto = None
#     max_count = 0
    
#     for produto, count in contagem.items():
#         #TODO: Encontre o produto com a maior contagem:
#         if count > max_count:
#             max_count = count
#             max_produto = produto        
    
#     return max_produto

# def obter_entrada_produtos():
#     #Solicita a entrada do usuário em uma única linha
#     entrada = input()
#     #TODO: Converta a entrada em uma lista de strings, removendo espaços extras:
#     produtos = [produto.strip() for produto in entrada.split(',')]
#     return produtos

# produtos = obter_entrada_produtos()
# print(produto_mais_vendido(produtos))

######################################



# class Venda:
#     def __init__(self, produto, quantidade, valor):
#         self.produto = produto
#         self.quantidade = quantidade
#         self.valor = valor

# class Relatorio:
#     def __init__(self):
#         self.vendas = []

#     def adicionar_venda(self, venda):
#         # Verifica se o objeto passado é uma instância da classe Venda.
#         if isinstance(venda, Venda):
#             self.vendas.append(venda)
#         else:
#             print("Objeto não é uma instância da classe Venda.")

#     def calcular_total_vendas(self):
#         total = 0
#         for venda in self.vendas:
#             # Multiplica a quantidade pelo valor e soma ao total.
#             total += venda.quantidade * venda.valor
#         return total

# def main():
#     relatorio = Relatorio()
    
#     for i in range(3):
#         produto = input("Digite o nome do produto: ")
#         quantidade = int(input("Digite a quantidade: "))
#         valor = float(input("Digite o valor unitário: "))
#         venda = Venda(produto, quantidade, valor)
#         relatorio.adicionar_venda(venda)
    
#     # Exibe o total de vendas usando o método calcular_total_vendas.
#     total_vendas = relatorio.calcular_total_vendas()
#     print(f"O total de vendas é: R$ {total_vendas:.2f}")

# if __name__ == "__main__":
#     main()
    
    
################################################################################

class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []

    # Método para adicionar uma venda à lista de vendas.
    def adicionar_venda(self, venda):
        self.vendas.append(venda)            
      
    # Método para calcular e retornar o total das vendas da categoria.
    def total_vendas(self):
        total = 0
        for venda in self.vendas:
            total += venda.quantidade * venda.valor
        return total

def main():
    categorias = []

    for i in range(2):
        nome_categoria = input()
        categoria = Categoria(nome_categoria)

        for j in range(2): 
            entrada_venda = input()
            produto, quantidade, valor = entrada_venda.split(',')
            quantidade = int(quantidade.strip())
            valor = float(valor.strip())

            venda = Venda(produto.strip(), quantidade, valor)
            # Adiciona a venda à categoria usando o método adicionar_venda.
            categoria.adicionar_venda(venda)

        categorias.append(categoria)
    
    # Exibindo os totais de vendas para cada categoria.
    for categoria in categorias:
        total_vendas = categoria.total_vendas()
        print(f"Total de vendas para a categoria '{categoria.nome}': R$ {total_vendas:.2f}")

if __name__ == "__main__":
    main()
