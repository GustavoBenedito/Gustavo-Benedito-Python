"""Calculadora"""


def somar():
    a = int(input("diga o primeiro valor a ser somado: "))
    b = int(input("diga o segundo valor a ser somado: "))
    soma = a + b
    print(f'o valor da soma será de {soma}')


def subtrair():
    a = int(input("diga o primeiro valor a ser subtraido: "))
    b = int(input("diga o segundo valor a ser subtraido:"))
    subtrair = a - b
    print(f'o valor da subtração será de {subtrair}')


def multiplicar():
    a = int(input("diga o primeiro valor a ser multiplicado: "))
    b = int(input("diga o segundo valor a ser multiplicado: "))
    multiplicar = a * b
    print(f'o valor da multiplicação será de {multiplicar}')


def dividir():
    a = int(input("diga o primeiro valor a ser dividido: "))
    b = int(input("diga o segundo valor a ser dividido: "))
    dividir = a / b
    print(f'o valor da divisão será de {dividir}')


decisao = input("decisa o que fazer com a calculadora: ")
while decisao != "sair":
    if decisao == "somar":
        somar()
    if decisao == "subtrair":
        subtrair()
    if decisao == "multiplicar":
        multiplicar()
    if decisao == "dividir":
        dividir()
    if decisao == "sair":
        break
    decisao = input("deseja fazer mais alguma operação? ")


print("calculadora desligando...")
