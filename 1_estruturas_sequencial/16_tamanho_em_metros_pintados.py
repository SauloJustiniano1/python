# 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
# da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades 
# de latas de tinta a serem compradas e o preço total.

tamanho_da_area = int(input("Tamanho da área a ser pintada (m²): "))

litro_da_tinta = int(tamanho_da_area / 3)
quantidade_das_latas = litro_da_tinta / 18
preco_total = quantidade_das_latas * 80

print(f"Foi usada {quantidade_das_latas:.1f} de latas.")
print(f"Foi gasto R${preco_total:.1f}.")
