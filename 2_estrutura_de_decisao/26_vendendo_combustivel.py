# 26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro. Escreva um algoritmo que leia o número de litros vendidos, 
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a 
# ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é 
# R$ 1,90.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

numero_de_litros = float(input("Quandos litros você quer colocar: "))
combustivel = input("Qual combustível é (A-álcool) ou (G-gasolina): ")

if combustivel in ("a", "A", "álcool", "Álcool"):
  if numero_de_litros > 1 and numero_de_litros <= 20:
    preco_dos_litros = numero_de_litros * 1.90
    desconto_do_litro = preco_dos_litros * 0.03
    desconto = preco_dos_litros - desconto_do_litro
    print("O litro do álcool é de R$1.90.")
    print(f"A cada 1 litro de álcool você tem o desconto de 3% do litro.")
    print(f"Sem o desconto de 3% ficaria de R${preco_dos_litros}.")
    print(f"Com {int(numero_de_litros)} litros de álcool você vai pagar R${desconto}.")
  
  elif numero_de_litros > 20:
    preco_dos_litros = numero_de_litros * 1.90
    desconto_do_litro = preco_dos_litros * 0.05
    desconto = preco_dos_litros - desconto_do_litro
    print("O litro do álcool é de R$1.90.")
    print(f"A cada 1 litro de álcool você tem o desconto de 5% do litro.")
    print(f"Sem o desconto de 3% ficaria de R${preco_dos_litros}.")
    print(f"Com {int(numero_de_litros)} litros de álcool você vai pagar R${desconto}.")
  
elif combustivel in ("g", "G", "gasolina", "Gasolina"):
  if numero_de_litros > 1 and numero_de_litros <= 20:
    preco_dos_litros = numero_de_litros * 2.50
    desconto_do_litro = preco_dos_litros * 0.04
    desconto = preco_dos_litros - desconto_do_litro
    print("O litro do álcool é de R$2.50.")
    print(f"A cada 1 litro de álcool você tem o desconto de 4% do litro.")
    print(f"Sem o desconto de 3% ficaria de R${preco_dos_litros}.")
    print(f"Com {int(numero_de_litros)} litros de álcool você vai pagar R${desconto}.")

  elif numero_de_litros > 20:
    preco_dos_litros = numero_de_litros * 2.50
    desconto_do_litro = preco_dos_litros * 0.06
    desconto = preco_dos_litros - desconto_do_litro
    print("O litro do álcool é de R$2.50.")
    print(f"A cada 1 litro de álcool você tem o desconto de 6% do litro.")
    print(f"Sem o desconto de 3% ficaria de R${preco_dos_litros}.")
    print(f"Com {int(numero_de_litros)} litros de álcool você vai pagar R${desconto}.")
