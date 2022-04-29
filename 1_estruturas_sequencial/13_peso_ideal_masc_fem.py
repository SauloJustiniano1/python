# 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

sexo = input("Escreva seu sexo (masculino) ou (feminino): ")

altura = float(input("Digite sua altura atual para saber seu peso ideal: "))

peso_ideal_masculino = (72.7 * altura) - 58
peso_ideal_feminino = (62.1 * altura) - 44.7

if sexo == "masculino":
  print(f"Seu peso ideal é de {peso_ideal_masculino:.2f}Kg.")

if sexo == "feminino":
  print(f"Seu peso ideal é de {peso_ideal_feminino:.2f}Kg.")
