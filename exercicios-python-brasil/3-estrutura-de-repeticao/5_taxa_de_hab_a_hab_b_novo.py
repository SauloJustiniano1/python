# 5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento 
# iniciais. Valide a entrada e permita repetir a operação.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

habitantes_de_a = int(input("Informe a população de A: "))
habitantes_de_b = int(input("Informe a população de B: "))

taxa_de_crescimento_de_a = float(input("Informa a taxa de crescimento de A em (%): "))
taxa_de_crescimento_de_b = float(input("Informa a taxa de crescimento de B em (%): "))

taxa_de_crescimento_de_a = taxa_de_crescimento_de_a / 100
taxa_de_crescimento_de_b = taxa_de_crescimento_de_b / 100

ano = 0

while habitantes_de_a <= habitantes_de_b:
  ano = ano + 1
  habitantes_de_a = (habitantes_de_a * taxa_de_crescimento_de_a) + habitantes_de_a
  habitantes_de_b = (habitantes_de_b * taxa_de_crescimento_de_b) + habitantes_de_b

print(f"É necessário {ano} anos para a população A chegar ou igualar a população B.")
