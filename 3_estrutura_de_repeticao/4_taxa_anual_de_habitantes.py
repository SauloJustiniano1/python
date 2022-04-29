# 4. Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de
# crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A 
# ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

habitantes_de_a = 80000
habitantes_de_b = 200000

ano = 0

while habitantes_de_a <= habitantes_de_b:
  ano = ano + 1
  habitantes_de_a = (habitantes_de_a * 0.03) + habitantes_de_a
  habitantes_de_b = (habitantes_de_b * 0.015) + habitantes_de_b

print(f"É necessário {ano} anos para a população A chegar ou igualar a população B.")
