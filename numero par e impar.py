"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
 Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

 while len(vetor) == 20:
    num = int(input("adicione numeros inteiros impares ou pares"))
    vetor.append(num)
    if len(vetor)/2 == 0:
        par = vetor
    else:
        impar = vetor

        carrinho = []
produto = 0
while carrinho != "sair":
    produto = input("adicione um produto ao carrinho ou digite 'sair' para sair: ")
    carrinho.append(produto)
    if produto == "sair":
        print("saindo da loja, volte sempre")
        break
carrinho.pop()
print("voce comprou {} produtos".format(len(carrinho)))
print(carrinho)

vetor = []
numero: int = 0
impar = []
par = []
while vetor != 5:
    numero = int(input("adicione um numero inteiro impar ou par: "))
    vetor.append(numero)
    if numero/2 == 0:
        par.append(numero)
    if numero/2 != 0:
        impar.append(numero)
    if len(vetor) == 5:
        print("finalizar operaçao")
        break
print(vetor)
print(impar)
print(par)
"""

vetor = []
impar = []
par = []
n = 0
while n != 5:
    numero = int(input("digita um numero ai: "))
    vetor.append(numero)
    n += 1
    if (numero % 2) == 0:
        print("numero par")
        par.append(numero)
        print(" ")
    else:
        print("numero impar")
        impar.append(numero)
        print(" ")
    if n == 5:
        print("encerrando aplicação: ")
        break
print(" ")
print("vetor principal: {}".format(vetor))
print(" ")
print("vetor impar: {}".format(impar))
print(" ")
print("vetor par: {}".format(par))
