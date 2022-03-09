# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

base = float(input("Digite a base do quadrado: "))
altura = float(input("Digite a altura do quadrado: "))

area_do_quadrado = base * altura

dobro_da_area = area_do_quadrado * 2

print(f"Área do quadrado é {area_do_quadrado:.0f} cm²")

print(f"Dobro da área do quadrado é {dobro_da_area:.0f} cm².")
