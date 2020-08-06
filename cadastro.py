"""Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'; """

nome = str(input("digite aqui o seu nome: "))
print("seu nome é: {}.".format(nome))

idade = int(input("insira aqui a sua idade: "))
if idade < 0 and idade > 150:
    print("valor invalido pois ninguem vive até essa idade, digite de novo:")
else:
    print("idade valida")

salario = float(input("digite aqui o valor do seu salário: R$"))

print(salario)

sexo = input("diga o seu sexo apenas inserindo f(feminino) ou m(masculino): ")

if sexo != "m" or sexo != "f":
    for n in range(0, 100):
        sexo = input("é preciso colocar um valor valido, f ou m: ")
        if sexo == "m" or sexo == "f":
            print("valor valido")
            break
else:
    print("valor valido")
