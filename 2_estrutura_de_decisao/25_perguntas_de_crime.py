# 25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação 
# da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como 
# "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado 
# como "Inocente".

import os 

os.system('cls' if os.name == 'nt' else 'clear')

frase_1 = input("Telefonou para a vítima? ")
frase_2 = input("Esteve no local do crime? ")
frase_3 = input("Mora perto da vítima? ")
frase_4 = input("Devia para a vítima? ")
frase_5 = input("Já trabalhou com a vítima? ")

if frase_1 == "sim" and frase_1 == "sim" and frase_3 == "sim" and frase_4 == "sim" and frase_5 == "sim":
  print("Assassino.")

elif (frase_1 == "sim" and frase_2 == "sim" and frase_3 == "sim" or 
      frase_2 == "sim" and frase_3 == "sim" and frase_4 == "sim" or
      frase_3 == "sim" and frase_4 == "sim" and frase_5 == "sim"):
  print("Cúmplice.")

elif (frase_1 == "sim" and frase_2 == "sim" or 
      frase_1 == "sim" and frase_3 == "sim" or 
      frase_1 == "sim" and frase_4 == "sim" or 
      frase_1 == "sim" and frase_5 == "sim" or 
      frase_2 == "sim" and frase_3 == "sim" or 
      frase_2 == "sim" and frase_4 == "sim" or 
      frase_2 == "sim" and frase_5 == "sim" or 
      frase_3 == "sim" and frase_4 == "sim" or 
      frase_3 == "sim" and frase_5 == "sim" or 
      frase_4 == "sim" and frase_5 == "sim"):
  print("Suspeito.")

else:
  print("Inocente.")
