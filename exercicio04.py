'''
construir um algoritmo que tenha a entrada de números inteiros escolhidos pelo usuário. A quantidade será escolhida, tabém, pelo usuário e o algoritmo mostrará:
1 - uma lista com todos os números
2 - uma lista co números ímpares
3 - uma lista com os números em ordem crescente
4 - uma lista com os números em ordem decrescente
5 - uma lista com um número removido pelo usuário
'''

print("Listagem Numérica")

numeros = []
print("A listagem possui quantos números?")
qntd = int(input())

for i in range(1, qntd + 1):
    print(f"insira o {i}º número:")
    numero = int(input())
    numeros.append(numero)
print("Lista numérica:")
print(numeros)

for i in numeros:
    if i % 2 == 1:
        print("\n")
        print("Lista c/ apenas os números ímpares:")
        print(i)

'''
print("Lista c/ apenas os números ímpares:")
print(numeros)
'''

print("\n")
numeros.sort()
print("Lista em ordem crescente: ")
print(numeros)


print("\n")
numeros.sort(reverse=True)
print("Lista ordem decrescente: ")
print(numeros)
numeros.sort(reverse=False)


print("\nEscolha um número para remover da lista: ")
remover = int(input())
numeros.remove(remover)
print("Lista atualizada:")
print(numeros)