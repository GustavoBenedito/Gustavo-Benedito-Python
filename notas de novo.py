"""carrinho = []
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

"""
nome = input("diga seu nome: ")
print("bem vindo {}, faremos a media de suas notas: ".format(nome))

nota1 = int(input("A nota da primeira prova: "))
nota2 = int(input("A nota da segunda prova: "))
nota3 = int(input("A nota da terceira prova: "))
nota4 = int(input("A nota da quarta prova: "))

media = (nota1 + nota2 + nota3 + nota4)/4

if media < 5:
    print("reprovado, tente da proxima vez")
elif media == 5:
    print("ufa, passou raspando")

else:
    print("parabeeeens voce passou")
