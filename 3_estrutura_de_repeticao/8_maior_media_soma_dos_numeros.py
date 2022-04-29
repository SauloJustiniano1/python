# 8. Faça um programa que leia 5 números e informe a soma e a média dos números.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

contador = soma = maior = 0

while contador < 5:
  numero = int(input("Digite um número: "))
  contador = contador + 1

  soma = soma + numero
  media = soma / 5

  if numero > maior:
    maior = numero
  
print(f"O maior número foi {maior}")
print(f"A soma é de {soma} e a média é de {media}")
