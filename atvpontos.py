# Criação do dicionário
pontos = {}
#Pedir ao usuário
for x in range(5):
    nome = input("Digite o nome do jogador: ")
    pontuação = float(input("Digite os pontos iniciais do jogador: "))

    pontos[nome] = pontuação
#Saída de dados
for nome, pontuação in pontos.items():
   print(f"{nome} | {pontuação}")

# Adição de pontos
nome = input("Qual o nome do jogador? ")
pontuação = int(input("Informe a quantidade de pontos: "))

if nome in pontos:
    pontos[nome] += pontuação
    print(f"\nNova pontuação de {nome}: {pontuação}")
else:
    print("Não foi encontrado")