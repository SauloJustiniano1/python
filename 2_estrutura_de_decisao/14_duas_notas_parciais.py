# 14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de 
# um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  # Média de Aproveitamento  Conceito
  # Entre 9.0 e 10.0        A
  # Entre 7.5 e 9.0         B
  # Entre 6.0 e 7.5         C
  # Entre 4.0 e 6.0         D
  # Entre 4.0 e zero        E

# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” 
# se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

nota_1 = float(input("Informe sua 1ª nota: "))
nota_2 = float(input("Informe sua 2ª nota: "))

media = (nota_1 + nota_2) / 2

if media >= 9 and media <= 10:
  print(f"Sua média foi de {media}.")
  print("APROVADO")
  print("Sua nota: A")

elif media >= 7.5 and media <= 9:
  print(f"Sua média foi de {media}.")
  print("APROVADO")
  print("Sua nota: B")

elif media >= 6 and media <= 7.5:
  print(f"Sua média foi de {media}.")
  print("APROVADO")
  print("sua nota: C")

elif media >= 4 and media <= 6:
  print(f"Sua média foi de {media}.")
  print("REPROVADO")
  print("Sua nota: D")

elif media >= 0 and media <= 4:
  print(f"Sua média foi de {media}.")
  print("REPROVADO")
  print("Sua nota: E")
