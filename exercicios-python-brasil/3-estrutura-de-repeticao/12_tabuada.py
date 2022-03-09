# 12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo 
# abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

import os 

os.system('cls' if os.name == 'nt' else 'clear')

numero = int(input("Informe um número para sua tabuada: "))

contador = 1
print(f"=-=-=TABUADA DO {numero}=-=-=-")
while contador < 11:
  soma = numero * contador
  print(f"{numero} x {contador} = {soma}")
  contador = contador + 1

print("Acabou !!!")
