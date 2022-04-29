# 24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja 
# realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# a. par ou ímpar;
# b. positivo ou negativo;
# c. inteiro ou decimal.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

numero_1 = float(input("Digite um número: "))
numero_2 = float(input("Informe mais um númer: "))

operacao = str(input("Qual operação você quer (+), (-), (*), (/): "))

adicao = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2

if operacao in ("adição", "+"):
  if adicao == 0:
    print("Erro!")

  if adicao % 2 == 0:
    print(f"O número {int(adicao)} é PAR.")
  else:
    print(f"O número {int(adicao)} é ÍMPAR.")
  
  if adicao > 0:
    print(f"O número {int(adicao)} é POSITIVO.")
  else:
    print(f"O número {int(adicao)} é NEGATIVO.")

  if adicao == round(adicao):
    print(f"O número {int(adicao)} é INTEIRO.")
  else:
    print(f"O número {adicao} é DECIMAL.")

if operacao in ("subtração", "-"):
  if subtracao == 0:
    print("Erro!")

  if subtracao % 2 == 0: 
    print(f"O número {int(subtracao)} é PAR.")
  else:
    print(f"O número {int(subtracao)} é ÍMPAR.")

  if subtracao > 0:
    print(f"O número {int(subtracao)} é POSITIVO.")
  else:
    print(f"O número {int(subtracao)} é NEGATIVO.")

  if subtracao == round(subtracao):
    print(f"O número {int(subtracao)} é inteiro.")
  else:
    print(f"O número {subtracao} é decimal.")

if operacao in ("multiplicação", "*"):
  if multiplicacao == 0:
    print("Erro!")

  if multiplicacao % 2 == 0:
    print(f"O número {int(multiplicacao)} é PAR.")
  else:
    print(f"O número {int(multiplicacao)} é ÍMPAR.")

  if multiplicacao > 0:
    print(f"O número {int(multiplicacao)} é POSITIVO.")
  else:
    print(f"O número {int(multiplicacao)} é NEGATIVO.")

  if multiplicacao == round(multiplicacao):
    print(f"O número {int(multiplicacao)} é INTEIRO.")
  else:
    print(f"O número {multiplicacao} é DECIMAL.")

if operacao in ("divisão", "/"):
  if divisao == 0:
    print("Erro!")

  if divisao % 2 == 0:
    print(f"O número {int(divisao)} é PAR.")
  else:
    print(f"O número {int(divisao)} é ÍMPAR.")

  if divisao > 0:
    print(f"O número {int(divisao)} é POSITIVO.")
  else:
    print(f"O número {int(divisao)} é NEGATIVO.")

  if divisao == round(divisao):
    print(f"O número {int(divisao)} é INTEIRO.")
  else:
    print(f"O número {divisao} é DECIMAL.")
  