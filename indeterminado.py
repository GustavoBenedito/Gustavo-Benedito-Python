"""Faça um programa que leia um número indeterminado de valores,
correspondentes a notas, encerrando a entrada de dados quando for informado um
valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

    Mostre a quantidade de valores que foram lidos;
    Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    Calcule e mostre a soma dos valores;
    Calcule e mostre a média dos valores;
    Calcule e mostre a quantidade de valores acima da média calculada;
    Calcule e mostre a quantidade de valores abaixo de sete;
    Encerre o programa com uma mensagem"""

vetor = []
num = 0
while num != -1:
    num = int(input("insira um numero: "))
    vetor.append(num)
    if num == -1:
        vetor.pop()

print("foram lidos {} valores".format(len(vetor)))
print(vetor)
print((sum(vetor)))
print((max(vetor)))
print((min(vetor)))
a = [7]
if vetor > a:
    print(vetor)
