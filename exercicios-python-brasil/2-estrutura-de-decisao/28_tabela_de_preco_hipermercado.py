# 28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      # Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o 
# cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo 
# e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

import os 

os.system('cls' if os.name == 'nt' else 'clear')

tipo_da_carne = str(input("Informe qual tipo da carne você deseja, (File Duplo), (Alcatra) ou (Picanha): "))
quantidade_de_carne = float(input("Informe a quantidade de carne desejada: "))
tipo_do_pagamento = str(input("Qual o tipo de pagamento: "))

if tipo_da_carne in ("File Duplo", "file duplo"):
  if quantidade_de_carne <= 5:
    valor_do_file_dulplo = quantidade_de_carne * 4.90
  else:
    valor_do_file_dulplo = quantidade_de_carne * 5.80

if tipo_da_carne in ("Alcatra", "alcatra"):
  if quantidade_de_carne <= 5:
    valor_do_alcatra = quantidade_de_carne * 5.90
  else:
    valor_do_alcatra = quantidade_de_carne * 6.80

if tipo_da_carne in ("Picanha", "picanha"):
  if quantidade_de_carne <= 5:
    valor_da_picanha = quantidade_de_carne * 6.90
  else:
    valor_da_picanha = quantidade_de_carne * 7.80

if tipo_do_pagamento in ("Dinheiro", "dinheiro"):
  if tipo_da_carne in ("File Duplo", "file duplo"):
    print(f"Tipo da carne: {tipo_da_carne}")
    print(f"Quantidade de carne: {quantidade_de_carne}Kg")
    print(f"Preço Total: R${valor_do_file_dulplo}")
    print(f"Tipo do pagamento: {tipo_do_pagamento}")
    print(f"Valor do desconto: R$0,0")
    print(f"Valor a pagar: R${valor_do_file_dulplo}")
  
  elif tipo_da_carne in ("Alcatra", "alcatra"):
    print(f"Tipo da carne: {tipo_da_carne}")
    print(f"Quantidade de carne: {quantidade_de_carne}Kg")
    print(f"Preço Total: R${valor_do_alcatra}")
    print(f"Tipo do pagamento: {tipo_do_pagamento}")
    print(f"Valor do desconto: R$0,0")
    print(f"Valor a pagar: R${valor_do_alcatra}")

  elif tipo_da_carne in ("Picanha", "picanha"):
    print(f"Tipo da carne: {tipo_da_carne}")
    print(f"Quantidade de carne: {quantidade_de_carne}Kg")
    print(f"Preço Total: R${valor_da_picanha}")
    print(f"Tipo do pagamento: {tipo_do_pagamento}")
    print(f"Valor do desconto: R$0,0")
    print(f"Valor a pagar: R${valor_da_picanha}")

if tipo_do_pagamento in ("Cartão", "cartão"):
  if tipo_da_carne in ("File Duplo", "file duplo"):
    desconto = valor_do_file_dulplo - (valor_do_file_dulplo * 0.10)
    print(f"Tipo da carne: {tipo_da_carne}")
    print(f"Quantidade de carne: {quantidade_de_carne}Kg")
    print(f"Preço Total: R${valor_do_file_dulplo}")
    print(f"Tipo do pagamento: {tipo_do_pagamento}")
    print(f"Valor do desconto: R${round(float(valor_do_file_dulplo * 0.10),1)}")
    print(f"Valor a pagar: R${round(desconto,1)}")
  
  elif tipo_da_carne in ("Alcatra", "alcatra"):
    desconto = valor_do_alcatra - (valor_do_alcatra * 0.10)
    print(f"Tipo da carne: {tipo_da_carne}")
    print(f"Quantidade de carne: {quantidade_de_carne}Kg")
    print(f"Preço Total: R${valor_do_alcatra}")
    print(f"Tipo do pagamento: {tipo_do_pagamento}")
    print(f"Valor do desconto: R${round(float(valor_do_alcatra * 0.10),1)}")
    print(f"Valor a pagar: R${round(desconto,1)}")

  elif tipo_da_carne in ("Picanha", "picanha"):
    desconto = valor_da_picanha - (valor_da_picanha * 0.10)
    print(f"Tipo da carne: {tipo_da_carne}")
    print(f"Quantidade de carne: {quantidade_de_carne}Kg")
    print(f"Preço Total: R${valor_da_picanha}")
    print(f"Tipo do pagamento: {tipo_do_pagamento}")
    print(f"Valor do desconto: R${round(float(valor_da_picanha * 0.10),1)}")
    print(f"Valor a pagar: R${round(desconto,1)}")
