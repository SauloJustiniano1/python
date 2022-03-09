# 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link 
# de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link 
# (em minutos).

tamanho_do_arquivo = float(input("Tamanho do arquivo para download (em MB): "))
velocidade_do_link = float(input("Velocidade do link de internet (em Mbps): "))

tempo = tamanho_do_arquivo / velocidade_do_link

minutos = tempo / 60

print(f"Demorou em volta de {minutos:.1f} minutos para fazer o download.")
