"""Leia uma temporatura em graus Fahrenheit e apresente-a onvertida em graus Celsius.
 A formula de conversao é: C= 5.0*(F - 32)/9, sendo C temperatura em celsius e F a temperatura em Fahrenheit)"""

F = int(input("declare qual é a temperatura de hoje para que o valor seja convertido: "))
C = 5*(F - 32)/9

print(f'{F} será igual a {C} em C')
