import os 

os.system('cls' if os.name == 'nt' else 'clear')

numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite mais um número: "))
numero_3 = int(input("Digite outro número: "))

if numero_1 == numero_2 ==  numero_3:
  print("Os 3 números são iguais.")

elif numero_1 < numero_2 and numero_1 < numero_3:
  print(f"O menor número é {numero_1}.")

elif numero_2 < numero_1 and numero_2 < numero_3:
  print(f"O menor número é {numero_2}.")

elif numero_3 < numero_1 and numero_3 < numero_2:
  print(f"O menor número é {numero_3}.")
  