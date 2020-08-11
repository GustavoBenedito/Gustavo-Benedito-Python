# Bora fazer uma biblioteca para adicionar e visualizar os filmes

filmes = ["A Viagem de Chihiro", "Crianças Lobo", "Alice no País das Maravilhas", "Django Livre"]
print(type(filmes))
filme = 0





def imprimir_filmes():
    for filme in filmes:
        print(filme)




for n in filmes:
    decisao = (input("digite adicionar pra adicionar filme, ver pra apenas visualizar a biblioteca, sair pra sair: "))
    if decisao == "adicionar":
        filme = input("adicione um filme: ")
        filmes.append(filme)
        imprimir_filmes()
    elif decisao == "ver":
        imprimir_filmes()
    elif decisao == "sair":
        print("saindo da biblioteca")
        imprimir_filmes()
        break