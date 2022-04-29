# 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do
# usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

nome = input("Nome: ")
senha = input("Senha: ")

while nome == senha:
  print("Erro")
  nome = input("Nome: ")
  senha = input("Senha: ")

print("Login Feito.")
