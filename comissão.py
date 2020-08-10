"""Escreva um programa que, dado o valor da venda, imprima a comissão que
 deverá ser paga ao vendedor. Para calcular a comissão, considere a tabela abaixo:

Venda mensal   Comissão
Maior ou igual a 100000,00                         700+16%das vendas
menor ou igual a 100000,00 ou igual a 80000,00     650+14% das vendas
menor que 80000,00 e maior ou igual a 60000,00      600+14% das vendas
menor que 60000,00 e maior ou igual a 400000,00     550+14% das vendas
menor que 400000,00 e maior ou igual a 20000,00     500 + 14% das vendas
menor que 200000,00                                 400 + 14% das vendas
else:
    comissao = (valorvenda + 0.14)
    vendacomissao = comissao + 650
    print(vendacomissao)
if valorvenda < 80000 or valorvenda >= 60000:
    comissao = (valorvenda + 0.14)
    vendacomissao = comissao + 600
    print(vendacomissao)
if valorvenda < 60000 or valorvenda >= 40000:
    comissao = (valorvenda + 0.14)
    vendacomissao = comissao + 550
    print(vendacomissao)
if valorvenda < 40000 or valorvenda >= 20000:
    comissao = (valorvenda + 0.14)
    vendacomissao = comissao + 500
    print(vendacomissao)
if valorvenda < 20000:
    comissao = (valorvenda + 0.14)
    vendacomissao = comissao + 400
    print(vendacomissao)"""

valorvenda = int(input("diga ai o valor da venda que fez:"))
if valorvenda >= 100000:
    comissao = (valorvenda + 0.16)
    vendacomissao = comissao + 700
    print(vendacomissao)
elif valorvenda <= 100000 or valorvenda >= 80000:
    comissao = (valorvenda + 0.14)
    vendacomissao = comissao + 650
    print(vendacomissao)
else:
    comissao = (valorvenda + 0.14)
    vendacomissao = comissao + 600
    print(vendacomissao)
