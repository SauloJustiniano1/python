# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input("Digite uma temperatura em Celsius: "))

fahrenheit = (celsius * (9 / 5) + 32)

print(f"{celsius}°C é igual a {fahrenheit}°F.")
