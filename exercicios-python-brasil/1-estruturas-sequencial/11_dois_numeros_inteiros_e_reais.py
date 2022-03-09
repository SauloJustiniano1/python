# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a. o produto do dobro do primeiro com metade do segundo.
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo.

numero_1 = int(input("Digite uma número inteiro: "))
numero_2 = int(input("Digite mais um número inteiro: "))
numero_real = float(input("Digite um número real: "))

a = (2 * numero_1) * (numero_2 / 2)
b = (3 * numero_1) + numero_real
c = numero_real ** 3

print(f"O produto do dobro do primeiro com metade do segundo é {a}")
print(f"A soma do triplo do primeiro com o terceiro é {b}")
print(f"O terceiro elevado ao cubo é {c}")
