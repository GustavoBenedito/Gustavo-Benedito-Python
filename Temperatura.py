"""Faça um programa que receba a temperatura média de cada mês do ano e armazene-as
em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as
temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ). """

temperatura = []
tempmes = 0
medianual = 0
n = 1

while n != 5:
    tempmes = int(input("diga qual é a temperatura do mes {}: ".format(n)))
    print("a media da temperatura do mes {} foi de {}".format(n, tempmes))
    n += 1
    print(" ")
    temperatura.append(tempmes)
print(temperatura)
print(sum(temperatura)/(n-1))
medianual = sum(temperatura)/(n-1)

#exercicio incompleto