nomes = input("Digite uma lista de nomes separados por vírgula: ").split(",")

nomes_sem_duplicatas = list(set(nomes))

print("Lista sem nomes duplicados:", nomes_sem_duplicatas)