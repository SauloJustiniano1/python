# 16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário 
# nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não 
# deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre 
# o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import os 

os.system('cls' if os.name == 'nt' else 'clear')

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = (b ** 2) - (4 * a * c)

if a == 0 and b > 0 and c > 0:
  print("Essa equação não é de segundo grau.")

elif delta < 0:
  print("A equação não possui raizes reais.")

elif delta == 0:
  x = (- b + (delta ** 0.5)) / 2 * a
  print("A equação possui apenas uma raiz real, que é x.")
  print(f"x = {x}.")

elif delta > 0:
  x1 = (- b + (delta ** 0.5)) / 2 * a
  x2 = (- b - (delta ** 0.5)) / 2 * a
  print("A equação possui duas raizes reais, x1 e x2.")
  print(f"x1 = {x1}.")
  print(f"x2 = {x2}.")  
