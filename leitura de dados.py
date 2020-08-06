"""Faça um programa que leia 5 números e informe o maior número. """
n = 0
for n in range(0, 6):
    print("quantas vezes foram inseridos numeros {} ".format(n))
    num = (input("insira aqui um numero: "))
    print(max(num))
