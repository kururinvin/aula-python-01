Victor = {"Laranja", "Morango", "Limão", "Limão"}
Italo = {"Cajá", "Morango", "Limão", "Mangustão"}
Alice = {"Morango", "Caqui", "Limão", "Banana"}
Brenda = {"Banana", "Melão", "Uva", "Limão"}

cliente1 = set(Victor)
cliente2 = set(Alice)
cliente3 = set(Italo)
cliente4 = set(Brenda)

#Itens que se repetem\
print(f"Itens de Victor: {cliente1}")
print(f"Itens de Alice: {cliente2}")
print(f"Itens de Italo: {cliente3}")
print(f"Itens de Brenda: {cliente4}")
#ITENS EM COMUNS 
itenscomuns = cliente1.intersection(cliente2, cliente3, cliente4)
print(f"Itens em comum nos quatro carrinhos: {itenscomuns}")
#TODOS OS ITENS
todositens = cliente1.union(cliente2, cliente3, cliente4)
print(f"Lista de todos os itens: {todositens}")
print(f"Total de itens: {len(todositens)}")
#ITENS QUE NÃO SE REPETEM
naorepete = todositens.difference(cliente1, cliente2, cliente3, cliente4)
print(f"Apenas as frutas que não se repete: {naorepete}")