"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja
inválido e continue pedindo até que o usuário informe um valor válido. """

nota = int(input("digite uma nota com valor entre zero e dez: "))
n = 1
if not nota < 0 and nota > 10:
    for n in range(0, 50):
        print("número de tentativas: {}".format(n))
        nota = int(input("valor adicionado foi {}, valor nao autorizado. Digite um valor entre zero e dez: ".format(nota)))
else:
    print("valor entre zero e dez, autorizado")
