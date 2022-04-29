# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota_1 = float(input("Digite sua 1º nota: "))
nota_2 = float(input("Digite sua 2º nota: "))
nota_3 = float(input("Digite sua 3º nota: "))
nota_4 = float(input("Digite sua 4º nota: "))

soma = nota_1 + nota_2 + nota_3 + nota_4

media = soma / 4

print(f"Sua média total foi de {media}.")
