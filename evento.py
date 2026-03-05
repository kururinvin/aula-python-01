workshop1 = {"Italo", "Brenda", "Victor", "Gustavo", "Alice", "Caio"}
workshop2 = {"Caio", "Heitor", "Juliana", "Douglas", "Maju", "Caio"}

participantes = set(workshop1)
participantes2 = set(workshop2)

print(f"Participantes do evento 1: {participantes}")
print(f"Participantes do evento 2: {participantes2}")

todos_participantes = participantes.union(participantes2)

print(f"Lista de todos os participantes: {todos_participantes}")
print(len(todos_participantes))

ambos_workshops = participantes.intersection(participantes2)
print(f"Participantes nos dois workshops: {ambos_workshops}")

so_1 = participantes.difference(participantes2)
print(f"Apenas participantes do priemiro evento: {so_1}")