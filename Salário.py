nome = input("digite o seu nome: ")

horas = float(input("quanto você ganha por hora? "))

mês = int(input("quantas horas por mês você trabalha?"))

salario:float = mês * horas
print("{}, você ganha R${} de salário por mês".format(nome,salario))

print('agora iremos adicionar os descontos:')

impostoderenda = salario/11
print("o seu Imposto de Renda será de: R${}".format(impostoderenda))

INSS = salario/8
print(" o seu INSS será de: R${}".format(INSS))

sindicato = salario/5
print("a taxa para o sindicato será de: R${}".format(sindicato))

salariobruto = salario - impostoderenda - INSS - sindicato
print("o seu salario bruto será de: R${}".format(salariobruto))




