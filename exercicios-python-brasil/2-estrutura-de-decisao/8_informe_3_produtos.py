# 8. Faça um programa que pergunte o preço de três produtos e informe qual produto 
# você deve comprar, sabendo que a decisão é sempre pelo mais barato.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

produto_1 = float(input("Informe qual é o preço: R$"))
produto_2 = float(input("Informe outro preço: R$"))
produto_3 = float(input("Informe mais outro preço: R$"))

if produto_1 < produto_2 and  produto_1 < produto_3:
  print(f"O preço mais barato é de {produto_1}.")

elif produto_2 < produto_1 and produto_2 < produto_3:
  print(f"O preço mais barato é de {produto_2}.")

elif produto_3 < produto_1 and produto_3 < produto_2:
  print(f"O preço mais barato é de {produto_3}.")
