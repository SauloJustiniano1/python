# 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa
# deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

import os

os.system('cls' if os.name == 'nt' else 'clear')

nota_1 = float(input("Digite sua primeira nota: "))
nota_2 = float(input("Digite sua segunda nota: "))

media_das_notas = (nota_1 + nota_2) / 2

if media_das_notas >= 7 and media_das_notas < 10:
    print(f"Sua média foi de {media_das_notas}.")
    print("Aprovado.")

elif media_das_notas < 7:
    print(f"Sua média foi de {media_das_notas}.")
    print("Reprovado.")

elif media_das_notas == 10:
    print(f"Sua média foi de {media_das_notas}.")
    print("Aprovado com Distinção.")
