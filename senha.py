"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações. """

nome = str(input("digite aqui o seu nome: "))
senha = str(input("digite aqui a sua senha: "))
n = 1
if nome == senha:
    for n in range(0, 1):
        print("tentativa número {}".format(n))
        print("o nome de usuário e a senha não podem ser iguais, digite ambos diferentes")
        nome = input("digite aqui o seu nome: ")
        senha = input("digite aqui a sua senha: ")
else:
    print("acesso autorizado")
