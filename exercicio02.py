print("O usuário escolhe os números")
numeros = []
quantidade = int(input("Quantos numeros você quer digitar na lista?\n"))

#for i in range(quantidade):
#    numero = int (input(f"Digite o {i+1}º número: "))

for i in range(1 , quantidade + 1 ):
    numero = int (input(f"Digite o {i}º número: "))
    numeros.append(numero)
print(f"Números digitados: {numeros}")


print("Mostrar somente os números pares")
for i in numeros:
    if i % 2 == 0:
        print(i)


