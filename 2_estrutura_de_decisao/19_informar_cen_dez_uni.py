# 19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e 
# unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades 
# Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

import os 

os.system('cls' if os.name == 'nt' else 'clear')

numero = int(input("Informe um número inteiro: "))

unidade = numero % 10
numero = int((numero - unidade) / 10)
dezena = numero % 10
numero = int((numero -  dezena) / 10)
centena = numero

if unidade == 1 and dezena == 1 and centena == 1:
  print(f"{centena} centena, {dezena} dezena e {unidade} unidade.")

elif unidade > 1 and dezena == 1 and centena == 1:
  print(f"{centena} centena, {dezena} dezena e {unidade} unidades.")
  
elif unidade == 1 and dezena > 1 and centena == 1:
  print(f"{centena} centena, {dezena} dezenas e {unidade} unidade.")

elif unidade == 1 and dezena == 1 and centena > 1:
  print(f"{centena} centenas, {dezena} dezena e {unidade} unidade.")

elif unidade == 0 and dezena > 1 and centena > 1:
  print(f"{centena} centenas, {dezena} dezenas e {unidade} unidade.")

elif unidade > 1 and dezena == 0 and centena == 1:
  print(f"{centena} centenas, {dezena} dezena e {unidade} unidade.")

elif unidade > 1 and dezena > 1 and centena == 0:
  print(f"{centena} centenas, {dezena} dezenas e {unidade} unidade.")

elif unidade > 1 and dezena == 0 and centena == 0:
  print(f"{centena} centenas, {dezena} dezena e {unidade} unidade.")

elif unidade == 0 and dezena > 1 and centena == 0:
  print(f"{centena} centenas, {dezena} dezenas e {unidade} unidade.")

elif unidade == 0 and dezena == 0 and centena > 1:
  print(f"{centena} centenas, {dezena} dezena e {unidade} unidade.")

elif unidade > 1 and dezena == 1 and centena == 0:
  print(f"{centena} centenas, {dezena} dezena e {unidade} unidade.")

elif unidade == 0 and dezena == 0 and centena == 0:
  print("Erro!")

else:
  print(f"{centena} centenas, {dezena} dezenas e {unidade} unidades.")
