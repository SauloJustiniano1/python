# 17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da 
# área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a 
# tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# a. comprar apenas latas de 18 litros;
# b. comprar apenas galões de 3,6 litros;
# c. misturar lat/as e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e 
# sempre arredonde os valores para cima, isto é, considere latas cheias.

import os

os.system('cls' if os.name == 'nt' else 'clear')

tamanho_do_metro_quadrado = float(input("Qual o tamanho do metro quadrado da área a ser pintada: "))

quantidade_de_tintas = tamanho_do_metro_quadrado / 6

print(f"")