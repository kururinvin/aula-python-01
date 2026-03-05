# Criação do dicionário
estoque = {

    "Camisa":50,
    "Calça":15,
    "Boné":25,
    "Tênis Nike":35
}
#Mostrar estoque atual
print("Estoque atual: ")
for produto, quantidade in estoque.items():
    print(f"{produto} : {quantidade}")
#Pedindo dados para o usuário do sistema
nome_produto = input("\n Informe o nome do produto vendido: ")
quantidade_vendida = int(input("\nInforme a quantidade vendida: "))
#Atualizar o estoque
if nome_produto in estoque:
    if quantidade_vendida <= estoque[nome_produto]:
       estoque[nome_produto] = estoque[nome_produto] - quantidade_vendida
       print("Venda realizada com sucesso.")
else:
    print("Produto não encontrado.")
#Mostrar produto atualizado
for produto, quantidade in estoque.items():
    print(f"{produto} | {quantidade}")