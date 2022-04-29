# 13. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro 
# número elevado ao segundo número. Não utilize a função de potência da linguagem.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

while True:
  base = int(input("Informe a base: "))
  if base < 0:
    print(f"A base é menor que 0.")
    break

  expoente = int(input("Informe o expoente: "))
  if expoente < 0:
    print(f"O expoente é menor que 0.")
    break

  else:
    potenciacao = base ** expoente
    print(f"{base} elevado a {expoente} = {potenciacao}")
    break
