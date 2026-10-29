
print("Entre com os nomes e organize em ordem alfabética crescente\n")

nomes = []
print("Escolha quantos nomes deseja inserir?")
quantidade = int(input())
for i in range(1, quantidade + 1):
    print(f"Digite o {i}º nome: ")
    nome = input("").title()
    nomes.append(nome)
nomes.sort()
print(f"Listagem em ordem alfabetica crescente: {nomes}")
nomes.sort(reverse=True)
print(f"Listagem em ordem alfabetica decrescente: {nomes}")

print("Escolha um nome para remover da lista: ")
remover = input("").title()
nomes.remove(remover)
print(f"Nomes: {nomes}")

