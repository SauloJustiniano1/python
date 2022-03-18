# 27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      # Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) 
# de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

quantidade_de_morango = float(input("Informe a quantidade de morangos em Kg: "))
quantidade_de_maca = float(input("Informe a quantidade de maça em Kg: "))

frutas = quantidade_de_maca + quantidade_de_morango

if quantidade_de_morango <= 5:
  valor_do_morango = quantidade_de_morango * 2.50
else:
  valor_do_morango = quantidade_de_morango * 2.20

if quantidade_de_maca <= 5:
  valor_da_maca = quantidade_de_maca * 1.80
else:
  valor_da_maca = quantidade_de_maca * 1.50
  
if valor_da_maca + valor_do_morango <= 25:
  print(f"O valor a ser pago é de R${float(valor_da_maca + valor_do_morango)}")
else:
  print(f"O valor a ser pago com 10% de desconto é de R$",
  f"{float((valor_da_maca + valor_do_morango) - (0.10 * (valor_da_maca + valor_do_morango)))}")

