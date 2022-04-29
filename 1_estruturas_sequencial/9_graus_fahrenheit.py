# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em 
# graus Celsius.
# C = 5 * ((F-32) / 9).

fahrenheit = float(input("Digite uma temperatura em Fahrenheit: "))

celsuis = 5 * ((fahrenheit - 32) / 9)

print(f"{fahrenheit:.0f}°F é igual a {celsuis:.4f}°C.")
