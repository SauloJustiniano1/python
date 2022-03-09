# 10. Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem 
# "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

turno = str(input("Qual o turno que você estuda (m) (v) (n): "))

if turno in ("m", "M", "matutino", "Matutino"):
  print("Bom Dia!")

elif turno in ("v", "V", "vespertino", "Vespertino"):
  print("Boa Tarde!")

elif turno in ("n", "N", "noturno", "Noturno"):
  print("Boa Noite!")
