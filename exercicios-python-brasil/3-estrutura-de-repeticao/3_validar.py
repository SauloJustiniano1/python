# 3. Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

import os 

os.system('cls' if os.name == 'nt' else 'clear')

nome = input("Nome: ")
while len(nome) < 4:
  nome = input("Nome: ")

idade = int(input("Idade: "))
while idade < 0 or idade > 150:
  idade = int(input("Idade: "))

salario = float(input("Salário: "))
while salario < 0:
  salario = float(input("Salário: "))

sexo = input("Sexo: ")
while sexo != "f" and sexo != "m":
  sexo = input("Sexo: ")

estado_civil = input("Estado Civil: ")
while estado_civil not in ("s", "c", "v", "d"):
  estado_civil = input("Estado Civil: ")

print("Cadastro Feito.")